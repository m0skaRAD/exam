print("\n Вітаємо в грі\n Вашою основною метою буде дійти до кінця лабіринту \n Все не так дегко, адже на кожному кутку вас чекатимуть противники  ")
print("\n Відкривайте скрині , знаходите спорядження та покращуйте персонажа \n Успіхів!")
f = open("inventory.txt", "w") 
f.write("Це твій інвентар \n") 
f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")



r = open("map.txt", "w") 
r.write("Це мапа лабіринту, користуйся ій \n") 
r.write(" ←━┳━━┳┓ \n ┣╸┃┏━┛┃ \n ┃╻╹┗┓╺┫ \n ┃┗┓╻┗╸┃ \n ┣╸┃┃╺━┫ \n ┃╺╋┛╺━┫ \n ┗━┻━━━↰")

class person:
    def __init__(self, life, stamina, weapon, armor):
        self.life = life
        self.stamina = stamina
        self.weapon = weapon
        self.armor = armor

class player(person):
    def __init__(self, life, stamina, weapon, armor):
        super().__init__(life, stamina, weapon, armor)
youplayer = player(life = 100, stamina = 100, weapon = "дерев'яний меч", armor = "немає")

f.write("Твоя зброя - {}\n".format(youplayer.weapon))
f.write("Твоя броня - {}\n".format(youplayer.armor))


ask1 = input("Киди йти? ")
ask1_lower = ask1.lower()  

if ask1.lower == "вперед":
    print("Ти йдеш вперед")
else:
    print("Упс, глухий кут. Дивись на мапу")