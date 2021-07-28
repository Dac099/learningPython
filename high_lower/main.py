import art                                                                                                                                                                                                                                  
import data
import random
import os

#Score 
score = 0

#Array that contain the index used by random numbers
index = []

#lenght of array data 
data_len = len(data.data)

#Ciclo que se va a cumplir mientras el usaurio no falle
while True:
    op1 = random.randrange(data_len)
    op2 = random.randrange(data_len)
    
    if op1 == op2:
        op1 = random.randrange(data_len)
        

    usr_1 = data.data[op1]['name']
    usr_2 = data.data[op2]['name']

    print(art.logo)
    print('Choose betwen the user with more followers')

    print(art.vs)
    print('\nWho has more followers?')
    answer = input(f' a: {usr_1} or b: {usr_2}\n>')
    os.system('clear')

    if answer == 'a' and data.data[op1]['follower_count'] > data.data[op2]['follower_count']:
        score += 1
        continue
    elif answer == 'b' and data.data[op1]['follower_count'] < data.data[op2]['follower_count']:
        score += 1
        continue
    else:
        print(f'Game over    score: {score}')
        break