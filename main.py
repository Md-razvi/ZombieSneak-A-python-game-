from direct.showbase.ShowBase import ShowBase
from direct.task import Task


class Game(ShowBase):

    def __init__(self):
        super().__init__()
        
        self.disableMouse()
        #Controls 
        
        
        
        self.keys={
            "left":False,
            "right":False,
            "forward":False,
            "backward":False
        }
        
        self.setUpControls()
        self.taskMgr.add(self.playerMovement,"playerMovement")
        
        #Player Cube
        self.cube = self.loader.loadModel("models/box")
        self.cube.reparentTo(self.render)
        self.cube.setColor(0, 0, 1, 1)

        # Camera
        self.cube.setPos(10,12,0)
        playerPos=self.cube.getPos()
        self.camera.setPos(playerPos.x,playerPos.y-30,playerPos.z+15)
        self.taskMgr.add(self.cameraFollow,"cameraFollow")
        self.camera.lookAt(self.cube)
        
        #Ground
        self.ground=self.loader.loadModel("models/box")
        self.ground.reparentTo(self.render)
        self.ground.setColor(0, 0.5, 0, 1)
        self.ground.setScale(20,25,0.1)
        self.ground.setPos(0,0,-1)
        print("Camera position:", self.camera.getPos())
        print("Cube position:", self.cube.getPos())
        cube_bounds = self.cube.getTightBounds()
        ground_bounds = self.ground.getTightBounds()
        cube_min, cube_max = cube_bounds
        ground_min, ground_max = ground_bounds
        print("Cube size:", cube_max - cube_min)
        print("Ground size:", ground_max - ground_min)
    def cameraFollow(self,task):
        playerPos=self.cube.getPos()
        self.camera.setPos(
            playerPos.x,
            playerPos.y-30,
            playerPos.z+15
        )
        self.camera.lookAt(self.cube)
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
        speed=10
        dt=globalClock.getDt();
        if self.keys["forward"]:
            self.cube.setY(self.cube.getY() + speed*dt)
        if self.keys["backward"]:
            self.cube.setY(self.cube.getY() - speed*dt)
        if self.keys["left"]:
            self.cube.setX(self.cube.getX() - speed*dt)
        if self.keys["right"]:
            self.cube.setX(self.cube.getX() + speed*dt)
        return Task.cont
            
                
        
        
game = Game()
game.run()