
N = 2300
coins = (500,100,50,10)
count = 0
money = N
# z  = 0
for coin in coins:
  count+= money // coin
  money %=coin
print(count)