import pygame
import modules.create_json as m_json
import modules.data_base as m_data
pygame.mixer.init()
class Item():
    def __init__(self, cell = 0,coordinate= (2,2), width_height= (100,100), rotate=0,name=None, take= False):
        self.ROW=0
        self.ATTACK=0
        self.CELL2=1
        self.CELL=cell
        self.LAST_CELL= 0
        self.IMG = None
        self.Y = coordinate[1]
        self.X = coordinate[0]
        self.START_POSITION= coordinate
        self.IMG2 = None
        self.WIDTH =width_height[0] 
        self.HEIGHT = width_height[1]
        self.ROTATE = rotate
        self.CHECK = True
        self.TAKE= take
        if name!=None:
            self.load_image(name)
    def load_image(self, name, blit=False):
        self.IMG = pygame.image.load(m_json.find_file(f"images/{name}.png"))
        self.IMG = pygame.transform.scale(self.IMG, (self.WIDTH,self.HEIGHT))
        self.IMG2 = name
        self.IMG = pygame.transform.rotate(self.IMG,self.ROTATE)
        self.IMG.set_colorkey((255,255,255))
        if blit != False:
            self.blit_sprite(blit)
    def blit_sprite(self,screen,coor= None):
        if coor== None:
            coor= (self.X, self.Y)
        screen.blit(self.IMG,coor)
class Bubble():
    def __init__(self,x,y,size,speed,count):
        self.X=x
        self.Y=y
        self.SPEED=speed
        self.SIZE=size
        self.COUNT=count
        # self.IMG = pygame.image.load(m_json.find_file(f"images/bubble.png"))
        # self.IMG = pygame.transform.scale(self.IMG, (size,size))
    # def blit_sprite(self,screen,coor= None):
    #     if coor== None:
    #         coor= (self.X, self.Y)
        
    def move(self,screen):
        self.Y-=self.SPEED
        # screen.blit(self.IMG,(self.X,self.Y))
        pygame.draw.circle(screen,(0,255,255),(self.X+self.SIZE/2,self.Y+self.SIZE/2),self.SIZE,3)
        m_data.display=1
        if self.Y<0- self.SIZE:
            self.SPEED=0
            return 1
        return 0
pygame.init()
pygame.mixer.music.set_volume(0.2)
def play_music(name_file= "shoot", loops= 0):
    # pygame.mixer.music.set_volume()
    pygame.mixer.music.load(m_json.find_file(f"audio/{name_file}.mp3"))
    a= pygame.mixer.music.play(loops)
    return a
music= play_music('music',-1)