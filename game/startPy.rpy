init 0 python:
    from Pastrymod import *
    import json
    import os
    import sys
    print (sys.argv[1]) #debug
    dataDir = sys.argv[1]+"\\game\\DATA"
    raceDir = dataDir+"\\Races"
    races = {}
    actors = []
    places = []
    #Set up races.
    for f in os.listdir(raceDir):
        racefile = open(raceDir+"\\"+f)
        current = json.loads(racefile.read())
        current["name"] = Race(current["name"],current["ears"],current["skinType"],current["skinColour"])
        races[current["name"].name] = current["name"]
        racefile.close
    #make a list that we can display in ren'py because it ONLY TAKES A LIST OF TUPLES
    #FOR SOME REASON
    racelist=[]
    #for e in races:
    #   racelist.append((e['name'],races[e]))
    print(races)
define plr = Character("MC")

label start:
    $ mc = Actor("Asriel",60,150,races['Human'],100,0,"white")
    $ narrator("Select a race:", interact=False)
    $ mc.race = renpy.display_menu(races)
    $ mc.skinColour = renpy.input("What colour is your "+mc.race.skinType+"?")
