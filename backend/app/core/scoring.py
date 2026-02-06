
def final_drift_status(score: float):
    if score < 0.2:
        return "stable"
    elif score < 0.5:
        return "warning"
    else:
        return "drifting"
