import hashlib

def find_duplicate_rows(df): 
    def hash_row(row):
        row_tuple = tuple(row)
        hash_value = hashlib.sha256(str(row_tuple).encode())
        return hash_value.hexdigest()

    hash_dict = {}
    for index, row in df.iterrows(): 
        row_hash = hash_row(row)
        print(row_hash)

        if row_hash in hash_dict: 
            hash_dict[row_hash].append(index)
        else: 
            hash_dict[row_hash] = [index]
    
    res = [dup_lists for dup_lists in hash_dict.values() if len(dup_lists) > 1]
    return res