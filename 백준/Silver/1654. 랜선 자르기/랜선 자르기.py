import sys

input = sys.stdin.readline

def can_divide(cur_lan_length, og_lans, N):
    checksum = 0
    for lan in og_lans:
        checksum += lan // cur_lan_length
    if checksum >= N:
        return True
    return False

def is_max_len(cur_lan_length, og_lans, N):
    if not can_divide(cur_lan_length, og_lans, N):
        return False, False
    elif can_divide(cur_lan_length + 1, og_lans, N):
        return False, True
    else:
        return True, True
    
def parametric_binary_search(start:int, end:int, check_condition, necessary_parameters:list):
    while start <= end:
        mid = (start + end) // 2
        satisfy_all_condition, go_up= check_condition(mid, *necessary_parameters)
        if satisfy_all_condition and go_up:
            return mid
        elif (not satisfy_all_condition) and go_up:
            start = mid + 1
        else:
            end = mid - 1


K, N = map(int, input().split())
og_lans = []
for _ in range(K):
    og_lans.append(int(input()))

start = 1
end = sum(og_lans) // N

result = parametric_binary_search(start, end, is_max_len, [og_lans, N])
print(result)
