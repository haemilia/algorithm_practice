N = int(input())
times = [tuple(map(int, input().split()))for _ in range(N)]

times.sort(key=lambda x: (x[1], x[0]))


count = 0
end_time = -1
for meeting in times:
    if end_time <= meeting[0]:
        count+= 1
        end_time = meeting[1]

print(count)