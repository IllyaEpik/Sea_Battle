import modules.data_base as m_data
import modules.map as m_map
import modules.clas as m_clas
import modules.bot as m_bot
def restart(screen):
    m_data.data()
    m_clas.play_music('music',-1)
    m_map.map()
    x,y= 44,503
    for count in range(4):
        m_data.ships.append(m_clas.Item(coordinate=(x,y),width_height=(50,50), take= True))
        m_data.ships[count].load_image("1",screen)
        x+=80
        if count == True and count != 2:
            x-=160
            y+=80
    m_data.ships.append(m_clas.Item(coordinate=(x,y),width_height=(100,50),take= True))
    m_data.ships.append(m_clas.Item(coordinate=(x,y-80),width_height=(100,50),take= True))
    m_data.ships.append(m_clas.Item(coordinate=(x+120,y-40),width_height=(100,50),take= True))
    m_data.ships.append(m_clas.Item(coordinate=(x+240,y),width_height=(150,50),take= True))
    m_data.ships.append(m_clas.Item(coordinate=(x+240,y-80),width_height=(150,50),take= True))
    m_data.ships.append(m_clas.Item(coordinate=(x+420,y-40),width_height=(200,50),take= True))
    m_map.bot_map= m_bot.bot_place(m_map.bot_map)
    m_map.ships(m_map.bot_map)
    for count in range(6):
        if count<3:
            num="2"
        elif count!=5:
            num="3"
        else:
            num="4"
        m_data.ships[count+4].load_image(num,screen)