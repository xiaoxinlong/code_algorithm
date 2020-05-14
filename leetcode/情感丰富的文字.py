from collections import Counter

def get_split(s):

    cur = 0
    string = []
    string_length = []

    while cur<len(s):
        cur_str = s[cur]
        temp_count = 0
        while s[cur]==cur_str:
            temp_count += 1
            if cur==len(s):
                break
        string.append(cur_str)
        string_length.append(temp_count)
    return string, string_length

def _helper(word, target_count):
    word_string, word_string_length = get_split(word)
    target_string, target_string_count = target_count[0], target_count[1]

    if len(target_string)!=len(word_string):
        return False

    for i in range(len(target_string)):
        pass



def solutions(S, words):
    target_count = get_split(S)
    count = 0
    for word in words:
        if _helper(word,target_count):
            pass

