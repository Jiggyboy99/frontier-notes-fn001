
"""
FN-001 | Evaluation Pipeline
Initial scaffold for comparing evaluation conditions.
"""

from pathlib import Path
import json

DATA_PATH = Path("data/sample_scenarios.jsonl")


def load_dataset(path):
    """Load evaluation scenarios from JSONL."""
    scenarios = []

    with open(path, "r", encoding="utf-8") as file:
        for line in file:
            if line.strip():
                scenarios.append(json.loads(line))

    return scenarios


def summarize_dataset(scenarios):
    """Summarize scenario categories and evaluation conditions."""
    print(f"Total scenarios: {len(scenarios)}")

    conditions = {}
    for scenario in scenarios:
        condition = scenario.get("condition", "unknown")
        conditions[condition] = conditions.get(condition, 0) + 1

    print("\nScenarios by condition:")
    for condition, count in conditions.items():
        print(f"  {condition}: {count}")


def main():
    if not DATA_PATH.exists():
        print(f"Dataset not found: {DATA_PATH}")
        print("Create the dataset before running this experiment.")
        return

    scenarios = load_dataset(DATA_PATH)
    summarize_dataset(scenarios)


if __name__ == "__main__":
    main()
