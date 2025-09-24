try:

    def rev_string(string):
        new_string = ''
        for word in string:

            if len(word) == 1:
                return word
            else:
                list_word = list(word)
                start = 0
                word_len = len(list_word) - 1

                while (start < word_len):

                    list_word[start], list_word[word_len] = (
                        list_word[word_len], list_word[start]
                    )
                    start += 1
                    word_len -= 1
                new_string += ''.join(list_word)
                new_string += " "

        return new_string
    string = input("Enter String-").strip()
    if not string:
        raise ValueError("invalid Input string")
    print(f"Reverse word of string - {string} is {rev_string(string.split())}")

except Exception as e:
    print(f"error:{e}")
