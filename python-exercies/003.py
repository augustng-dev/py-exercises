def convert_input_to_list_and_tuple(s):
    arr = s.split(",")
    return (arr, tuple(arr))

print(convert_input_to_list_and_tuple("3,6,5,3,2,8"))