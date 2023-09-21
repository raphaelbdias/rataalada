# import all required modules
import random
import time
import os
from os import system, name
import sys
import climage

# Clearing the Screen
os.system("cls")

# FUNCTIONS
def clear():

    # for windows
    if name == "nt":
        _ = system("cls")

    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system("clear")


# function to cypher the text


# cypher messages
def cypher(text):
    symbols = {
        "A": "∞",
        "B": "π",
        "C": "œ",
        "D": "@",
        "E": "§",
        "F": "#",
        "G": "«",
        "H": "†",
        "I": "∑",
        "J": "!",
        "K": "≠",
        "L": "$",
        "M": "¡",
        "N": "&",
        "O": "≈",
        "P": "%",
        "Q": "£",
        "R": "ß",
        "S": "¢",
        "T": "æ",
        "U": "*",
        "V": "•",
        "W": "å",
        "X": "¬",
        "Y": "¶",
        "Z": "µ",
    }
    text = text.upper()
    for key, value in symbols.items():
        text = text.replace(key, value)
    return text


# function to decypher the text
# decypher messages
def decypher(text):
    symbols = {
        "A": "∞",
        "B": "π",
        "C": "œ",
        "D": "@",
        "E": "§",
        "F": "#",
        "G": "«",
        "H": "†",
        "I": "∑",
        "J": "!",
        "K": "≠",
        "L": "$",
        "M": "¡",
        "N": "&",
        "O": "≈",
        "P": "%",
        "Q": "£",
        "R": "ß",
        "S": "¢",
        "T": "æ",
        "U": "*",
        "V": "•",
        "W": "å",
        "X": "¬",
        "Y": "¶",
        "Z": "µ",
    }
    for key, value in symbols.items():
        text = text.replace(value, key)
    return text


# progressbar
def progressbar(it, prefix="", size=60, out=sys.stdout):  # Python3.3+
    count = len(it)

    def show(j):
        x = int(size * j / count)
        print(
            "{}{}{} {}/{}".format(prefix, "█" * x, "." * (size - x), j, count),
            end="\r",
            file=out,
            flush=True,
        )

    show(0)
    for i, item in enumerate(it):
        yield item
        show(i + 1)
    print("\n", flush=True, file=out)


