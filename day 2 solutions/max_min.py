'''allan 8/2/2017'''
def find_max_min(i):
    if min(i) == max(i):
      return [len(i)]
    else:
      return [min(i), max(i)]