nums = [1, 2, 3, 1]
check = False
bf = False
for i in range(0, len(nums)) :
    if bf == True :
        break
    for t in range(i+1, len(nums)):
        if (nums[i] == nums[t]) :
            check = True
            bf = True
            break
        else :
            check = False
print(check)