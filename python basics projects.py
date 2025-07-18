'''
#Project 1

start = int(input('Enter Start: '))
end = int(input('Enter End: '))
def divide_numbers(start, end):
    even_numbers = []
    odd_numbers = []
    
    for number in range(start, end + 1): 
        if number % 2 == 0:
            even_numbers.append(number)
        else:
            odd_numbers.append(number)
    
    print(f'Even numbers:', even_numbers)
    print(f'Odd numbers:', odd_numbers)


divide_numbers(start, end)
'''


'''
#Projec2


sentence = input('Enter the sentence : ')
def Duplicate_remover(sentence):
    no_duplicate = []

    for word in sentence.split( ):
        if word not in no_duplicate:
            no_duplicate.append(word)

    new_sentence = ' '.join(no_duplicate)
    print(new_sentence)

    redudent = len(sentence.split( ))-len(no_duplicate)
    print( redudent )


Duplicate_remover(sentence)
'''



'''

#Project 3

def count_up(self):
Number = int(input("Enter a number: "))
for x in range(Number + 1):
    print(x)
'''


'''
#Project 4
def divisible_by_one(self):
x = int(input("Enter the frist number:"))
y = int(input("Enter the second number:"))
if y == 0:
    print("You can't divide by zero please enter another number")
else:
    print("The numbers are:")
    for i in range(1,x+1):    
        if i % y == 0:
            print(i)

'''


'''

#Project 5

def divisible_by_both(self):
x = int(input("Enter the frist number:"))
y = int(input("Enter the second number:"))

print("The numbers are:")
for i in range(101):
    if i % x == 0 and i % y == 0:
        print(i)


'''



#Project 6



class Game:
    def __init__(self):
        while True:
            print('''Welcome to my game, Enter game number:
    1 - Divide Numbers into Even and Odd
    2 - Remove Duplicate Words from Sentence
    3 - Count from 0 to a Given Number
    4 - Print Numbers Divisible by Another
    5 - Print Numbers Divisible by Two Numbers (0 to 100)
    6 - Exit''')

            user_choice = int(input('Enter game number: '))
            if user_choice == 1:
                self.divide_numbers()
            elif user_choice == 2:
                self.duplicate_remover()
            elif user_choice == 3:
                self.count_up()
            elif user_choice == 4:
                self.divisible_by_one()
            elif user_choice == 5:
                self.divisible_by_both()
            elif user_choice == 6:
                print('Goodbye ...')
                break
            else:
                print("Invalid choice!")

            play_again = input('press y  to play again or press n to exit :')
            if play_again == 'n':
                break

            elif play_again == 'y':
                continue
            else:
                print('Invalid ')
    def divide_numbers(self):
        start = int(input('Enter Start: '))
        end = int(input('Enter End: '))

        even_numbers = []
        odd_numbers = []

        for number in range(start, end + 1):
            if number % 2 == 0:
                even_numbers.append(number)
            else:
                odd_numbers.append(number)

        print('Even numbers:', even_numbers)
        print('Odd numbers:', odd_numbers)

    def duplicate_remover(self):
        sentence = input('Enter the sentence: ')
        no_duplicate = []

        for word in sentence.split():
            if word not in no_duplicate:
                no_duplicate.append(word)

        new_sentence = ' '.join(no_duplicate)
        redundant = len(sentence.split()) - len(no_duplicate)

        print("Sentence without duplicates:", new_sentence)
        print("Number of removed duplicate words:", redundant)

    def count_up(self):
        number = int(input("Enter a number: "))
        for x in range(number + 1):
            print(x)

    def divisible_by_one(self):
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        if y == 0:
            print("You can't divide by zero. Please enter another number.")
        else:
            print(f"Numbers from 1 to {x} that are divisible by {y}:")
            for i in range(1, x + 1):
                if i % y == 0:
                    print(i)

    def divisible_by_both(self):
        x = int(input("Enter the first number: "))
        y = int(input("Enter the second number: "))
        if x == 0 or y == 0:
            print("You can't divide by zero.")
            return
        print(f"Numbers from 0 to 100 divisible by both {x} and {y}:")
        for i in range(101):
            if i % x == 0 and i % y == 0:
                print(i)


game = Game()




