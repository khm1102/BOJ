def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome(num):
    num_str = str(num)
    return num_str == num_str[::-1]

def find_smallest_palindrome_prime(N):
    num = N
    while True:
        if is_prime(num) and is_palindrome(num):
            return num
        num += 1

if __name__ == "__main__":
    N = int(input())
    result = find_smallest_palindrome_prime(N)
    print(result)
