ori_text = ''

while True:
    try:
        ori_text += input() + '\n'
    except EOFError:
        break

while '"' in ori_text:
    ori_text = ori_text.replace('\"', '``', 1)
    ori_text = ori_text.replace('\"', "\'\'", 1)
print(ori_text, end='')
