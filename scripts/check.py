"""Check navigation, source cards and the published exercise result offline."""
import re
import subprocess
import sys
from pathlib import Path
from urllib.parse import unquote, urlsplit

ROOT = Path(__file__).resolve().parents[1]
errors = []
library = ROOT / "library"
index = (library / "README.md").read_text()
cards = sorted(library.glob("*/README.md"))
if not cards:
    errors.append("The reading library has no cards")
for card in cards:
    if f"]({card.relative_to(library)})" not in index:
        errors.append(f"Unlisted source card: {card}")
    content = card.read_text()
    if not re.search(r"github\.com/[\w.-]+/[\w.-]+/tree/[a-f0-9]{40}\)", content):
        errors.append(f"Missing pinned revision: {card}")
    if "Upstream licence at the reviewed revision:" not in content:
        errors.append(f"Missing source terms: {card}")

for doc in ROOT.rglob("*.md"):
    for link in re.findall(r"\]\(([^)\s]+)\)", doc.read_text()):
        url = urlsplit(link)
        if url.scheme or url.netloc:
            continue
        target = (doc.parent / unquote(url.path)).resolve() if url.path else doc
        if not target.is_relative_to(ROOT) or not target.is_file():
            errors.append(f"{doc.relative_to(ROOT)}: broken link {link}")

exercise = ROOT / "exercises/intake"
result = subprocess.run(
    [sys.executable, str(exercise / "score.py"), str(exercise / "baseline.csv")],
    capture_output=True, text=True,
)
expected_totals = ["Exact matches: 5/8", "Required reviews missed: 3/4", "Queue suggestions: 7/8"]
if result.returncode or result.stdout.splitlines()[-3:] != expected_totals:
    errors.append("The baseline result differs from the worked example")

if errors:
    sys.exit("\n".join(errors))
print(f"Checked local links, {len(cards)} source cards and the worked example.")
