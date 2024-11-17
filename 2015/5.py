from utils import *

xmaslist = read_file_2_list("5.txt")
vowels = ["a", "e", "i", "o", "u"]
naughty_combinations = ["ab", "cd", "pq", "xy"]
nice_list = []
naughty_list = []

def twice(s):
    i = 0
    j = i+1
    while j < len(s):
        if s[i] == s[j]:
            return True
        i += 1
        j += 1
    return False

def has3vowels(s):
    vowels_found = 0
    for v in vowels: 
        vowels_found += s.count(v)
    return vowels_found >= 3       

def naughty_combo_present(s):
    for bad_combo in naughty_combinations:
        if bad_combo in s:
            return True
    return False

def is_nice_word(s):
    return has3vowels(s) and twice(s) and not naughty_combo_present(s)

print('ugknbfddgicrmopn',is_nice_word('ugknbfddgicrmopn'))
print('aaa',is_nice_word('aaa'))
print('jchzalrnumimnmhp',is_nice_word('jchzalrnumimnmhp'))
print('dvszwmarrgswjxmb',is_nice_word('dvszwmarrgswjxmb'))


for s in xmaslist:
    if is_nice_word(s):
        nice_list.append(s)
    else:
        naughty_list.append(s)


print("Nice lists:", len(nice_list))
print(nice_list[0])
print("Naughty lists", len(naughty_list))