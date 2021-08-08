def threeSum(nums):
    ans = set()

    nums.sort()

    for x in range(0, len(nums)):
        curr = nums[x]

        twoSum_target = -1 * curr

        start = x + 1
        end = len(nums) - 1

        while start < end:

            start_elem = nums[start]
            end_elem = nums[end]

            print("TARGET IS", twoSum_target, "s", start_elem, "e", end_elem)

            if start_elem + end_elem == twoSum_target:
                entry = [curr, start_elem, end_elem]
                entry.sort()
                entry = tuple(entry)
                ans.add(entry)

                start += 1
                end -= 1

            elif start_elem + end_elem > twoSum_target:
                end -= 1

            else:
                start += 1

    return ans


test = [-1,0,1,2,-1,-4]

print(threeSum(test))