# first interaction with riddler
def level_1(message):
    global letters, health, popularity
    print("\u001b[32m \033[1m")  # green text
    clear()
    for i in range(3):  # interface of riddler
        clear()
        time.sleep(1)
        print(f"\033[1m{'<?>': ^100}")
        time.sleep(1)
    # variables to count rounds and points
    rounds = 1
    points = 0

    # introduction to player
    intro = [
        "LET'S PLAY A GAME JUST ME AND YOU.\n",
        "I HAVE GOT SOME QUESTIONS. YOU HAVE BEEN LOOKING FOR SOME ANSWERS.\n",
        "I HAVE BEEN EXPECTING YOU. LET'S PLAY A GAME?\n",
    ]
    # dictionary of riddles with answers
    riddles = {
        "bribe": "If you are justice, please do not lie. What is the price for your blind eye?",
        "friend": "The less of them you have, the more one is worth. what are they?",
        "clock": "If You Look At The Numbers On My Face, You Won't Find 13 Anyplace. who am i?",
        "book": "Generally my leaves aren't turned at night, usually I'm full of worms by day, lots of words but deathly quiet. what am i?",
        "tomorrow": "What is always on its way here but never arrives?",
        "street": "I can be easy or a dead end. Careful when you cross me. who am i?",
    }
    # if player gets answer right
    correct = [
        "YOU ARE SMARTER THAN I THOUGHT YOU'D BE. TRY THIS NEXT RIDDLE.",
        "YOU HAVE UNMASKED THE TRUTH. TRY ONE MORE RIDDLE.",
        "YOU ARE CORRECT",
        "YOU ARE GOOD. ONTO THE NEXT ONE.",
    ]
    # if player gets answer wrong
    wrong = [
        "YOU ARE CLEARLY NOT AS SMART AS I THOUGHT YOU WERE. WHY DON'T YOU TRY AGAIN",
        "STOP GUESSING AND START THINKING. TRY ANOTHER ONE.",
        "YOU GOT IT WRONG. WHY DON'T YOU TRY AGAIN...",
        "YOU ARE TRYING TO UNMASK THE TRUTH. BUT YOU ARE NOT THERE YET.",
        "HOW WILL GOTHAM BE SAVED WITH ANSWERS LIKE THAT",
        "YOU CAN'T GET THIS THIS ONE, CAN YOU? DON'T WORRY TRY AGAIN.",
    ]
    # start questioning
    print("\u001b[32m \033[1m")  # green text

    print(f">> {random.choice(intro)}")
    time.sleep(2)
    start = input("\u001b[32m>> PROCEED [Y/N]\n")
    time.sleep(2)

    if start.lower() == "y":
        open_statement = [
            "READY TO UNCOVER THE TRUTH? LET'S GET STARTED.\n",
            "HERE WE GO. THREE RIGHT ANSWERS AND JUSTICE WILL BE YOUR REWARD.\n",
        ]

        print(f">> {random.choice(open_statement)}")
        time.sleep(3)
        # for loop to check if the player guessed the right answer
        for answer, riddle in riddles.items():
            # if player loses
            if rounds == 6 and points < 3:
                time.sleep(2)
                print("\n>> LOOKS LIKE YOU ARE NOT UP FOR A CHALLENGE TODAY.")
                time.sleep(2)
                print("\n>> WHAT IS BLACK AND BLUE AND DEAD ALL OVER?")
                time.sleep(2)
                print("\n>> THE BATMAN")
                time.sleep(2)
                print("\n>> BAD MOVE. GOTHAM HAS PERISHED.")
                time.sleep(1)
                print(f"{'<?>': ^150}")
                time.sleep(4)
                clear()
                print("\n\n\t\tGAME OVER <?>")
                time.sleep(2)
                sys.exit("\n\nTHE PROGRAM HAS BEEN TERMINATED")

            #  if player is still has a chance of winning
            elif points < 4 and rounds < 6:
                print(f"\n>> {riddle.upper()}\n")
                user = input("\u001b[32m")

                time.sleep(3)

                # if player
                if answer in user.lower():
                    points += 1

                    if points < 3:
                        response_1 = random.choice(correct)
                        print(f"\n>> {response_1}")
                        x = correct.index(response_1)
                        popularity += 10
                        del correct[x]
                    # if player gets 3 right back to back
                    elif points == 3 and rounds == 3:
                        print(
                            "\n>> THREE OUT OF THREE. I SEE THAT YOU ARE ONE OF THE SMART ONES..."
                        )
                        time.sleep(2)

                        print(
                            "\n>> YOU HAVE COME THIS FAR. \
              \n\nNOW, LET'S SEE IF YOU'RE WILLING TO DISCOVER MORE. \
              \n\nWHILE YOU UNMASK EVERYTHING THAT HAS YET TO BE REVEALED, I'M SAFE HERE. \
              \n\nWITH MY NEW FRIEND."
                        )

                        time.sleep(2)
                        print("\n>> LETS SEE WHAT YOUR HARDWORK HAS REVEALED")
                        cypher_choice = input("\n[CLICK ENTER TO RECIEVE REWARD]\n")

                        if cypher_choice == "":
                            for i in progressbar(range(100), "  LOADING: ", 50):
                                time.sleep(0.05)  # any code you need
                            print("\n")
                            print(message)
                            print(decypher(message))
                            letters.append(decypher(message))
                            print(
                                f"\nHEALTH : {health}\nPOPULARITY : {popularity}\nUTILITY BELT : {letters}"
                            )

                            time.sleep(4)
                            print("\n\n\tSEE YOU SOON <?>")

                        break

                    elif points == 3 and rounds > 3:
                        print(
                            "\n>> WHEN SHADOW FALLS, TRUTH SHALL RISE. YOU ARE CORRECT"
                        )
                        time.sleep(2)

                        print(
                            "\n>> YOU HAVE COME THIS FAR. \
              \n\nNOW, LET'S SEE IF YOU'RE WILLING TO DISCOVER MORE. \
              \n\nWHILE YOU UNMASK EVERYTHING THAT HAS YET TO BE REVEALED, I'M SAFE HERE. \
              \n\nWITH MY NEW FRIEND."
                        )

                        time.sleep(2)
                        print("\n>> LETS SEE WHAT YOUR HARDWORK HAS REVEALED")
                        cypher_choice = input("\n[CLICK ENTER TO RECIEVE REWARD]\n")

                        if cypher_choice == "":
                            for i in progressbar(range(100), "  LOADING: ", 50):
                                time.sleep(0.05)  # any code you need
                            print("\n")
                            print(message)
                            print(decypher(message))
                            letters.append(decypher(message))
                            print(
                                f"\nHEALTH : {health}\
                            \nPOPULARITY : {popularity}\
                            \nUTILITY BELT : {letters}"
                            )

                            time.sleep(4)
                            print("\n\n\tSEE YOU SOON <?>")

                        break

                else:
                    response_2 = random.choice(wrong)
                    health += -10
                    popularity += -5
                    print(f"\n>> {response_2}")
                    x = wrong.index(response_2)
                    del wrong[x]

                rounds += 1
                time.sleep(2)

    else:
        time.sleep(2)
        print("\n>> LOOKS LIKE YOU ARE NOT UP FOR A CHALLENGE TODAY.")
        time.sleep(2)
        print("\n>> WHAT IS BLACK AND BLUE AND DEAD ALL OVER?")
        time.sleep(2)
        print("\n>> THE BATMAN")
        time.sleep(2)
        print("\n>> BAD MOVE. GOTHAM HAS PERISHED.")
        time.sleep(1)
        print(f"{'<?>': ^150}")
        time.sleep(4)
        clear()
        print("\n\n\t\tGAME OVER <?>")
        time.sleep(2)
        sys.exit("\n\nTHE PROGRAM HAS BEEN TERMINATED")


