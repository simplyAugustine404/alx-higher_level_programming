#!/usr/bin/python3
ans=[]
def search_replace(my_list, search, replace):
    for i in my_list:
        if i == search:
            i = replace
        ans.append(i)
    return ans
