from utils import *

def box_surface_area(dims_str: str):
    l, w, h = lmap(int, dims_str.split("x"))
    return 2*l*w + 2*w*h + 2*h*l + min(l*w, w*h, h*l)

dim_str_list = read_file_2_list("2.txt")

print(sum(lmap(box_surface_area, dim_str_list)))

def box_ribbon_amt(dims_str: str):
    l, w, h = lmap(int, dims_str.split("x"))
    return(2 * min(l + w, w + h, h + l)) + l * w * h

print(box_ribbon_amt(dim_str_list[0]))
print(sum(lmap(box_ribbon_amt, dim_str_list)))

def box_ribbon_amt2(dims_str: str):
    '''
    takes dimensions as a string 'LxWxH' and then calculates the amount of ribbon needed
    it sorts.    
    '''
    l, w, h = lmap(int, dims_str.split("x"))
    temp_list = [l, w, h]
    temp_list.sort()
    a,b = temp_list[:2]
    return (a*2 + b*2) + l * w * h

print(sum(lmap(box_ribbon_amt2, dim_str_list)))