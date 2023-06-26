import random
import modules.map as m_map
import modules.data_base as m_data
import modules.clas as m_clas

# import pygame
# import modules.c
a= lambda  target: 1 if target > 1 else 0

def bot_place(map):
    test = 1
    while test < 5:
        print(1)
        target = [random.randint(0,9),random.randint(0,9)]
        if map[target[0]][target[1]]== 0:
            map[target[0]][target[1]] = [1,random.randint(0,3)*90,target,False]
            map=m_map.block_map(map)
            test += 1
    while test < 8:
        print(2,test)
        target = [random.randint(0,9),random.randint(0,9)]
        if map[target[0]][target[1]]== 0:
            map[target[0]][target[1]] = 2
            save= []
            save+= target
            target1 = random.randint(0,3)   
            # print([0,0,target])         
            c=0       
            check1=0
            if target1 == 0 and target[1]>0 and map[target[0]][target[1]-1]==0:
                # map[target[0]][target[1]-1] = [2,0,[0,0,target[0],target[1]-1], 0]
                rotate=0
                target[1]-=1
            elif target1 == 1 and target[1]<9 and map[target[0]][target[1]+1]==0:
                # map[target[0]][target[1]+1] = [2,180,[-48,0]+target, 0]#True
                rotate=180;check1=1
                target[1]+=1
            elif target1 == 2 and target[0]<9  and map[target[0]+1][target[1]]==0:
                # map[target[0]+1][target[1]] = [2,-90,[0,-48,]+target, 1]#True
                rotate=-90; check1=1
                target[0]+=1; c=1
            elif target1 == 3 and target[0]> 0 and map[target[0]-1][target[1]]==0:
                # map[target[0]-1][target[1]] = [2,90,[0,0,target[0]-1,target[1]], 1]#True
                rotate=90;c=1
                target[0]-=1
            else: 
                map[target[0]][target[1]]=0
                continue
            map[target[0]][target[1]]=2
            if check1:
                target=save
            map[target[0]][target[1]]= [2,rotate,[0,0]+target,c]
            test += 1
        map=m_map.block_map(map)
    while test < 10:
        print(3)
        for count in range(1):
            target = [random.randint(0,9),random.randint(0,9)]
            # print(map[target[0]][target[1]], target,test)
            # m_map.bot_map=m_map.print_map(m_map.bot_map)
            if  map[target[0]][target[1]]== 0:
                map[target[0]][target[1]] = 3
                # print(map[target[0]][target[1]])
                test += 1
                target1 = random.randint(0,3)
                save =[]
                save += target
                check= True
                c=0 
                if target1 == 0 and target[1]>0 and map[target[0]][target[1]-1]== 0:
                    target[1]=1-target[1]; check=False
                elif target1 == 1 and target[1]<9 and map[target[0]][target[1]+1]== 0:
                  
                    target[1]=1+target[1]
                elif target1 == 2 and target[0]<9  and map[target[0]+1][target[1]]== 0:
                    target[0]=1+target[0]; c=1
                elif target1 == 3 and target[0]> 0 and map[target[0]-1][target[1]]== 0:
                    target[0]=1-target[0]; check= False; c= 1
                else: 
                    test-=1
                    map[target[0]][target[1]] = 0
                    continue
                map[target[0]][target[1]]= 3




                if target1 == 0 and target[1]>0 and map[target[0]][target[1]-1]== 0:
                    target[1]-=1; rotate= 0; cor=[0,0]
                elif target1 == 1 and target[1]<9 and map[target[0]][target[1]+1]== 0:
                    print(target,map[target[0]][target[1]+1])
                    target[1]=1+target[1]; rotate= 180; cor=[-1,0]
                    print(target,map[target[0]][target[1]])
                elif target1 == 2 and target[0]<9  and map[target[0]+1][target[1]]== 0:
                    target[0]+=1; rotate= -90; cor=[0,-1]#True
                elif target1 == 3 and target[0]> 0 and map[target[0]-1][target[1]]==0: 
                    target[0]-=1; rotate= 90; cor =[0,0]
                else: 
                    test-=1
                    map[target[0]][target[1]] = 0
                    map[save[0]][save[1]] = 0
                    continue
                map[target[0]][target[1]]= 3
                if check:
                    target= save
                
                a= lambda: 1 if target1 > 1 else 0
                map[target[0]][target[1]]= (3,rotate,cor+ target,  c)
            map=m_map.block_map(map)
    print(3)

    
    while test < 11:
        print(4)
        target = [random.randint(0,9),random.randint(0,9)]
        if map[target[0]][target[1]]== 0:
            # print(4)
            map[target[0]][target[1]] = 4
            test += 1
            target1 = random.randint(0,3)
            save =[]
            save += target
            if target1 == 0 and target[1]>0 and map[target[0]][target[1]-1]== 0:
                target[1]-=1
            elif target1 == 1 and target[1]<9 and map[target[0]][target[1]+1]== 0:
                target[1]+=1
            elif target1 == 2 and target[0]<9  and map[target[0]+1][target[1]== 0]:
                target[0]+=1
            elif target1 == 3 and target[0]> 0 and map[target[0]-1][target[1]]== 0:
                target[0]-=1
            else: 
                test-=1
                map[target[0]][target[1]] = 0
                continue
            map[target[0]][target[1]]= 4
            save1= []+target
            print(target)


            if target1 == 0 and target[1]>0 and map[target[0]][target[1]-1]== 0:
                target[1]-=1
            elif target1 == 1 and target[1]<9 and map[target[0]][target[1]+1]== 0:
                target[1]+=1
            elif target1 == 2 and target[0]<9  and map[target[0]+1][target[1]]== 0:
                target[0]+=1
            elif target1 == 3 and target[0]> 0 and map[target[0]-1][target[1]]== 0:
                target[0]-=1
            else: 
                test-=1
                map[target[0]][target[1]] = 0
                map[save[0]][save[1]] = 0
                continue
            map[target[0]][target[1]]= 4
            save2 =[]
            save2 += target
            check= 1
            c=0
            if target1 == 0 and target[1]>0 and  map[target[0]][target[1]-1]== 0:
                target[1]-=1; rotate= 0; cor =[0,0]; check = 0; c=0
            elif target1 == 1 and target[1]<9 and  map[target[0]][target[1]+1]== 0:
                target[1]+=1; rotate= 180; cor =[0,0];c= 0
            elif target1 == 2 and target[0]<9  and  map[target[0]+1][target[1]]== 0:
                target[0]+=1; rotate=-90; cor =[0,0];c = 1
            elif target1 == 3 and target[0]> 0 and  map[target[0]-1][target[1]]== 0:
                target[0]-=1; rotate= 90; cor=[0,0]; check =0; c= 1
            else: 
                test-=1
                map[target[0]][target[1]] = 0
                map[save[0]][save[1]] = 0
                map[save1[0]][save1[1]] = 0
                map[save2[0]][save2[1]] = 0
                continue
            map[target[0]][target[1]]= 4
            if check:
                target= save
            map[target[0]][target[1]]= (4, rotate,(cor+ save),c)
            print((target1))
            map=m_map.block_map(map)
    print(4)
    map=m_map.block_map(map)
    if m_map.check_map(map):
        map=[]
        for count in range(10):
            map.append([0,0,0,0,0,0,0,0,0,0])
        map=bot_place(map)
    return map
