# Production Architecture

```text
Dashboard -> FastAPI -> Episode Orchestrator -> Job Queue
                                  |
                  +---------------+----------------+
                  |               |                |
                 LLM             TTS          Visual/Video
                  |               |                |
                  +---------------+----------------+
                                  |
                            FFmpeg Renderer
                                  |
                       Safety/Quality Gate
                                  |
                           Human Approval
                                  |
                         YouTube Publisher
                                  |
                             Analytics
                                  |
                          Strategy Feedback
```

## Safety gates

- Original characters and story prompts only.
- No automatic reuse of copyrighted scripts, songs, or character likenesses.
- Human approval is mandatory by default.
- Publishing is disabled until OAuth credentials are configured.
- Secrets are environment variables, never source-controlled.

## Provider strategy

All external AI/media services sit behind interfaces in `app/providers.py`. This makes the pipeline provider-agnostic and allows a local demo mode without paid APIs.
