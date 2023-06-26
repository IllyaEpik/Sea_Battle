def data():
    global step, last_attack, coor_button, turn, step_text, color_button, rect, color_rect,start_game, text,text_coor,text_coor2, ships, color_step,attack,attacks,attacko,count_bot_step,attacko1,check,last_attack1,check1,win_lose,difficulty,select_difficulty,hard_color,easy_color,medium_color,display
    global list_bubble
    step = 1
    last_attack=None
    coor_button= [[800,640],[930,470]]
    turn=False
    step_text="хід гравця"
    color_button= [[255,255,50],[75,75,255],[255,255,50]]
    rect=[8,468,984,50]
    color_rect=[0,200,0]
    start_game= False
    text= "Start Game"
    text_coor= []
    text_coor= coor_button[0]+ text_coor
    text_coor2=[500,460]
    ships=[]
    color_step=[128,128,200]
    attack=0
    attacks=0
    count_bot_step=0
    attacko=0
    attacko1=0
    check=1
    last_attack1= 0
    check1=0
    win_lose=False
    difficulty= None
    select_difficulty= 1
    hard_color= [0,0,0]
    medium_color= [0,0,0]
    easy_color= [0,0,0]
    display= True
# data()
    list_bubble=[]