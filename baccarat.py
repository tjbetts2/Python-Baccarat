#!/usr/bin/env python3

#Baccarat Chemin de Fer
#Created by Trevor Betts

import random
import time
import sys


def Intro():
    player_names = [0,0,0,0]
    player_bet = [0,0,0,0]
    player_pocket = [0,0,0,0]
    print("Welcome to Chemin de Fer.", "\n")
    j = 0
    i = 0
    while i == 0:
        num_players = input("How many players are there? (2 to 4): ")
        if num_players == "2" or num_players == "3" or num_players == "4":
            i = 1
        else:
            print("Please enter a numerical integer value between 2 and 4.\n")
    num_players_int = int(num_players)
    i = 0
    del player_names[num_players_int:]
    del player_bet[num_players_int:]
    del player_pocket[num_players_int:]
    while i <= num_players_int:
        player_names[0] = input("Player 1, what is your name?: ")
        print("\n")
        i = 1
        if i == num_players_int:
            break
        player_names[1] = input("Player 2, what is your name?: ")
        print("\n")
        i = 2
        if i == num_players_int:
            break
        player_names[2] = input("Player 3, what is your name?: ")
        print("\n")
        i = 3
        if i == num_players_int:
            break
        player_names[3] = input("Player 4, what is your name?: ")
        print("\n")
        i = 4
        if i == num_players_int:
            break
    i = 0
    while i == 0:
        order = input("Would you like to sit in numerical or random order: ")
        if order.lower() == "numerical":
            print("Players will sit in this order:",player_names[0:])
            i = 1
        elif order.lower() == "random":
            random.shuffle(player_names)
            print("Players will sit in this order:",player_names[0:])
            i = 1
        else:
            print("Please enter 'numerical' or 'random'")
    i = 1
    Baccarat(i, player_names, num_players_int, player_bet, player_pocket, j)
