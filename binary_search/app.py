# Firtst take the list of numbers
# for use the binary search we should have a sorted array

def binary_search(list, element):
    start_position = 0
    end_position = len(list)
    midle_position = 0
    step = 0
    while(start_position<= end_position):
        print("Step : ", step, "\n", str(list[start_position:end_position]))
        step +=1
        midle_position = int((start_position + end_position)/2)
        if (element == list[midle_position]):
            return midle_position
        if(list[midle_position] < element):
            start_position = midle_position + 1
        else:
            end_position = midle_position - 1
    return -1


try:
    my_list = []
    print("Enter the values in sorted order and enter End at last to close the list : ")
    while True:
        my_list.append(float(input()))

# if the input is not-integer, just print the list
except:
    print("End of the list parameters")

print("Please enter the searching value : ")
finder = float(input())
print("Searching ------- \n")
position = binary_search(my_list, finder)
print("Your value is in the ", position, "of the list. :)")


