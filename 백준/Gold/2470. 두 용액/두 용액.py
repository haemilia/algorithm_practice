import sys
input = sys.stdin.readline

n = int(input())
sol = list(map(int, input().split()))

sol.sort()

left = 0
right = n-1

min_sum = abs(sol[-1] + sol[0])
min_pair = [sol[0], sol[-1]]

while left < right:
    cur_sum = sol[left] + sol[right]
    
    if abs(cur_sum) < min_sum:
        min_sum = abs(cur_sum)
        min_pair = [sol[left], sol[right]]
    if cur_sum < 0:
        left += 1
    else:
        right -= 1

print(*min_pair)