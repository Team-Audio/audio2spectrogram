verbosity_level = 0


# print at different verbosity levels

def vprint1(*args, **kwargs):
    if verbosity_level > 0:
        print(*args, **kwargs)


def vprint2(*args, **kwargs):
    if verbosity_level > 1:
        print(*args, **kwargs)


def vprint3(*args, **kwargs):
    if verbosity_level > 2:
        print(*args, **kwargs)
