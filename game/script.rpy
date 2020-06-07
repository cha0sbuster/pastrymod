# The script of the game goes in this file.

init python:
    import json
    from actor import *
    human = race("Human","human","skin","white")
    goat = race("Goat","caprine","fur","white")
    races = [human,goat]
    racelist = []
    for i in races:
        racelist.append((i.name,i))

    mc = actor("Asriel",60,150,human,100,0,"white")

define plr = Character("MC")

label start:
    $ narrator("Select a race:", interact=False)
    $ mc.race = renpy.display_menu(racelist)
    $ mc.skinColour = renpy.input("What colour is your "+mc.race.skinType+"?")