def help_attack_bot(map):
    
    
    if m_data.attack== 1 and m_data.last_attack1[1]<9 and m_map.attacks_player_map[m_data.last_attack1[0]][m_data.last_attack1[1]+1]!= None:
        m_data.last_attack1[1]+=1
    elif m_data.attack==0 and m_data.last_attack1[1]>0 and m_map.attacks_player_map[m_data.last_attack1[0]][m_data.last_attack1[1]-1]!=None:
        m_data.last_attack1[1]-=1
    elif m_data.attack==3 and m_data.last_attack1[0]<9 and m_map.attacks_player_map[m_data.last_attack1[0]+1][m_data.last_attack1[1]]!=None:
        m_data.last_attack1[0]+=1

    elif m_data.attack==2 and m_data.last_attack1[0]>0 and m_map.attacks_player_map[m_data.last_attack1[0]-1][m_data.last_attack1[1]]!=None:
        m_data.last_attack1[0]-=1
    else:
        print(1)
        m_data.attack=0
        m_data.attacks=False
        m_data.attacko1=0
        m_data.attacko=0
        m_data.check1=0
    if map[m_data.last_attack1[0]][m_data.last_attack1[1]]==0 or map[m_data.last_attack1[0]][m_data.last_attack1[1]]==5:
            print(2)
            m_data.step=1
            m_data.step_text="хід гравця"
            m_data.color_step=[155,223,255]
            m_data.attack=0
            m_data.attacks=False
            m_data.attacko1=0
            m_data.attacko=0
            m_data.check1=0
    elif m_map.attacks_player_map[m_data.last_attack1[0]][m_data.last_attack1[1]]!= None:
        m_clas.play_music()
    m_map.attacks_player_map[m_data.last_attack1[0]][m_data.last_attack1[1]]=None
    return map
