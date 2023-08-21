import tkinter
from tkinter import *
import random


# --------------------------------------------------
# GAME BACKEND


def choice1():
    start_game("rock")


def choice2():
    start_game("scissors")


def choice3():
    start_game("paper")


def exit_game():
    window.quit()


def repeat_game():
    gameWindow.destroy()


def end_game(winner, player_choice, pc_choice):
    global gameWindow

    gameWindow = Toplevel(window)
    gameWindow.geometry("600x200")
    gameWindow.resizable(width=False, height=False)
    gameWindow.title("Rock Paper Scissors")
    gameWindow.iconphoto(False, tkinter.PhotoImage(file=".\\media\\main_Icon.png"))

    goodbye_label1 = Label(gameWindow,
                           font=("Arial", 20),
                           text="Game over!")
    goodbye_label1.pack(side=TOP)

    end_label = Label(gameWindow)
    if winner == "Draw":
        end_label.config(font=("Arial", 15),
                         text="It's draw, because computer and you chose " + player_choice)
        end_label.pack()
    elif winner == "Player":
        end_label.config(font=("Arial", 15),
                         text="You won, because computer chose " + pc_choice +
                              ", \n and you chose " + player_choice)
        end_label.pack()
    else:
        end_label.config(font=("Arial", 15),
                         text="You lost, because computer chose" + pc_choice +
                              ", \n but you chose " + player_choice)
        end_label.pack()

    goodbye_label2 = Label(gameWindow,
                           font=("Arial", 20),
                           text="Wanna try again?")
    goodbye_label2.pack()

    repeat_button = Button(gameWindow,
                           font=("Arial", 20),
                           text="Again",
                           command=repeat_game)
    repeat_button.place(x=100, y=130)

    exit_button = Button(gameWindow,
                         font=("Arial", 20),
                         text="Quit game",
                         command=exit_game)
    exit_button.place(x=400, y=130)


def start_game(player_choice):
    pc_choice = random.choice(["rock", "scissors", "paper"])
    winner = None
    if player_choice == pc_choice:
        winner = "Draw"
    elif player_choice == "rock":
        if pc_choice == "scissors":
            winner = "Player"
        else:
            winner = "Computer"
    elif player_choice == "scissors":
        if pc_choice == "paper":
            winner = "Player"
        else:
            winner = "Computer"
    elif player_choice == "paper":
        if pc_choice == "rock":
            winner = "Player"
        else:
            winner = "Computer"
    end_game(winner, player_choice, pc_choice)


# --------------------------------------------------
# window main settings   #GUI BLOCK


window = Tk()
window.geometry("600x200")
window.resizable(width=False, height=False)
window.title("Rock Paper Scissors")
window.iconphoto(False, tkinter.PhotoImage(file=".\\media\\main_Icon.png"))

# --------------------------------------------------
# GAME FRONTEND

HelloLabel = Label(window,
                   text="Hello, choose your item",
                   font=("Arial", 20))
HelloLabel.pack()

Button1 = Button(window,
                 text="rock",
                 font=("Arial", 25),
                 command=choice1)
Button1.place(x=40, y=100)

Button2 = Button(window,
                 text="scissors",
                 font=("Arial", 25),
                 command=choice2)
Button2.place(x=215, y=100)

Button3 = Button(window,
                 text="paper",
                 font=("Arial", 25),
                 command=choice3)
Button3.place(x=420, y=100)

window.mainloop()
# --------------------------------------------------
