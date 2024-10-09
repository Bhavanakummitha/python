def is_perfect(n):
    divisors_sum = sum(i for i in range(1, n) if n % i == 0)
    return divisors_sum == n

def find_perfect_numbers(limit):
    perfect_numbers = [n for n in range(1, limit + 1) if is_perfect(n)]
    return perfect_numbers


