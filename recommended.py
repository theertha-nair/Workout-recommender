import pandas as pd
import random
from typing import Dict, List


def load_exercises(path: str = "data\exercises.csv") -> pd.DataFrame:
    """Load the exercises dataset."""
    return pd.read_csv(path)


def filter_exercises(user: Dict, df: pd.DataFrame) -> pd.DataFrame:
    """Filter exercises by user profile (level, goal, equipment)."""
    mask = (df["level"] == user["level"]) & (df["goal"] == user["goal"])
    filtered = df[mask]

    if user["equipment"]:
        filtered = filtered[filtered["equipment"].isin(user["equipment"])]

    return filtered


def generate_plan(user: Dict, df: pd.DataFrame) -> Dict[str, List[Dict]]:
    """Generate a workout plan with dicts of exercise details."""
    filtered = filter_exercises(user, df)

    plan = {}
    for day in range(1, user["days"] + 1):
        exercises = filtered.sample(n=min(4, len(filtered)), replace=False).to_dict(orient="records")
        plan[f"Day {day}"] = exercises

    return plan
