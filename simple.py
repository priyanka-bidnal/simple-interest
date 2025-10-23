P = float(input("Enter Principal amount: ₹"))
R = float(input("Enter Rate of Interest (%): "))
T = float(input("Enter Time (in years): "))

SI = (P * R * T) / 100
CI = P * ((1 + R / 100) ** T) - P

print(f"Simple Interest: ₹{SI}")

print(f"Compound Interest: ₹{CI}")
