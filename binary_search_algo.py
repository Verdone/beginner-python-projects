# a function that takes a list and target parameter
# multiple vars: middle, start, end, steps
# recursion or while loop
# increase the steps each time a split is done
# conditions to track target position

def binary_search(list, element):
    middle, start, stepNumber = 0
    end = len(list)

    while(start <= end):
        print("Step ", stepNumber, ": ", str(list[start:end+1]))