import re
from .models import Episode, GenerateRequest, Scene, Status

CHARACTERS = ["Milo the panda", "Pip the rabbit", "Tara the turtle", "Nia the fox"]


def _slug(text: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")


def generate_episode(req: GenerateRequest) -> Episode:
    topic = req.topic.strip()
    lesson = req.lesson.strip().lower()
    scenes = []
    beats = [
        f"Meet the friends as they discover {topic}.",
        f"The friends notice a small problem involving {topic}.",
        f"They pause, listen, and think of a safe solution.",
        f"Everyone works together and practices {lesson}.",
        f"The friends see how their choice helps someone else.",
        f"They celebrate and repeat the lesson in a simple way.",
    ]
    beats = beats[: req.scene_count]
    for i, beat in enumerate(beats, 1):
        character = CHARACTERS[(i - 1) % len(CHARACTERS)]
        scenes.append(Scene(
            number=i,
            narration=f"{beat} {character} says, 'We can learn and help together!'",
            visual_prompt=(f"Bright original 3D children's animation, {character}, "
                           f"friendly rounded shapes, {topic}, safe classroom/storybook setting, "
                           "no copyrighted characters, wholesome, expressive faces."),
            duration_seconds=8,
        ))
    title = f"{topic.title()}: A Little Lesson in {lesson.title()}"
    return Episode(
        title=title,
        lesson=lesson,
        age_range=req.age_range,
        status=Status.READY,
        description=(f"An original story for ages {req.age_range} about {lesson}. "
                     "Created with KidsTube-Autopilot and reviewed before publishing."),
        tags=[_slug(topic), _slug(lesson), "kids stories", "educational", "original animation"],
        scenes=scenes,
    )
