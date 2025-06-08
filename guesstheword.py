from time import sleep

# Title
print("-=" * 49)
print("""\033[1;32m
   _____ _    _ ______  _____ _____   _______ _    _ ______  __          ______  _____  _____  _ 
  / ____| |  | |  ____|/ ____/ ____| |__   __| |  | |  ____| \ \        / / __ \|  __ \|  __ \| |
 | |  __| |  | | |__  | (___| (___      | |  | |__| | |__     \ \  /\  / / |  | | |__) | |  | | |
 | | |_ | |  | |  __|  \___ \\___ \      | |  |  __  |  __|     \ \/  \/ /| |  | |  _  /| |  | | |
 | |__| | |__| | |____ ____) |___) |    | |  | |  | | |____     \  /\  / | |__| | | \ \| |__| |_|
  \_____|\____/|______|_____/_____/     |_|  |_|  |_|______|     \/  \/   \____/|_|  \_\_____/(_)
                                                                                                 
                                                                                                 
\033[m""")

print("-=" * 49)
# Game
while True:
    word = input("Type a word:\n").strip().capitalize()
    topic = input("The principal topic (fruit, animal, videogames...):\n")
    tip1 = input("1° Tip:\n")
    tip2 = input("2° Tip:\n")
    tip3 = input("3° Tip:\n")
    print("\033[1;34mStarting game...\033[m")
    sleep(1.75) # Wait
    print("\n" * 100)
    print(f"Topic:\n \033[1;32m{topic}\033[m")
    guess = input("Guess the word:\n").strip().capitalize()
    if guess == word:
        print("You are...")
        sleep(1.25)
        print("\033[1;32mCorrectly!\033[m")
        toclose = input("Type 'Close' to close the game or only press 'Enter' to start a new game:\n").strip().capitalize()
        if toclose == "Close":
            print("Closing...")
            break
        else:
            input("Press 'Enter' to start a new game!")
    elif guess != word:
            print("You are...")
            sleep(1.25)
            print("\033[1;31mIncorrect!\033[m")
            print(f"1° Tip: {tip1}")
            guess_tentative_1 = input("Try again! Guess the word:\n").strip().capitalize()
            if guess_tentative_1 == word:
                print("You are...")
                sleep(1.25)
                print("\033[1;32mCorrectly!\033[m")
                toclose = input("Type 'Close' to close the game or only press 'Enter' to start a new game:\n").strip().capitalize()
                if toclose == "Close":
                    print("Closing...")
                    break
                else:
                    input("Press 'Enter' to start a new game!")
            elif guess_tentative_1 != word:
                print("You are...")
                sleep(1.25)
                print("\033[1;31mIncorrect!\033[m")
                print(f"2° Tip: {tip2}")
                guess_tentative_2 = input("Try again! Guess the word:\n").strip().capitalize()
                if guess_tentative_2 == word:
                    print("You are...")
                    sleep(1.25)
                    print("\033[1;32mCorrectly!\033[m")
                    toclose = input("Type 'Close' to close the game or only press 'Enter' to start a new game:\n").strip().capitalize()
                    if toclose == "Close":
                        print("Closing...")
                        break
                    else:
                        input("Press 'Enter' to start a new game!")
                elif guess_tentative_2 != word:
                    print("You are...")
                    sleep(1.25)
                    print("\033[1;31mIncorrect!\033[m")
                    print(f"3° Tip: {tip3}")
                    guess_tentative_3 = input("Try again! This is your last tentative! Guess the word:\n").strip().capitalize()
                    if guess_tentative_3 == word:
                        print("You are...")
                        sleep(1.25)
                        print("\033[1;32mCorrectly!\033[m")
                        toclose = input("Type 'Close' to close the game or only press 'Enter' to start a new game:\n").strip().capitalize()
                        if toclose == "Close":
                            print("Closing...")
                            break
                        else:
                            print("Press 'Enter' to start a new game!")
                    elif guess_tentative_3 != word:
                        print("You are...")
                        sleep(1.25)
                        print("\033[1;31mIncorrect!\033[m")
                        print(f"The word was... \033[1;32m{word}\033[m")
                        toclose = input("Type 'Close' to close the game or only press 'Enter' to start a new game:\n").strip().capitalize()
                        if toclose == "Close":
                            print("Closing...")
                            break
                        else:
                            input("Press 'Enter' to start a new game!")