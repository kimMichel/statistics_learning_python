metrics = {
    "total_requests": 25000,
    "failed_requests": 750,
    "previous_latency": 250,
    "current_latency": 200,
    "processing_timer": 100
}

def success_rate(metrics):
    total = metrics.get("total_requests", 0)
    failed = metrics.get("failed_requests", 0)
    if total == 0:
        raise ValueError("Total requests cannot be zero")
    return ((total - failed) / total) * 100

def failed_rate(metrics):
    total = metrics.get("total_requests", 0)
    failed = metrics.get("failed_requests", 0)
    if total == 0:
        raise ValueError("Total requests cannot be zero")
    return (failed / total) * 100

def latency_change(metrics):
    previous = metrics.get("previous_latency", 0)
    current = metrics.get("current_latency", 0)
    if previous == 0:
        raise ValueError("Previous latency cannot be zero")
    return ((current - previous) / previous) * 100

def throughput(metrics):
    total = metrics.get("total_requests", 0)
    processing_time = metrics.get("processing_timer", 0)
    if processing_time == 0:
        raise ValueError("Processing time cannot be zero")
    return total / processing_time

def success_requests(metrics):
    total = metrics.get("total_requests", 0)
    failed = metrics.get("failed_requests", 0)
    if total == 0:
        raise ValueError("Total requests cannot be zero")
    return total - failed

print(f"Success Rate: {success_rate(metrics):.2f}%")
print(f"Failed Rate: {failed_rate(metrics):.2f}%")
print(f"Latency Change: {latency_change(metrics):.2f}%")
print(f"Throughput: {throughput(metrics):.2f}")
print(f"Successful Requests: {success_requests(metrics):.2f}")