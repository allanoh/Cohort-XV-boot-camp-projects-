def find_missing(a, b):
    longer = list(set(a) - set(b))
    if len(longer) == 0:
        longer = list(set(b) - set(a))
    if len(a + b) == 0:
        longer = 0
    if b == a:
        longer = 0
    if longer != 0:
        return longer[0]
    else:
        return 0
