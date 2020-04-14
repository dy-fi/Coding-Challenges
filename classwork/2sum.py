def two_sum(nums, t):
    results = []

    # iterate through num array
    for num in range(len(nums)):
        # if num's compliment with respect to T exists in the arr
        if t - num in nums:
            # append to results list as a tuple
            results.append((num, t - num))
    
    return results

# a worse solution
def two_sum2(nums, t):
    results = []
    for i in range(len(nums)):
        for j in range(len(nums)):
            if nums[i] + nums[j] == t:
                results.append((nums[i], nums[j]))
    return results