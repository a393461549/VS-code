text2018 = open('sale2018.csv', 'r')
text2019 = open('sale2019.csv', 'r')
for line in text2018:
    sale2018 = [line.strip().split(',')[0], float(line.strip().split(',')[1])]
for line in text2019:
    sale2019 = [line.strip().split(',')[0], float(line.strip().split(',')[1])]
saleset2018 = {x[0] for x in sale2018}
saleset2019 = {x[0] for x in sale2019}
n = int(input())
if n == 1:
    print(sorted(list(saleset2018)))
    print(sorted(list(saleset2019)))
elif n == 2:
    s2018and2019 = saleset2018 & saleset2019
    print(sorted(list(s2018and2019)))
elif n == 3:
    s2018all2019 = saleset2019 | saleset2018
    print(sorted(list(s2018all2019)))
elif n == 4:
    s2019 = saleset2019-saleset2018
    print(sorted(list(s2019)))
elif n == 5:
    new = saleset2018 ^ saleset2019
    print(sorted(list(new)))
