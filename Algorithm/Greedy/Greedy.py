N = 1280
coin=[10,50,100,500]
coin=sorted(coin,reverse=True)
print(coin)

for i in coin:
    print('%s원 %s개'%(i,N//i))
    N=N%i

activities = [[1, 4], [3, 5], [0, 6], [5, 7], [3, 9], [5, 9], [6, 10], [8, 11], [8, 12], [2, 14], [12, 16]]
activities.sort(key = lambda x: x[1])

print(activities[0])

i = 0
for j in range(1, len(activities)):
    if activities[j][0] >= activities[i][1]:
        print(activities[j])
        i = j