
numbers = [1,2,3,4,5]
target = 4
tfound = False
for item in numbers:
    if item == target:
        tfound = True
        print("target found" , target)
    else:
        print("target not found")
        item = item + 1
