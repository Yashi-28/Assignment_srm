def anagram(list_given):
    dict = {}
    for word in list_given:
        key = ''.join(sorted(word))
        if key in dict:
            dict[key].append(word)
        else:
            dict[key] = [word]
    return list(dict.values())

list_given=["eat", "tea", "tan", "ate", "nat", "bat"]
print(anagram(list_given))