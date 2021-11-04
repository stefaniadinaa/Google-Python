# #exemplu 1: instructiunea if cu elif
# my_var = 5
#
# if my_var > 6:
#     print("Set instructiuni 1")
# elif my_var > 10:
#     print("Set intructiuni 2")
# else:
#     print("Nicio conditie nu este respectata")
#
# #exemplu 2
# my_var = 5
# msg = "Nicio conditie nu este respectata"
#
# if my_var > 6:
#     msg = "Set instructiuni 1"
# elif my_var > 10:
#     msg = "Set intructiuni 2"
# print(msg)
#
# #exemplu 3
# my_var = 5
# msg = "Nicio conditie nu este respectata"
# msg1 = 0
#
# if my_var < 6:
#     msg, msg1 = "Set instructiuni 1", my_var
# elif my_var > 10:
#     msg = "Set intructiuni 2"
# print(msg, msg1)
#
# #exemplu 3: operator ternal
#
# a = 1
# b = 2
# x = 1 if a > b else -1
# #var = sintaxa_then if conditie else sintaxa_else
# print(x)
#
# #exemplu 4: instructiunea while
#
# while True:
#     print("Set instructiuni")
#     break
#
# #exemplu 5: instructiune for
#
# for i in range(10):
#     print(f'Set instructiuni {i}')
# #se executa de 10 ori
#
# #exemplu 6: list comprehenshion
#
# variabila = "Ana are mere"
# lista = []
# for i in variabila:
#     lista.append(i)
# lista = [i for i in variabila]
# print(lista)
# for item, value in enumerate(variabila):
#     print(f"{item} => {value}")
#
# #exemplu 7: dictionar
# dictionar = {"key1": "value1", "key2": "value2"}
# for item in dictionar.items():
#     #print(item)
# #luam separat cheia si valoarea
#     item0, item1 = item
#     print(item0, item1)
#
# #exemplu 8: este tuplu
# variabila = (1,)
# variabila2 = ('1', '2')
# print(type(variabila))
#
# #exemplu 9: ghilimele
# variabila = "Ana \"are\" mere"
# print(variabila)
#
# variabila = 'Ana "are" mere'
# print(variabila)

