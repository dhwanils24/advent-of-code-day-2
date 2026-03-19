safe = 0

with open('input.txt', 'r') as file:

    for line in file:
        nums = list(map(int, line.split()))
        increasing = True
        decreasing = True
        isValid = True
        
        for i in range(len(nums)-1):
            diff = nums[i+1] - nums[i]

            if abs(diff) > 3 or abs(diff) < 1:
                isValid = False
                break
            if diff > 0:
                decreasing = False
            if diff < 0:
                increasing = False
        if isValid and (increasing or decreasing):
            safe += 1

print(safe)

