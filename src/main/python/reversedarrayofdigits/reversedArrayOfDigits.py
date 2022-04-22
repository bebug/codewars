def digitize(n: int):
    out = [int(a) for a in str(n)]
    out.reverse()
    return out