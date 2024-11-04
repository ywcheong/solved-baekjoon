def is_palindrome(n):
    return list(reversed(str(n))) == list(str(n))

# Testing True
assert is_palindrome(1)
assert is_palindrome(22)
assert is_palindrome(313)
assert is_palindrome(4224)
assert is_palindrome(54345)

# Testing False
assert not is_palindrome(21)
assert not is_palindrome(312)
assert not is_palindrome(4234)
assert not is_palindrome(4223)
assert not is_palindrome(53125)

while True:
    n = int(input())

    if n == 0:
        break

    print("yes" if is_palindrome(n) else "no")
