# Python Program that prints the reversed version of a string.

# option 1
s = "Hello"

print(s[::-1])

# option 2

s = "hello"
reversed_word = s[::-1]
print(reversed_word)

# option 3

s = "hello"
reversed_word = "" .join(reversed(s))
print(reversed_word)
