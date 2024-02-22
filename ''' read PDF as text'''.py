def greatest_number(*args):
    greatest = 0
    for number in args:
        if number > greatest:
            greatest = number
    return greatest
    print greatest_number(3, 6, 9, 12, 15, 18, 21)