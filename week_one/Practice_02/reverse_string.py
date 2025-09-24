try:

    def reverse_string(string):
        left = 0
        right = len(string) - 1

        while (left < right):
            temp = string[right]
            string[right] = string[left]
            string[left] = temp

            left += 1
            right -= 1
        return ''.join(string)

    string = list(input("enter string -"))
    if len(string) == 1:
        print(''.join(string))
    else:
        print(reverse_string(string))
except Exception as e:
    print(f"error:{e}")
