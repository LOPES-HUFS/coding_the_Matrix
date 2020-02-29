def boston_cryptograph_encryption(p, k):
    if p == 0:
        if k == 0:
            return 0
        elif k == 1:
            return 1
    elif p == 1:
        if k == 0:
            return 1
        elif k == 1:
            return 0
