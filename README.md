# ParkingLot

Lightweight Python implementation of a Parking Lot system (single-process CLI). This repo contains a minimal domain model and a small runner to exercise it.

## Quick start

1. Create and activate the virtual environment (Windows PowerShell):

```powershell
& "d:\\LLD PRACTICE\\ParkingLot\\.venv\\Scripts\\Activate.ps1"
```

2. Install dependencies:

```bash
pip install -r requirement.txt
```

3. Run the app:

```bash
python parking_lot.py
```

## Project structure

- `parking_lot.py` — CLI runner and orchestration point (entrypoint).
- `spot_class.py` — spot-related domain logic (types/capacity).
- `ticket_class.py` — ticket lifecycle and printing logic.
- `vehicle_class.py` — vehicle model and validation.
- `source/` — supplemental helpers and utilities (inspect before changing).
- `requirement.txt` — runtime dependencies.

## Developer notes

- Architecture: small, single-responsibility modules. Core orchestration lives in `parking_lot.py`; most behavior is implemented inside the domain classes listed above.
- State: in-memory data structures only. There is no DB or external service integration.
- Conventions: snake_case filenames, one main class or concept per file. Prefer adding behavior to the relevant class file rather than creating wide utility modules.

## Making changes

- To add a new spot type or capacity rule, edit `spot_class.py` and update initialization in `parking_lot.py`.
- To change ticket behavior (issue/close/print), update `ticket_class.py` and callers in `parking_lot.py`.
- Add any new integrations or persistence behind a clear adapter in `source/` and document required environment variables.

## Tests

There are no automated tests included. Add tests next to modules you change.

## For AI coding agents

- See [.github/copilot-instructions.md](.github/copilot-instructions.md) for repository-specific guidance and examples for making small, focused edits.

If you want the README expanded (examples, usage scenarios, or a developer checklist), tell me which sections to expand.
