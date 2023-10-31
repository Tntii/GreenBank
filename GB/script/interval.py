

def interval(db, value):
    for element in db:
        if value in range(int(element.start), int(element.end)):
            return element.rate
    return 0
