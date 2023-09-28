N, K = input().split(" ")
N = int(N)
K = int(K)

coins = []
for i in range(N):
    coin = int(input())
    if coin <= K:
        coins.append(coin)

coins.reverse()

count = 0
for coin in coins:
    count += K // coin
    K = K % coin
    #print(count, coin)


print(count)
        
