# CV source and assets

This uses the existing two-page LaTeX template and Python generator, brought
into the repository from the working source matching the public CV on
2026-10-24. It is not reconstructed from a different PDF.

- `content.json`: editable content; retain verified dates and qualifications.
- `template.tex`: existing preamble and contact header (10 pt, 2 cm margins).
- `build.py`: generates `Xu_Han_CV.tex` and a matching editable Markdown copy.
- `sync_assets.py`: requires `pypdf` and Poppler; checks the two-page count,
  renders both previews from the compiled PDF, and updates download cache keys.

From the repository root:

```sh
python3 cv/build.py
mkdir -p local/cv-build
tectonic -X compile --untrusted --keep-logs -o local/cv-build cv/Xu_Han_CV.tex
python3 cv/sync_assets.py local/cv-build/Xu_Han_CV.pdf --date '24 October 2026'
bundle exec jekyll build
```

For a later revision, update the visible date in `template.tex` and pass that
same date to the synchronization command. Inspect both rendered pages before
publishing. `--pdftoppm /absolute/path/to/pdftoppm` supports a bundled Poppler.
The `cv/` source directory is excluded from the generated public website;
only the PDF, preview PNGs and public page are published. Build logs and
temporary files belong under ignored `local/`, never under `files/`.
