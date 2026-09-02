# ADR 0001: Initial Toolchain

- Status: Accepted
- Date: 2026-09-02

## Context

The team needs a small, understandable toolchain for building an initial
client-server prototype in Python.

## Decision

Use FastAPI for the backend API, Uvicorn as the development server, Streamlit
for the frontend, Requests for HTTP communication, and Pytest for automated
tests.

## Consequences

- The whole prototype can be developed in Python.
- Frontend development is fast, but Streamlit offers less control than a
  dedicated browser framework.
- The backend and frontend run as separate local processes.
- Dependencies must be installed from `requirements.txt`.
