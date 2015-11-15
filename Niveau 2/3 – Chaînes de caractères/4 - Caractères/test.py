nbNombre = int(input())
for loop in range(nbNombre):
   num = int(input())
   if num > 0:
      print('+', end="")
   else:
      print('-', end="")
   if num > 100:
      print('>>>')
   elif num > 50:
      print('>')
   elif num > 10:
      print('>')
   else:
      print()