from app.generator import generate_episode
from app.models import GenerateRequest
from app.renderer import RenderEngine

if __name__ == "__main__":
    episode = generate_episode(GenerateRequest(topic="A lost little star", lesson="kindness"))
    result = RenderEngine().build_manifest(episode)
    print(f"Episode: {episode.title}")
    print(f"Scenes: {len(episode.scenes)}")
    print(f"Manifest: {result.manifest_path}")