# second interaction with riddler
def level_2(message):
    global letters, health, popularity
    for i in range(3):  # interface of riddler
        clear()
        time.sleep(1)
        print(f"\033[1m{'<?>': ^100}")
        time.sleep(1)
    # variables to count rounds and points
    rounds = 1
    points = 0

    intro = [
        "THERE YOU ARE. IT SEEMS THAT YOU MET MY FRIEND. READY FOR ROUND TWO? JUST ME AND YOU.\n"
    ]
    riddles = {
        "secret": "The more I'm revealed, the less I exist. what am i?",
        "shadow": "Without a doubt, Gotham's elite live here―between light and dark. what is this?",
        "darkness": "When I fall, I rise. Though I am not human, some say I have a heart. who am i?",
        "son": "From birth to death. From boy to man. All things change, but what is that one thing he will always be? ",
        "confusion": "I am first a fraud or a trick. Or maybe a blend of the two. That's up to your misinterpretation. what am i?",
    }

    correct = [
        "YOU ARE SMARTER THAN I THOUGHT YOU'D BE. TRY THIS NEXT RIDDLE.",
        "YOU ARE CORRECT AGAIN. I AM IMPRESSED",
        "YOU MAY HAVE GOTTEN THIS ONE. BUT ONLY I HAVE ALL THE ANSWERS. HERE'S ANOTHER.",
    ]

    wrong = [
        "YOU ARE CLEARLY NOT AS SMART AS I THOUGHT YOU WERE. WHY DON'T YOU TRY AGAIN",
        "POWER HAS CORRUPTED YOU, AND YOUR ANSWERS. THINK A LITTLE HARDER.",
        "YOU GOT IT WRONG. WHY DON'T YOU TRY AGAIN...",
        "YOU ARE TRYING TO UNMASK THE TRUTH. BUT YOU ARE NOT THERE YET.",
        "HOW WILL GOTHAM BE SAVED WITH ANSWERS LIKE THAT",
        "YOU CAN'T GET THIS THIS ONE, CAN YOU? DON'T WORRY TRY AGAIN.",
    ]

    print(f">> {random.choice(intro)}")
    time.sleep(2)
    start = input("\u001b[32m>> PROCEED [Y/N]\n")
    time.sleep(2)

    if start.lower() == "y":
        open_statement = [
            "READY TO UNCOVER THE TRUTH? LET'S GET STARTED.\n",
            "HERE WE GO. THREE RIGHT ANSWERS AND JUSTICE WILL BE YOUR REWARD.\n",
        ]

        print(f"\n>> {random.choice(open_statement)}")
        time.sleep(3)

        for answer, riddle in riddles.items():
            if rounds == 5 and points < 3:
                time.sleep(2)
                print("\n>> LOOKS LIKE YOU ARE NOT UP FOR A CHALLENGE TODAY.")
                time.sleep(2)
                print("\n>> WHAT IS BLACK AND BLUE AND DEAD ALL OVER?")
                time.sleep(2)
                print("\n>> THE BATMAN")
                time.sleep(2)
                print("\n>> BAD MOVE. GOTHAM HAS PERISHED.")
                time.sleep(1)
                print(f"{'<?>': ^150}")
                time.sleep(4)
                clear()
                print("\n\n\t\tGAME OVER <?>")
                time.sleep(2)
                sys.exit("\n\nTHE PROGRAM HAS BEEN TERMINATED")

            elif points < 4 and rounds < 6:
                print(f"\n>> {riddle.upper()}\n")
                user = input("\u001b[32m")

                time.sleep(3)

                if answer in user.lower():
                    points += 1

                    if points < 3 and rounds < 6:
                        response_1 = random.choice(correct)
                        print(f"\n>> {response_1}")
                        x = correct.index(response_1)
                        popularity += 10
                        del correct[x]

                    elif points == 3 and rounds == 3:
                        print(
                            "\n>> THREE OUT OF THREE. I SEE THAT YOU ARE ONE OF THE SMART ONES..."
                        )

                        time.sleep(2)
                        print(
                            "\n>> NOW THAT YOU HAVE ACHIEVED THE HIGHEST SCORE, HERE'S WHAT YOU ARE LOOKING FOR."
                        )
                        cypher_choice = input("\n[CLICK ENTER TO RECIEVE REWARD]\n")

                        if cypher_choice == "":
                            for i in progressbar(range(100), "  LOADING: ", 50):
                                time.sleep(0.05)  # any code you need
                            print("\n")
                            print(message)
                            print(decypher(message))
                            letters.append(decypher(message))
                            print(
                                f"\nHEALTH : {health}\nPOPULARITY : {popularity}\nUTILITY BELT : {letters}"
                            )

                            time.sleep(4)
                            print("\n\n\tSEE YOU SOON <?>")

                        break

                    elif points == 3 and rounds > 3:
                        print(
                            "\n>> WHEN SHADOW FALLS, TRUTH SHALL RISE. YOU ARE CORRECT"
                        )

                        time.sleep(2)
                        print("\n>> LETS SEE WHAT YOUR HARDWORK HAS REVEALED")
                        cypher_choice = input("\n[CLICK ENTER TO RECIEVE REWARD]\n")

                        if cypher_choice == "":
                            for i in progressbar(range(100), "  LOADING: ", 50):
                                time.sleep(0.05)  # any code you need
                            print("\n")
                            print(message)
                            print(decypher(message))
                            letters.append(decypher(message))
                            print(
                                f"\nHEALTH : {health}\nPOPULARITY : {popularity}\nUTILITY BELT : {letters}"
                            )

                            time.sleep(4)
                            print("\n\n\tSEE YOU SOON <?>")

                        break

                else:
                    response_2 = random.choice(wrong)
                    print(f"\n>> {response_2}")
                    x = wrong.index(response_2)
                    health += -10
                    popularity += -5
                    del wrong[x]

                rounds += 1
                time.sleep(2)

    else:
        time.sleep(2)
        print("\n>> LOOKS LIKE YOU ARE NOT UP FOR A CHALLENGE TODAY.")
        time.sleep(2)
        print("\n>> WHAT IS BLACK AND BLUE AND DEAD ALL OVER?")
        time.sleep(2)
        print("\n>> THE BATMAN")
        time.sleep(2)
        print("\n>> BAD MOVE. GOTHAM HAS PERISHED.")
        time.sleep(1)
        print(f"{'<?>': ^150}")
        time.sleep(4)
        clear()
        print("\n\n\t\tGAME OVER <?>")
        time.sleep(2)
        sys.exit("\n\nTHE PROGRAM HAS BEEN TERMINATED")


