#!/usr/bin/env python3
"""Mirror published Rulr samples without changing their executable payloads."""

from __future__ import annotations

import argparse
from concurrent.futures import ThreadPoolExecutor
import hashlib
import json
from pathlib import Path
import re
import textwrap
from urllib.error import HTTPError
from urllib.parse import urljoin
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
SITE = "https://www.rulr.app"
REPOSITORY = "https://github.com/snowfallapps/rulr-rules"
CATALOG_URL = SITE + "/rule-gallery/catalog.json"
SLUG = re.compile(r"[a-z0-9]+(?:-[a-z0-9]+)*")


def fetch(url: str) -> bytes:
    request = Request(url, headers={"User-Agent": "Rulr-Official-Rule-Sync/1.0"})
    with urlopen(request, timeout=45) as response:
        if not response.url.startswith(SITE + "/"):
            raise ValueError(f"Unexpected download host: {response.url}")
        return response.read()


def source_catalog(site: Path) -> dict:
    """Bootstrap from the website checkout; daily sync uses the public catalog."""
    manifest = json.loads((site / "data/rule_gallery.json").read_text())
    pages = {}
    for path in (site / "content/rules").glob("*.md"):
        text = path.read_text()
        match = re.search(r'^rule_slug:\s*"([a-z0-9-]+)"\s*$', text, re.M)
        if match:
            front, body = text.split("---", 2)[1:]
            intro = re.search(r"^intro: \|\n((?:[ \t]+[^\n]*\n|\n)*)", front, re.M)
            if not intro:
                raise ValueError(f"Missing block intro: {path.name}")
            pages[match[1]] = (textwrap.dedent(intro[1]).strip(), body.strip())
    rules = []
    for entry in manifest["rules"]:
        if not entry.get("page"):
            continue
        intro, body = pages[entry["slug"]]
        payload = (site / "static" / entry["download"].lstrip("/")).read_bytes()
        keys = ("slug", "title", "description", "download", "page", "categories",
                "primaryCategory", "level", "requiredConfiguration")
        rules.append({**{key: entry[key] for key in keys}, "intro": intro,
                      "documentation": body, "sha256": hashlib.sha256(payload).hexdigest()})
    return {"version": 1, "categories": manifest["categories"], "rules": rules}


def markdown(text: str, detail: str) -> str:
    # Keep links useful on GitHub instead of resolving them inside this repository.
    text = re.sub(r"\]\((/[^)\s]*)\)", lambda m: "](" + SITE + m[1] + ")", text)
    text = re.sub(r'\{\{<\s*published-post-link\s+path="([^"]+)"\s+label="([^"]+)"\s*>\}\}',
                  lambda m: f"[{m[2]}]({SITE}{m[1].rstrip('/')}/)", text)
    text = re.sub(r"\{\{[<%].*?[%>]\}\}", f"[View the interactive preview]({detail})", text, flags=re.S)
    return text.strip()


def selected_documentation(rule: dict) -> str:
    body = rule["documentation"].strip()
    parts = re.split(r"(?m)^## (.+)\n", body)
    sections = list(zip(parts[1::2], parts[2::2]))
    selected = []
    for index, (heading, content) in enumerate(sections):
        essential = re.match(r"(?:Configure|Requirements|Dependencies|Set up|Scope|Clipboard|Choose the article)", heading)
        if index == 0 or essential:
            selected.append(f"## {heading}\n\n{content.strip()}")
    return markdown("\n\n".join(selected) if selected else body, SITE + rule["page"])


def rule_readme(rule: dict) -> str:
    slug = rule["slug"]
    detail = SITE + rule["page"]
    download = f"{REPOSITORY}/raw/refs/heads/main/rules/{slug}/{slug}.rulr"
    return f"""# {rule['title']}

{markdown(rule['intro'], detail)}

[Website preview and full setup]({detail}) · [Download {slug}.rulr]({download}) · [All rules](../../README.md)

Download the `.rulr` file and open it with Rulr, or use **Open this Rule in Rulr**
on the linked website page. Review permissions and app-specific settings before
enabling the Rule. The instructions below refer to Rulr and that detail page.

{selected_documentation(rule)}

---

This README reuses selected sections of the [official Rule Detail]({detail}).
The website has the interactive preview and complete explanation. Rule files are
synced without changing their contents; edit your imported copy in Rulr.
"""


