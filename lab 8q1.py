import random

def vacuum_cleaner():
    rooms = {"A": random.randint(0, 1), "B": random.randint(0, 1), "C": random.randint(0, 1), "D": random.randint(0, 1)}

    print("Initial Room States:", rooms)

    for room in rooms:
        if rooms[room] == 1:
            print(f"Cleaning room {room}")
            rooms[room] = 0

    print("Final Room States:", rooms)
vacuum_cleaner()
