# Filename:lambda.py

def make_repeater(n):
    return lambda s: s*n

twice = make_repeater(2)
fifth = make_repeater(5)

print(twice(2))
print(twice('Ok'))
print(fifth(2))
print(fifth('Ok'))
