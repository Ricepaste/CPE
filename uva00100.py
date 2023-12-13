def run3n_1(temp_n, dict_table):
    if (dict_table.get(temp_n) is not None):
        return dict_table[temp_n], dict_table
    else:
        if (temp_n == 1):
            dict_table[1] = 1
            return 1, dict_table
        elif (temp_n % 2 == 1):
            cycle_len, dict_table = run3n_1(3 * temp_n+1, dict_table)
            cycle_len += 1
            dict_table[temp_n] = cycle_len
            return cycle_len, dict_table
        else:
            cycle_len, dict_table = run3n_1(temp_n/2, dict_table)
            cycle_len += 1
            dict_table[temp_n] = cycle_len
            return cycle_len, dict_table


while True:
    try:
        start, end = map(int, input().split())
        a, b = start, end
        start, end = (start, end) if start < end else (end, start)
        cycle_dict = {}
        max_len = 0
        for i in range(start, end+1):
            temp_n = i

            if (cycle_dict.get(temp_n) is not None):
                continue
            else:
                now_len, cycle_dict = run3n_1(temp_n, cycle_dict)
                if (now_len > max_len):
                    max_len = now_len

        print(a, b, max_len)
    except:
        break
