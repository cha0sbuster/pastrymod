#imports lul
from pastrymod import *
import json
import os

#initialize race list, move into the races folder and print the files for debug
races=[]
try:
    os.chdir("DATA\\Races")
    print(os.listdir())
except FileNotFoundError:
    # pastrymod.setup() //run the directory setup script that i am going to make at some point i'm sure
    os.mkdir("DATA\\Races") # makes the Races folder if it got deleted somehow
for i in os.listdir():
    racefile = open(i)
    current = json.loads(racefile.read())
    print(current)
    race = Race(current["name"],current["ears"],current["skinType"],current["skinColour"])
    races.append(race)
    racefile.close

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
