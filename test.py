def delete_third_and_seventh(input_list):
    """
    Remove the third and seventh elements of the input list.
    [ A, B, C, D, E, F, G, H ] --> [ A, B, D, E, F, H ]
    """

    del input_list[2] 
    del input_list[6]

    print input_list
    print input_list[5]
    print input_list[8]

delete_third_and_seventh([0,1,2,3,4,5,6,7,8,9,10])