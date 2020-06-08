init 0 python:
    from Pastrymod import *
    import json
    import os
    import sys
    print (sys.argv[1]) #debug
    dataDir = sys.argv[1]+"\\game\\DATA"
    raceDir = dataDir+"\\Races"
    races = []
    actors = []
    places = []
    #Set up races.
    for f in os.listdir(raceDir):
        racefile = open(raceDir+"\\"+f)
        current = json.loads(racefile.read())
        race = Race(current["name"],current["ears"],current["skinType"],current["skinColour"])
        races.append(race)
        racefile.close
        print(race.name)
    #make a list that we can display in ren'py because it ONLY TAKES A LIST OF TUPLES
    #FOR SOME REASON
    racelist=[]
    for i in races:
        racelist.append((i.name,i))

define plr = Character("MC")

label start:
    $ mc = Actor("Asriel",60,150,human,100,0,"white")
    $ narrator("Select a race:", interact=False)
    $ mc.race = renpy.display_menu(racelist)
    $ mc.skinColour = renpy.input("What colour is your "+mc.race.skinType+"?")
