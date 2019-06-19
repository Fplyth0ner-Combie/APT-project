def clever(lll, j, row, bigest, f):
    if j == bigest:
        return

    for a in lll[j]:
        if j == bigest - 1:
            row1 = row + str(a)
            f.write(row1 + '\n')
        else:
            row1 = row + str(a)

        clever(lll, j+1, row1, bigest, f)

row = ''
dic = ''
count = 1
list_tmp = '['
digit = input('num digit: ')

print('please input a list num,for example: 1,2,5,6')
for i in range(digit):
    tmp = raw_input('List num: ')
    tmp = '[' + tmp + ']'
    if i < digit-1:
        list_tmp = list_tmp + tmp + ','
    else:
        list_tmp = list_tmp + tmp

list_tmp += ']'

exec('num_list = ' + list_tmp)

for i in range(digit):
    count *= len(num_list[i])

print 'Total:' + str(count)

with open('dic.txt', 'w') as f:
    clever(num_list, 0, row, digit, f)

print 'dic.txt is ok !'