# clear screen    # variables to count rounds and points
# third interaction with riddler
def level_3(message):
    global letters, health, popularity
    for i in range(3):  # interface of riddler
        clear()
        time.sleep(1)
        print(f"\033[1m{'<?>': ^100}")
        time.sleep(1)
    # variables to count rounds and points
    rounds = 1
    points = 0

    intro = ["COULDN'T STAY AWAY... READY FOR MORE?\n"]
    riddles = {
        "envelope": "It starts with an 'e' and has only one letter in it. What is it?",
        "mask": "Fear he who hides behind...what?",
        "punchline": "Once you've been set up, it hits you at the end straight on.",
        "joker": "To wit: A wild card in the truest sense.",
    }

    correct = [
        "PRECISELY. NOW LET'S SEE IF YOU HAVE WHAT IT TAKES TO ANSWER ANOTHER",
        "YOU ARE CORRECT. ONTO THE NEXT ONE",
        "YOU MAY HAVE GOTTEN THIS ONE. BUT ONLY I HAVE ALL THE ANSWERS. HERE'S ANOTHER.",
    ]

    wrong = [
        "ARE YOU SURE YOU HAVE WHAT IT TAKES",
        "POWER HAS CORRUPTED YOU, AND YOUR ANSWERS. THINK A LITTLE HARDER.",
        "YOU ARE TRYING TO UNMASK THE TRUTH. BUT YOU ARE NOT THERE YET.",
        "HOW WILL GOTHAM BE SAVED WITH ANSWERS LIKE THAT",
    ]

    print(f">> {random.choice(intro)}")
    time.sleep(2)
    start = input("\u001b[32m>> PROCEED [Y/N]\n")
    time.sleep(2)

    if start.lower() == "y":
        open_statement = [
            "READY TO UNCOVER THE TRUTH? LET'S GET STARTED.\n",
            "\nHERE WE GO. THREE RIGHT ANSWERS AND JUSTICE WILL BE YOUR REWARD.\n",
        ]

        print(f">> {random.choice(open_statement)}")
        time.sleep(3)

        for answer, riddle in riddles.items():
            if points < 4:
                print(f"\n>> {riddle.upper()}\n")
                user = input("\u001b[32m")

                time.sleep(3)

                if answer in user.lower():
                    points += 1

                    if points < 3:
                        response_1 = random.choice(correct)
                        print(f"\n>> {response_1}")
                        x = correct.index(response_1)
                        popularity += 10
                        del correct[x]

                    elif points == 3 and rounds == 3:
                        print(
                            "\n>> THREE OUT OF THREE. I SEE THAT YOU ARE ONE OF THE SMART ONES..."
                        )

                        time.sleep(2)
                        print("\n>> LETS SEE WHAT YOUR HARDWORK HAS REVEALED")
                        cypher_choice = input("[CLICK RECIEVE REWARD]\n")
                        if cypher_choice == "":
                            print(decypher(message))
                            letters.append(decypher(message))
                            print(
                                f"\nHEALTH : {health}\nPOPULARITY : {popularity}\nUTILITY BELT : {letters}"
                            )

                            time.sleep(4)
                            print("\n\n\tSEE YOU SOON <?>")
                            time.sleep(4)

                        break

                    elif points == 3 and rounds > 3:
                        print(
                            "\n>> WHEN SHADOW FALLS, TRUTH SHALL RISE. YOU ARE CORRECT"
                        )
                        time.sleep(2)

                        print("\n>> LETS SEE WHAT YOUR HARDWORK HAS REVEALED")
                        cypher_choice = input("[CLICK RECIEVE REWARD]\n")
                        if cypher_choice == "":
                            print(decypher(message))
                            letters.append(decypher(message))
                            print(
                                f"\nHEALTH : {health}\nPOPULARITY : {popularity}\nUTILITY BELT : {letters}"
                            )

                            time.sleep(4)
                            print("\n\n\tSEE YOU SOON <?>")
                            time.sleep(4)

                elif points < 3 and rounds == 4:
                    print(
                        ">> YOU ARE NOT ABLE TO SAVE GOTHAM. NOW SEE WHAT'S ABOUT TO HAPPEN."
                    )
                    time.sleep(2)
                    print(">> what is black and blue and dead all over?".upper())
                    time.sleep(2)
                    print(">> YOU!")
                    time.sleep(4)
                    exit()
                else:
                    response_2 = random.choice(wrong)
                    print(f"\n>> {response_2}")
                    x = wrong.index(response_2)
                    health += -10
                    popularity += -5
                    del wrong[x]

                rounds += 1
                time.sleep(2)

            else:
                time.sleep(2)
                print("\n>> LOOKS LIKE YOU ARE NOT UP FOR A CHALLENGE TODAY.")
                time.sleep(2)
                print("\n>> WHAT IS BLACK AND BLUE AND DEAD ALL OVER?")
                time.sleep(2)
                print("\n>> THE BATMAN")
                time.sleep(2)
                print("\n>> BAD MOVE. GOTHAM HAS PERISHED.")
                time.sleep(1)
                print(f"{'<?>': ^150}")
                time.sleep(4)
                clear()
                print("\n\n\t\tGAME OVER <?>")
                sys.exit("\n\nTHE PROGRAM HAS BEEN TERMINATED")

    else:
        time.sleep(2)
        print("\n>> LOOKS LIKE YOU ARE NOT UP FOR A CHALLENGE TODAY.")
        time.sleep(2)
        print("\n>> WHAT IS BLACK AND BLUE AND DEAD ALL OVER?")
        time.sleep(2)
        print("\n>> THE BATMAN")
        time.sleep(2)
        print("\n>> BAD MOVE. GOTHAM HAS PERISHED.")
        time.sleep(1)
        print(f"{'<?>': ^150}")
        time.sleep(4)
        clear()
        print("\n\n\t\tGAME OVER <?>")
        sys.exit("\n\nTHE PROGRAM HAS BEEN TERMINATED")


