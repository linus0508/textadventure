import random
import time

name = ""
location = ""
gold = 0
wood = 0
health = 100
hunger = 100
sword = False
armor = False

def setName():
    reset()
    global name
    name = input("Hallo Fremder! Bitte gebe deinen Namen ein: ")
    print(f"Hallo {name}! Schön dich kennenzulernen.")
    gameLoop()

def gameLoop():
    print("Was ist deine Mission?")
    print ("1. Reisen")
    print ("2. Handeln")
    print ("3. Ruhen")
    print ("4. Kämpfen")
    print ("5. Arbeiten")
    print ("6. Inventar")
    print ("7. Stats")
    task = input("Deine Wahl: ")

    match task:
        case "1":
            travel()
        case "2":
            trade()
        case "3":
            rest()
        case "4":
            fight()
        case "5":
            work()
        case "6":
            inventory()
        case "7":
            stats()

def travel():
    print("Wohin deines Weges?")
    print("1. Dorf")
    print("2. Festung")
    print("3. Höhle")
    print("4. Wald")
    global location
    input_location = input("Deine Wahl: ")
    match input_location:
        case "1":
            location = "Dorf"
        case "2":
            location = "Festung"
        case "3":
            location = "Höhle"
        case "4":
            location = "Wald"
    print(f"Willkommen {name}! Deine neue Location ist {location}.")
    gameLoop()

def trade():
    if (location == "Dorf"):
        print("Mit wem möchtest du Handeln?")
        print("1. Schmied")
        print("2. Baecker")
        print("3. Zimmermann")
        npc_input = input("Deine Wahl: ")

        match npc_input:
            case "1":
                npc = "Schmied"
            case "2":
                npc = "Baecker"
            case "3":
                npc = "Zimmermann"
        npc_trade(npc)
    else:
        print("Hier ist es Menschenleer! Suche dir einen gut besuchten Ort um zu Handeln.")
        gameLoop()

def rest():
    global health
    if (location == "Dorf" or location == "Höhle"):
        regen = random.randint(10, 30)
        health = health + regen
        if (health > 100):
            health = 100
        print(f"Das war ein erholsamer Schlaf! Du hast nun {health} Leben!")
        gameLoop()
    else:
        print("Hier ist es zu Gefährlich! Suche dir einen geeigneten Ort zum Ruhen!")
        gameLoop()

def fight():
    global health
    global armor
    global sword
    global gold

    if (location == "Festung"):
        print("Ein Krieger erscheint! Erkämpfe dir dein Loot!")
        krieger_health = random.randint(40, 90)
        while (krieger_health > 0):
            if (sword == True):
                attack = random.randint(10, 25)
            else:
                attack = random.randint(5, 15)
            krieger_health = krieger_health - attack
            print(f"Das war effektiv. Du hast {attack} Schaden verteilt")

            if (armor == True):
                attack = random.randint(3, 10)
            else:
                attack = random.randint(5, 15)
            health = health - attack
            print(f"Pass auf! Du hast {attack} Schaden erhalten und noch {health} Leben.")

            if (health < 10):
                print(f"Rückzug, {name}! Du hast nur noch {health} Leben")
                gameLoop()
            if (health <= 0):
                print(f"You died...")
                setName()
        print(f"Sehr gut {name}. Das war ein voller Erfolg")
        loot = random.randint(3, 20)
        gold = gold + loot
        print(f"Dein Gegner hatte {loot} Gold dabei. Die sind nun dein!")
        gameLoop()
    else:
        print("Hier sind alle friedlich! Suche dir einen anderen Ort zum unruhe Stiften!")
        gameLoop()

def work():
    global wood
    global hunger
    if (location == "Wald"):
        print("Hier kannst du Bäume fällen. Denke an ausreichend Nahrung!")
        while (hunger > 10):
            holz = random.randint(3, 10)
            print(f"Du hast einen Baum gefällt. Das bringt dir {holz} Holz.")
            wood = wood + holz
            work_hunger = random.randint(1, 5)
            hunger = hunger - work_hunger
        print(f"{name}! Du hast hunger! Besorge dir etwas essbares.")
        gameLoop()
    else:
        print("Hier gibt es keine Arbeit für dich.")
        gameLoop()

