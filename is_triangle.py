def is_triangle(a, b, c):
    condition = a < b + c and b < a + c and c < a + b
    return condition


print(is_triangle(3, 4, 15))
