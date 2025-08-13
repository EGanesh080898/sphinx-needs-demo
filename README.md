# Sphinx‑Needs IVC Demo (Online-Editor Friendly)

A tiny, opinionated example showing how to document **requirements**, **architecture**, **implementation**, **tests**, and **process** for an *IVC (Inter‑Vehicle Communication) module* using **Sphinx‑Needs**.

It is set up to work well in a cloud **Online Editor** like **Gitpod** (VS Code in the browser) or locally on your machine.

---

## Quick start (Gitpod — Online Editor)

1. Create an empty GitHub repository (e.g. `ivc-sphinx-needs-demo`).
2. Upload these files to that repo (or push from local with `git`).
3. Open Gitpod for your repo by navigating to:

   ```
   https://gitpod.io/#<YOUR_GITHUB_REPO_URL>
   ```

   Example:
   ```
   https://gitpod.io/#https://github.com/yourname/ivc-sphinx-needs-demo
   ```

4. When the workspace opens, it will install Python deps and start a live Sphinx server.
5. A port (8000) will be exposed automatically — open it to view the docs.
6. Edit files in `docs/` and watch the preview update live.

> If port doesn't open automatically, run in the terminal:
>
> ```bash
> make live
> ```

---

## Quick start (local)

```bash
python -m venv .venv && source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt

# one-off build
make html
# open docs/_build/html/index.html in your browser

# or run live-reload server
make live
```

---

## What’s inside

- **Sphinx-Needs config** in `docs/conf.py` (need types, extra fields).
- **Example needs** in:
  - `docs/ivc_overview.rst`
  - `docs/ivc_requirements.rst`
  - `docs/ivc_architecture.rst`
  - `docs/ivc_impl_and_tests.rst`
  - `docs/process.rst`
- **Dashboards** in `docs/dashboards.rst`
- **`needtable` filters** to show coverage and gaps.

Customize the IDs, tags, and fields to match your project.