def help_bot_attack(map):
    if m_data.check1:
        map=help_attack_bot(map)
    else:
        if m_data.attack==0 and m_data.last_attack[1]< 9 and m_map.attacks_player_map[m_data.last_attack[0]][m_data.last_attack[1]+1]!= None:
            m_data.last_attack[1]+=1
        elif m_data.attack==1  and m_data.last_attack[1]>0 and m_map.attacks_player_map[m_data.last_attack[0]][m_data.last_attack[1]-1]!= None:
            m_data.last_attack[1]-= 1
        
        elif m_data.attack==2 and m_data.last_attack[0]<9 and m_map.attacks_player_map[m_data.last_attack[0]+1][m_data.last_attack[1]]!=None:
            m_data.last_attack[0]+=1
            
        elif m_data.attack==3 and m_data.last_attack[0]>0 and m_map.attacks_player_map[m_data.last_attack[0]-1][m_data.last_attack[1]]!= None:
            m_data.last_attack[0]-=1                                                                                                      
        else:
            print(11)
            m_data.check1=1
        # m_data.attack=0
        # m_data.attacks=False
        # m_data.attacko1=0
        # m_data.attacko=0
        if map[m_data.last_attack[0]][m_data.last_attack[1]]==0 or map[m_data.last_attack[0]][m_data.last_attack[1]]==5:
            print(22)
            m_data.step=1
            m_data.step_text="хід гравця"
            m_data.color_step=[155,223,255]
            m_data.check1=1
            # m_data.attack=0
            # m_data.attacks=False
            # m_data.attacko1=0
            # m_data.attacko=0
        elif m_map.attacks_player_map[m_data.last_attack[0]][m_data.last_attack[1]]!= None:
            m_clas.play_music()
        m_map.attacks_player_map[m_data.last_attack[0]][m_data.last_attack[1]]=None
    return map
def bot_help_attack(map):
    if m_data.attacko1:
        map=help_bot_attack(map)
    else:
        # 
        check=True
        last_attack=[]
        last_attack+=m_data.last_attack
        
        if m_data.attack==0 and last_attack[1]<9 and m_map.attacks_player_map[last_attack[0]][last_attack[1]+1]!=None:
            last_attack[1]+= 1
            
        elif m_data.attack==1 and last_attack[1]>0 and m_map.attacks_player_map[last_attack[0]][last_attack[1]-1]!=None:
            last_attack[1]-=1
        elif m_data.attack==2 and last_attack[0]<9 and m_map.attacks_player_map[last_attack[0]+1][last_attack[1]]!=None:
            last_attack[0]+=1
        elif m_data.attack==3 and  last_attack[0]>0 and m_map.attacks_player_map[last_attack[0]-1][last_attack[1]]!=None:
            last_attack[0]-=1
        else:
            # print(m_data.attack, last_attack[1], m_map.attacks_player_map[last_attack[0]][last_attack[1]])
            m_data.attack+=1
            check=False
            
            if m_data.attacko1 or m_data.attack>3 :
                print(111)
                m_data.check=1
                m_data.attack=0
                m_data.attacks=False
                m_data.attacko1=0
                m_data.attacko=0 
            
            if m_data.check:
                    m_data.attack-=1
                    m_data.check=0
            
            # map=bot_help_attack(map)пока
        # if m_data.attacko1:
            # m_data.last_attack=last_attack
        if check:
            attack= m_map.player_map[last_attack[0]][last_attack[1]]
            # m_clas.play_music()
            # if m_map.attacks_player_map[last_attack[0]][last_attack[1]]!= None:
                
            m_map.attacks_player_map[last_attack[0]][last_attack[1]]=None
            if attack==0 or attack==5:
                m_data.step =1
                m_data.step_text="хід гравця"
                m_data.color_step=[155,223,255]
                m_data.attack+=1
                if m_data.attacko1:
                    print(222)
                    m_data.attack=0
                    m_data.attacks=False
                    m_data.attacko1=0
                    m_data.attacko=0
                    m_data.check=1
                if m_data.check:
                    m_data.attack-=1
                    m_data.check-=1
            elif   m_map.player_map[last_attack[0]][last_attack[1]]!=2 or type(m_map.player_map[last_attack[0]][last_attack[1]])!= int and m_map.player_map[last_attack[0]][last_attack[1]][0]!= 2:
                m_data.last_attack=[]
                m_data.last_attack+=last_attack
                # m_data.attack-=1
                m_clas.play_music()
                m_data.attacko1=1
            else:
                m_data.attack=0
                # m_clas.play_music()
                m_data.attacks=False
                m_data.attacko1=0
                m_data.attacko=0
    return map
