n = int(input())
di = dict()

for i in range(n):
    customer, good, quantity = input().split(' ')
    if customer not in di:
        di[customer] = {}
        di[customer][good] = int(quantity)
    else:
        if good not in di[customer]:
            di[customer][good] = int(quantity)
        else:
            di[customer][good] += int(quantity)

sorted_dict = {k: di[k] for k in sorted(di)}

for customer, good in sorted_dict.items():
    li = []
    for g, quantity in good.items():
        li.append(str(g) + ' ' + str(quantity))
        sorted_li = sorted(li)
    print(customer, ':', sep='')
    print(*sorted_li, sep='\n')
    print()
