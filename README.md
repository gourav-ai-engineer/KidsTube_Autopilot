# KidsTube Autopilot

Production-oriented starter for an original kids YouTube content automation platform.

## Current vertical slice

- FastAPI service and browser dashboard
- Original story/episode generator with reusable character bible
- Episode persistence as JSON for zero-setup local development
- Human approval gate before publication
- Health endpoint and typed Pydantic models
- Clean provider boundary ready for LLM, TTS, image/video, and YouTube adapters

## Run locally

```bash
python -m venv .venv
# Windows: .venv\\Scripts\\activate
pip install -e ".[test]"
uvicorn app.main:app --reload
```

Open `http://127.0.0.1:8000`.

## Roadmap

1. Provider adapters (LLM/TTS/image/video)
2. FFmpeg rendering worker and asset manifests
3. Thumbnail + metadata generation
4. YouTube OAuth upload/scheduling
5. PostgreSQL + Redis queue
6. Analytics feedback loop
7. Docker/CI and production deployment

No credentials are stored in the repository. Publishing remains an explicit human-approved action until the production integrations are validated.
