# System Specification

## Purpose

This repository contains the SYSEN 5151 Team 12 project. The initial system
demonstrates communication between a Streamlit frontend and a FastAPI backend.

## Components

- `Backend/main.py`: exposes the application API.
- `Frontend/app.py`: displays project information and data returned by the API.
- `tests/`: contains automated checks for expected behavior.
- `docs/`: records project context, environment details, prompts, and decisions.

## Current Behavior

1. The backend serves `GET /` on `http://127.0.0.1:8000`.
2. The endpoint returns a JSON object containing the Lab 0 message.
3. The frontend requests that endpoint and displays its message.

## Acceptance Criteria

- The backend starts without errors.
- `GET /` returns HTTP 200 and the expected message.
- The frontend starts without errors when the backend is available.
- Team and development documentation remains current as the project evolves.
