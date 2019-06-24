
# find the longest substring of unique characters in a string
def findUnqiue(s):
    curr = ""
    result = ""
    index = 0
    sd = dict(range(len(s)), s.split(""))
    for key in sorted(sd.keys())[index:]:
        if sd[key] not in curr:
            curr += sd[key]
        else:
            index += 1
        if len(curr) > len(result):
            result = curr
        index += 1