def hard_bot( row, cell):
    map= m_map.attacks_player_map
    past= 0
    # print(cell>0,map[])
    if cell> 0 and map[row][cell-1]==0:
        past+= 1
       
        print(map)
    if cell< 9 and map[row][cell+1]==0:
       past+= 1
    for count in range(3):
        try:
            if map[row+1][cell-1 + count]== 0 and cell+ count >0:
                past+= 1 
        except IndexError:
            pass
        try:
            if map[row-1][cell-1 +count]==0 and row>0 and cell+count>0:
                past+=1
        except IndexError:
            pass
    return past
def bot_attack(map):
    
    
    while True:
        if not  m_data.attacks:
            attack=m_data.last_attack
            if m_data.difficulty== "hard":
                cells= []
                count_row= -1
                past= 0
                count_cell= -1
                for row in m_map.attacks_player_map:
                    count_row+= 1
                    for cell in row:
                        count_cell+= 1
                        if cell== 0:
                            cells.append([count_row, count_cell, hard_bot(count_row, count_cell)])
                    count_cell= -1
                print(cells)
                for cello in cells:
                    if cello[2]> past:
                        past= cello[2]
                print(past)
                count=-1
                for count1 in range(len( cells)):
                    count+=1
                    cells[count]
                    if cells[count][-1]< past:
                        print(cells[count])
                        del cells[count]
                        count-=1
                    
                
                attack1= random.randint(0,len(cells)-1)
                attack= cells[attack1]
                print(cells)
                del attack[2]
            elif m_data.attacko==False:

                attack = [random.randint(0,9),random.randint(0,9)]
            
            if  m_map.attacks_player_map[attack[0]][attack[1]]!=None:
                m_data.last_attack1= attack
                m_data.last_attack=attack
                    
                if map[attack[0]][attack[1]] == 0 or map[attack[0]][attack[1]] == 5:
                    m_data.step =1
                    m_data.step_text="хід гравця"
                    m_data.color_step=[155,223,255]
                    m_data.attack= 0
                    # pygame.mixer.music.load(m_find) пока
                
                else:
                    m_clas.play_music()
                    if m_data.difficulty!='easy':
                    # print(-9)
                        try:

                            if m_map.player_map[attack[0]][attack[1]][0] !=1:
                                m_data.attacks= True
                                # m_clas.play_music()
                                
                                # map= bot_help_attack(map)
                            # print(-10)
                        except TypeError:
                            if 5!=m_map.player_map[attack[0]][attack[1]]!=1!=m_map.player_map[attack[0]][attack[1]]!=0:
                                m_data.attacks=True
                            # map=bot_help_attack(map)
                # if m_map.attacks_player_map[attack[0]][attack[1]]!= None:
                    
                m_map.attacks_player_map[attack[0]][attack[1]] = None  
                break
        else:
            map=bot_help_attack(map)
            break
    m_data.display=1
    return map