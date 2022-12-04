#!/usr/bin/python3
def multiple_returns(sentence):
    if len(sentence) == 0:
        j = None
    else:
        j = sentence[0]
    ans = (len(sentence), j)
    return ans
