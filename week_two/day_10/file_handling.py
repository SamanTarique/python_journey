# try:
#     file = open('handling.txt', 'w+')
#     file.write('my name is anurodh\n')
#     file.close()

#     reading = open('handling.txt', 'r')
#     print(reading.read())

# except Exception as e:
#     print(f"error: {e}")
# finally:
#     file.close()

writing = open('jsawn.json', 'a')
# reading = open('jsawn.json', 'r')

try:

    json_data = """{
        "firstname": "Anurodh",
        "lastname": "Kumar"
    },\n"""
    writing.write(json_data)

    # print(reading.read())

except Exception as e:
    print(f"error: {e}")
finally:
    writing.close()
    # reading.close()
