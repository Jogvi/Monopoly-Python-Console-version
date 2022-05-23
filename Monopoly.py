import random as r
import time as t
import pickle as p
global_position=0
number_of_players=0


valid_number_of_players = False

positions=[]
players=[]
yes_inputs= ["y",'yes','yesaroo','yep']
no_inputs=['n','no','nope']
board = ['go','Mediterranean ave.','Community Chest','Baltic ave.',\
         'Income Tax','Reading Railroad','Oriental ave.','Chance',\
         'Vermont ave.','Conneticut ave.','In Prison-Just Visiting',\
         'St. Charles place','Electric company','States ave.', 'Virginia ave.',\
         'Pennsylvania Railroad','St James place','Community Chest','Tenessee ave.',\
         'New York ave.','Free Parking', 'Kentucky ave.','Chance','Indiana ave.',\
         'Illinois ave.','Ventnor ave.','Water Works','Marvin Gardens','Jail',\
         'Pacific ave.','North Carolina Ave.','Community Chest','Pennsylvania',\
         'Short Line','Chance','Park place','Luxury Tax','Broadwalk']
property_type=[0,1,0,1,4,2,1,0,1,1,0,1,3,1,1,2,1,0,1,1,0,1,0,1,1,1,3,1,0,1,1,\
               0,1,2,0,1,5,1]
owned_utilities=['The Bank','The Bank']
positions=[]
buyable = [False,True,False,True,False,True,True,False,True,True,False,True,\
           True,True,True,True,True,False,True,True,False,True,False,True,True,\
           True,True,True,True,True,False,True,True,False,True,True,False,True,\
           False,True]
value = [0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,\
         220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,0,400]
money=[]
net_worth=[]
houses=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hotels=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,\
        0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
owned = [False,False,False,False,False,False,False,False,False,False,\
         False,False,False,False,False,False,False,False,False,False,False,\
         False,False,False,False,False,False,False,False,False,False,False,\
         False,False,False,False,False,False,False,False]
rentable = [False,False,False,False,"The Bank",False,False,False,False,False,\
            False,False,False,False,False,False,False,False,False,False,False,\
            False,False,False,False,False,False,False,False,False,False,False,\
            False,False,False,False,False,False,False,False]
railroads_owned=['Bank','Bank','Bank','Bank']


while not valid_number_of_players:
    try:
        number_of_players= int(input('Welcome! How many players are playing?'))
        valid_number_of_players = True
        if number_of_players>10:
            print(f'{number_of_players} is too much! Please choose at maxium 10')
            valid_number_of_players=False
    except ValueError:
        print('Sorry, that was not a valid number. Please type them in numbers and not letters')
for i in range (0,number_of_players):
    players.append(input(f'who is player {i+1}?'))
    positions.append(0)
    money.append(1500)
    positions.append(0)
    net_worth.append(1500)

def save(obj,file):
    p.dump( obj, open( file, "wb" ) )
def load(file):
    import_result=p.load(open(file,'rb'))
    return import_result
def header(text,caps_type,size):
    semi_size=int(size/2)
    size+=len(text)+2
    print('='*size)
    if caps_type == 1:
        print('-'*semi_size,text,'-'*semi_size)
        print('='*size)
    elif caps_type == 2:
        print('-'*semi_size,text.title(),'-'*semi_size)
        print('='*size)
    elif caps_type == 3:
        print('-'*semi_size,text.upper(),'-'*semi_size)
        print('='*size)
def advance(arrival):
    positions[player]+=arrival-positions[player]
def chance(player):
    drawn_card=r.randint(1,16)
    drawn_card=5
    print('drawing your card...')
    t.sleep(2)
    f = open("Chancecards.txt","r")
    print(f.readlines()[drawn_card])
    if drawn_card == 1:
       advance(39)
    elif drawn_card ==2:
        positions[player]=0
        money[player]+=200
    elif drawn_card==3:
        advance(24)
    elif drawn_card==4:
        advance(11)
    elif drawn_card==5:
        nearest_railroad(positions[player],player)


def nearest_railroad(position,player):
    if position<35:
        while property_type[position]!=2:
            position+=1
            positions[player]+=1
    else:
        positions[player]=5
        money[player]+=200
    if rentable[position]!= False and rentable[position] != players[player]:
        rent(position,player,2)
    else:
        if buyable[position] and money[player]>=value[position]:
           buy_process(position,player)
