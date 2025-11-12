def process(number):
    """
    Recursive function to process an input 4 digit number
    Sorts number into ascending and descending order and minuses
    ascending from descending.
    The result is then passed back into the function recursively
    and runs again, until the number reaches 6174.
    """
    if number == 6174: return True
    number = [int(d) for d in str(number)]
    if len(number) != 4: print("Input number must be 4 digits"); return False
    ascending = int(''.join(map(str,sorted(number))))
    descending = int(''.join(map(str,sorted(number, reverse=True))))
    result = descending - ascending
    return process(result)

"""
Runs through all numbers between 1000 and 10000 and logs all
and outputs all numbers that do not adhere to the 6174 rule
"""
out = []
for i in range(1000, 10000):
    number = i
    print(f"{i} Start: {number}")
    output = process(number)
    if output == False:
        out.append(i)
    continue

print(out)

quit()

