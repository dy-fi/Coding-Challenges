def k_largest(nums, k):
    # edge case where k > the list size
    if len(nums) < k: return "error"
    # sort list and slice the end off at the compliment of k with respect to the size of the arr
    return sorted(nums)[len(nums) - k:]


# worse solution
def k_largest2(nums, k):
    # edge case where k > the size of the list
    if len(nums) < k: 
        return "error"
    
    a = nums 
    result = []

    # take max and pop
    for i in range(k):
        t = max(a)
        result.append(t)
        a.pop(a.index(t))
    
    return result