import random
def choice_result(option):
    if option=="s":
        return "SCISSOR"
    elif option=="p":
        return "PAPER"
    elif option=="r":
        return "ROCK"
def result(player,computer):
    if player==computer:
        print("------------------ITS A TIE------------------")
    elif(player>computer):
        print("-----------------YOU WIN!, CONGRATULATION-----------------")
    else:
        print("-------------COMPUTER WINS! , BETTER LUCK NEXT TIME-------------")

run=True
player_point=0
computer_point=0
valid_choice=["r","p","s"]
print("----------------------STONE PAPER SCISSOR----------------------")
print("------- |r for Rock|  && |p for Paper| && |s for Scissor|-------")
print("-----------------------|0(zero) for EXIT|-----------------------")
while run:
    player_choice=input("Enter your choice:").strip().lower()
    computer_choice=random.choice(valid_choice)
    if player_choice=="0":
        result(player_point,computer_point)
        print("     ---------------THANKS FOR PLAYING---------------     ")
        run=False
    elif player_choice not in valid_choice:
        print("        XXXXXXXXXX      Invalid choice      XXXXXXXXXX        ")
        print("------------------PLEASE ENTER A VALID CHOICE-----------------R")
    elif player_choice==computer_choice:
        print("                --->COMPUTER CHOICE:"+choice_result(computer_choice))
        print("-------------------------TIE-----------------------")
        print("----------------------PLAYER POINT:",player_point)
        print("----------------------COMPUTER POINT:",computer_point)
    elif ((player_choice=="r" and computer_choice=="s") or (player_choice=="p" and computer_choice=="r") or (player_choice=="s" and computer_choice=="p")):
        print("                     --->COMPUTER CHOICE:"+choice_result(computer_choice))
        player_point+=1
        print("------------------- PLAYER WIN ---------------------")
        print("----------------------PLAYER POINT:",player_point)
        print("----------------------COMPUTER POINT:",computer_point)

    else:
        print("                --->COMPUTER CHOICE:"+choice_result(computer_choice))
        computer_point+=1
        print("------------------- COMPUTER WIN ---------------------")
        print("----------------------COMPUTER POINT:",computer_point)
        print("----------------------PLAYER POINT:",player_point)
        
    print("\n"+"----------------------------------------------------------------------------------------")