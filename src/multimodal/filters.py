from src.config.settings import VISUAL_TOPICS


def is_visual_topic(topic: str | None) -> bool:
    if not topic:
        return False

    topic = topic.lower().strip()

    return any(keyword in topic for keyword in VISUAL_TOPICS)