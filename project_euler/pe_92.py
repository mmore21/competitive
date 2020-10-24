"""
Problem: 92 - Square Digit Chains
URL: https://projecteuler.net/problem=92
"""

dict = { 1:1, 89:89 }

# set count of 89 to 0
total = 0

# loop over first ten million numbers
for i in range(1, 11):
    if i % 1000:
        print(i)
    if i in dict and dict[i] == 89:
        total += 1
    else:
        new_dict_nums = []
        while i not in [1, 89]:
            # add i to list to be added to dict
            new_dict_nums.append(i)

            # splits the digits
            digits = [int(j) for j in str(i)]
            if 0 in digits:
                digits.remove(0)
            digits.sort()
            print(digits)

            # reset i to zero to hold sum of squared digits
            i = 0
            for digit in digits:
                i += digit ** 2

        for n in new_dict_nums:
            dict[n] = i
    

print(total)