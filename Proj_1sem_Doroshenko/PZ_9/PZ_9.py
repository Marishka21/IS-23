#Даны три словаря на три элемента каждый. Объединить все словари в
#один. Вывести исходные словари и результирующий.

a = dict(s1="1" , s2="4" , s3="9")
print(a)
b = dict(f1="1" , f2="8" , f3="27")
print(b)
c = dict(d1="1" , d2="16" , d3="81")
print(c)
x = {**a, **b, **c}
print(x)