def calculate_rate(quantity, time):
    if time == 0:
        raise ValueError("Time cannot be zero")

    return quantity / time

requests = 12_000
seconds = 60

rate = calculate_rate(requests, seconds)
print(f"Throughput: {rate:2.2f} requests per second")