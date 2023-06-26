import modules.data_base as m_data
def win_lose(map,attack_map,win):
    check=1
    for row in range(10):
        for cell in range(10):
            if 0!=map[row][cell]!=5:
                if attack_map[row][cell]!=None:
                    check=0
    if check:
        m_data.display= 1
        m_data.win_lose=1
        m_data.text= "restart"
        if win:
            m_data.step_text="Ви виграли"
            m_data.color_step=[155,223,255]
        else:
            m_data.step_text="Ви програли"
            m_data.color_step=[200,50,25]    
        for ship in m_data.ships:
            ship.ATTACK=1