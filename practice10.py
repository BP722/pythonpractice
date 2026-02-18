#You are given this messy Python snippet:

 
# messy.py (do not execute this block)
# numbers=[1,2,3,4,5]
# def PrintLastNumber(v):print("Last number in the list is "+str(v[len(v)-1]))
# PrintLastNumber(numbers);exit(5)
 
# Your tasks:

# At the top of your file, make a commented list of at least 7 problems with this code (naming, style, exit code, lack of error handling, etc.).
# 1. Variable name 'numbers' is not descriptive.
# 2. Function name 'PrintLastNumber' is not descriptive and doesn't follow PEP 8 naming conventions.
# 3. The function doesn't return anything, it just prints.
# 4. The exit code is hardcoded to 5, which is not a good practice.
# 5. No error handling for empty lists.
# 6. No docstring to explain what the function does.
# 7. The code uses string concatenation instead of f-strings.

# Rewrite the code so it follows class conventions (PEP 8, clear names, docstrings, safe handling of empty list, f-strings, etc.).
# Keep the intended behavior: print the last number in the list.

# 1. PEP 8 Naming: 'PrintLastNumber' uses PascalCase; functions should be snake_case.
# 2. Fragility: Accessing v[len(v)-1] will raise an IndexError if the list is empty.
# 3. Hardcoded Exit: exit(5) is arbitrary and prevents the script from being imported elsewhere.
# 4. String Formatting: Uses '+' concatenation which is less readable than f-strings.
# 5. Type Hinting: No indication of what 'v' is supposed to be, making it harder for IDEs to help.
# 6. Documentation: Lack of a docstring makes the intent unclear to other developers.
# 7. Global Execution: The code runs immediately on import rather than using an 'if __name__ == "__main__":' block.
import sys
from typing import List, Any

def print_last_element(items: List[Any]) -> None:
    """
    Identifies and prints the final element of a provided list.

    Args:
        items: A list of elements of any type.
    
    Returns:
        None. Prints a message to stdout or an error message if the list is empty.
    """
    if not items:
        print("Error: The list is empty. There is no last element to display.")
        return
    
    last_item = items[-1]
    print(f"Last number in the list is {last_item}")

def main() -> None:
    """Main entry point for the script."""
    sample_numbers = [1, 2, 3, 4, 5]
    print_last_element(sample_numbers)

if __name__ == "__main__":
    main()