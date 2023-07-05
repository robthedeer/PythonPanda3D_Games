from asyncio.mixins import _global_lock
from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.actor.Actor import Actor
from panda3d.core import Vec3, Vec4

class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        #Window size
        properties =WindowProperties()
        properties.setSize(800,680)
        self.win.requestProperties(properties)

        #Load Environment
        self.environment =self.loader.loadModel("/Users/macrob/Documents/PandaSampleModels-master/Environment/environment.egg")
        self.environment.reparentTo(self.render)

        #Load Actor1
        self.Actor1 =Actor("/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/act_p3d_chan.egg.pz",{"walk":"/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/a_p3d_chan_walk.egg.pz"})
        self.Actor1.reparentTo(self.render)
        self.Actor1.setPos(0,7,0)
        self.Actor1.loop("walk")


        #Load Actor 2
        self.Actor2 =Actor("/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/act_p3d_chan.egg.pz",{"run":"/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/a_p3d_chan_run.egg.pz"})
        self.Actor2.reparentTo(self.render)
        self.Actor2.setPos(2,7,0)
        self.Actor2.getChild(0).setH(0)
        self.Actor2.loop("run")

        #load Actor 3
        self.Actor3=Actor("/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/act_p3d_chan.egg.pz")
        self.Actor3.reparentTo(self.render)
        self.Actor3.setPos(1,7,0)
        #Set the position of the camera
        #self.camera.setPos(0,0,32)
        #self.camera.setP(-90)


    #UpdateTask
        self.updateTask = taskMgr.add(self.update, "update")





    #KeyMap
        self.KeyMap ={
        "up": False,
        "down": False,
        "left": False,
        "right": False,
        "shoot": False
    } 
    

    #Key registration
        self.accept("w",self.updateKeyMap,["up",True])
        self.accept("w-up",self.updateKeyMap,["up",False])

        self.accept("s",self.updateKeyMap,["down",True])
        self.accept("s-up",self.updateKeyMap,["down",False])

        self.accept("a", self.updateKeyMap, ["left", True])
        self.accept("a-up", self.updateKeyMap, ["left", False])

        self.accept("d", self.updateKeyMap, ["right", True])
        self.accept("d-up", self.updateKeyMap, ["right", False])

        self.accept("mouse1", self.updateKeyMap, ["shoot", True])
        self.accept("mouse1-up", self.updateKeyMap, ["shoot", False])




    def updateKeyMap(self,controlName,controlState):
        self.KeyMap[controlName] =controlState
        print(controlName,"set to",controlState )

    def update(self, task):

        dt =globalClock.getDt()

        #Calculate the distance and move the character
        if self.KeyMap["up"]:
            self.Actor1.setPos(self.Actor1.getPos() + Vec3(0, 5.0*dt, 0))
        if self.KeyMap["down"]:
            self.Actor1.setPos(self.Actor1.getPos() +Vec3(0,-0.5*dt, 0 ))
        if self.KeyMap["left"]:
            self.Actor1.setPos(self.Actor1.getPos() + Vec3(-5.0*dt, 0,0))
        if self.KeyMap["right"]:
            self.Actor1.setPos(self.Actor1.getPos() + Vec3(5.0*dt ,0,0))

        if self.KeyMap["shoot"]:
            print("Ouch!")
        
        return task.cont

    #Сontrolling the character(Actor)


game = Game()
game.run()