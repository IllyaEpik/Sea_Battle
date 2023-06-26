import modules.data_base as m_data
import pygame
import modules.clas as m_clas
# def set_difficulty(coor):
    # m_data.difficulty
def look_difficulty(coordinate,check=0):
    # check1= None
    # check2= None
    # if not (0,0,0)== m_data.medium_color:check1= 2
    # if m_data.hard_color!= (0,0,0):check1= 1
    # if m_data.easy_color!=(0,0,0):check1=3

    if m_data.select_difficulty:
        m_data.hard_color=(0,0,0)
        m_data.easy_color=(0,0,0)
        m_data.medium_color=(0,0,0)
        print(pygame.mouse.get_pos())
        if 94<coordinate[1]<204 and 573>coordinate[0]>435:
            if check:
                m_data.difficulty="hard"
            m_data.hard_color=[255,25,25]
        if 610>coordinate[0]>400 and 297< coordinate[1]<404:
            if check:
                m_data.difficulty="medium"
            m_data.medium_color=[255,155,15]
        if 500<coordinate[1]<600 and 573>coordinate[0]>435:
            if check:
                m_data.difficulty= "easy"
            m_data.easy_color=[75,255,15]
        if m_data.difficulty!=None:
            m_data.select_difficulty= 0
            # set_volume
            # m_clas.music.set_volume(0.05)
            pygame.mixer.music.pause()
    # if not m_data.hard_color== m_data.easy_color== m_data.medium_color and :