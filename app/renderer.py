from dataclasses import dataclass
from pathlib import Path
import json
from app.models import Episode

@dataclass(frozen=True)
class RenderResult:
    episode_id: str
    manifest_path: str
    status: str = "render-manifest-ready"

class RenderEngine:
    """Provider-neutral renderer boundary.

    Real media providers can consume this manifest and produce MP4 assets. The
    manifest-first design keeps API orchestration testable without API keys.
    """
    def build_manifest(self, episode: Episode, output_dir: Path = Path("data/renders")) -> RenderResult:
        output_dir.mkdir(parents=True, exist_ok=True)
        manifest = {
            "episode_id": episode.id,
            "title": episode.title,
            "aspect_ratio": "16:9",
            "resolution": "1920x1080",
            "scenes": [s.model_dump() for s in episode.scenes],
            "next_steps": ["generate_visual_assets", "generate_voiceover", "mix_audio", "compose_mp4"],
        }
        path = output_dir / f"{episode.id}.json"
        path.write_text(json.dumps(manifest, indent=2), encoding="utf-8")
        return RenderResult(episode.id, str(path))
