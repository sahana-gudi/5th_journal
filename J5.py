import sys

# If arguments are provided, use them
if len(sys.argv) == 4:
    P = float(sys.argv[1])   # Principal
    R = float(sys.argv[2])   # Rate of interest (%)
    T = float(sys.argv[3])   # Time (years)
else:
    # Fall back to interactive input
    P = float(input("Enter principal amount: "))
    R = float(input("Enter rate of interest (%): "))
    T = float(input("Enter time (years): "))

# Calculate Simple Interest
SI = (P * R * T) / 100

# Output
print("Simple Interest =", SI)
