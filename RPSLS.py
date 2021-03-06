# Rock-paper-scissors-lizard-Spock template


# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors
#Scissors cut Paper
#Paper covers Rock
#Rock crushes Lizard
#Lizard poisons Spock
#Spock smashes Scissors
#Scissors decapitate Lizard
#Lizard eats Paper
#Paper disproves Spock
#Spock vaporizes Rock
#Rock crushes Scissors


# helper functions
def name_to_number(name):
    # convert name to number using if/elif/else
        if name=="rock":
            number=0
            return number	
        elif name=="paper":
            number=2
            return number
        elif name=="scissors":
            number=4
            return number
        elif name=="lizard":
            number=3
            return number
        elif name=="Spock":
            number=1
            return number
        else :
            print "numbering problem"

def number_to_name(number):
    # convert number to a name using if/elif/else
    if number==0:
        name="rock"
        return name	
    elif number==2:
        name="paper"
        return name
    elif number=="4":
        name="scissors"
        return name
    elif number==3:
        name="lizard"
        return name
    elif number==1:
        name="Spock"
        return name
    else :
        print "naming problem"
        
def rpsls(player_choice): 
    # print a blank line to separate consecutive games
    print " "
    
    # print out the message for the player's choice
    print "Player chooses", player_choice
    
    # convert the player's choice to player_number using the function name_to_number()
    player_number=name_to_number(player_choice)
    
    # compute random guess for comp_number using random.randrange()
    import random
    comp_number=random.randrange(0,4)
    
    # convert comp_number to comp_choice using the function number_to_name()
    comp_choice=number_to_name(comp_number)
    
    # print out the message for computer's choice
    print "Computer chooses", comp_choice
    
    # compute difference of comp_number and player_number modulo five
    result_number= (comp_number-player_number)%5
    print result_number
    
    # use if/elif/else to determine winner, print winner message
    if result_number==2:
        print "Computer wins!"
    elif result_number==1:
        print "Computer wins!"
    elif result_number==3:
        print "Player wins!"
    elif result_number==4:
        print "Player wins!"
    elif result_number==0:
        print "Tie!"
        
    
# test your code - THESE CALLS MUST BE PRESENT IN YOUR SUBMITTED CODE
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")