# library
def level_5():
    global letters, health, popularity
    # library interaction
    print("\u001b[31m \033[1m")
    clear()
    print("\n(CHAOS OUTSIDE THE LIBRARY...A POLICE OFFICER APPROACHES YOU...)\n")
    time.sleep(3)
    interact = input("\nINTERACT WITH OFFICER [Y/N]")
    clear()

    if interact.lower() == "y":
        print(
            "\nBATMAN! GOTHAM ACADEMY STUDENTS WERE ON A FEILD TRIP TO THE LIBRARY.....\n"
        )

        time.sleep(2)
        print(
            "\nTHEY ARE TRAPPED INSIDE WITH OTHER PEOPLE. THERE'S A DETONATOR CONNECTED TO ALL DOORS.\n"
        )

        time.sleep(2)
        print(
            "\nBUT THERE IS A FOUR-DIGIT COMBINATION TO DEACTIVATE THE DETONATORS AT THE DOORS"
        )

        time.sleep(2)
        code_lib = input(
            f"\nTO DEACTIVATE THE DETONATORS, YOU HAVE TO DERIVE THE FOUR DIGITS FROM THE EQUATIONS THAT YOU COLLECTED FROM THE RIDDLER\
            \nEQUATION 1: {letters[0]} \nEQUATION 2: {letters[2]}\n\
  \n"
        )
        # to check if the code is correct
        if int(code_lib) == 4114:
            print(
                "\nYOU SUCCESSFULLY DEACTIVATED THE DETONATORS. THE CHILDREN ARE SAFE.\n"
            )
            popularity += 20
            print(
                f"HEALTH : {health}\
            \nPOPULARITY : {popularity}\
            \nITEMS : {letters}"
            )
            # if player loses
            time.sleep(3)
            print("\nONE OF THE CHILDREN HANDS YOU AN ENVELOPE...")
        else:
            print("\nTHE BATMAN IS BAD AT MATH. GAME OVER")
            exit()
    else:
        print("\nDWELED TO LONG. YOU LOSE.")
        exit()


