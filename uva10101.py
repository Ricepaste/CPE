def unit(hun_int):
    unit_int = ""
    if hun_int % 10 > 0:
        unit_int = f"{hun_int % 10} shata " + unit_int

    hun_int //= 10
    if hun_int % 100 > 0:
        unit_int = f"{hun_int % 100} hajar " + unit_int

    hun_int //= 100
    if hun_int % 100 > 0:
        unit_int = f"{hun_int % 100} lakh " + unit_int

    hun_int //= 100
    if hun_int % 100 > 0:
        unit_int = f"{hun_int % 100} kuti " + unit_int
    elif hun_int > 0:
        unit_int = f"kuti " + unit_int

    hun_int -= hun_int % 100
    carry_num = hun_int

    return carry_num, unit_int


def trans_int(ori_int):
    if ori_int == 0:
        return "0"
    elif ori_int % 100 == 0:
        trans_output = ""
    else:
        trans_output = str(ori_int % 100)

    while ori_int >= 100:
        ori_int //= 100
        ori_int, unit_int = unit(ori_int)
        trans_output = unit_int + trans_output

    return trans_output


index = 1
while True:
    try:
        ori_int = int(input())
        ans = f"{index}. {trans_int(ori_int)}"
        print(ans)
        index += 1
    except:
        break
