import sys

if len(sys.argv) != 4:
    print("Usage: python simple_interest.py <principal> <rate> <time>")
    sys.exit(1)

P = float(sys.argv[1])
R = float(sys.argv[2])
T = float(sys.argv[3])

si = (P * R * T) / 100

print("Simple Interest:", si)
