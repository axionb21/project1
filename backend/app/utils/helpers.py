
def safe_float(v, default=0.0):
    try:
        return float(v)
    except:
        return default
