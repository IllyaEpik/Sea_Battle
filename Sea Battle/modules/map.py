# import modules.bot as m_bot
import modules.data_base as m_data
import modules.clas as m_clas
import pygame
# import random
import modules.create_json as m_json
pygame.init()
def map():
    global player_map, bot_map, attacks_player_map, attacks_bot_map 
    player_map = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
    bot_map = [
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    attacks_bot_map=[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
    attacks_player_map=[
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]
        ]
map()
# attacks_player_map
# [5][6]=None
def print_map(map):
    # del map2[0]
    m_json.create_json({"map":map},"copy")
    for count in range(10):
        for count1 in range(10):
            try:
                map[count][count1]= map[count][count1][0]
            except TypeError:
                continue

        print(map[count])
    map=0
    map=m_json.read_json("copy")["map"]
    return map
    
def cross(x,y,screen,color=(255,50,50)):
    pygame.draw.line(screen,color,start_pos=(x,y),end_pos=(x+40,y+40),width=5)
    pygame.draw.line(screen,color,start_pos=(x+40,y),end_pos=(x,y+40),width=5)
# def help_check_map(map,num,row,cell,quetion):
#     answer=1
#     if  map[row][cell]==num and  (9>cell>0 and quetion or 9>row>0 and not quetion)  :
#         answer=0
#     return answer
    
def check_map(map):
    answer=1
    check=[0,0,0,0]
    count_row=-1
    count_cell=-1
    for row in map:
        count_row+=1
        for cell in row:
            count_cell+=1
            try:
                if cell[0]==1:
                    check[0]+=1
                elif cell[0]==2:
                    check[1]+=1
                elif cell[0]==3:
                    check[2]+=1
                elif cell[0]==4:
                    check[3]+=1
                num0=cell[0]
                print(cell,7777)
                
                if count_cell<9 and type( map[count_row][count_cell+1])== int and map[count_row][count_cell+1]!=num0 and map[count_row][count_cell+1]!=5:
                    answer=0
            
                if count_cell>0 and type( map[count_row][count_cell-1])== int and map[count_row][count_cell-1]!=num0 and map[count_row][count_cell-1]!=5:
                    answer=0
                if count_row<9 and type( map[count_row+1][count_cell])== int and map[count_row+1][count_cell]!=num0 and  map[count_row+1][count_cell]!=5:
                    answer=0
                if count_row>0 and type( map[count_row-1][count_cell])== int and map[count_row-1][count_cell]!=num0 and map[count_row-1][count_cell]!=5:
                    answer=0
                    
                    
                if count_row<9 and count_cell<9 and type( map[count_row+1][count_cell+1])== int and map[count_row+1][count_cell+1]!=num0 and map[count_row+1][count_cell+1]!=5:
                    answer=0
                if count_cell>0  and count_row>0 and type( map[count_row-1][count_cell-1])== int and map[count_row-1][count_cell-1]!=num0 and map[count_row-1][count_cell-1]!=5:
                    answer=0
                if count_cell>0 and count_row<9 and type( map[count_row+1][count_cell-1])== int and map[count_row+1][count_cell-1]!=num0 and map[count_row+1][count_cell-1]!=5:
                    answer=0
                if count_row>0 and count_cell<9 and type( map[count_row-1][count_cell+1])== int and map[count_row-1][count_cell+1]!=num0 and map[count_row-1][count_cell+1]!=5:
                    answer=0



                if count_cell<9 and type( map[count_row][count_cell+1])!= int and map[count_row][count_cell+1][0]!=num0 and map[count_row][count_cell+1][0]!=5:
                    answer=0
            
                if count_cell>0 and type( map[count_row][count_cell-1])!= int and map[count_row][count_cell-1][0]!=num0 and map[count_row][count_cell-1][0]!=5:
                    answer=0
                if count_row<9 and type( map[count_row+1][count_cell])!= int and map[count_row+1][count_cell][0]!=num0 and  map[count_row+1][count_cell][0]!=5:
                    answer=0
                if count_row>0 and type( map[count_row-1][count_cell])!= int and map[count_row-1][count_cell][0]!=num0 and map[count_row-1][count_cell][0]!=5:
                    answer=0
                    
                    
                if count_row<9 and count_cell<9 and type( map[count_row+1][count_cell+1])!= int and map[count_row+1][count_cell+1][0]!=num0 and map[count_row+1][count_cell+1][0]!=5:
                    answer=0
                if count_cell>0 and count_row>0 and type( map[count_row-1][count_cell-1])!= int  and map[count_row-1][count_cell-1][0]!=num0 and map[count_row-1][count_cell-1][0]!=5:
                    answer=0
                if count_cell>0 and count_row<9 and type( map[count_row+1][count_cell-1])!= int  and map[count_row+1][count_cell-1][0]!=num0 and map[count_row+1][count_cell-1][0]!=5:
                    answer=0
                if count_row>0 and  count_cell<9 and type( map[count_row-1][count_cell+1])!= int and map[count_row-1][count_cell+1][0]!=num0 and map[count_row-1][count_cell+1][0]!=5:
                    answer=0
                if num0!=1:
                    list_cells= []
                    if count_row<9 :
                        list_cells.append(map[count_row+1][count_cell])
                    if count_row>0:
                        list_cells.append(map[count_row-1][count_cell])
                    if count_cell<9:
                        list_cells.append(map[count_row][count_cell+1])
                    if count_cell>0:
                        list_cells.append(map[count_row][count_cell-1])
                    count2=0
                    for cell1 in list_cells:
                        if cell1==num0:
                            count2+=1
                        if type(cell1)!=int and cell1[0]==num0:
                            count2+=1
                    if count2==0:
                        answer=0
            except TypeError:

                num0=cell

                # print(num0)
                if 0!=num0!=5  and  type(num0)==int:
                    # print(count_row,count_cell)                
                    if count_cell<9 and type( map[count_row][count_cell+1])== int and map[count_row][count_cell+1]!=num0 and map[count_row][count_cell+1]!=5:
                        answer=0
            
                    if count_cell>0 and type( map[count_row][count_cell-1])== int and map[count_row][count_cell-1]!=num0 and map[count_row][count_cell-1]!=5:
                        answer=0
                    if count_row<9 and type( map[count_row+1][count_cell])== int and map[count_row+1][count_cell]!=num0 and  map[count_row+1][count_cell]!=5:
                        answer=0
                    if count_row>0 and type( map[count_row-1][count_cell])== int and map[count_row-1][count_cell]!=num0 and map[count_row-1][count_cell]!=5:
                        answer=0
                        
                        
                    if count_row<9 and count_cell<9  and type( map[count_row+1][count_cell+1])== int and map[count_row+1][count_cell+1]!=num0 and map[count_row+1][count_cell+1]!=5:
                        answer=0
                    if count_cell>0  and count_row>0 and type( map[count_row-1][count_cell-1])== int and map[count_row-1][count_cell-1]!=num0 and map[count_row-1][count_cell-1]!=5:
                        answer=0
                    if count_cell>0 and count_row<9 and type( map[count_row+1][count_cell-1])== int and map[count_row+1][count_cell-1]!=num0 and map[count_row+1][count_cell-1]!=5:
                        answer=0
                    if count_row>0 and count_cell<9 and type( map[count_row-1][count_cell+1])== int and map[count_row-1][count_cell+1]!=num0 and map[count_row-1][count_cell+1]!=5:
                        answer=0
                    if count_cell<9  and type( map[count_row][count_cell+1])!= int and 0!=map[count_row][count_cell+1][0]!=num0 and map[count_row][count_cell+1][0]!=5:
                        answer=0
                    
                    if count_cell>0 and type( map[count_row][count_cell-1])!= int and map[count_row][count_cell-1][0]!=num0 and map[count_row][count_cell-1][0]!=5:
                        answer=0
                    if count_row<9 and type( map[count_row+1][count_cell])!= int and map[count_row+1][count_cell][0]!=num0 and  map[count_row+1][count_cell][0]!=5:
                        answer=0
                    if count_row>0 and type( map[count_row-1][count_cell])!= int and map[count_row-1][count_cell][0]!=num0 and map[count_row-1][count_cell][0]!=5:
                        answer=0
                        
                        
                    if count_row<9 and count_cell<9 and type( map[count_row+1][count_cell+1])!= int  and map[count_row+1][count_cell+1][0]!=num0 and map[count_row+1][count_cell+1][0]!=5:
                        answer=0
                    if count_cell>0 and count_row>0 and type( map[count_row-1][count_cell-1])!= int   and map[count_row-1][count_cell-1][0]!=num0 and map[count_row-1][count_cell-1][0]!=5:
                        answer=0
                    if count_cell>0 and count_row<9 and type( map[count_row+1][count_cell-1])!= int  and map[count_row+1][count_cell-1][0]!=num0 and map[count_row+1][count_cell-1][0]!=5:
                        answer=0
                    if count_row>0 and count_cell<9 and type( map[count_row-1][count_cell+1])!= int  and map[count_row-1][count_cell+1][0]!=num0 and map[count_row-1][count_cell+1][0]!=5:
                        answer=0
                    list_cells= []
                    if count_row<9 :
                        list_cells.append(map[count_row+1][count_cell])
                    if count_row>0:
                        list_cells.append(map[count_row-1][count_cell])
                    if count_cell<9:
                        list_cells.append(map[count_row][count_cell+1])
                    if count_cell>0:
                        list_cells.append(map[count_row][count_cell-1])
                    count2=0
                    for cell1 in list_cells:
                        if cell1==num0:
                            count2+=1
                        if type(cell1)!=int and cell1[0]==num0:
                            count2+=1
                    if count2==0:
                        answer=0
        count_cell=-1     
    if check==[4,3,2,1] and answer:
        answer=0
    else:
        answer=1
    return answer
def help_check(map,row,cell,attack_map,quetion,quetion2=True):
    if quetion and quetion2 and  attack_map[row][cell]==0 and (map[row][cell]==0 or map[row][cell]==5):
        attack_map[row][cell]=None
    return attack_map
def check(map, coor, attack_map):
    for row in range(10):
        for cell in range(10):
            check1= 1
            cell1= map[row][cell]
            cell2= coor[row][cell]
            
            if type (cell1)!= type(0):
                if True:
                    cell10= 0
                    cell11= 0
                    # if cell1[3]:
                    #     cell10= 1
                    #     cell11= 0
                    # if cell1[0]==1:
                        # cell10= 0
                        # cell11=0
                    
                    if True:
                        # print(attack_map)
                        for count in range(cell1[0]):
                            try:

                                if attack_map[row+ (count* cell10)][cell+ (count*cell11)]==0 :
                                    # print(777)
                                    check1= 0
                                
                            except IndexError:
                                pass
                            if  cell1[3]:
                                cell10=1
                            else:
                                cell11=1
                    # print(check1)
                    cell10= 0
                    cell11= 0
                    if check1:
                        for count in m_data.ships:
                            if count.X-20 < cell2[0]<count.X+40 and count.Y-20 < cell2[1]<count.Y+40:
                                # print(count.IMG2)
                                count.ATTACK= 1

                        for count in range(cell1[0]):
                            try:
                                attack_map= help_check(map,row+cell10*count,cell+1+cell11*count,attack_map,cell<9,)
                                attack_map= help_check(map,row+1+cell10*count,cell+cell11*count,attack_map,row<9,)
                                attack_map= help_check(map,row+cell10*count,cell-1+cell11*count,attack_map,cell>0,)
                                attack_map= help_check(map,row-1+cell10*count,cell+cell11*count,attack_map,row>0,)
                                
                                attack_map= help_check(map,row-1+cell10*count,cell+1+cell11*count,attack_map,cell<9 , row>0,)
                                attack_map= help_check(map,row+1+cell10*count,cell+1+cell11*count,attack_map,cell<9 , row<9,)
                                attack_map= help_check(map,row-1+cell10*count,cell-1+cell11*count,attack_map,cell>0,row>0)
                                attack_map= help_check(map,row+1+cell10*count,cell-1+cell11*count,attack_map,cell>0,row<9)
                            except IndexError:
                                pass
                            if cell1[3]:
                                cell10=1
                            else:
                                cell11=1
                            
                # elif check1:
                #     for count in m_data.ships:
                #             if count.X-20 < cell2[0]<count.X+40 and count.Y-20 < cell2[1]<count.Y+40:
                #                 count.ATTACK= 1
    return attack_map
def block_map(map,num=5):
    num2=0
    if num==0:
        num2=5
    for count in range(10):
        for count1 in range (10):
            if 0!=map[count][count1] and map[count][count1]!=5:
                if count1<9 and map[count][count1+1]==num2:
                    map[count][count1+1]=num
                # map=help_block_map(way,map,num,num2,count,count1,count1<9,0,1)
                # map=help_block_map(way,map,num,num2,count,count1,count1>0,0,-1)
                # map=help_block_map(way,map,num,num2,count,count1,count<9,1,0)
                
                if count1>0 and map[count][count1-1]==num2:
                    map[count][count1-1]=num
                if count<9 and map[count+1][count1]==num2:
                    map[count+1][count1]=num
                if count>0 and map[count-1][count1]==num2:
                    map[count-1][count1]=num
                    
                    
                if count<9 and count1<9 and map[count+1][count1+1]==num2:
                    map[count+1][count1+1]=num
                if count1>0  and count>0 and map[count-1][count1-1]==num2:
                    map[count-1][count1-1]=num
                if count1>0 and count<9 and map[count+1][count1-1]==num2:
                    map[count+1][count1-1]=num
                if count>0 and count1 <9 and map[count-1][count1+1]==num2:
                    map[count-1][count1+1]=num
    return map
def unblock_map(map):
    for row in range(10):
        for cell in range(10):
            # print(map)
            if map[row][cell]==5:
                map[row][cell]=0
    return map
list_coor=[]
list_coor2= []
list_coor_enemy= []
x,y=-40,-40
for count in range(len(player_map)):
    y+=45.5
    list_coor_enemy+= [[]]
    list_coor2.append([])
    for count1 in range(10):
        x+=45.5
        list_coor.append((x,y,count,count1))
        list_coor_enemy[count].append((x+ 543,y,count,count1))
        list_coor2[count].append([x,y,count,count1])
    
    x=-40
# bot_map= m_bot.bot_place(bot_map)
# print_map(bot_map)
def create_map(screen,cor= (2,2), width_height= (500,500)):
    x= cor[0]
    y= cor[1]
    for count in range(11):
        pygame.draw.line(screen,(155,223,236), (cor[0],y),(width_height[0]-44+cor[0], y), 5)
        y += width_height[1]/11
    for count in range(11):
        pygame.draw.line(screen,(155,223,236), (x,cor[1]),(x, width_height[1]-44+cor[1]), 5)
        x += width_height[0]/11

def ships(map,list_coor1= list_coor_enemy, take= False):   
        counts= [0,4,7]
        x,y=503,-40
        for count in range(10):
            y+=45.5
            for count1 in range(10):
                x+=45.5
                try:
                    # print("not")
                    # ship=None
                    # print(count,count1)
                    save= list_coor1[count][count1]
                    save1= map[count][count1]
                    
                    
                    if take:
                        for count2 in range(4):
                            if save1[0]== 1:
                                ch= m_data.ships[counts[0]]
                                ch.X= save[0]
                                ch.Y= save[1]
                                ch.HEIGHT=40
                                ch.WIDTH= 40
                                ch.ROTATE= save1[1]
                                ch.load_image('1')

                        for count2 in range(3):
                            if save1[0]== 2:
                                
                                ch= m_data.ships[counts[1]]
                                ch.X, ch.Y= save[0]+ save1[2][0], save[1]+ save1[2][1]
                                ch.HEIGHT, ch.WIDTH= 40,87
                                ch.ROTATE= save1[1]
                                ch.load_image('2')
                        for count2 in range(2):
                            if save1[0]== 3:
                                ch= m_data.ships[counts[2]]
                                ch.X, ch.Y= save[0]+ save1[2][0], save[1]+save1[2][1]
                                ch.HEIGHT, ch.WIDTH= 40, 130
                                ch.ROTATE= save1[1]
                                ch.load_image('3')
                        if save1[0]== 4:
                            ch= m_data.ships[9]
                            ch.X, ch.Y= save[0]+save1[2][0],save[1]+ save1[2][1]
                            ch.HEIGHT, ch.WIDTH= 40, 175
                            ch.ROTATE= save1[1]
                            ch.load_image('4')
                        ch.LAST_CELL=[count,count1]
                    if map[count][count1][0] == 1:
                        ship=m_clas.Item(coordinate=save,width_height=(40,40),rotate= map[count][count1][1], name="1")
                        counts[0]+= 1
                    elif map[count][count1][0]==4:
                        ship=m_clas.Item(coordinate=(save[0]+ save1[2][0], save[1]+ save1[2][1]),width_height= (175,40),rotate= map[count][count1][1],name="4")
                    elif map[count][count1][0]== 3:
                            ship=m_clas.Item(coordinate=(save[0]+ save1[2][0], save[1]+ save1[2][1]), width_height=(130,40), rotate= map[count][count1][1],name="3")
                            counts[2]+= 1
                    elif  map[count][count1][0]== 2:
                            ship=m_clas.Item(coordinate=(save[0]+ save1[2][0], save[1]+ save1[2][1]),width_height= (87,40),rotate= map[count][count1][1],name="2")
                            counts[1]+= 1 
                    # ship.load_image(name=ship.CELL)
                    # if ship!= None:
                    if not take:
                        m_data.ships.append(ship)
                    # m_data.ships[m_data.ships.index(ship)].load_image(ship.CELL)
                    # print("not")
                except TypeError:
                    pass
            x=503