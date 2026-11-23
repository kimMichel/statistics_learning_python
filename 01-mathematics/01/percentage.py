def percentage(part, total):
    if total == 0:
        raise ValueError("Total cannot be zero")

    return (part / total) * 100

errors = 35
requests = 500

error_rate = percentage(errors, requests)

print(f"Error rate: {error_rate:2.2f}%")