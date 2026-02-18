def appletree():
    count = 0
    for i in range(1,10):
        for j in range(1,10):
            if i * j == 36:
                count += 1
    return count
[print(appletree())]