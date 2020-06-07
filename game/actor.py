from time import sleep
races = []
class race:
    def __init__(self,name,ears,skinType,skinColour):
        self.name=name
        self.ears=ears
        self.skinType=skinType
        self.skinColour=skinColour

class actor:
    def __init__(self,name,height,weight,race,stomachCap,stomachVolume,skinColour):
        self.name=name
        self.race=race
        self.height=height
        self.weight=weight
        self.stomachCap=0.0
        self.stomachVolume=0.0
        self.skinColour=race.skinColour
    
    def fill(self,amount,weightMod):
        self.stomachVolume=self.stomachVolume+amount
        self.weight=self.weight+weightMod
        return "Stomach Volume: "+str(self.stomachVolume)+" Weight: "+str(self.weight)

    def look(self):
        try:
            if self.name==plr.name:
                self.persp="Your"
            else:
                self.persp="their"
        except NameError:
            #if it can't find "plr" that means the player instance hasn't been made! we're probably in a test
            self.persp="Your"
        return self.persp+" name is "+self.name+". You are a "+self.race.name+". You are "+str(self.height)+" inches tall and weigh "+str(self.weight)+" pounds."

def actortest():
    print("RUNNING ACTORTEST")
    for i in races:
        print(i.name)
    gote = race("Goat","caprine","fur","white")
    plr = actor("Asriel",72,300,gote,100,0,"white")
    print(plr.look())

    for i in range(1,10):
        print(plr.fill(10,-5))
        sleep(0.05)
    print("ACTORTEST DONE")