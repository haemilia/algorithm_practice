import sys
input = sys.stdin.readline

def main():
    # get N
    N = int(input())

    # Somewhere to store reservation info
    # If I don't append 
    info = [{"T": 0, "S": 0} for _ in range(366)]
    # Receive input
    max_days = 0
    for i in range(N):
        customer, start, end = input().split()
        start, end = int(start), int(end)
        for day in range(start - 1, end):
            info[day][customer] += 1
        max_days = max(max_days, end - start + 1)
    # Go through info and get the information I need
    more_than_one_customer = 0
    max_customer = 0
    non_fight_days = 0
    non_fight_max_customer = 0
    for day_info in info:
        num_of_customer = sum(day_info.values())
        if num_of_customer> 0:
            more_than_one_customer += 1
            max_customer = max(max_customer, num_of_customer)
            if day_info["T"] == day_info["S"]:
                non_fight_days += 1
                non_fight_max_customer = max(non_fight_max_customer, num_of_customer)

    print(more_than_one_customer)
    print(max_customer)
    print(non_fight_days)
    print(non_fight_max_customer)
    print(max_days)

if __name__ == "__main__":
    main()