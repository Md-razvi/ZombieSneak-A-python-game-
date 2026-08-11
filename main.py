from direct.showbase.ShowBase import ShowBase
from direct.task import Task
from direct.actor.Actor import Actor


class Game(ShowBase):

    def __init__(self):
        super().__init__()
        
        
        self.disableMouse()
        #Controls 
        self.isWalking=False
        
        
        self.keys={
            "left":False,
            "right":False,
            "forward":False,
            "backward":False
        }
        
        self.setUpControls()
        self.taskMgr.add(self.playerMovement,"playerMovement")
        
        #Player Cube
        #self.cube = self.loader.loadModel("game_assets\characterRIGGED.glb")
        #self.cube.reparentTo(self.render)
        
        # Changing it to player 
        self.player=Actor("game_assets/models/Human1.glb")
        self.player.reparentTo(self.render)
        self.player.setH(180)
        self.player.loop("Idle")
        
        
        # self.cube.setColor(0, 0, 1, 1)

        # Camera
        self.player.setPos(0,0,0)
        playerPos=self.player.getPos()
        self.camera.setPos(playerPos.x,playerPos.y-30,playerPos.z+15)
        self.taskMgr.add(self.cameraFollow,"cameraFollow")
        self.camera.lookAt(self.player)
        print("animation", self.player.getAnimNames())
        #self.player.loop("Walk")
        
        #Ground
        self.ground=self.loader.loadModel("models/box")
        self.ground.reparentTo(self.render)
        self.ground.setColor(0, 0.5, 0, 1)
        self.ground.setScale(20,25,0.1)
        self.ground.setPos(0,0,-1)
        print("Camera position:", self.camera.getPos())
        print("Player position:", self.player.getPos())
        cube_bounds = self.player.getTightBounds()
        ground_bounds = self.ground.getTightBounds()
        cube_min, cube_max = cube_bounds
        ground_min, ground_max = ground_bounds
        print("Cube size:", cube_max - cube_min)
        print("Ground size:", ground_max - ground_min)
    def cameraFollow(self,task):
        playerPos=self.player.getPos()
        self.camera.setPos(
            playerPos.x,
            playerPos.y-8,
            playerPos.z+2
        )
        self.camera.lookAt(self.player)
        return Task.cont;
    def setUpControls(self):
        self.accept("arrow_up",self.setKey,["forward",True])
        self.accept("arrow_up-up",self.setKey,["forward",False])
        
        self.accept("arrow_down",self.setKey,["backward",True])
        self.accept("arrow_down-up",self.setKey,["backward",False])
        
        self.accept("arrow_right",self.setKey,["right",True])
        self.accept("arrow_right-up",self.setKey,["right",False])
        
        self.accept("arrow_left",self.setKey,["left",True])
        self.accept("arrow_left-up",self.setKey,["left",False])
    
    # def moveForward(self):
    #     self.cube.setY(self.cube.getY() + 1)
    # def moveBackward(self):
    #     self.cube.setY(self.cube.getY() - 1)
    # def moveRight(self):
    #     self.cube.setX(self.cube.getX() + 1)
    # def moveLeft(self):
    #     self.cube.setX(self.cube.getX() - 1)
    
    def setKey(self,key,value):
        self.keys[key]=value
        
    def playerMovement(self,task):
        speed=5
        dt=globalClock.getDt()
        if self.keys["forward"]:
            self.player.setY(self.player.getY() + speed*dt)
        if self.keys["backward"]:
            self.player.setY(self.player.getY() - speed*dt)
        if self.keys["left"]:
            self.player.setX(self.player.getX() - speed*dt)
        if self.keys["right"]:
            self.player.setX(self.player.getX() + speed*dt)
        # we are creating a bool value for animation
        moving =(self.keys["forward"])
        if moving and not self.isWalking:
            self.player.loop("Walk")
            self.player.setPlayRate(2.0, "Walk")
            self.isWalking=True
        elif not moving and self.isWalking:
            self.player.stop()
            
            self.isWalking=False
            
        return Task.cont
            
                
        
        
game = Game()
game.run()