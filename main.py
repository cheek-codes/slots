#generate random values so no cheating
import random

#constants
MAX_LINES = 3
MAX_BET = 100
MIN_BET = 1

ROWS = 3
COLUMNS = 3



#collect user input (deposit & bet)
def deposit():

    #continously ask user to enter deposit until they give a valid amount
    while True:
        amount = input("What would you like to deposit? $")

        #check if amount given by user is a number. If not, ask them to enter a number
        if amount.isdigit():

            #convert to integer
            amount = int(amount)
            
            #check if amount is > 0. If not, ask them to enter a number greater than 0
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Please enter a number")
    
    return amount


#collect bet from user. how much they want to be bet, how many lines they want to bet on. multiply bet amount by lines
def get_number_of_lines():

    #continously ask user to enter number of lines they want to be until they give a valid amount
    while True:
        lines = input(f"Enter the number of lines to bet on (1- {str(MAX_LINES)})? ")

        #check if lines given by user is a number. If not, ask them to enter a number
        if lines.isdigit():

            #convert to integer
            lines = int(lines)
            
            #check if lines is within the boundaries. If not, ask them to enter a number that is within the boundaries
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Enter a valid number of lines.")
        else:
            print("Please enter a number")
    
    return lines

def get_bet():
    
    #continously ask user to enter an amount they want to bet until they give a valid amount
    while True:
        amount = input("How much would you like to bet on each line? $")

        #check if amount given by user is a number. If not, ask them to enter a number
        if amount.isdigit():

            #convert to integer
            amount = int(amount)
            
            #check if amount is within the boundaries. If not, ask them to enter a number that is within the boundaries
            if MIN_BET <= amount <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} - ${MAX_BET}.")
        else:
            print("Please enter a number")
    
    return amount

#when the program finishes, call the function to start all over
def main():
    balance = deposit()
    lines = get_number_of_lines()

    #check if the user's balance can cover the bet
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}, while you are trying to bet ${total_bet}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. Total bet is equal to ${total_bet}")

main()