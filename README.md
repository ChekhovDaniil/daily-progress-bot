# Daily Progress Bot

## Development setup

Install [uv](https://docs.astral.sh/uv/) if it is not already installed, then
run these commands from the project directory in PowerShell:

```powershell
uv sync --extra dev
uv run pytest tests/tests.py
```

`uv sync` creates or updates the local `.venv` and installs the runtime and
development dependencies. To activate the environment manually:

```powershell
.venv\Scripts\Activate.ps1
```

The project currently contains task storage, service logic, and command
handlers. Telegram polling and message routing are not wired up yet.
