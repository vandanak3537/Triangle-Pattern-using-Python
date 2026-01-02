# Type Content here...
n = int(input("Enter a number: "))
# Loop through each row
for i in range(1, n + 1):
    # Calculate the number to be printed in the current row
    num = n - i + 1
    # Print the number 'num' i times
    for j in range(i):
        print(num, end=" ")
    print()