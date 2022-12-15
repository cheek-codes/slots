#generate random values so no cheating
import random

#constants
MAX_LINES = 3
MAX_BET = 9999999
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "A": 2,
    "B": 4,
    "C": 6,
    "D": 8
}

symbol_value ={
    "A": 5,
    "B": 4,
    "C": 3,
    "D": 2
}

def check_winnings(columns, lines, bet, values):
    winnings = 0
    winning_lines = []
    #loop through row the user bet on. 
    for line in range(lines):
        #check symbol
        symbol = columns[0][line]
        #loop though and check for that symbol
        for column in columns:
            symbol_to_check = column[line]
            #check if won, go to the next
            if symbol != symbol_to_check:
                break
        else:
            winnings += values[symbol] * bet
            winning_lines.append(line + 1)
    return winnings, winning_lines

def get_slot_machin_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range(symbol_count):
            all_symbols.append(symbol)

    columns = []
    #make dem columns
    for _ in range(cols):
        column =  []
        #pick random values for the columns. make a copy  of all_symbols so changes won't cause a change to the real all_symbols, when we take out the value that's picked so it doesn't get picked again. 
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        
        columns.append(column)

    return columns

def print_slot_machine(columns):
    #loop through row, and loop through column to make it print in a column instead of a row
    for row in range(len(columns[0])):
        for i, column in enumerate(columns):
            if i != len(columns) - 1:
                print(column[row], end=" | ")
            else:
                print(column[row], end="")

        print()

#collect user input (deposit & bet)
def deposit():

    #continously ask user to enter deposit until they give a valid amount
    while True:
        amount = input("How much you wanna deposit? $")

        #check if amount given by user is a number. If not, ask them to enter a number
        if amount.isdigit():

            #convert to integer
            amount = int(amount)
            
            #check if amount is > 0. If not, ask them to enter a number greater than 0
            if amount > 0:
                break
            else:
                print("Come on, it has to be more than $0.")
        else:
            print("That's not a number!!")
    
    return amount


#collect bet from user. how much they want to be bet, how many lines they want to bet on. multiply bet amount by lines
def get_number_of_lines():

    #continously ask user to enter number of lines they want to be until they give a valid amount
    while True:
        lines = input(f"How many lines you want to bet on? (1- {str(MAX_LINES)}) ")

        #check if lines given by user is a number. If not, ask them to enter a number
        if lines.isdigit():

            #convert to integer
            lines = int(lines)
            
            #check if lines is within the boundaries. If not, ask them to enter a number that is within the boundaries
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print("Really? I didn't give you those choices. ")
        else:
            print("A real number please")
    
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
            print("Use a real amount. I don't accept gum as payment")
    
    return amount

def spin(balance):
    lines = get_number_of_lines()

    #check if the user's balance can cover the bet
    while True:
        bet = get_bet()
        total_bet = bet * lines

        if total_bet > balance:
            print(f"You do not have enough to bet that amount. Your current balance is ${balance}, while you are trying to bet ${total_bet}")
        else:
            break

    print(f"You are betting ${bet} on {lines} lines. So your total bet is ${total_bet}")

    slots = get_slot_machin_spin(ROWS, COLS, symbol_count)
    print_slot_machine(slots)
    winnings, winning_lines = check_winnings(slots, lines, bet, symbol_value)
    print(f"You won ${winnings}.")
    print(f"You won on lines: ", *winning_lines)
    return winnings - total_bet

#when the program finishes, call the function to start all over
def main():
    balance = deposit()
    while True:
        print(f"Current balance is ${balance}")
        again = input("Press Enter to play. Type [q] to quit. ")
        if again == "q" or again == "Q":
            break
        balance += spin(balance)

    print(f"You are leaving with ${balance}! Congrats, I guess.")

main()