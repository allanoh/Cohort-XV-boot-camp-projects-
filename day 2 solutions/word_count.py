'''allan 8/2/2017'''
def words(line):
    """To count the occurrences of characters in a given string and return in a
         dictonary
       """
    word_list = line.split()
    word_dict = {}
    for word in word_list:
        word = word.strip()
        if word.isdigit():
            word = int(word)
        if not word in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] += 1
    return word_dict