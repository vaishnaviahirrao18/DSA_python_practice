binary_array = [1, 1, 0, 1, 1, 1, 0, 1, 1, 1, 1]

max_count = 0
current_count = 0

for num in binary_array:
    if num == 1:
        current_count += 1
        if current_count > max_count:
            max_count = current_count
    else:
        current_count = 0

print("The maximum number of consecutive 1s is:", max_count)
