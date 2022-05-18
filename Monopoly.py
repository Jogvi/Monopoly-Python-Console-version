import random as r
import time as t
global_position=0
number_of_players=0
positions=[5,5,5,5]
valid_number_of_players = False
players=[]
board = ['go','Mediterranean ave.','Community','Baltic ave.','Income Tax','Reading Railroad','Oriental ave.','Chance','Vermont ave.','Conneticut ave.','In Prison-Just Visiting','St. Charles place','Electric company','States ave.', 'Virginia ave.','Pennsylvania Railroad','St James place','Community','Tenessee ave.','New York ave.','Free Parking', 'Kentucky ave.','Chance','Indiana ave.','Illinois ave.','Ventnor ave.','Water Works','Marvin Gardens','Jail','Pacific ave.','North Carolina Ave.','Community','Pennsylvania','Short Line','Chance','Park place','Luxury Tax','Broadwalk']
buyable = [False,True,False,True,False,True,True,False,True,True,False,True,True,True,True,True,True,False,True,True,False,True,False,True,True,True,True,True,True,True,False,True,True,False,True,True,False,True,False,True]
value = [0,60,0,60,0,200,100,0,100,120,0,140,150,140,160,200,180,0,180,200,0,220,0,220,240,200,260,260,150,280,0,300,300,0,320,200,0,350,0,400]
money=[]

while not valid_number_of_players:
    try:
        number_of_players= int(input('how many players are playing?'))
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
def buy_process(position,player):
    print(f'You can buy {board[position]} for {value[position]}.')
    print('You have {money[player]} and will have {money[player] - value[position]} $ left after the transaction')
    action = input('would you like to buy {board[position]}?')
    if action is in yes_inputs:
        buy()
    elif action is in no_inputs:
    else:
        print('you appear to have misspelt your action. Please use {yes_inputs} or {no_inputs}')
def player_turn(position,player):
    roll1=r.randint(1,6)
    print(roll1)
    t.sleep(1)
    roll2=r.randint(1,6)
    print(roll2)
    position+=roll1+roll2
    print(f'you have landed on {position}, which is {board[position]}!') 
    t.sleep(2)
    if buyable[position] && money[player]>=values[position]:
       buy_process
       elif buyable[position] 
    if roll1 == roll2:
        print('you have rolled a double! you get a re-roll!')
        player_turn(position)
    else:
        print("turn ended")
def turn():
    while number_of_players>1:
          for i in range (0,number_of_players):
            print(f"This is {players[i]}'s turn")
            player_turn(positions[i], i)
turn()