def Baccarat(i, player_names, num_players_int, player_bet, player_pocket, j):
    l = 0    #START OF PICKING THE BANKER FOR THE ROUND
    k = 0
    while i == 1:
        if k == num_players_int:
            k = 0
        if l == 0:
            j = 0
        print(player_names[j],",")
        be_banker = input("Would you like to take the shoe and be the banker? (y/n): ")
        if be_banker.lower() == "y":
            print(player_names[j],"will be the banker for at least the first round.")
            print("Betting will take place in this order:",player_names[0:])
            banker = player_names[j]
            i = 0
        elif be_banker.lower() == "n":
            j = j + 1
            l = 1
            if j == num_players_int:
                j = 0
                print("since no one chose to be banker,",player_names[j],"has been automatically selected, because he/she is to the right of the dealer.")
                print("Betting will take place in this order:",player_names[0:])
                banker = player_names[j]
                i = 0
        else:
            print("Invalid choice, please type y or n.")
    if i == 2:
        print(player_names[j],",")
        shoe_pass = input("Would you like to pass the shoe to your right? (y/n) :")
        if shoe_pass.lower() == "n":
            print(player_names[j],"will continue to be the banker.")
            banker = player_names[j]
        elif show_pass.lower() =="y":
            while i == 2:
                if k == num_players_int:
                    k = 0
                if l == 0:
                    k = j + 1
                print(player_names[k],",")
                be_banker = input("Would you like to take the shoe and be the banker? (y/n): ")
                if be_banker.lower() == "y":
                    print(player_names[k],"will be the banker for the round.")
                    j = k
                    banker = player_names[j]
                    i = 0
                elif be_banker.lower() == "n":
                    k = k + 1
                    l = 1
                    if k == j:
                        j = j + 1
                        print("since no one chose to be banker,",player_names[j],"has been automatically chosen.")
                        banker = player_names[j]
                        i = 0
                else:
                    print("Invalid choice, please type y or n.")
                    l = 1
        else:
            print("Invalid choice, please type y or n.")
    if i == 3:
        print("Since the banker lost the last round, the shoe will move to the right")
        while i == 3:
            if k == num_players_int:
                k = 0
            if l == 0:
                k = j + 1
            if k == j:
                j = j + 1
                print("Since no one chose to be banker,",player_names[j],"has been automatically chosen.")
                banker = player_names[j]
                i = 0
            print(player_names[k],",")
            be_banker = input("Would you like to take the shoe and be the banker? (y/n): ")
            if be_banker.lower() == "y":
                print(player_names[k],"will be the banker for the round.")
                j = k
                banker = player_names[j]
                i = 0
            elif be_banker.lower() == "n":
                k = k + 1
                l = 1
            else:
                print("Invalid choice, please type y or n.")
                l = 1
    l = 0
    k = 0
    i = 0
    player_bet_sum = 0    #START OF ROUND OF BETTING
    while True:   
        try:
            print(player_names[j],",") 
            player_bet[j] = int(input("As the banker, how much would you like to bet?: "))
            player_pocket[j] = player_pocket[j] - player_bet[j]
            break
        except ValueError:
            print("Please enter an integer value.")
            continue
    print(" ")
    k = j + 1
    while k != j:
        while True:
            try:
                print(player_names[k],",")
                player_bet[k] = int(input("How much would you like to bet against the banker?: "))
                player_pocket[k] = player_pocket[k] - player_bet[k]
                break
            except ValueError:
                print("Please enter an integer value.")
                continue
        player_bet_sum = player_bet_sum + (player_bet[k])
        if player_bet_sum > int(player_bet[j]):
            player_bet_sum = player_bet_sum - int(player_bet[k])
            print("Combined players' wager cannot exceed the banker wager")
        elif player_bet_sum == int(player_bet[j]):
            print("Maximum combined players bets has been reached, no more betting will take place.")
            if int(player_bet[k]) == int(player_bet[j]):
                print(player_names[k],": Banco!")
                print(player_names[k],"has called banco and will be the only player for this round.")
                banco = 1
                break
            banco = 0
            break
        else:
            k = k + 1
            if k == num_players_int:
                k = 0
            banco = 0
    w = player_bet[j]
    player_bet[j] = 0
    k = player_bet.index(max(player_bet))
    print(player_names[k],"has the highest bet against the banker, so he/she will be the player for the round.")
    player_bet[j] = w
    #Start of the game itself
    deck = [1,1,1,1,1,1,2,2,2,2,2,2,3,3,3,3,3,3,4,4,4,4,4,4,5,5,5,5,4,4,6,6,6,6,6,6,7,7,7,7,7,7,8,8,8,8,8,8,9,9,9,9,9,9,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0]
    random.shuffle(deck)
    plc1 = deck.pop()
    bkc1 = deck.pop()
    plc2 = deck.pop()
    bkc2 = deck.pop()
    plc3 = "None"
    bkc3 = "None"
    if (plc1 + plc2) < 10:
        plhd = (plc1 + plc2)
    else:
        plhd = (plc1 + plc2) - 10
    if (bkc1 + bkc2) < 10:
        bkhd = (bkc1 + bkc2)
    else:
        bkhd = (bkc1 + bkc2) - 10
    print("Does either the player or banker have a natrual?")
    if 8 <= plhd <= 9 and bkhd <= 7:
        print("Player has a natural")
        EndGame(plhd, bkhd, i, j, k, player_names, player_bet, num_players_int, player_bet_sum, player_pocket)
    elif 8 <= bkhd <= 9 and plhd <= 7:
        print("Banker has a natural")
        EndGame(plhd, bkhd, i, j, k, player_names, player_bet, num_players_int, player_bet_sum, player_pocket)
    elif 8 <= plhd <= 9 and 8 <= bkhd <= 9:
        print("Player and Banker have naturals")
    print("No naturals, contine the game.")
    print(player_names[j],"(Banker), please look away while",player_names[k],"(Player) considers his/her hand.")
    print("Player hand:",plhd)
    if banco == 1:
        if plhd != 0:
            pl3rd = input("Since you,",player_names[k],",called banco and your hand is not zero, would like a third card? (y/n): ")
            if pl3rd.lower() == "y":
                plc3 = deck.pop()
                print("Player Card #3:", plc3, "\n")
                plhd = plhd + plc3
                if plhd < 10:
                    pass
                else:
                    plhd = plhd - 10
            elif pl3rd.lower() == "n":
                pass
        elif plhd == 0:
            print("Since your hand is zero, a third card will automatically be drawn.")
            plc3 = deck.pop()
            print("Player Card #3:", plc3, "\n")
            plhd = plhd + plc3
            if plhd < 10:
                pass
            else:
                plhd = plhd - 10
    else:
        if plhd <= 4:
            print("Since the player hand is less than or equal to four, a third card will be automatically drawn for the player.")
            plc3 = deck.pop()
            print("Player Card #3:", plc3, "\n")
            plhd = plhd + plc3
            if plhd < 10:
                pass
            else:
                plhd = plhd - 10
        elif plhd >= 6:
            print("Since the player hand is greater than or equal to six, no additional card will be drawn for the player.")
            pass
        elif plhd == 5:
            pl3rd = (input("Since the player hand is five, would you (player) like to drawn a third card? (y/n): "))
            if pl3rd.lower() == "y":
                plc3 = deck.pop()
                print("Player Card #3:", plc3, "\n")
                plhd = plhd + plc3
                if plhd < 10:
                    pass
                else:
                    plhd = plhd - 10
            elif pl3rd.lower() == "n":
                pass
    print("Player Hand:",plhd)
    while True:
        cont1 = (input("Are done reviewing your hand? (y/n): "))
        if cont1.lower() == "y":
            break
        elif cont1.lower() == "n":
            continue
        else:
            print("Invalid choice, please type y or n.")
    clear = "\n"*100
    print(clear)
    print(player_names[j],"(Banker) may now return to the game.\n")
    print("Banker Hand:",bkhd)
    print("Player's third card was a(n):", plc3)
    bk3rd = (input("Would you (banker) like to draw a third card? (y/n): "))
    if bk3rd.lower() == "y":
        bkc3 = deck.pop()
        print("Banker Card #3:", bkc3, "\n")
        bkhd = bkhd + bkc3
        if bkhd < 10:
            pass
        else:
            bkhd = bkhd - 10
    elif bk3rd.lower() == "n":
        pass
    print("Banker Hand:",bkhd,"\n")
    while True:
        cont2 = (input("Are done reviewing your hand? (y/n): "))
        if cont2.lower() == "y":
            break
        elif cont2.lower() == "n":
            continue
        else:
            print("Invalid choice, please type y or n.")
    print("\n\n\n")
    print("All hands are final.\n\n\n")
    EndGame(plhd, bkhd, i, j, k, player_names, player_bet, num_players_int, player_bet_sum, player_pocket)
