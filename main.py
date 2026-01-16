from datetime import datetime

def iso_to_millis(iso_time):
    dt = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%S.%fZ")
    return int(dt.timestamp() * 1000)

# IMPLEMENT: format 1 → unified format
def transform_format_1(item):
    return {
        "name": item["name"],
        "value": item["value"],
        "timestamp": iso_to_millis(item["timestamp"])
    }

# IMPLEMENT: format 2 → unified format
def transform_format_2(item):
    return {
        "name": item["metric"],
        "value": item["reading"],
        "timestamp": item["ts"]
    }
