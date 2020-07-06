def operations(operator, x, y):
    return {
        'add': lambda: x+y,
        'sub': lambda: x-y,
        'mul': lambda: x*y,
        'div': lambda: x/y}.get(operator, lambda: 'Not a valid operation')()


a = operations("mul", 2,8)
print(a)