# python3
def MaxPairwiseProduct(numbers):
    n = len(numbers)
    maximum = 0
    for first in range(n):
        for second in range(first + 1, n):
            maximum = max(maximum,numbers[first] * numbers[second])

    return maximum


if __name__ == '__main__':
    num = int(input())
    number = [int(x) for x in input().split()]
    print(MaxPairwiseProduct(number))
