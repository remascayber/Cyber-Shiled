import json
import os

HISTORY_FILE = os.path.join(
    os.path.dirname(__file__), "history.json"
)

def save_analysis(risk_level):
    history = load_history()
    history.append({"level": risk_level})

    with open(HISTORY_FILE, "w", encoding="utf-8") as file:
        json.dump(history, file, indent=4)


def load_history():
    if not os.path.exists(HISTORY_FILE):
        return []

    with open(HISTORY_FILE, "r", encoding="utf-8") as file:
        return json.load(file)


def get_statistics():
    history = load_history()

    return {
        "total": len(history),
        "low": sum(
            1 for item in history
            if "low" in item["level"].lower()
        ),
        "medium": sum(
            1 for item in history
            if "medium" in item["level"].lower()
        ),
        "high": sum(
            1 for item in history
            if "high" in item["level"].lower()
        )
    }