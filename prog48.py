r = int(input())
v = list(map(int,input().split()[:r]))
avg = 0
for i in v:
    avg = i+avg
print(int(avg/r))
