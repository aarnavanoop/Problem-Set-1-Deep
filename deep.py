def main():
    user_input = input("What is the Answer to the Great Question of Life, the Universe, and Everything? ").lower().strip()
    check(user_input)

def check(n):
    if n == "42" or n == "forty-two" or n == "forty two":
        print("Yes")
    else:
        print("No")




main()