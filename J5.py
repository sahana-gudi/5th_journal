import numpy as np
values = np.array([
    float(input("Enter the principal amount: ")),
    float(input("Enter the rate of interest (in %): ")),
    float(input("Enter the time (in years): "))
])

principal, rate, time = values
simple_interest = (principal * rate * time) / 100
print(f"Simple Interest = {simple_interest}")
