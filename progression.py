from typing import Dict, List


def progress_exercise(ex: Dict, week: int) -> Dict:
    """Apply progression rules to a single exercise and return updated dict."""
    ex = ex.copy()
    sets = int(ex.get("default_sets", 3))
    reps = int(ex.get("default_reps", 10))
    unit = ex.get("default_rep_unit", "reps")

    if unit == "reps":
        ex["progressed_sets"] = sets
        ex["progressed_reps"] = reps + week

    elif unit == "seconds":
        ex["progressed_sets"] = sets
        ex["progressed_time"] = reps + (week * 5)

    elif unit == "kg":
        base_weight = ex.get("base_weight", 20)
        ex["progressed_sets"] = sets
        ex["progressed_reps"] = reps
        ex["progressed_weight"] = base_weight + (2.5 * week)

    return ex


def progress_plan(plan: Dict[str, List[Dict]], week: int) -> Dict[str, List[Dict]]:
    """Apply progression to the full plan, returning updated dicts."""
    progressed = {}
    for day, exercises in plan.items():
        progressed[day] = [progress_exercise(ex, week) for ex in exercises]
    return progressed
