def reverseString(s):
    # return s[::-1]
    # return ''.join(reversed(s))
    if not s or len(s)<=1:
        return s
    lo=0
    hi=len(s)-1
    while lo<hi:
        s[lo],s[hi]=s[hi],s[lo]
        lo +=1
        hi -=1
    return s

