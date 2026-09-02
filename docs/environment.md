# Development Environment

## Prerequisites

- Git
- Python 3.11 or newer

## Setup

From the repository root:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
```

## Run

Start the backend:

```powershell
python -m uvicorn Backend.main:app --reload
```

In a second terminal, start the frontend:

```powershell
python -m streamlit run Frontend/app.py
```

## Test

```powershell
python -m pytest
```
