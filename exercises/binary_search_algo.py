def binary_search(list, element):
    # variable instantiation
    middle = 0
    start = 0
    step_number = 0
    end = len(list)

    while(start <= end): # while loop

        print("Step ", step_number, ": ", str(list[start:end+1]))

        step_number += 1 # increase steps each time a split is done
        middle = (start + end) // 2

        if element == list[middle]: #if/else elements to track target position
            return middle
        if element < list[middle]:
            end = middle - 1
        else:
            start = middle + 1

    return -1

my_list = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
target = int(input("> Enter a target between 1 and 20: \n>"))

if 1 < target < 20:
        pass
else:
    print("Input not in accepted range, restart application to try again.")
    quit()

binary_search(my_list,target)

# in the case of time constraints binary search could be quicker than
# linear search, as it does not have to 'look at every result' when searching.