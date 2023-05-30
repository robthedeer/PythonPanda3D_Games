

from direct.showbase.ShowBase import ShowBase
from panda3d.core import WindowProperties
from direct.actor.Actor import Actor

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
        self.Actor =Actor("/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/act_p3d_chan.egg.pz",{"walk": "/Users/macrob/Documents/Panda3DTutorial/p3d_samples-master/models/a_p3d_chan_run.egg.pz"})
        self.Actor.reparentTo(self.render)

        #Loop
        self.Actor.loop("walk")



game =Game()
game.run()