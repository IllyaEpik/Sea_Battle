import pygame
import modules.create_json as m_json
import modules.data_base as m_data
font= pygame.font.SysFont("comicsansms",34)
font1=pygame.font.SysFont("comicsansms",54)
img_turn=pygame.image.load(m_json.find_file("images/turn.png"))
img_turn=pygame.transform.scale(img_turn,(50,50))
def cross(x,y,screen,color=(255,50,50)):
    pygame.draw.line(screen,color,start_pos=(x,y),end_pos=(x+40,y+40),width=5)
    pygame.draw.line(screen,color,start_pos=(x+40,y),end_pos=(x,y+40),width=5)
def create_button(screen,):
    global font1
    global font
    # print(m_data.coor_button[1])
    if m_data.select_difficulty:
        x,y=500,100
        text="hard"
        color_text=(255,25,25)
        border_color=m_data.hard_color
        for count in range(3):
            width,height=font1.size(text)
            x-= width/2
            pygame.draw.line(screen, border_color,[x-4,y], [x+width+15,y], width=10)
            pygame.draw.line(screen, border_color,[x-4,y+100], [x+width+15,y+100], width=10)
            pygame.draw.line(screen, border_color,[x,y], [x,y+100], width=10)
            pygame.draw.line(screen, border_color,[x+width+10,y], [x+width+10,y+100], width=10)
            screen.blit(font1.render(text, True,color_text), [x+5,y])
            text="medium"
            color_text=(255,155,15)
            border_color= m_data.medium_color
            if count== 1:
                border_color=m_data.easy_color
                text="easy"
                color_text=(75,255,15)
            y+=200
            x= 500
    else:
        if m_data.win_lose or not m_data.start_game:
            pygame.draw.rect(screen,m_data.color_button[0],m_data.coor_button[0]+ [190,50])
            pygame.draw.rect(screen,m_data.color_button[1],[m_data.coor_button[0][0]+5,m_data.coor_button[0][1]+5,180,40 ])
            screen.blit(font.render(m_data.text, True,[255,255,255]), m_data.text_coor)
        if not m_data.start_game:
           
            pygame.draw.rect(screen,m_data.color_button[0],m_data.coor_button[1]+[60,60])
            pygame.draw.rect(screen,m_data.color_button[1],[m_data.coor_button[1][0]+5,m_data.coor_button[1][1]+5,50,50])
            cross(m_data.coor_button[1][0]+9.3,m_data.coor_button[1][1]+9.3,screen,(50,255,50))
            pygame.draw.rect(screen,m_data.color_button[2],[m_data.coor_button[1][0]-100,m_data.coor_button[1][1]]+[60,60])
            pygame.draw.rect(screen,m_data.color_button[1],[m_data.coor_button[1][0]-95,m_data.coor_button[1][1]+5,50,50])
            
            screen.blit(img_turn,(m_data.coor_button[1][0]-95,m_data.coor_button[1][1]+5))
        else:
            pygame.draw.rect(screen,m_data.color_rect,m_data.rect)
            text=font.render(m_data.step_text, True,m_data.color_step)
            screen.blit(text, (m_data.text_coor2[0]-text.get_width()/2,m_data.text_coor2[1]))