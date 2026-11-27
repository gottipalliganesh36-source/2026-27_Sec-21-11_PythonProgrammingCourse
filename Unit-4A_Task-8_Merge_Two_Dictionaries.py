dict_data = {"a": 1, "b": 2}
dict_extra = {"b": 3, "c": 4}

dict_merged = dict_data.copy()  # copy
dict_merged.update(dict_extra)  # update
print("Merged:", dict_merged)