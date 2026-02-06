
def calculate_drift(current_avg, baseline_avg):
    if baseline_avg == 0:
        return 0
    return abs(current_avg - baseline_avg) / baseline_avg
