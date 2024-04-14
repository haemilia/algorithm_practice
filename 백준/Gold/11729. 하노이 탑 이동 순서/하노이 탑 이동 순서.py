n = int(input())
k = 2 ** n - 1
def hanoi(n, a, b, c):
    if n == 1:
        print(a, c)
        return
    hanoi(n-1, a, c, b)
    print(a, c)
    hanoi(n-1, b, a, c)

print(k)
hanoi(n, 1, 2, 3)