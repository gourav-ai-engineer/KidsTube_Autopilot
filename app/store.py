from pathlib import Path
import json
from .models import Episode

ROOT = Path("data/episodes")

def save_episode(episode: Episode) -> None:
    ROOT.mkdir(parents=True, exist_ok=True)
    (ROOT / f"{episode.id}.json").write_text(
        json.dumps(episode.model_dump(mode="json"), indent=2), encoding="utf-8"
    )

def load_episodes() -> list[Episode]:
    if not ROOT.exists():
        return []
    episodes = []
    for path in sorted(ROOT.glob("*.json")):
        try:
            episodes.append(Episode.model_validate_json(path.read_text(encoding="utf-8")))
        except Exception:
            continue
    return episodes
