import modules.map as m_map
import modules.data_base as m_data
import modules.clas as m_clas
def transfer(coor,take, check= False):
    for count in take:
        width,height=count.WIDTH,count.HEIGHT
        if count.ROTATE % 180!=0:
            height,width=count.WIDTH,count.HEIGHT
        if count.X < coor[0] < count.X + width and count.Y < coor[1] < count.Y + height:
            # if not check:
            #     count.X = coor[0]-count.WIDTH/ 2
            #     count.Y = coor[1]- count.HEIGHT/ 2
            return count
def place(take,list_coor,coor):
    checks= True
    count2=-1
    for count in list_coor:
                count2+=1
                check2= False
                vertical=1
                # print((int(take.IMG2) + count[2]-1))
                if take.ROTATE %  180== 0:
                                        if int(take.IMG2)+ count[3]-1< 10:
                                            check2 = True
                elif (int(take.IMG2) + count[2]-1)< 10:
                                check2 = True
                #                 vertical=10
                # if check2:
                #     for count1 in range(int(take.IMG2)-1):
                #         if list_coor[count2+count1*vertical+1]!=0:
                #             check2=0
                if count[0]< coor[0]< count[0]+40 and count[1]< coor[1]< count[1]+40 and check2 :
                            take.X= count[0]
                            take.Y= count[1]
                            take.CELL= [count[2],count[3]]
                            checks= False
    return (take,checks)

def attack(coor):
    ship= 0
    for row in m_map.list_coor_enemy:
        for coor_cell in row:
            if coor_cell[0]<coor[0]<coor_cell[0]+40 and coor_cell[1]<coor[1]<coor_cell[1]+40:
                cell=m_map.bot_map[coor_cell[2]][coor_cell[3]]
                if m_map.attacks_bot_map[coor_cell[2]][coor_cell[3]]==0:
                    if cell==0 or cell==5:
                        m_data.step_text="хід бота"
                        m_data.step=0
                        m_data.color_step=[200,50,25]
                # if type (cell)!= int:
                #     ship= cell[2]
                #     if ship!= 0:
                #        m_map.bot_map[ship[0]] [ship[1]]
                    else:
                        m_clas.play_music()
                m_map.attacks_bot_map[coor_cell[2]][coor_cell[3]]=None
    