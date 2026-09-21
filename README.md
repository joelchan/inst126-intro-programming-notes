# inst126-intro-programming-notes

I ([Joel Chan](http://joelchan.me/)) am experimenting with hosting lecture notes for INST126 (Intro to Programming for Information Science) in [Jupyter Book](https://jupyterbook.org) format, for enhanced usability and searchability. 

This is an ongoing work in progress. 

Test update.

## Building locally

Requires [uv](https://docs.astral.sh/uv/) (or any way to get a Python 3.11 venv — 3.11 is what CI uses).

```bash
cd 2-Notes
uv venv --python 3.11 .venv
uv pip install -r requirements.txt
.venv/bin/jupyter-book build .
open _build/html/index.html
```

Notes:

- `execute_notebooks: auto` in `_config.yml` means every `.md` chapter is executed at build time (they have no stored outputs). **If a code cell raises, execution halts and every cell after it in that chapter renders blank on the live site** — so watch the build log for `CellExecutionError`, and check `_build/html/reports/*.err.log` for the traceback.
- `_build/` and `.venv/` are already gitignored.
- Force a full re-execute with `.venv/bin/jupyter-book build . --all`.
