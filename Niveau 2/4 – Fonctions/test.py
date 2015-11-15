
import time
import random
start_time = time.time()


#nbMaisons = int(input())
nbMaisons = 5000

biggestposX = 0
biggestposY = 0
smallestposX = 100000000
smallestposY = 100000000

for loop in range(nbMaisons):
   #posX = int(input())
   #posY = int(input())
   posX = random.randrange(500)
   posY = random.randrange(500)

   if (posX>=biggestposX):
      biggestposX = posX
   if (posY>=biggestposY):
      biggestposY = posY

   if (posX<=smallestposX):
      smallestposX = posX
   if (posY<=smallestposY):
      smallestposY = posY

perimetre = (biggestposY-smallestposY)*2 + (biggestposX-smallestposX)*2
print(perimetre)


print("--- %s seconds ---" % (time.time() - start_time))