def community():
    drawn_card=r.randint(1,16)
    f = open("Communitycards.txt","r")
    print(f.readlines()[drawn_card])

def buy_process(position,player):
    landlord=rentable[position]
    print(f'You can buy {board[position]} for {value[position]}$.'\
          f'You have {money[player]} and will have {money[player] - value[position]} $ left after the transaction')
    action = input(f'would you like to buy {board[position]}?')
    if action in yes_inputs:
        money[player]-=value[position]
        owned[position]=players[player]
        rentable[position]=players[player]
        buyable[position]=False
        if property_type==2:
            if position==5:
                owned_railroads[0]=player
            elif position==15:
                owned_railroads[1]=player
            elif position==25:
                owned_railroads[2]=player
            elif position==35:
                owned_railroads[3]=player
        elif property_type[position]==3:
            if position==12:
                owned_utilities[0]=players[player]
            elif position==27:
                owned_utilities[1]=player
        net_worth[player]+=value[position]
    elif action in no_inputs:
        print('ok, nevermind...')
    else:
        print(f'you appear to have misspelt your action. Please use {yes_inputs} or {no_inputs}')
        t.sleep(2)
        buy_process(position,player)
def rent (position,player,multiplier):
    #houses
    landlord=rentable[position]
    rent=0
    if property_type[position] == 1:
        if houses[position] == 0 and hotels[position] == 0:
            rent=value[position]/10
        elif hotels[position]>0:
            rent= value[position]/10*5
        else:
            rent = (value[position]/10)*houses[position]*5
    #railroads
    elif property_type[position]==2:
        number_of_railroads=0
        for i in range(len(railroads_owned)):
         if i == landlord:
                number_of_railroads+=1
        if number_of_railroads == 1:
            rent = 25
        elif number_of_railroads ==2:
            rent=50
        elif number_of_railroads == 3:
            rent=100
        elif number_of_railroads ==4:
            rent=200
    elif property_type[position]==4:
        #tax
        if position==4:
            action=input('Would you like to pay 10% of your worth, or 200$(press 0 for 10%, and 1 for 200$')
            if action==0:
                money[player]-=net_worth[player]/10
                print(f"You've just paid {net_worth[player]/10}$ in tax")
                input('Press [Enter] to continue')
            elif action==1:
                money[player]-=200
                print('You paid 200$ in tax...')
                input('Press [Enter] to continue')
        elif position == 37:
            money[player]-=75
            print('You just paid 75$ in tax!')
    elif property_type[position] == 3:
        #utilities
        utilities_owned=0
        for i in range(0,len(owned_utilities)):
            if owned_utilities[i]==landlord:
                utilities_owned+=1
        if utilities_owned==1:
            roll1=r.randint(1,6)
            print(roll1)
            roll2=r.randint(1,6)
            print(roll2)
            input('Press [Enter] to continue')
            rent=(roll1+roll2)*4
        elif utilities_owned==2:
            roll1=r.randint(1,6)
            print(roll1)
            roll2=r.randint(1,6)
            print(roll2)
            input('Press [Enter] to continue')
            rent=(roll1+roll2)*10
    rent*=multiplier
    money[player]-=rent
    print(f'{players[player]}, you just paid {rent} to {landlord}!')
    
def player_turn(position,player):
    roll1=r.randint(1,6)
    print(roll1)
    t.sleep(1)
    roll2=r.randint(1,6)
    print(roll2)
    t.sleep(1)
    position+=roll1+roll2
    position=7
    if position>40:
        position-=40
        money[player]+=200
        input('You have passed GO!Press enter to collect your money!')
    positions[player]=position
    print(f'you have landed on {position}, which is {board[position]}!') 
    t.sleep(2)
    if rentable[position]!= False and rentable[position] != players[player]:
        rent(position,player,1)
    else:
        if buyable[position] and money[player]>=value[position]:
           buy_process(position,player)
        elif buyable[position] and money[player]<value[position]:
            print("Sorry, you do not have enough money. Careful or you'll have to mortgage your properties")
    if board[position] == "Chance":
        chance(player)
    if position == "Community Chest":
        community_chest()
    if roll1 == roll2:
        print('you have rolled a double! you get a re-roll!')
        player_turn(position,player)
    else:
        header("turn ended",3,80)
        t.sleep(3)
        
def turn():
    while number_of_players>1:
          for i in range (0,number_of_players):
            print(f"This is {players[i]}'s turn")
            t.sleep(1)
            player_turn(positions[i], i)
turn()
