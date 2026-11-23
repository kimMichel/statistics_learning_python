# Nivel 1

def percentage(part, whole):
    if whole == 0:
        raise ValueError("Whole cannot be zero")
    return (part / whole) * 100

def percentage_change(initial, final):
    if initial == 0:
        raise ValueError("Initial value cannot be zero")
    return ((final - initial) / initial) * 100

def rule_of_three(a, b, c):
    if a == 0:
        raise ValueError("Value 'a' cannot be zero")
    return (b * c) / a

ex01 = percentage(175, 2500)
ex02 = percentage_change(400, 520)
ex03 = rule_of_three(80, 56, 100)

print(f"Percentage: {ex01:.2f}%")
print(f"Percentage Change: {ex02:.2f}%")
print(f"Rule of Three: {ex03:.2f}%")


ex04 = percentage_change(240, 180)
print(f"Percentage Change: {ex04:.2f}%")

ex05 = 18_000 / 120
print(f"Throughput: {ex05:.2f}")

ex06a = 30_000 / 100
ex06b = 45_000 / 180
print(f"Throughput 06a: {ex06a:.2f}")
print(f"Throughput 06b: {ex06b:.2f}")

ex06c = rule_of_three(ex06a, ex06b, 100)
print(f"Percentage difference: {100 - ex06c:.2f}%")

ex07 = (12_500 * 4) / 100
print(f"Expected error number: {ex07:.2f}")

ex08 = (120 * 100) / 40
print(f"Total of vulnerabilities: {ex08:.2f}")

