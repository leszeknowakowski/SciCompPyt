L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

def reverse_range(list,start,stop):
    '''my way to construct function reversing a subrange of list'''
    new_list= list[start:stop+1]
    new_list.sort(reverse=True)
    list[start:stop+1] = new_list
    return list

print("my function output is: ", reverse_range(L,3,6))

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def reverse_range_rec(list, start, stop):
    '''recursive sorting subrange of list'''
    if start >= stop:
       return list
    else:
        list[start], list[stop] = list[stop], list[start]
        return  reverse_range_rec(list, start+1, stop-1)

print("recursive version of function: ",reverse_range_rec(L,3,6))

L = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
def reverse_range_iter(list, start, stop):
    '''iterative sorting subrange of list'''
    while start<stop:
        list[start],list[stop] = list[stop], list[start]
        start += 1
        stop -= 1
    return list

print("iterative version of function: ",reverse_range_iter(L,3,6))