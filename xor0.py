# X and O
# functie care actualizeaza harta
def harta(x, XO):
      newstring = ""
      if  x == '1':
            XO[0] = 'X'
            newstring = "".join(XO)
            print(newstring)
      if  x == '2':
            XO[2] = 'X'
            newstring = "".join(XO)
      if x == '3':
            XO[4] = 'X'
            newstring = "".join(XO)
      if x == '4':
            XO[6] = 'X'
            newstring = "".join(XO)
      if x == '5':
            XO[8] = 'X'
            newstring = "".join(XO)
      if x == '6':
            XO[10] = 'X'
            newstring = "".join(XO)
      if x == '7':
            XO[12] = 'X'
            newstring = "".join(XO)
      if x == '8':
            XO[14] = 'X'
            newstring = "".join(XO)
      if x == '9':
            XO[16] = 'X'
            newstring = "".join(XO)
      return newstring

def check(map):

      if (
         map[0] == map[2] == map[4] and
         map[0] != '_' and map[2] != '_' and map[4] != '_'
         or
         map[0] == map[6] == map[12] and
         map[0] != '_' and map[6] != '_' and map[12] != '_'
         or
         map[0] == map[8] == map[16] and
         map[0] != '_' and map[8] != '_' and map[16] != '_'
         or
         map[2] == map[8] == map[14] and
         map[2] != '_' and map[8] != '_' and map[14] != '_'
         or
         map[4] == map[10] == map[16] and
         map[4] != '_' and map[10] != '_' and map[16] != '_'
         or
         map[4] == map[8] == map[12] and
         map[4] != '_' and map[8] != '_' and map[12] != '_'
         or
         map[6] == map[8] == map[10] and
         map[6] != '_' and map[8] != '_' and map[10] != '_'
         or
         map[12] == map[14] == map[16] and
         map[12] != '_' and map[14] != '_' and map[16] != '_'
         ):
            checkul = 1

      else:
            checkul = 0

      return checkul


XO = "_|_|_\n_|_|_\n_|_|_"
newstring = ""

# ce locuri am ocupat deja
already_have = []

# al cui este randul
flag = 1
k = 0
# daca s-a terminat runda
checkul = 0

XOplay = list(XO)

while checkul == 0:
      if XOplay.count('_'):
            if flag == 1:
                        x = input("Introdu o cifra de la 1 la 9: ")
                        if x == "":
                              print("Te rugam introdu o cifra de la 1 la 9: ")

                        if already_have.count(x):
                              print("Locul este ocupat")
                        else:
                              already_have.append(x)
                              harta(x, XOplay)
                              flag = 0

                              # k verifica cine castiga
                              k = 1
                              checkul = check(harta(x, XOplay))
            else:
                        if not already_have.count('5'):
                              XOplay[8] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('5')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('1') and flag == 0:
                              XOplay[0] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('1')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('3') and flag == 0:
                              XOplay[4] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('3')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('7') and flag == 0:
                              XOplay[12] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('7')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('9') and flag == 0:
                              XOplay[16] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('9')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('2') and flag == 0:
                              XOplay[2] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('2')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('4') and flag == 0:
                              XOplay[6] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('4')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('6') and flag == 0:
                              XOplay[10] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('6')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)

                        if not already_have.count('8') and flag == 0:
                              XOplay[14] = '0'
                              newstring = "".join(XOplay)
                              already_have.append('8')
                              flag = 1
                              k = 0
                              checkul = check(newstring)
                              print(newstring)
      else:
            print("Remiza")
            k = 9
            break

if k == 1:
      print("Ai castigat!")
if k == 0:
      print("Ai pierdut!")










