def main():
    time = convert(input("What time is it? "))
    if 7 <= time <= 8:
        print("breakfast time")
    elif 12 <= time <= 13:
        print("lunch time")
    elif 18 <= time <= 19:
        print("dinner time")


def convert(time):
    period = None
    if time.endswith(("a.m.", "p.m.")):
        time, period = time.split(" ")

    hours, minutes = time.split(":")
    hours = int(hours)
    minutes = int(minutes)

    if period == "p.m." and hours != 12:
        hours = hours + 12
    elif period == "a.m." and hours == 12:
        hours = 0
    return hours + minutes / 60

if __name__ == "__main__":
    main()