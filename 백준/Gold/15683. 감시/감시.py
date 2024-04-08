import sys
input = sys.stdin.readline
from itertools import product
from copy import deepcopy

def mark_not_blind(blind_cnt, x, y, room_map, dxdy, direction):
    dx, dy = dxdy[direction]
    N = len(room_map)
    M = len(room_map[0])
    while x > -1 and y > -1 and x < N and y < M:
        if room_map[x][y] == 6:
            break
        elif room_map[x][y] == 0:
            room_map[x][y] = -1
            blind_cnt -= 1
        x += dx
        y += dy
    return blind_cnt, room_map

N, M = map(int, input().split())
room = [] # Store information about the room
cctv_spots = [] # Get location imformation about each CCTV
cctv_5 = []
blind_spot = 0


for i in range(N): 
    row = list(map(int, input().split())) #Store room information in room
    room.append(row)
    for j, item in enumerate(row):
        if item== 0: # If it isn't CCTV or wall, ignore
            blind_spot += 1
        elif item == 5:
            cctv_5.append((i, j))
        elif 1 <= item and item < 5:
            cctv_spots.append((i,j)) 

dxdy = [(0, 1), (0,-1), (-1, 0), (1, 0)] # up, down, left, right
directions = {
    4: [[0, 2, 3], [0, 1, 2], [1, 2, 3], [0, 1, 3]],
    3: [[0, 2], [0, 3], [1, 2], [1, 3]],
    2: [[0, 1], [2, 3]],
    1: [[0], [1], [2], [3]]
}
# Mark cctv_5
if cctv_5:
    for cctv in cctv_5:
        x, y = cctv
        for direction in [0, 1, 2, 3]:
            blind_spot, room = mark_not_blind(blind_spot, x, y, room, dxdy, direction)

product_lst = []
for cx, cy in cctv_spots:
    product_lst.append(directions[room[cx][cy]])
possible_config = list(product(*product_lst))

min_blind_spot = blind_spot
for config in possible_config:
    cur_blind_spot = blind_spot
    room_copy = deepcopy(room)
    for cctv_id, cctv_dir in enumerate(config):
        cx, cy = cctv_spots[cctv_id]
        for direction in cctv_dir:
            cur_blind_spot, room_copy = mark_not_blind(cur_blind_spot, cx, cy, room_copy, dxdy, direction)
    min_blind_spot = min(min_blind_spot, cur_blind_spot)

print(min_blind_spot)           
