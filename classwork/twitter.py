
########## First Solution ###########
import sys
# num of similar letters
def similarity(og, user2):
    # length of the set intersection, so no duplicates
    return len(og.intersection(set(user2)))

def twitter(target: str, users: [str]) -> [str]:
    og = set(target.split(''))
    leng = len(target)
    highest = sys.maxsize * -1
    for i in users:
        s = similarity(og, i)
        # similar letters minus non similar
        final = s - (leng - s)
        if final > highest: highest = final

    return highest

########## Second Solution ###########
def twitter2(target: str, users: [str]) -> [str]:
    highest = sys.maxsize * -1 
    for user in users:

        curr = 0
        for j, y in enumerate(target):
            if user[j] == y:
                curr += 1
            else:
                curr -= 1

        if curr > highest: highest = curr  