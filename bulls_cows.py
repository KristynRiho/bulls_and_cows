import random
import datetime

print(
    f"Hi there!\nI've generated a random 4 digit number for you.\nLet's play a bulls and cows game."
)
time_start = datetime.datetime.now()

numbers = []
while len(numbers) < 4:
    number = random.randint(0, 9)
    if number in numbers:
        continue
    elif number not in numbers:
        numbers.append(number)

print(numbers)  # smaž až to bude fungovat

bulls = 0
cows = 0
pocet_pokusu = 0
while bulls < 5:
    if bulls == 4:
        print(f"Gratuluju, uhodl jsi číslo! Trefil jsi se na {pocet_pokusu} pokusů.")
        time_stop = datetime.datetime.now()
        break
    else:
        tip = list(input("Zadej čtyřmístné číslo.\n"))
        pocet_pokusu += 1
        bulls = 0
        cows = 0
        for i in tip:
            string = tip.pop(0)
            string = int(string)
            tip.append(string)

        for index, cislo in enumerate(numbers):
            if cislo in tip and index == tip.index(cislo):
                bulls += 1
            elif cislo in tip:
                cows += 1
            elif cislo not in tip:
                continue
        print(f"{bulls} bulls, {cows} cows")

total_time = time_stop - time_start
print(f"Hra ti trvala docela dlouho... {total_time} minut :-).")

statistika = f"\nPočet pokusů: {pocet_pokusu}, celkový čas hry: {total_time}"
statistika_file = open("statistika_bulls_cows.txt", "a")
statistika_file.write(statistika)
statistika_file.close()

volba_statistika = input("Chceš se podívat do statistiky minulých her? ano/ne: ")
if volba_statistika == "ano":
    kuk = open("statistika_bulls_cows.txt", "r")
    print(kuk.read())
    kuk.close()
else:
    print(f"Tak si trhni, kámo! :)")