def table_text(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def repository_readme(catalog: dict) -> str:
    lines = ["# Rulr rules", "", "Official rule samples for [Rulr](https://www.rulr.app/), a Mac automation app built around **When → If → Do**.",
             "", "[Browse the interactive Rule Gallery](https://www.rulr.app/rules/) · [Download Rulr](https://www.rulr.app/download/Rulr.dmg)",
             "", "## Use a rule", "", "1. Choose a sample below and read its setup and limitations.",
             "2. Download the `.rulr` file from its folder and open it with Rulr. You can also use **Open this Rule in Rulr** on its website detail page.",
             "3. Select your own apps, folders, devices, and shortcuts where required. Grant only the permissions needed by the sample, then enable it.",
             "", "Rulr requires macOS 26 or later. Some Triggers and Actions require Rulr Pro; each linked detail page explains the requirements. The `.rulr` files are JSON rule configurations, not the Rulr app's source code.",
             "", "## Rule directory", "", f"{len(catalog['rules'])} samples. Each has a stable folder containing `README.md` and a same-named `.rulr` file. Categories below use each sample's primary Gallery category."]
    for category in catalog["categories"]:
        entries = sorted((r for r in catalog["rules"] if r["primaryCategory"] == category["id"]), key=lambda r: (r["title"].casefold(), r["slug"]))
        if not entries:
            continue
        lines += ["", f"### {category['label']}", "", "| Rule and instructions | What it does | Website preview |", "| --- | --- | --- |"]
        for rule in entries:
            lines.append(f"| [{table_text(rule['title'])}](rules/{rule['slug']}/) | {table_text(rule['description'])} | [Preview and setup]({SITE}{rule['page']}) |")
    lines += ["", "## Updates and contributions", "", "The website is the source of truth for rule configurations and setup text. This repository mirrors the published catalog daily and supports manual synchronization. It uses only public website URLs, without access to the private website or app repositories.",
              "", "If you find a problem or want another rule, [open an issue](https://github.com/snowfallapps/rulr-rules/issues). Include the rule name, macOS and Rulr versions, expected result, and what happened. Remove private text, file paths, device identifiers, and credentials before sharing a custom rule.",
              "", "Pull requests with fixes or new examples are welcome. Mirrored files may be replaced by synchronization, so rule and documentation changes must also be incorporated into the website source. See [CONTRIBUTING.md](CONTRIBUTING.md).", "", "## License", "", "The examples, documentation, and sync script in this repository are available under the [MIT License](LICENSE). This does not license the Rulr app or its trademarks.", ""]
    return "\n".join(lines)


def validate_catalog(catalog: dict) -> None:
    if catalog.get("version") != 1 or not catalog.get("rules"):
        raise ValueError("Unsupported or empty catalog; leaving existing files unchanged")
    seen = set()
    for rule in catalog["rules"]:
        slug = rule["slug"]
        if not SLUG.fullmatch(slug) or slug in seen:
            raise ValueError(f"Invalid or duplicate slug: {slug}")
        seen.add(slug)
        if rule["download"] != f"/rule-gallery/rules/{slug}.rulr":
            raise ValueError(f"Unexpected download path: {slug}")
        if not re.fullmatch(r"/rules/[a-z0-9-]+/", rule["page"]):
            raise ValueError(f"Invalid detail path: {slug}")
        if not re.fullmatch(r"[a-f0-9]{64}", rule["sha256"]):
            raise ValueError(f"Invalid checksum: {slug}")
        if not rule.get("intro") or not rule.get("documentation"):
            raise ValueError(f"Missing website documentation: {slug}")


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--site-source", type=Path, help="Bootstrap from a local website checkout")
    args = parser.parse_args()
    if args.site_source:
        catalog = source_catalog(args.site_source.resolve())
    else:
        try:
            catalog = json.loads(fetch(CATALOG_URL))
        except HTTPError as error:
            if error.code != 404:
                raise
            print("::warning::Website catalog is not deployed yet. Existing rule mirror left unchanged.")
            return
    validate_catalog(catalog)

    def get_payload(rule: dict) -> tuple[str, bytes]:
        # Bootstrap also verifies every file against the already public website.
        payload = fetch(urljoin(SITE, rule["download"]))
        if hashlib.sha256(payload).hexdigest() != rule["sha256"]:
            raise ValueError(f"Published file changed or is not deployed: {rule['slug']}")
        data = json.loads(payload)
        if not isinstance(data, dict) or not all(k in data for k in ("id", "title", "ruleData")):
            raise ValueError(f"Invalid rule payload: {rule['slug']}")
        return rule["slug"], payload

    with ThreadPoolExecutor(max_workers=6) as executor:
        payloads = dict(executor.map(get_payload, catalog["rules"]))
    # No writes happen until all downloads and checksums have passed.
    rendered = {rule["slug"]: rule_readme(rule) for rule in catalog["rules"]}
    rules_dir = ROOT / "rules"
    rules_dir.mkdir(exist_ok=True)
    for slug, payload in payloads.items():
        folder = rules_dir / slug
        folder.mkdir(exist_ok=True)
        (folder / f"{slug}.rulr").write_bytes(payload)
        (folder / "README.md").write_text(rendered[slug], encoding="utf-8")
    # Keep retired folders available so existing GitHub download URLs do not break.
    (ROOT / "README.md").write_text(repository_readme(catalog), encoding="utf-8")
    (ROOT / "catalog.json").write_text(json.dumps(catalog, ensure_ascii=False, indent=2, sort_keys=True) + "\n", encoding="utf-8")
    print(f"Synced {len(payloads)} rules and READMEs; every payload matches its published SHA-256.")


if __name__ == "__main__":
    main()
