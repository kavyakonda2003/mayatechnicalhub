def digital_root(num):
    if num == 0:
        return 0
    elif num % 9 == 0:
        return 9
    else:
        return num % 9

# Read the input
num = int(input())

# Print the result
print(digital_root(num))


here it adds all digits until makes it to single digit
