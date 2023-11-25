import random

#pick random word from word_list.txt
with open("word_list.txt", 'r') as file:                    #"with" closes file after use
    word_list = [word.strip() for word in file.readlines()] #"[]" to declare list; word.strip to remove whitespaces; word temporary variable file.readlines to get the words from lines

random_word = random.choice(word_list)
word_length = len(random_word)

progress_count = 0 
mistake_count = 0


def add_mistake():
    
    global mistake_count

    #animation programmieren
    mistake_count += 1



def main():

    game_condition = 1                      #"1" running; "0" lose; "2" win
    progress_string = '_' * word_length     #initial progress - will be modified by progress()

    print("Das Spiel beginnt. Umlaute werde ae/ue/oe geschrieben. Es gibt 6 Fehlversuche.")
    print(progress_string)

    guess = ""
    guessed = []
    

    while game_condition == 1:

        while (len(guess) != 1 or guess.isalpha() == False or guess in guessed):

            if not guess in guessed:
                guess = input("Errate einen Buchstaben:")

            else:
                guess = input("Du hast diesen Buchstaben schon geraten, neuen Buchstaben eingeben:")
                    
            guess = guess.lower()
        
        guessed += guess


        if guess in random_word:                    #Correct -> add progress and print progress
            
            global progress_count                   #declare progress_count as global


            mod_list = list(progress_string)        #convert (copy of) string to list

            for i, letter in enumerate(random_word): #iterate through enumerated random_word
                if  guess == letter:
                    mod_list[i] = guess
                    progress_count += 1

            progress_string = ''.join(mod_list)
            print(progress_string)
           

            if progress_count == word_length:       #Winning condition exits loop
                game_condition = 2

        else:                                       #Mistake -> Add mistake and print the number of mistake or V2 the hangman picture
            add_mistake()              
            print(f"Anzahl Fehler: {mistake_count}")

            if mistake_count == 7:
                game_condition = 0

        guess = ""




    if game_condition == 2:
        print("SIEG")

    else:
        print("VERLOREN")




# Execute Program
if __name__ == "__main__":
    main()