try:

    def rev_string(string):
        spaces = [i for i, val in enumerate(string) if val == ' ']
        print("spaces-", spaces)
        new_string = "".join([i for i in string if i != ' '])
        print(list(string))
        print(new_string)
        print("".join(string))

        # k = 0
        # m = 1
        # for i in range(k, spaces[m]):

    # string = input("Enter string-").strip()
    # print(f"reverse word string - {rev_string(string)}")

except Exception as e:
    print(f"error:{e}")
