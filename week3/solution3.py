def minCoins(cash) -> int:

  cash = int(cash.split('.')[0]) * 100 + int(cash.split('.')[1])
  # the above line of code parses the pounds and pence value into only pence

  coins = [5000, 2000, 1000, 500, 200, 100, 50, 20, 10, 5, 2, 1]
  count = 0

  for coin in coins:
    if cash >= coin:
      count += cash // coin
      cash %= coin

  return count


def main():
  print(minCoins(input('Input some money in pounds and pence:\n')))

if __name__ == '__main__':
  main()
  