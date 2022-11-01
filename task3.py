# Задайте список из n чисел последовательности $(1+\frac 1 n)^n$ и выведите на экран их сумму.

n= int(input('n='))
d= {}
sum= 0
for i in range(1, n+1):
    d[i]= round((1+1/i)**i, 2)
    sum+=d[i]
print (d)
print(round(sum, 2))