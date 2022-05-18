import random as r
import time as t
global_position=0
number_of_players=0
positions=[]
valid_number_of_players = False
players=[]
board = ['go','Mediterranean ave.','Community','Baltic ave.','Income Tax','Reading Railroad','Oriental ave.','Chance','Vermont ave.','Conneticut ave.','IPJV','St. Charles place','Electric company','States ave.', 'Virginia ave.','Pennsylvania Railroad','St James place','Community','Tenessee ave.','New York ave.','Free Parking', 'Kentucky ave.','Chance','Indiana ave.','Illinois ave.','Ventnor ave.','Water Works','Marvin Gardens','Jail','Pacific ave.','North Carolina Ave.','Community','Pennsylvania','Short Line','Chance','Park place','Luxury Tax','Broadwalk']
while not valid_number_of_players:
    try:
        number_of_players= int(input('how many players are playing?'))
        valid_number_of_players = True
    except :
        print('sorry, that was not a valid number. Please type them in numbers and not letters')
    for i in range (0,number_of_players):
        players.append(input(f'who is player {i+1}?'))
def player_turn(position):
    roll1=r.randint(1,6)
    print(roll1)
    t.sleep(1)
    roll2=r.randint(1,6)
    print(roll2)
    position+=roll1+roll2
    print(f'you have landed on {position}, which is {board[position]}!')
    t.sleep(3)
    if roll1 == roll2:
        print('you have rolled a double! you get a re-roll!')
        player_turn(position)
    else:
        print("turn ended")
        
player_turn(global_position)
