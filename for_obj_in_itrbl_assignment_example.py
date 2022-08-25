# Emy Kay's original off-the-cuff example to explain basics of Python dict, fstring, assignment

p = {"hello": "world",
    "eggs": "spam"}

print(f"before for loop, p == {p}")

for p, v in p.items():
    print(f"{p} , {v}")

print(f"after for loop, p== {p}")