# orphanage
def level_6():
    global letters, health, popularity
    # orphanage interaction
    print("\u001b[31m \033[1m")
    clear()
    # interaction with riddler in the orphanage
    print("\n(YOU ARRIVED AT THE ORPHANAGE... FORMERLY KNOWN AS WAYNE MANOR.)\n")
    time.sleep(3)
    print(
        "\nTHERE IS NOBODY AROUND... IT IS DARK... YOU SEE A FAMILIAR DIM GREEN FLASHING LIGHT COMING FROM ROOM.\n"
    )

    time.sleep(2)
    print("\nYOU GO TO IT... IT IS A COMPUTER WITH THE RIDDLER'S INTERFACE\n")

    # start to interact
    go_in = input("\nINTERACT [Y/N] \n")
    clear()

    if go_in.lower() == "y":
        print("\u001b[32m \033[1m")  # green text
        for i in range(3):  # interface of riddler
            clear()
            time.sleep(1)
            print(f"\033[1m{'<?>': ^100}")
            time.sleep(1)

        time.sleep(2)
        print(
            ">> WELL DONE BATMAN. YOU HAVE MANAGED TO SAVE ALL THOSE PEOPLE\
            \n\n>> YOU HAVE COME TO THE END OF THIS GAME, BUT SOME GAMES NEVER END.\
            \n"
        )

        time.sleep(2)
        print(
            ">> I HAVE A BONUS REWARD FOR YOU FOR COMING THIS FAR...\
            \n"
        )
        # start the interaction
        open_image = input("[CLICK ENTER]")
        if open_image == "":
            for i in progressbar(range(100), "  LOADING ", 50):
                time.sleep(0.05)  # any code you need
            time.sleep(2)
            print("A wildcard in the truest sense. ha ha ha ".upper())
            time.sleep(4)
            clear()

            # inform of ANSI Escape codes
            output = climage.convert("Joker.png", is_unicode=True)

            # prints output on console.
            print(output)


