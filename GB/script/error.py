

def int_error(nb, start=None, end=None):
    try:
        nb = int(nb)
        if start is not None and nb >= start:
            if end is not None and nb <= end:
                return False
            elif end is None:
                return False
        return True

    except ValueError:
        return True


def choice_error(db, value):
    try:
        db.objects.get(type=value)
        return False
    except db.DoesNotExist:
        return True
