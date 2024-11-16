def remove_line_ending(s:str):
    return s.replace('\n','')

def read_file_2_list(filename):
    fp = open(filename)
    return list(map(remove_line_ending, fp.readlines()))

def read_file_2_string(filename):
    return ''.join(read_file_2_list(filename))

def lmap(func, iterable):
    return list(map(func, iterable))

def count_characters_in_file(filename):
    content = read_file_2_string(filename)
    return len(content)
