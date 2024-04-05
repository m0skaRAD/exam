import random
import datetime
import time

print("\n Вітаємо в грі\n Вашою основною метою буде дійти до кінця лабіринту \n Все не так дегко, адже на кожному кутку вас чекатимуть противники  ")
print("\n Відкривайте скрині , знаходите спорядження та покращуйте персонажа \n Успіхів!")

class person:
    def __init__(self, life, stamina, weapon, armor, skill, max_life, max_stamina):
        self.life = life
        self.stamina = stamina
        self.weapon = weapon
        self.armor = armor
        self.skill = skill
        self.max_life = max_life
        self.max_stamina = max_stamina

class player(person):
    def __init__(self, life, stamina, weapon, armor, skill, max_life, max_stamina):
        super().__init__(life, stamina, weapon, armor, skill, max_life, max_stamina)
youplayer = player(life = 100, stamina = 50, weapon = "дерев'яний меч", armor = "немає", skill = "немає", max_life = 100, max_stamina = 50 )

f = open("inventory_and_stats.txt", "w") 
f.write("Це твій інвентар \n") 
f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")
f.write("Твоя зброя - {}\n".format(youplayer.weapon))
f.write("Твоя броня - {}\n".format(youplayer.armor))
f.write("Твоє життя - {}\n".format(youplayer.life))
f.write("Твоя єнергія - {}\n".format(youplayer.stamina))
f.write("Твій навик - {}\n".format(youplayer.skill))
f.close()

r = open("map.txt", "w") 
r.write("Це мапа лабіринту, користуйся ій \n") 
r.write(" ←━┳━━┳┓ \n ┣╸┃┏━┛┃ \n ┃╻╹┗┓╺┫ \n ┃┗┓╻┗╸┃ \n ┣╸┃┃╺━┫ \n ┃╺╋┛╺━┫ \n ┗━┻━━━↰")
r.close()

def fight1():
    print("О ні, ти зустрів монстра!!")
    time.sleep(1)
    monsterlife = 100
    notu = 2
    u = 2
    while monsterlife > 0 and youplayer.life > 0 and youplayer.stamina > 0:
        if youplayer.life > 0:
            print("Що ти хочеш робити?")
            time.sleep(1)
            print("1-атака 2-парирувати 3-втікти 4 -навики")
            time.sleep(1)
            askfight = int(input())
            if askfight == 1:
                if youplayer.weapon == "дерев'яний меч":
                    if notu == 1:
                        print("Монстр відбив твой удар")
                        time.sleep(1)
                        notu = 2
                    else:
                        monsterlife -= 20
                        print("Ти вдарив монстра, його життя", monsterlife)
                        time.sleep(1)
                elif youplayer.weapon == "сокира":
                    if notu == 1:
                        print("Монстр відбив твой удар")
                        time.sleep(1)
                    else:
                        monsterlife -= 35
                        print("Ти вдарив монстра, його життя", monsterlife)
                        time.sleep(1)
            elif askfight == 2:
                u = random.randint(1,2)
                if u == 1:
                    print("Ти відіб'єш наступний удар")
                    youplayer.stamina -= 15
                    time.sleep(1)
                    f = open("inventory_and_stats.txt", "w") 
                    f.write("Це твій інвентар \n") 
                    f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")
                    f.write("Твоя зброя - {}\n".format(youplayer.weapon))
                    f.write("Твоя броня - {}\n".format(youplayer.armor))
                    f.write("Твоє життя - {}\n".format(youplayer.life))
                    f.write("Твоя єнергія - {}\n".format(youplayer.stamina))
                    f.write("Твій навик - {}\n".format(youplayer.skill))
                    f.close()
                    u = 2
                else:
                    print("Ти не відіб'єш наступний удар:(")
                    time.sleep(1)
                    youplayer.stamina -= 5
            elif askfight == 3:
                print("Не вийде))")
                time.sleep(1)
            elif askfight == 4:
                if youplayer.skill == "немає":
                    print("В тебе немає навичок")
                    time.sleep(1)
                elif youplayer.skill == "файрбол":
                    print("Ти використав файрбол \n Стаміна -25 \n Життя монстра - 40,", monsterlife)
                    monsterlife -= 40
                    youplayer.stamina -= 25
                    time.sleep(1)
                    f = open("inventory_and_stats.txt", "w") 
                    f.write("Це твій інвентар \n") 
                    f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")
                    f.write("Твоя зброя - {}\n".format(youplayer.weapon))
                    f.write("Твоя броня - {}\n".format(youplayer.armor))
                    f.write("Твоє життя - {}\n".format(youplayer.life))
                    f.write("Твоя єнергія - {}\n".format(youplayer.stamina))
                    f.write("Твій навик - {}\n".format(youplayer.skill))
                    f.close()
        if monsterlife > 0:
            print("Xід монстра")
            m = random.randint(1,2)
            time.sleep(1)
            if m == 1:
                if u == 1:
                    print("Ти відбив удар")
                    time.sleep(1)
                else:
                    print("Удар пройшов по тобі, -15хп")
                    youplayer.life -= 15
                    time.sleep(1)
                    with open("log.txt", "a") as log:
                        log.write(f"[{datetime.datetime.now()}] Тебе побили, життя - {youplayer.life} \n")
                    f = open("inventory_and_stats.txt", "w") 
                    f.write("Це твій інвентар \n") 
                    f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")
                    f.write("Твоя зброя - {}\n".format(youplayer.weapon))
                    f.write("Твоя броня - {}\n".format(youplayer.armor))
                    f.write("Твоє життя - {}\n".format(youplayer.life))
                    f.write("Твоя єнергія - {}\n".format(youplayer.stamina))
                    f.write("Твій навик - {}\n".format(youplayer.skill))
                    f.close()
            elif m == 2:
                notu = random.randint(1,2)
                if notu == 1:
                    print("Монстр хоче відбити удар")
                    time.sleep(1)
                    print("Монстр відіб'є удар")
                    time.sleep(1)
                else:
                    print("Монстр хоче відбити удар")
                    time.sleep(1)
                    print("Бий сміло, монстр не відіб'є удар)")
                    time.sleep(1)

    print("бій закінчен")
    time.sleep(1)
    if monsterlife == 0:
        print("Ти вийграв у цій битві")
        youplayer.life = youplayer.max_life
        youplayer.stamina = youplayer.max_stamina
    else:
        print("Ти програв, але як?")
        time.sleep(1)
        print("Гра закінчена")
        try: 
            if youplayer.life > 0:
                youplayer.life += 0
        except ZeroDivisionError: 
            with open("log.txt", "a") as log:
                log.write(f"[{datetime.datetime.now()}] ZeroDivisionError, життя - {youplayer.life} \n") 
        exit()


