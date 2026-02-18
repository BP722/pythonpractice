def print_values():
    """Prints the last value of a predefined list of numbers."""
    numbers = [1, 2, 3, 4, 5]
    if not numbers:
        print("The list is empty. No values to print.")
        return
    last_number = numbers[-1]
    print(f"Last number in the list is {last_number}")
def main():
    print_values()
if __name__ == "__main__":    
    main()
