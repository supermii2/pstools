from collections import Counter

INPUT_STRING = "boofartac"
NAME_LIST = ["foo","bar","cat","dog"]

def can_be_made(c1, c2):
    return all(c1[char] <= c2[char] for char in c1)

def anagram_finder(input, terms, idx):
    if input == Counter({}):
        return [[]]
    ans = []
    for i in range(idx, len(terms)):
        if can_be_made(terms[i][0], input):
            res = anagram_finder(input - terms[i][0], terms, i)
            for j in res:
                j.append(terms[i])
            ans.extend(res)
    return ans

def anagram_solver(input_string, names):
    input_counter = Counter(input_string)
    name_list_counter = list(map(lambda x: (Counter(x), x), names))
    return list(map(lambda x: list(map(lambda y: y[1], x)), anagram_finder(input_counter, name_list_counter, 0)))

print(anagram_solver(INPUT_STRING, NAME_LIST))