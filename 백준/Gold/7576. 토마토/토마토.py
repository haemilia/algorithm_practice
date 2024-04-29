import sys
from collections import deque

# Fast input
input = sys.stdin.readline

def bfs(queue, box, N, M):
    # Directions for adjacent cells (left, right, up, down)
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while queue:
        cx, cy = queue.popleft()
        for i in range(4):
            nx = cx + dx[i]
            ny = cy + dy[i]

            # Check boundaries and ripening condition
            if 0 <= nx < N and 0 <= ny < M and box[nx][ny] == 0:
                box[nx][ny] = box[cx][cy] + 1
                queue.append((nx, ny))
    return box

def search(box, N, M):
    result = 0
    for i in range(N):
        for j in range(M):
            if box[i][j] == 0:
                # Found unripe tomato
                return -1
            # Find maximum number of days it took to ripen all tomatoes
            result = max(result, box[i][j])
    return result - 1  # Adjust for day-based indexing

def main():
    # Input and grid setup
    M, N = map(int, input().split())
    boxes = [list(map(int, input().split())) for _ in range(N)]

    # Queue initialization for BFS
    queue = deque()
    ripe_count = 0  # Keep track of ripe tomatoes

    for i in range(N):
        for j in range(M):
            if boxes[i][j] == 1:
                queue.append((i, j))
                ripe_count += 1  # Count ripe tomatoes

    # Handle case where there are no ripe tomatoes initially
    if ripe_count == 0:
        # If there are unripe tomatoes and no ripe tomatoes, return -1
        if any(0 in row for row in boxes):
            print(-1)
            return
        # If there are no unripe tomatoes, everything is already ripened
        else:
            print(0)
            return

    # Apply BFS to propagate ripening
    ripened_boxes = bfs(queue, boxes, N, M)

    # Find the result (days to ripen all tomatoes or -1 if impossible)
    result = search(ripened_boxes, N, M)
    print(result)

# Execute the main function
if __name__ == '__main__':
    main()
