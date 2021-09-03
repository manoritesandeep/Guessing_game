import random
num = random.randint(1,100)
# The rules of the game are as follows:

print('Welcome to the guessing game! ')
print('The rules of the game are as follows: \n')
print('The user enters a number between 1 or greater than 100. Anything beyond the range will be considered OUT OF BOUNDS. ')
print('When the initial guess is within 10 of the number, you`re WARM. ')
print('When the initial guess is more than 10 of the number, you`re COLD. ')
print('When the next guess is closer to the number than the previous guess, you`re getting WARMER. ')
print('When the next guess is father to the number than the previous guess, you`re getting COLDER. ')
print('Upon guessing the right number, congratulations you`re right and number of tries will be displayed')
print('Let`s go! ')

guesses = [0]

while True:
    
    guess = int(input("I`m thinking of a number between 1 and 100. \n Now your turn to guess, that is: "))
    
    if guess < 1 or guess >100:
        print('You`re OUT OF BOUNDS! Please try again: ')
        continue
    
    break

while True:

   
    guess = int(input("I`m thinking of a number between 1 and 100. \n Now your turn to guess, that is: "))
    
    if guess < 1 or guess >100:
        print('You`re OUT OF BOUNDS! Please try again: ')
        continue
    
    #comparing the player`s guess to my input
    if guess == num:
        print(f'Congratulations, you guessed it only in {len(guesses)} number of guesses!!')
        break
        
    #if guess was incorrect, we +1 to the number of guesses.
    guesses.append(guess)
    
    if guesses[-2]:  
        if abs(num-guess) < abs(num-guesses[-2]):
            print('WARMER!')
        else:
            print('COLDER!')
   
    else:
        if abs(num-guess) <= 10:
            print('WARM!')
        else:
            print('COLD!')
