def sort_food_listp(foods, nutrient):
    # Sort the food list based on the percent-by-calories of the
    # given nutrient ('protein', 'carbs' or 'fat')
    # The list is sorted in-place; nothing is returned.
    if int(nutrient) is 1:
        quicksortp(foods, 0 , len(foods)-1)
    elif int(nutrient) is 2:
        quicksortc(foods, 0, len(foods) - 1)
    else:
        quicksortf(foods, 0, len(foods) - 1)

    pass

# protein sort
def partitionp(foods, start_index, end_index):
    mid_point = start_index + (end_index - start_index) // 2
    pivot = foods[mid_point].protein
    # low and high start at the end of th segment list and move towards each other
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while foods[low] < pivot
        while foods[low].protein < pivot:
            low = low + 1


        # Decrement high while picot < foods[high]
        while pivot < foods[high].protein:
            high = high - 1

        # If low and High have crossed, the loop is done.
        # If not the elements are swapped, low is incremented and high is decremented
        if low >= high:
            done = True
        else:
            temp = foods[low]
            foods[low] = foods[high]
            foods[high] = temp
            low = low + 1
            high = high - 1

    return high

def quicksortp(foods, start_index, end_index):
    # Only attempt to sort the list segment if the are +2
    if end_index <= start_index:
        return

    # partition the list
    high = partitionp(foods, start_index, end_index)

    # recursive sort the left segment
    quicksortp(foods, start_index, high)

    # recursive sort the right segment
    quicksortp(foods, high + 1, end_index)

#carb sort
def partitionc(foods, start_index, end_index):
    mid_point = start_index + (end_index - start_index) // 2
    pivot = foods[mid_point].carbs
    # low and high start at the end of th segment list and move towards each other
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while foods[low] < pivot
        while foods[low].carbs < pivot:
            low = low + 1


        # Decrement high while picot < foods[high]
        while pivot < foods[high].carbs:
            high = high - 1

        # If low and High have crossed, the loop is done.
        # If not the elements are swapped, low is incremented and high is decremented
        if low >= high:
            done = True
        else:
            temp = foods[low]
            foods[low] = foods[high]
            foods[high] = temp
            low = low + 1
            high = high - 1

    return high

def quicksortc(foods, start_index, end_index):
    # Only attempt to sort the list segment if the are +2
    if end_index <= start_index:
        return

    # partition the list
    high = partitionc(foods, start_index, end_index)

    # recursive sort the left segment
    quicksortc(foods, start_index, high)

    # recursive sort the right segment
    quicksortc(foods, high + 1, end_index)


#carb sort
def partitionf(foods, start_index, end_index):
    mid_point = start_index + (end_index - start_index) // 2
    pivot = foods[mid_point].fat
    # low and high start at the end of th segment list and move towards each other
    low = start_index
    high = end_index

    done = False
    while not done:
        # Increment low while foods[low] < pivot
        while foods[low].fat < pivot:
            low = low + 1


        # Decrement high while picot < foods[high]
        while pivot < foods[high].fat:
            high = high - 1

        # If low and High have crossed, the loop is done.
        # If not the elements are swapped, low is incremented and high is decremented
        if low >= high:
            done = True
        else:
            temp = foods[low]
            foods[low] = foods[high]
            foods[high] = temp
            low = low + 1
            high = high - 1

    return high

def quicksortf(foods, start_index, end_index):
    # Only attempt to sort the list segment if the are +2
    if end_index <= start_index:
        return

    # partition the list
    high = partitionf(foods, start_index, end_index)

    # recursive sort the left segment
    quicksortf(foods, start_index, high)

    # recursive sort the right segment
    quicksortf(foods, high + 1, end_index)


    """
    the percentage of the calories must mach what was provided. calorines / 
    """