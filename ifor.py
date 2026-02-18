def print_triangle(n):
    n = int(input("Enter the number of rows for the triangle: "))
    for i in range(1, n + 1):
        print('*' * i)
print_triangle(5)