def inventory():
    global gold
    global wood
    global armor
    global sword
    print(f"Du hast {gold} Gold und {wood} Holz im Inventar")
    if (armor == True):
        print(f"Außerdem besitzt du eine Rüstung.")
    if (sword == True):
        print(f"Außerdem besitzt du ein Schwert.")
    gameLoop()

def stats():
    print(f"Aktuell hast du {health} Leben und {hunger} Hunger.")
    gameLoop()

def npc_trade(npc):
    match npc:
        case "Schmied":
            print("Ich sehe du brauchst Ausstattung! Was kann ich dir anbieten?")
            print("1. Schwert (10 Gold)")
            print("2. Rüstung (50 Gold)")
            buy = input("Deine Wahl: ")
            if (buy == "1"):
                buy_item("schwert", 10)
            if (buy == "2"):
                buy_item("rüstung", 50)

        case "Baecker":
            print("Ich sehe du hast Hunger! Was kann ich dir anbieten?")
            print("1. Brot (1 Gold)")
            print("2. Kuchen (2 Gold)")
            buy = input("Deine Wahl: ")
            if (buy == "1"):
                buy_item("brot", 1)
            if (buy == "2"):
                buy_item("kuchen", 2)

        case "Zimmermann":
            print("Ich sehe du brauchst Gold! Ich brauche Holz. Wir sollten Handeln!")
            print("Gebe mir 10 Holz und ich entlohne dich mit 1 Gold!")
            trade = input("Bäume verkaufen? (ja/nein): ")
            if trade.lower() == "ja":
                trade_wood()
            else:
                print("Vielleicht ein anderes Mal.")
                gameLoop()

def buy_item(item, price):
        global gold
        global hunger
        global sword
        global armor
        if (price > gold):
            print("Du hast leider nicht genug Gold. Verdiene erst etwas!")
            gameLoop()
        else:
            gold = gold - price
            match item:
                case "schwert":
                    sword = True
                    gameLoop()
                case "rüstung":
                    armor = True
                    gameLoop()
                case "brot":
                    hunger = hunger + 5
                    print(f"Du hast nun {hunger} Hunger.")
                    opt = input("Darf es noch mehr sein? (ja/ nein): ")
                    if (opt.lower == "ja"):
                        npc_trade("Baecker")
                    else: 
                        gameLoop()
                case "kuchen":
                    hunger = hunger + 15
                    print(f"Du hast nun {hunger} Hunger.")
                    opt = input("Darf es noch mehr sein? (ja/ nein): ")
                    if (opt.lower == "ja"):
                        npc_trade("Baecker")
                    else: 
                        gameLoop()

def trade_wood():
    global wood
    global gold
    print(f"Du hast {wood} Holz. Wie viel möchtest du verkaufen? (10 Holz = 1 Gold)")
    amount = int(input("Anzahl der Holzstapel (je 10 Holz): "))
    if amount * 10 > wood:
        print("Du hast nicht genug Holz.")
        gameLoop()
    else:
        wood -= amount * 10
        gold += amount
        print(f"Du hast nun {gold} Gold.")
        gameLoop()

def reset():
    global name, location, gold, wood, health, hunger, sword, armor
    name = ""
    location = ""
    gold = 0
    wood = 0
    health = 100
    hunger = 100
    sword = False
    armor = False

def loadingScreen():
    print(r"""
___________              __               _____       .___                    __                        
\__    ___/___ ___  ____/  |_            /  _  \    __| _/__  __ ____   _____/  |_ __ _________   ____  
  |    |_/ __ \\  \/  /\   __\  ______  /  /_\  \  / __ |\  \/ // __ \ /    \   __\  |  \_  __ \_/ __ \ 
  |    |\  ___/ >    <  |  |   /_____/ /    |    \/ /_/ | \   /\  ___/|   |  \  | |  |  /|  | \/\  ___/ 
  |____| \___  >__/\_ \ |__|           \____|__  /\____ |  \_/  \___  >___|  /__| |____/ |__|    \___  >
             \/      \/                        \/      \/           \/     \/                        \/  
    """)

    for x in range(0, 30):
        bar = "#" * x
        print(f"[{bar.ljust(30)}]", end="\r", flush=True)
        time.sleep(0.2)
    print()


    
    print("Herzlich Willkommen zum TextAdventure Game 1.0")
    print("Viel Spaß beim Spielen!")
    time.sleep(2)
    


##Calls##

loadingScreen()
print()
print()
setName()