def first_chest():
    print("Ти знайшов сундук!!")
    time.sleep(1)
    ask_first_chest = input("Хочеш його відкрити?? ")
    if ask_first_chest == "так":
        print("Ти відкрив сундук.")
        time.sleep(1)
        wats_inside = random.randint(1,3)
        if wats_inside == 1:
            print("Тобі випала сокира!! Урон - 35")
            time.sleep(1)
            sokura = input("Змінити свою зброю на сокиру? ")
            if sokura == "так":
                print("Твоя зброя - сокира")
                youplayer.weapon = "сокира"
                f = open("inventory_and_stats.txt", "w") 
                f.write("Це твій інвентар \n") 
                f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")
                f.write("Твоя зброя - {}\n".format(youplayer.weapon))
                f.write("Твоя броня - {}\n".format(youplayer.armor))
                f.write("Твоє життя - {}\n".format(youplayer.life))
                f.write("Твоя єнергія - {}\n".format(youplayer.stamina))
                f.write("Твій навик - {}\n".format(youplayer.skill))
                f.close()
            else:
                print("Твій вибір")


        elif wats_inside ==2:
            print("Тобі випало збільшення статистики! \n Життя +20 \n Стаміна +20")
            youplayer.max_life += 20
            youplayer.max_stamina += 20
            f = open("inventory_and_stats.txt", "w") 
            f.write("Це твій інвентар \n") 
            f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")
            f.write("Твоя зброя - {}\n".format(youplayer.weapon))
            f.write("Твоя броня - {}\n".format(youplayer.armor))
            f.write("Твоє життя - {}\n".format(youplayer.life))
            f.write("Твоя єнергія - {}\n".format(youplayer.stamina))
            f.write("Твій навик - {}\n".format(youplayer.skill))
            f.close()
        else:
            print("Тобі випав навик вогняний шар")
            youplayer.skill = "файрбол"
            f = open("inventory_and_stats.txt", "w") 
            f.write("Це твій інвентар \n") 
            f.write("Знаходь речі та зброю, щоб швидше перемагати супротивників \n")
            f.write("Твоя зброя - {}\n".format(youplayer.weapon))
            f.write("Твоя броня - {}\n".format(youplayer.armor))
            f.write("Твоє життя - {}\n".format(youplayer.life))
            f.write("Твоя єнергія - {}\n".format(youplayer.stamina))
            f.write("Твій навик - {}\n".format(youplayer.skill))
            f.close()


