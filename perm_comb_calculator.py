import math


def calculate_permutation(n: int, r: int) -> int:
    return math.perm(n, r)  # Python 3.8+


def calculate_combination(n: int, r: int) -> int:
    return math.comb(n, r)  # Python 3.8+


def main():
    print("📊 Permutations and Combinations Calculator")

    try:
        n = int(input("Enter n (total items): "))
        r = int(input("Enter r (items to choose or arrange): "))

        if n < 0 or r < 0:
            raise ValueError("n and r must be non-negative integers.")
        if r > n:
            raise ValueError("r cannot be greater than n.")

        p = calculate_permutation(n, r)
        c = calculate_combination(n, r)

        print(f"\nPermutation P({n}, {r}) = {p}")
        print(f"Combination C({n}, {r}) = {c}")

    except ValueError as e:
        print(f"❌ Input Error: {e}")


if __name__ == "__main__":
    main()
