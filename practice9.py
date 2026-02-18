# Write a program that repeatedly asks the user for an integer between 1 and 345 inclusive.
from __future__ import annotations

def classify(n: int) -> str:
    if n % 28 == 0:
        return "QuadSept"
    if n % 4 == 0:
        return "Quad"
    if n % 7 == 0:
        return "Sept"
    return str(n)

def main() -> None:
    prompt = "Enter integer between 1 and 345 (outside range to exit): "
    while True:
        s = input(prompt).strip()
        try:
            n = int(s)
        except ValueError:
            print("Invalid input; please enter an integer.")
            continue

        if not (1 <= n <= 345):
            print("Exiting.")
            break

        print(classify(n))

if __name__ == "__main__":
    main()