def walk1():
    go2 = ['вперед','наліво','вперед','наліво','направо','вперед']
    indexnetuda = 0
    while indexnetuda < len(go2):
        asknetuda = input("Куди хочеш йти? ")
        time.sleep(1)
        if asknetuda == go2[indexnetuda]:
            gonetuda1 = f"Ти пійшов {go[indexnetuda]}, куди це приведе.. "
            gonetuda2 = "Ти йдеш вірно, що ж попереду"
            gonetuda3 = "Куди ж ти йдеш"
            gonetuda_list = [gonetuda1, gonetuda2, gonetuda3]
            whatgonetuda = random.choice(gonetuda_list)
            print(whatgonetuda)
            indexnetuda += 1
        else:
            netuda1= f"{go[indexnetuda]}, стіна "
            netuda2 = "Стіна. Тобі не сюди"
            netuda3 = "Нініні, тобі не сюда"
            netuda_list = [netuda1, netuda2 ,netuda3 ]
            whatnetuda = random.choice()
            print(whatnetuda)
    else:
        first_chest()
        
def final_fight():
    youplayer.life = youplayer.max_life
    print("Це - дракон, вінальний бос гри.")
    time.wait(1)
    print("Вб'єш його, пройдеш гру")
    time.wait(1)
    print("Доречі, вітаю. Вся зброя яку ти знайшов, всі навики, тут на потрібні:)")
    print("Дракон б'є в одну з сторін ліво|право|вперед, тобі потрібно стати на вірну сторону, щоб не попасти під його атаку!!")
    time.wait(1)
    print("(за кожну правильну сторону, у дракона знімається 20хп, а вього їх 100)")
    time.wait(2)
    print("Готов? Гра починається:)")
    dragon_hp = 100
    watside_list = ["ліво","право","вперед"]
    whatside = random.randint(watside_list)
    playerchose = input("Куди станеш:) ")
    time.wait(1)
    while dragon_hp > 0 and youplayer.life > 0:
        whatside = random.randint(watside_list)
        playerchose = input("Куди станеш:) ")
        if playerchose == whatside:
            youplayer.life -= 20
            print(f"-уупс, дракон попав по тобі \n твоє життя {youplayer.life} \n життя дракона {dragon_hp}")
        else:
            dragon_hp -= 20
            print(f"Вірна сторона \n твоє життя {youplayer.life} \n життя дракона {dragon_hp}")
    else:
        if dragon_hp == 0:
            print("Ти вийграв!!!")
            time.wait(1)
            print("Кінець гри, тепер")
            exit()
        else:
            print("Ти програв, капець")
            time.wait(1)
            print("Поганий кінець")


    

    

go = ['вперед', 'вперед', 'направо', 'вперед', 'вперед', 'вперед', 'наліво', 'вперед', 'направо', 'вперед', 'вперед', 'вперед', 'наліво', 'вперед']
def where(go):
    index = 0
    with open("log.txt", "a") as log:
        log.write(f"[{datetime.datetime.now()}] Хп - 100, проблем немає \n")
    while index < len(go):
        ask = input("Куди йти ")
        if ask == go[index]:
            tudago1 = "Йди, йди"
            tudago2 = f"Ти пійшов {go[index]}"
            tudago3 = "Ти йдеш вірно, але куди це приведе"
            tudago_list = [tudago1, tudago2, tudago3]
            whattudago = random.choice(tudago_list)
            print(whattudago)
            index += 1
            if index == 3:
                fight1()
            if index == 5:
                print("Хмм, розвилка ")
                kydu = input("Куди хочеш йти? ")
                if kydu == "направо":
                    walk1()
                else:
                    (f"Ти пійшов {go[index]}, а правіше було щось цікаве")
                    index += 1
            if index == 12:
                print("Тобі не здається, що все якось тихо?")
                    
        else:
            tupik1 = "Тупик, тобі не сюди"
            tupik2 = f"Дивись на мапу, тобі не {ask}"
            tupik3 = "Ти повернув не туди("
            tupik_list = [tupik1,tupik2,tupik3]
            whattupik = random.choice(tupik_list)
            print(whattupik)
    else:
        import time
        print("Вітаю, ти пройшов лабіринт до кінця!!")
        print("exit()..")
        time.wait(2)
        print("Оні!!!!")
        time.wait(1)
        print("Що ж це летить?!")
        time.wait(1)
        final_fight()




where(go)