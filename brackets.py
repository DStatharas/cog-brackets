# Write a function to determine if a string of brackets is balanced. A string is considered balanced if:
#
#     Every opening bracket has a corresponding closing bracket of the same type.
#     Brackets are properly nested.
#
# Example
#
# Input: "()"
# Output: True
#
# Input: "({[]})"
# Output: True
#
# Input: "([)]"
# Output: False
#
# Input: "{[}"
# Output: False
import os


def quitCheck(x):
    if x.lower() == 'q':
        quit()

def bracketCheck(inputtedBrackets):
    # Define helper lists
    openingBrackets = ['{', '[', '(']
    closingBrackets = ['}', ']', ')']
    bracketBuffer = []

    # Loop through user list
    for i in inputtedBrackets:

        # Check for brackets in user list
        if i not in openingBrackets and i not in closingBrackets:
            return False

        # Check for opening bracket and appended to buffer
        if i in openingBrackets:
            bracketBuffer.append(i)

        # Check for closing bracket and indexing it in helper list (does not get appended to buffer)
        elif i in closingBrackets :
            closingPosition = closingBrackets.index(i)

            # Check if buffer is empty and if closing bracket matches latest append into buffer.
            # If it does, buffer get default popped and loop moves into next iteration.
            # If not, brackets are surely unbalanced due to the previous bracket being an unmatching opening bracket.
            if len(bracketBuffer) > 0 and openingBrackets[closingPosition] == bracketBuffer[len(bracketBuffer) - 1]:
                bracketBuffer.pop()

            else:
                return False

    # If buffer is empty it means all closing brackets have popped
    # all corresponding opening brackets and input was balanced.
    # If not, then opening brackets remain unclosed and input was unbalanced.
    if len(bracketBuffer) == 0:
        return True

    else:
        return False


# Main Menu
active = True

while active:

    os.system('cls')
    print('Welcome to Balanced Brackets!'
          '\nAre your brackets balanced according to industry standards? Find out with this useful program!'
          '\nAcceptable types of brackets: {} [] ()'
          '\nType "Q" at any point to quit.')

    try:
        userInput = input('\nPlease enter your series of brackets: ')

    except Exception as e:
        print('ERROR: Unrecognized exception. Are you sure you only entered brackets? '
              'Please send the following error message to the administrator:')
        print(f'\n{e}')
        quitCheck(input('\nEnter anything to continue...'))
        continue

    quitCheck(userInput)

    if userInput == '':
        continue

    try:
        userBrackets = list(userInput)

    except Exception as e:
        print('ERROR: Unrecognized exception. Are you sure you only entered brackets? '
              'Please send the following error message to the administrator:')
        print(f'\n{e}')
        quitCheck(input('\nEnter anything to continue...'))
        continue


    try:
        balanceCheck = bracketCheck(userBrackets)

    except Exception as e:
        print('ERROR: Unrecognized exception. '
              'Please send the following error message to the administrator:')
        print(f'\n{e}')
        quitCheck(input('\nEnter anything to continue...'))
        continue

    print(f'\nYour brackets:'
          f'\n{''.join(userBrackets)}')

    if balanceCheck:
        print('\nYour brackets are balanced!')

    elif not balanceCheck:
        print('\nYour brackets are either not balanced or contain characters other than brackets.')

    else:
        print('\nERROR: unexpected result. Please send this error message to the administrator.')

    quitCheck(input('\nEnter anything to continue...'))

    continue