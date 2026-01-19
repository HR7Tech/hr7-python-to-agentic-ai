def calculate_love_score(name1, name2):
    name = name1.upper() + name2.upper()

    true_count = 0

    for char in name:
        if char == "T":
            true_count += 1
        elif char == "R":
            true_count += 1
        elif char == "U":
            true_count += 1
        elif char == "E":
            true_count += 1

    love_count = 0

    for char in name:
        if char == "L":
            love_count += 1
        elif char == "O":
            love_count += 1
        elif char == "V":
            love_count += 1
        elif char == "E":
            love_count += 1

    love_score = str(true_count) + str(love_count)

    print(love_score)


calculate_love_score("Brad Pitt", "Angelina Jolie")