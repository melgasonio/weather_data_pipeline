# Update df's indices to new_indices
def update_df_index(df, new_indices):
    df.index = new_indices
    
    return df

# Get list of keys from dict
def get_keys_as_list(dict):
    key_list = []
    for key in dict:
        key_list.append(key)
    
    return key_list

# Return all elements of arr except for elements inside except_list
def remove_arr_elems(arr, except_list):
    new_list = []
    for item in arr:
        if item not in except_list:
            new_list.append(item)
    
    return new_list