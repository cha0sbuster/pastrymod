# The starting point for the project. Right now it's some setup code and a debug character creator.
# I'll probably move a lot of this to pastrymod.py.

init 0 python:
    import json, os, sys
    from PastryMod import * #IDK why it insists that I do a wildcard import, it won't work if i just import it with the others /shrug
    print (sys.argv[1]) #debug print: if this isn't the project's directory, something's fucked
    dataDir = sys.argv[1]+"\\game\\DATA" #tell the game where author-created data is
    raceDir = dataDir+"\\Races" #some shorthand strings
    races = {} #races is a dict for reasons
    actors = [] #but everything else should (?????) be okay as lists. i mean i'm probably gonna have to make them dicts anyways, but whatever
    places = []
    #Set up races.
    for f in os.listdir(raceDir):
        racefile = open(raceDir+"\\"+f)
        current = json.loads(racefile.read())
        current["name"] = Race(current["name"],current["ears"],current["skinType"],current["skinColour"])
        races[current["name"].name] = current["name"]
        racefile.close
    racelist=list(races.items()) #turn the race dict into a list that we can display in ren'py because it ONLY TAKES A LIST OF TUPLES
    print(races) #debug print
define plr = Character("MC")

label start:
    $ mc = Actor("Asriel",60,150,races['Human'],100,0,"white")
    $ mc.name = renpy.input("Welcome to PastryMod's debug character creator! What is your name?")
    $ narrator("Select a race:", interact=False)
    $ mc.race = renpy.display_menu(racelist)
    $ mc.skinColour = renpy.input("What colour is your "+mc.race.skinType+"?")
    $ print(str(mc)) #Debug print since the concatenated in-game print won't work
    # TODO: find out why this doesn't work
    #$ mc("Your name is "+mc.name+", and you are a "+mc.race+"with "+mc.skinColour+" "+mc.skinType".")
