largeursol = int(input())
largeurciel = int(input())
HAUTEUR = 1
volumetot = 0

for loop in range(largeursol-largeurciel+1):
    volumetmp = ((loop+largeurciel)**2)*HAUTEUR
    volumetot = volumetot + volumetmp

print(volumetot)
