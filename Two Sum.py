nums = [2,7,11,15]
target = 9

seen = {}
def Two_sum():
    for idx,num in enumerate(nums):
        val = target - num
        if val in seen:
            return (seen[val], idx)
        seen[num] = idx

val = Two_sum()
print(val)