#!/usr/bin/python3
def search_replace(my_list, search, replace):
    ans = []
    for i in my_list:
        if i == search:
            i = replace
        ans.append(i)
    return ans
