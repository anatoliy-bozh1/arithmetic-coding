from decimal import Decimal, getcontext
import math

getcontext().prec = 200

FMT = Decimal("1." + "0" * 40)

text = "Божко Анатолий Анатольевич"
message = "".join(text.upper().split())

freq = {}
for c in message:
    if c in freq:
        freq[c] += 1
    else:
        freq[c] = 1

n = len(message)
alphabet = sorted(freq, key=lambda x: freq[x], reverse=True)

left = {}
right = {}
cur = Decimal(0)

print(f"таблица отрезков символов")
print(f"символ | левая граница | правая граница")

for c in alphabet:
    p = Decimal(freq[c]) / Decimal(n)
    left[c] = cur
    right[c] = cur + p
    print(f"{c} | {left[c]:.40f} | {right[c]:.40f}")
    cur = right[c]
print()

L = Decimal(0)
R = Decimal(1)

print(f"таблица шагов кодирования")
print(f"шаг | символ | левая граница | правая граница")
print(f"0 | - | {L:.40f} | {R:.40f}")

step = 1
for c in message:
    width = R - L
    R = L + width * right[c]
    L = L + width * left[c]
    print(f"{step} | {c} | {L.quantize(FMT)} | {R.quantize(FMT)}")
    step += 1
print()

width = R - L
bits = math.ceil(-math.log2(float(width)))
x = (L + R) / 2
binary = format(int(x * (2 ** bits)), f"0{bits}b")

print(f"итоговый отрезок [{L.quantize(FMT)}, {R.quantize(FMT)})")
print(f"бинарный код {binary}")
print(f"длина {bits} бит")