clear()
# start game from here

print("\u001b[31m \033[1m")
print(
    f"\n\n{'THERE IS NO SHAME IN CHEATING IF YOU ADMIT YOU CANNOT SOLVE MY CHALLENGES':^100}\n\n"
)
game = input(f"{'[WANT TO PLAY? Y/N]':^100}\n")
clear()

while game.lower() == "y":

    # Secret messages to batman.

    messages = [
        "æ†§ ¡∞¶≈ß'¢ ≈##∑œ§ ∑¢ ß§@",
        "æ†§ «≈æ†∞¡ œ∑æ¶ %*π$∑œ $∑πß∞ß¶",
        "æ†§ «≈æ†∞¡ ≈ß%†∞&∞«§",
    ]
    health = 100
    popularity = 30
    letters = []
    # Red and bold all texts
    print("\u001b[31m \033[1m")

    ####################################################### level one begins here #######################################################

    # email to batman
    print(
        "HELLO BATMAN,\
    \n\nGOTHAM CITY IS IN DANGER. THE RIDDLER HAS SET OUT TO TERRORIZE THE CITY.\
    \nHE WILL ONLY NEGOTIATE WITH YOU. WE FOUND THIS LETTER ADDRESSED TO YOU.\
    \nIT CONTAINS A CYPHER. WE HOPE THAT YOU CAN HELP US DECODE THAT.\
    \n\nEVEN THOUGH I HAVE ABSOLUTE CONFIDENCE IN YOU, WE KNOW THAT GOTHAM CITY PD HAS IT'S RESERVATION FROM COLLABORATING WITH A VIGILANTE,\
    \nSO THIS IS A GOOD OPPORTUNITY TO INCREASE THEIR TRUST.\
    \n\nJAMES W. GORDAN SR.\
    \nPOLICE COMMISSIONER OF GOTHAM CITY.\n\n"
    )
    print(f"HEALTH : {health}\nPOPULARITY : {popularity}\nUTILITY BELT : {letters}")

    # attched letter to the batman
    print(f"{'TO THE BATMAN':^100}")

    start_opt = input(f"{'[CLICK ENTER TO OPEN]': ^100}")
    if start_opt == "":
        time.sleep(1)
        clear()
        print(f"{'TO THE BATMAN':^100}")
        print(f"\n\u001b[31m{'YOU ARE EL RATA ALADA': ^100}\u001b[0m")
        print(f"\n\u001b[31m{messages[0]: ^100}")
        print(f"\n\u001b[31m{'10 × 4 - 2 × (4² ÷ 4) ÷ 2 ÷ 1/2 + 9': ^100}")
        letters.append("10 × 4 - 2 × (4² ÷ 4) ÷ 2 ÷ 1/2 + 9")

    start_mission = input(f"\033[1m\n{'[CLICK ENTER TO START MISSION]': ^100}\u001b[0m")
    mayor_office = "b"

    # Green and bold all texts
    print("\u001b[32m \033[1m")  # green text

    while start_mission == "" and mayor_office.lower() == "b":
        print("\u001b[32m \033[1m")  # green text
        if start_mission == "":
            clear()
            time.sleep(2)
            for i in progressbar(range(100), "  HTTPS://WWW.RATAALADA.COM ", 50):
                time.sleep(0.05)

            level_1(messages[0])  # calling for level 1

        time.sleep(5)

        ########## found the mayor ###########
        clear()
        print("\u001b[31m \033[1m")
        mayor_office = input(
            "\n[CLICK ENTER TO GO TO MAYOR'S OFFICE OR TYPE B TO GO BACK]\n\n"
        )
        ####################################################### level two begins here #######################################################
    if mayor_office == "":

        # interaction at mayors office
        print("\u001b[31m \033[1m")
        clear()
        print("\n(MUFFLING SOUNDS...FROM INSIDE THE LOCKED MAYOR'S OFFICE)\n")
        time.sleep(3)
        break_door = input("BREAK DOWN DOOR? [Y/N]")
        clear()
        if break_door.lower() == "y":
            print(
                "\nYOU SEE THE MAYOR TAPED AND HANDCUFFED TO A CHAIR. AND THERE'S A BOMB STRAPPED TO IT.....\n"
            )
            time.sleep(2)
            red_wire = input(
                "\nTO STOP THE BOMB FROM EXPLODING YOU NEED TO CUT ONE OF THE THREE WIRES; RED, GREEN OR BLUE\
      \nSELECT ONE [R/G/B]\
      \n"
            )
            if red_wire.lower() == "r" or red_wire.lower() == "red":
                print("\nYOU SUCCESSFULLY DIFFUSED THE BOMB. THE MAYOR IS SAFE.")
                popularity += 5
                print(
                    f"\nHEALTH : {health}\
                \nPOPULARITY : {popularity}\
                \nUTILITY BELT : {letters}"
                )
                time.sleep(3)
                print(
                    "\nTHERE IS A RED FIREPROOF ENVELOPE STUCK ON THE MAYOR'S CHEST ADDRESSED TO THE BATMAN..."
                )
                time.sleep(2)

                # Red and bold all texts
                print("\u001b[31m \033[1m")
                print(f"\n\n{'TO THE BATMAN':^100}")

                # next letter to batman

                start_opt = input(f"\n{'[CLICK ENTER TO OPEN]': ^100}")
                if start_opt == "":

                
                    time.sleep(1)
                    clear()
                    print(f"{'TO THE BATMAN':^100}")
                    print(
                        f"\n\u001b[31m{'WHAT BUILDING HAS THE MOST STORIES?': ^100}\u001b[0m"
                    )
                    print(f"\n\u001b[31m{messages[1]: ^100}")
                    print(f"\n\u001b[31m{'10 ÷ (20 ÷ 2² × 5 ÷ 5) × 8 - 2': ^100}")
                    letters.append("10 ÷ (20 ÷ 2² × 5 ÷ 5) × 8 - 2")

                start_mission = input(
                    f"\033[1m\n{'[CLICK ENTER TO START MISSION]': ^100}\u001b[0m"
                )

                print("\u001b[32m \033[1m")  # green text
                if start_mission == "":
                    clear()
                    for i in progressbar(
                        range(100), "  HTTPS://WWW.RATAALADA.COM ", 50
                    ):
                        time.sleep(0.05)  # any code you need
                    clear()
                    level_2(messages[1])  # calling for level 2

            else:
                print("WRONG CHOICE. THE BOMB DETONATED. GAME OVER.")
                exit()
        else:
            print("DWELED TO LONG. YOU LOSE.")
            exit()

        time.sleep(5)

        ########## found the library ###########
    clear()
    print("\u001b[31m \033[1m")
    library = input("[CLICK ENTER TO GO TO CITY LIBRARY]\n\n")

    ####################################################### level three begins here #######################################################

    # interaction at the library
    if library == "":
        level_5()

    # Red and bold all texts
    time.sleep(4)
    clear()

    print("\u001b[31m \033[1m")
    print(f"\n\n{'TO THE BATMAN':^100}")

    # batmans next letter
    start_opt = input(f"\n{'[CLICK ENTER TO OPEN]': ^100}")
    if start_opt == "":
        time.sleep(1)
        clear()
        print(f"{'TO THE BATMAN':^100}")
        print(
            f"\n\u001b[31m{'I GREW UP AS A SEED, AS TOUGH AS A WEED. BUT IN A MANSION, IN A SLUM, I WILL NEVER KNOW WHERE I COME FROM': ^100}\u001b[0m"
        )
        print(f"\n\u001b[31m{messages[2]: ^100}")

    start_mission = input(f"\033[1m\n{'[CLICK ENTER TO START MISSION]': ^100}\u001b[0m")

    print("\u001b[32m \033[1m")  # green text
    if start_mission == "":
        clear()
        for i in progressbar(range(100), "  HTTPS://WWW.RATAALADA.COM ", 50):
            time.sleep(0.05)  # any code you need
        clear()
        level_3(messages[2])
    print("\u001b[31m \033[1m")
    clear()
    orphanage = input("\n[CLICK ENTER TO GO TO THE ORPHANAGE]")

    # interaction at orphange
    if orphanage == "":
        level_6()

    time.sleep(10)
    clear()
    print(
        f"\u001b[31m \033[1m\n\n{'THERE IS NO SHAME IN CHEATING IF YOU ADMIT YOU CANNOT SOLVE MY CHALLENGES':^100}\n\n"
    )
    game = input(f"{'[WANT TO PLAY? Y/N]':^100}")
    clear()
