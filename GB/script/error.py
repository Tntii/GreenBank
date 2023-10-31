

def int_error(nb):
    try:
        nb = int(nb)
        return False

    except ValueError:
        return True