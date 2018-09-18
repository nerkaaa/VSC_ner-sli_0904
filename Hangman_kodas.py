import random
lygis = input("iveskite lygi:")
zodziu_sarasas = []
while lygis <= 2:
    lygis = input("iveskite lygi:")

failo_objektas = open("zodziu_sarasas.txt", "r")
for zodis in failo_objektas.readlines():
    zodzio_ilgis  = zodis.__len__()
    if int(lygis) >= int(zodzio_ilgis):
        zodziu_sarasas.append(zodis.replace("\n", ""))

# pasirinkt random skaiciu

random_index = random.randint(0,zodziu_sarasas.__len__())
zodis_kuri_spet = zodziu_sarasas[random_index]
print zodis_kuri_spet

#Random zodzio ilgi surandam:, yeaaah, pavyko

#print(len(zodis_kuri_spet))  #sita reiks istrint
a = "_ " * (len(zodis_kuri_spet))
print a

klaidos = 0
word_string = list(zodis_kuri_spet)
no_of_guesses=len(zodis_kuri_spet*2) #sita reikia sulinikint kazkaip

while lygis != klaidos:
    guess = raw_input("Guess a letter")
    if len(guess) != 1:
        print ("Enter a single letter")
    if guess not in "abcdefghijklmnopqrstuvwxyz":
        print ("Enter a letter")
        continue
    if guess in word_string:
        print "Correct!", guess #jei speja teisinga raide
        for i, x in enumerate(zodis_kuri_spet):
            if x == guess:
                p_list = list(a)
                p_list[i*2]=guess
                a="".join(p_list)#a listu ir atgal i stringa
                print a
    if a == zodis_kuri_spet: #sito nespausdina
            print "Congratulations, you won!"
            break;
else:
    klaidos = klaidos + 1 #sitas neveikia kaip turetu, ty klaidingu
    print "You lost!"   #jei klaidu skaicius virsija lygio pasirinkto skaiciu




