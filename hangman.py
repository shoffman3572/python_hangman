from random import randint
# variable setup
round = 0

# set up list of words
words = ("discount", "activate", "window",
         "england", "scotland", "python")  # tuple

# pick a word from the words tuple at random
random_number = randint(0, 3)
word = words[random_number]

# convert the word into a list
word_set = [*word]  # unpacking operator

# set up another list to store and display the user's progress
user_progress = []
list_size = len(word_set)
for s in range(list_size):
    user_progress.append("_")

while round != 14:
    # ask user to guess a word
    user_guess = input("Enter a word: ")

    if user_guess.lower() in word_set:
        # get all locations of the entered character
        for char_pos in range(list_size):
            if word_set[char_pos] == user_guess:
                # then update the user_progress list at the same location in the list
                user_progress[char_pos] = user_guess
        print("Found!")
        # check to see if the user has completed the puzzle
        if "_" not in user_progress:
            print(user_progress)
            print("You win!")
            break
        round += 1
        print(user_progress)
        # give the user the opportunity to guess the word
        guess_word = input("Would you like to guess the word? (y,n) ")
        if guess_word.lower() == "y":
            word_guess = input("What do you think the word is? ")
            if word_guess.lower() == word:
                print("Correct! You win!")
                break
            else:
                print("Nope!")
                round += 1  # the user loses another round
    else:
        print("Not found!")
        round += 1
        print(user_progress)
else:
    print("You lose! Better luck next time.")
