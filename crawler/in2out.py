fp_i = open('types_in.txt', mode = 'r', encoding='UTF-8')
fp_o = open('types_out.txt', mode = 'a', encoding='UTF-8')
while True:
    tmp = fp_i.readline()
    res = tmp.split('\t')
    adcode = res[0]
    if adcode == '':
        break
    fp_o.write(adcode)
    fp_o.write('\n')