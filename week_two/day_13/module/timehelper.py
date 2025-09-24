from datetime import datetime, time


def greet(name):
    current_time = datetime.now().time()
    # print(current_time)

    if current_time < time(12, 0, 0) and current_time > time(0, 0, 0):
        return print(f"Good Morning, {name}")
    elif current_time > time(12, 0, 0) and current_time < time(4, 0, 0):
        return print(f"Good Afternoon, {name}")
    else:
        return print(f"Good Night, {name}")
