#declarare lista
my_list = [7, 8, 9, 2, 3, 1, 4, 10, 5, 6]

#sortare lista in ordine ascendenta
sorted_list = sorted(my_list)
print(sorted_list)

#sortare lista in ordine descendenta
sorted_list_des = sorted(my_list, reverse = True)
print(sorted_list_des)

#selectare elemente pare din lista
even_number = my_list[1:4:2] + my_list[6:10:3]
even_number.insert(len(even_number) + 1, my_list[-3])
print(even_number)

#selectare elemente impare din lista
odd_number = my_list[0:4:2] + my_list[5:9:3]
print(odd_number)

#multiplii lui 3 din lista
multiple = []
j = 0
for i in my_list:
    if i % 3 == 0:
        multiple.insert(j, i)
        j = j + 1

print(multiple)


