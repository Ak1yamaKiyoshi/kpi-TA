"""
comparison
replacement
"""

Radix = 10
logging = []  # Initialize an empty list to store logging steps

def bucketInitialzier(array, decimal_placement, max_length, logging=None):
    global Radix
    temp_bucket_list = [[] for x in range(Radix)]

    for i in array:
        selected_temp_integer = i / decimal_placement
        
        selected_digit = selected_temp_integer % Radix

        temp_bucket_list[int(selected_digit)].append(i)

        if selected_temp_integer and max_length > 0:
            max_length = False

    return temp_bucket_list, max_length


def add_bucket_to_list(array, temp_bucket_list, logging=None):
    global Radix
    
    #if logging is not None:
    #    logging.append("Adding bucket to list")

    index_tracker = 0
    for bucket in range(Radix):
        sub_bucket = temp_bucket_list[bucket]
        for element in sub_bucket:
            array[index_tracker] = element
            index_tracker += 1
            #if logging is not None:
            #    logging.append(f"Added {element} to array at index {index_tracker - 1}")
    return array


def split_absolute_pos_neg(array, logging=None):
    positive = []
    negative = []
    for i in array:
        if i >= 0:
            positive.append(i)
        else:
            negative.append(-1*i)
    if logging is not None:
        logging.append(f"Splitted array into: \n  > {positive}\n  > {negative}")
    return positive, negative


def radix_sorting_procedure(array, logging=None):
    max_length = False
    decimal_placement = 1
    if logging is not None:
        logging.append("")
    while max_length is False:
        max_length = True
        
        temp_bucket_list, max_length = bucketInitialzier(array,
                                                        decimal_placement,
                                                        max_length,
                                                        logging)
        if logging is not None:
            if f"temp bucket: {temp_bucket_list}" not in logging:
                logging.append(f"temp bucket: {temp_bucket_list}")
    
        array = add_bucket_to_list(array, temp_bucket_list, logging)
        if logging is not None:
            if f"Array: {array}" != logging[-1]:
                logging.append(f"Array: {array}")
        decimal_placement *= Radix
    return array


def lsd_radixsort(array, logging=None):
    if len(array) >= 1:
        pass
    else:
        raise Exception('Your list must contain one or more integer in order \
            for Radix sort to operate')
    if all(isinstance(item, int) for item in array) is True:
        pass
    else:
        raise Exception('This function can only sort integers without \
            decimal floats.')

    positive_array, abs_negative_array = split_absolute_pos_neg(array, logging)
    
    sorted_positive_array = radix_sorting_procedure(positive_array, logging)
    if len(abs_negative_array) >= 1:
        sorted_abs_negative_array = radix_sorting_procedure(abs_negative_array, logging)
        temp_negative_array = list(reversed(sorted_abs_negative_array))
        sorted_negative_array = [-x for x in temp_negative_array]
        if logging is not None:
            logging.append(f"Reverse and sort negative array: \n {sorted_abs_negative_array}")
        return sorted_negative_array + sorted_positive_array

    else:
        return sorted_positive_array