def EndGame(plhd, bkhd, i, j, k, player_names, player_bet, num_players_int, player_bet_sum, player_pocket):
    print("Banker Hand:",bkhd)
    print("Player Hand:",plhd)
    if plhd > bkhd:
        print("Player hand is closer to nine, player wins!\n")
        print("Banker loses his/her wager and pays all player wagers 2:1")
        i = 3
        t = 0
        while t < num_players_int:
            if t == j:
                player_pocket[j] = player_pocket[j]
                print(player_names[j],"lost",player_bet[j],"dollars in the hand.")
                print(player_names[j],"now has",player_pocket[j],"dollars total.\n")
                t = t + 1
            else:
                player_pocket[t] = player_pocket[t] + (2*player_bet[t])
                print(player_names[t],"won",(2*player_bet[t]),"dollars in the hand.")
                print(player_names[t],"now has",player_pocket[t],"dollars total.\n")
                t = t + 1
    elif bkhd > plhd:
        print("Banker hand is closer to nine, banker wins!\n")
        print("Players lose all wagers, and Banker collects all wagers with 5% commission to the house.")
        i = 2
        t = 0
        while t < num_players_int:
            if t == j:
                player_pocket[t] = player_pocket[t] + int((player_bet[t]) + ((player_bet_sum) - ((0.05)*(player_bet_sum))))
                print(player_names[t],"won",(player_bet[t]+(int(((player_bet_sum) - ((0.05)*(player_bet_sum)))))),"dollars in the hand.")
                print(player_names[t],"now has",player_pocket[t],"dollars total.\n")
                t = t + 1
            else:
                player_pocket[t] = player_pocket[t]
                print(player_names[t],"lost",player_bet[t],"dollars in the hand.")
                print(player_names[t],"now has",player_pocket[t],"dollars total.\n")
                t = t + 1
    elif bkhd == plhd:
        print("Both hand are the same, so the round ends in a tie. All wagers are returned.\n")
        i = 2
        t = 0
        while t < num_players_int:
            player_pocket[t] = player_pocket[t] + player_bet[t]
            t = t + 1
    while True:
        Play_Again = (input("Would you like to play again?(y/n): "))
        if Play_Again.lower() == "y":
            Baccarat(i, player_names, num_players_int, player_bet, player_pocket, j)
        elif Play_Again.lower() == "n":
            print("Thanks for Playing.")
            sys.exit()
            break
        else:
            print("Invalid choice, please enter y or n.")
Intro()

