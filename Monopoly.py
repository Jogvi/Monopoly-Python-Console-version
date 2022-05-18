import random as r
import time as t

global_position=0
number_of_players=0


valid_number_of_players = False

positions=[]
players=[]
yes_inputs= ["y",'yes','yesaroo','yep']
no_inputs=['n','no','nope']
board = ['go','Mediterranean ave.','Community Chest','Baltic ave.','Income Tax','Reading Railroad','Oriental ave.','Chance','Vermont ave.','Conneticut ave.','In Prison-Just Visiting','St. Charles place','Electric company','States ave.', 'Virginia ave.','Pennsylvania Railroad','St James place','Community Chest','Tenessee ave.','New York ave.','Free Parking', 'Kentucky ave.','Chance','Indiana ave.','Illinois ave.','Ventnor ave.','Water Works','Marvin Gardens','Jail','Pacific ave.','North Carolina Ave.','Community Chest','Pennsylvania','Short Line','Chance','Park place','Luxury Tax','Broadwalk']
positions=[]
buyable = [False,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True]
value = [0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,0,400]
money=[]
houses=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
hotels=[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
owned = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]
rentable = [False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False,False]



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

def chance():
    drawn_card=r.randint(1,16)
    print('drawing your card...')
    t.sleep(2)
    f = open("Chancecards.txt","r")
    print(f.readlines()[drawn_card])
def community():
    drawn_card=r.randint(1,16)
    f = open("Communitycards.txt","r")
    print(f.readlines()[drawn_card])

def buy_process(position,player):
    print(f'You can buy {board[position]} for {value[position]}$.')
    print(f'You have {money[player]} and will have {money[player] - value[position]} $ left after the transaction')
    action = input(f'would you like to buy {board[position]}?')
    if action in yes_inputs:
        money[player]-=value[position]
        owned[position]=players[player]
        rentable[position]=players[player]
    elif action in no_inputs:
        print('ok, nevermind...')
    else:
        print(f'you appear to have misspelt your action. Please use {yes_inputs} or {no_inputs}')
        t.sleep(2)
        buy_process(position,player)
        
def rent (position,player):
    if houses[position] == 0 and hotels[position] == 0:
        rent=value[position]/10
    elif hotels[position]>0:
        rent= value[position]/10*5
    else:
        rent = (value[position]/10)*houses[position]*5
    money[player]-=rent
    print(f'{player}, you just paid {rent} to {rentable[position]}!')
    
    
def player_turn(position,player):
    roll1=r.randint(1,6)
    print(roll1)
    t.sleep(1)
    roll2=r.randint(1,6)
    print(roll2)
    t.sleep(1)
    position=7
    if position>40:
        position-=40
        money[player]+=200
    positions[player]=position
    print(f'you have landed on {position}, which is {board[position]}!') 
    t.sleep(2)
    if rentable[position]!= False:
        rent(position,player)
    else:
        if buyable[position] and money[player]>=value[position]:
           buy_process(position,player)
        elif buyable[position] and money[player]<value[position]:
            print("Sorry, you do not have enough money. Careful or you'll have to mortgage your properties")
    if board[position] == "Chance":
        chance()
    if position == "Community Chest":
        community_chest()
    if roll1 == roll2:
        print('you have rolled a double! you get a re-roll!')
        player_turn(position,player)
    else:
        header("turn ended",3,50)
        t.sleep(3)
        
def turn():
    while number_of_players>1:
          for i in range (0,number_of_players):
            print(f"This is {players[i]}'s turn")
            t.sleep(1)
            player_turn(positions[i], i)
turn()
