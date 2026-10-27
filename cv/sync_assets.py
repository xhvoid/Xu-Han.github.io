"""Publish a compiled two-page CV and regenerate its previews and cache keys."""
from pathlib import Path
import argparse
import hashlib
import re
import shutil
import subprocess
import tempfile

from pypdf import PdfReader

parser = argparse.ArgumentParser(description=__doc__)
parser.add_argument("pdf", type=Path)
parser.add_argument("--pdftoppm", default="pdftoppm")
parser.add_argument("--date", required=True, help="Visible update date, e.g. 24 October 2026")
args = parser.parse_args()
site = Path(__file__).resolve().parents[1]
if len(PdfReader(args.pdf).pages) != 2:
    raise ValueError("The CV must contain exactly two pages; no assets were replaced.")

with tempfile.TemporaryDirectory() as directory:
    prefix = Path(directory) / "page"
    subprocess.run([args.pdftoppm, "-scale-to", "1800", "-png", str(args.pdf), str(prefix)], check=True)
    assets = [(args.pdf, site / "files/Xu_Han_CV.pdf")]
    assets += [(Path(f"{prefix}-{n}.png"), site / f"images/cv/xu-han-cv-page-{n}.png") for n in (1, 2)]
    page = site / "_pages/cv.md"
    text = page.read_text()
    for source, destination in assets:
        key = hashlib.sha256(source.read_bytes()).hexdigest()[:12]
        relative = "/" + str(destination.relative_to(site))
        text = re.sub(re.escape(relative) + r"\?v=[a-zA-Z0-9]+", relative + "?v=" + key, text)
        shutil.copyfile(source, destination)
    text = re.sub(r"\*Updated [^*]+\.\*", f"*Updated {args.date}.*", text)
    page.write_text(text)
print("Synchronized final PDF, both rendered previews and all CV cache keys.")
