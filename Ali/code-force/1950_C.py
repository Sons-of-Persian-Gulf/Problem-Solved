for _ in range(int(input())):
    t = input().split(":")
    hour = t[0]
    minute = t[1]
    if 0 < int(hour) < 12:
        print(f"{hour}:{minute} AM")
    elif hour == "00":
        print(f"{12}:{minute} AM")
    elif hour == "12":
        print(f"{hour}:{minute} PM")
    else:
        hour = str(int(hour) - 12).zfill(2)
        print(f"{hour}:{minute} PM")