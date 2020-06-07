from actor import *
import json
import os

races=[]
os.chdir("DATA\\Races")
print(os.listdir())

for i in os.listdir():
    racefile = open(i)
    current = json.loads(racefile.read())
    print(current)
    race = race(current["name"],current["ears"],current["skinType"],current["skinColour"])
    races.append(race)

#human = race("human","human","skin","white")
#goat = race("goat","caprine","fur","white")
#races = [human,goat]

def test():
    #print("RUNNING ACTORTEST")
    #goat = race("Goat","caprine","fur","white")
    #plr = actor("Asriel",72,300,goat,100,0)
    #print(plr.look())

    #for i in range(1,10):
    #    print(plr.fill(10,-5))
    #    sleep(0.05)

    print("Loaded Races:")
    for i in races:
        print(i.name)
    
    print("ACTORTEST DONE")

test()
