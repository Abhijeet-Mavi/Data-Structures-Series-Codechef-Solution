def months_Required(act, n, origin):
    laddus = divisor = 0
    for i in range(n):
        if act[i][0] == "CONTEST_WON":
            if int(act[i][1]) < 20:
                laddus += (300+(20-int(act[i][1])))
            else:
                laddus += 300
        elif act[i][0] == "TOP_CONTRIBUTOR":
            laddus += 300
        elif act[i][0] == "BUG_FOUND":
            laddus += int(act[i][1])
        elif act[i][0] == "CONTEST_HOSTED":
            laddus += 50
    if origin == "INDIAN":
        divisor = 200
    else:
        divisor = 400
    return int(laddus/divisor)

if __name__ == "__main__":
    t = int(input())
    while t > 0:
        n_and_origin = list(map(str, input().split()))
        activities = list()
        for i in range(int(n_and_origin[0])):
            act = list(map(str, input().split()))
            activities.append(act)
        print(months_Required(activities, int(
            n_and_origin[0]),n_and_origin[1]))
        t -= 1
