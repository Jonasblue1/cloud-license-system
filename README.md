# Cloud-Native License Management System

Hybrid cloud license tracking using Azure Arc principles, FastAPI backend, and lightweight dashboard.

## Run locally (Python)
cd backend
pip install -r requirements.txt
uvicorn main:app --reload

## Run with Docker
docker compose up --build

## Agent
Run PowerShell:
.\collect.ps1
