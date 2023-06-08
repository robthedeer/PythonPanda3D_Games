

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.actor.Actor import Actor
from panda3d.core import AmbientLight
from panda3d.core import Vec4
from panda3d.core import DirectionalLight
#from  panda3d.core import Vec4,Vec3
class Game(ShowBase):
    def __init__(self):
        ShowBase.__init__(self)

        properties =WindowProperties()
        properties.setSize(1000, 800)
        self.win.requestProperties(properties)

        #Load enveronment
        
        self.environment = self.loader.loadModel("/Users/macrob/Documents/Panda3DTutorial/PandaSampleModels-master/Environment/environment.egg")
        self.environment.reparentTo(self.render)
        # Load Actor
        self.Actor =Actor("/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/act_p3d_chan",{"walk": "/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/a_p3d_chan_run"})
        self.Actor.reparentTo(self.render)

        
        #Set rotation and position of the Actor
        self.Actor.setPos(0,7,0)
        

        #Set actor to run
        self.Actor.loop("walk")
        
        #Move the camera to a position high above the screen
        # # --that is, offset it along the z-axis.
        self.camera.setPos(0,0,32)
        self.camera.setP(-90)

        #Light and color
        self.ambientLight =AmbientLight("ambient light")
        self.ambientLight.setColor(Vec4(0.2,0.2,0.2,1))
        self.ambientLightNodePath =self.render.attachNewNode(self.ambientLight)
        self.render.setLight(self.ambientLightNodePath)
        self.mainLight = DirectionalLight("main light")
        self.mainLightNodePath =self.render.attachNewNode(self.mainLight)
        #Turn it around by 45 degrees and tilt it down by 45 degrees
        self.mainLightNodePath.setHpr(45,-45,0)
        self.render.setLight(self.mainLightNodePath)

        #Task manager method
       # self.updateTask =self.taskMgr.add(self.update,"update")


        #set a key-map diectionary for key responses
        self.keyMap ={
            "up":False,
            "down":False,
            "left":False,
            "right":False
        }

        self.accept("w",self.updateKeyMap,["up",True])
        self.accept("w-up",self.updateKeyMap,["up",False])
        self.accept("s",self.updateKeyMap,["down",True])
        self.accept("s-up",self.updateKeyMap,["down",False])
        self.accept("a",self.updateKeyMap,["left",True])
        self.accept("a-up",self.updateKeyMap,["left",False])
        self.accept("d",self.updateKeyMap,["right",True])
        self.accept("d-up",self.updateKeyMap,["right",False])
        self.accept("mouse1",self.updateKeyMap,["shoot",True])
        self.accept("mouse1-up",self.updateKeyMap,["shoot",False])

    def updateKeyMap(self,controlName,controlState):
        self.keyMap[controlName]=controlState
        print(controlName,"set to",controlState)
    #Update and controls
    #def update(self,task,dt):
        #get the amount of time since the last update
       # self.dt =self.globalClock.getDt()
        #if the keys are pressed , use the time and clock  function to calcuclate how fare to move the character
       # if self.keyMap["up"]:
           # self.Actor.setPos(self.Actor.getPos()+Vec3(0,5.0*dt,0))
        #if self.keyMap["down"]:
            #self.Actor.setPos(self.Actor)
            
            
            
        #return task.cont


game =Game()
game.run()