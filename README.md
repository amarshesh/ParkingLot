# ParkingLot

Lightweight Python implementation of a Parking Lot system (single-process CLI). This repo contains a minimal domain model and a small runner to exercise it.

## Parking Lot System (Python)

A Low Level Design (LLD) implementation of a Parking Lot system in Python. The project models a real-world parking system with floors, parking spots, vehicles, ticketing, pricing strategies, allocation strategies, and payment handling.

This project was built to practice object-oriented design and common design patterns used in system-design interviews.

## Features

- Multi-floor parking lot
- Spot allocation strategies (pluggable)
- Pricing strategies per vehicle type
- Vehicle entry and exit workflow
- Ticket generation and billing
- Payment processing with multiple options
- Display board showing available spots
- Thread-safe allocation (basic concurrency support)
- Modular folder structure for easy extension

## System Architecture (high level)

ParkingLot
 ├── Floors
 │    └── Spots
 │
 ├── Entry / Exit workflow
 │
 ├── Allocation Strategies
 │
 ├── Pricing Strategies
 │
 ├── Payment Service
 │
 └── Display Board

Core entities:

- `Vehicle`
- `Spot`
- `Floor`
- `Ticket`
- `ParkingLot`

## Design Patterns Used

- Strategy Pattern — used for pluggable algorithms (e.g., `SpotAllocationStrategy`, `PricingStrategy`).
- Factory Pattern — used to create or select a pricing/payment strategy dynamically (e.g., `VehiclePricingFactory`, `PaymentFactory`).
- Resolver/Delegator — to select which allocation strategy to use based on vehicle attributes.

## Project Structure

```
parking_lot/

main.py
core/
	parking_lot.py
	spot_class.py
	ticket_class.py
	vehicle_class.py

floors/
gates/
parking_slots_status/
strategies/
	allocation/
	pricing/
	payment/

source/
```

## How to Run

1. Create a virtual environment

```powershell
python -m venv .venv
```

2. Activate the virtual environment (Windows PowerShell)

```powershell
.venv\Scripts\Activate.ps1
```

3. Install dependencies (if any)

```bash
pip install -r requirement.txt
```

4. Run the program

```bash
python main.py
```

## Example Flow

Vehicle enters parking:

Vehicle arrives
↓
ParkingLot receives request
↓
Allocation strategy finds spot
↓
Ticket generated
↓
DisplayBoard updated

Vehicle exits:

Ticket scanned
↓
Parking duration calculated
↓
Pricing strategy applied
↓
Payment processed
↓
Spot released

## Learning Goals

This project demonstrates:

- Object-oriented system design
- Strategy and Factory pattern usage
- Clean separation of responsibilities
- Modular project structure
- Basic concurrency handling

It is intended as a practice project for Low Level Design interviews.

## Future Improvements

Possible enhancements:

- REST API interface
- Database persistence
- Multiple parking gates / distributed coordination
- Admin dashboard and analytics

## Author

Built as a learning project for system-design practice.

If you'd like, I can also suggest three small improvements to make the repository more professional for recruiters (README badges, CI, example unit tests).

## Project structure

- `main.py` — CLI runner and orchestration point (entrypoint).
- `core/` — domain classes: `parking_lot.py`, `spot_class.py`, `ticket_class.py`, `vehicle_class.py`.
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
