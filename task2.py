def find_longest(arr: list):
    unique_arr = set(map(lambda x: x[0], arr))
    final_arr = sorted([max(filter(lambda x: i in x, arr)) for i in unique_arr])
    return [(i, len(i)) for i in final_arr]


arr = ['aa', 'aaaaa', 'b', 'bb', 'bbbb', 'cc', 'ccc', 'aaaaaaaa']
print(find_longest(arr))
