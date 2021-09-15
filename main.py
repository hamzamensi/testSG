# This is a sample Python script.

# Press Maj+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def gcd(numbers: list):
    great_divisor = 1
    for i in range(2, min(numbers) + 1):
        if max(numbers) % i == 0 and min(numbers) % i == 0:
            great_divisor = i
    return great_divisor


def test_profit(numbers):
    min_index = 0
    max_index = 0
    max_profit = 0
    for i in range(0, len(numbers)):
        for j in range(i+1, len(numbers)):
            if numbers[j] - numbers[i] > max_profit:
                max_profit = numbers[j] - numbers[i]
                min_index = i
                max_index = j
    return max_profit, min_index, max_index


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print(gcd([2, 3, 5, 8]))
    print(gcd([3, 3]))
    print(gcd([5, 4, 9]))
    profit, buy_day, sell_day = test_profit([18, 15, 10, 5, 9, 6, 24, 2, 16])
    print('you must buy at ', buy_day, 'st day and sell at', sell_day, 'st day and you will have a profit =', profit)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
