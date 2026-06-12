# Flask Demo

Minimal Flask demo app with a few tiny utility functions and routes.

Quick start (PowerShell):

```powershell
python -m venv .venv; .\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; python app.py
```

Endpoints:
- `/` : demo home page
- `/hello/<name>` : renders a greeting
- `/api/add?a=1&b=2` : returns JSON with the sum

Run tests:

```powershell
.\.venv\Scripts\Activate.ps1; pip install -r requirements.txt; pytest -q
```
