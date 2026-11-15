def main():
    answer = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").strip().lower()
    if is_yes(answer):
        print("Yes")
    else:
        print("No")

def is_yes(n):
    match n:
        case "42" | "forty-two" | "forty two":
            return True
        case _:
            return False


main()
