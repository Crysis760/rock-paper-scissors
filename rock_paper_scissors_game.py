import tkinter
from tkinter import *
import random


# --------------------------------------------------
# GAME BACKEND


def choice1():
    global player_choice
    player_choice = "Камень"
    start_game()


def choice2():
    global player_choice
    player_choice = "Ножницы"
    start_game()


def choice3():
    global player_choice
    player_choice = "Бумагу"
    start_game()


def exit_game():
    window.quit()


def repeat_game():
    gameWindow.destroy()


def end_game():
    global gameWindow

    gameWindow = Toplevel(window)
    gameWindow.geometry("600x200")
    gameWindow.resizable(width=False, height=False)
    gameWindow.title("Rock Paper Scissors")
    gameWindow.iconphoto(False, tkinter.PhotoImage(file="C:\\Users\\crysis76\\Desktop\\exe py projects\\"
                                                        "rock paper scissors\\main_Icon.png"))

    goodbye_label1 = Label(gameWindow,
                           font=("Arial", 20),
                           text="Игра окончена!")
    goodbye_label1.pack(side=TOP)

    end_label = Label(gameWindow)
    if winner == "Ничья":
        end_label.config(font=("Arial", 15),
                         text="Вы сыграли в ничью, так как компьютер выбрал " + pc_choice +
                              ", \n вы выбрали " + player_choice)
        end_label.pack()
    elif winner == "Игрок":
        end_label.config(font=("Arial", 15),
                         text="Вы победили, так как компьютер выбрал " + pc_choice +
                              ", \n вы выбрали " + player_choice)
        end_label.pack()
    else:
        end_label.config(font=("Arial", 15),
                         text="Вы проиграли, так как компьютер выбрал " + pc_choice +
                              ", \n вы выбрали " + player_choice)
        end_label.pack()

    goodbye_label2 = Label(gameWindow,
                           font=("Arial", 20),
                           text="Хотите сыграть ещё?")
    goodbye_label2.pack()

    repeat_button = Button(gameWindow,
                           font=("Arial", 20),
                           text="Заново",
                           command=repeat_game)
    repeat_button.place(x=100, y=130)

    exit_button = Button(gameWindow,
                         font=("Arial", 20),
                         text="Выйти",
                         command=exit_game)
    exit_button.place(x=400, y=130)


def start_game():
    global winner
    global pc_choice
    pc_choice = random.choice(["Камень", "Ножницы", "Бумагу"])
    if player_choice == "Камень" and pc_choice == "Камень":
        winner = "Ничья"
    elif player_choice == "Камень" and pc_choice == "Ножницы":
        winner = "Игрок"
    elif player_choice == "Камень" and pc_choice == "Бумагу":
        winner = "Компьютер"
    elif player_choice == "Ножницы" and pc_choice == "Ножницы":
        winner = "Ничья"
    elif player_choice == "Ножницы" and pc_choice == "Бумагу":
        winner = "Игрок"
    elif player_choice == "Ножницы" and pc_choice == "Камень":
        winner = "Компьютер"
    elif player_choice == "Бумагу" and pc_choice == "Бумагу":
        winner = "Ничья"
    elif player_choice == "Бумагу" and pc_choice == "Камень":
        winner = "Игрок"
    else:
        winner = "Компьютер"

    end_game()


# --------------------------------------------------
# window main settings   #GUI BLOCK


window = Tk()
window.geometry("600x200")
window.resizable(width=False, height=False)
window.title("Rock Paper Scissors")
window.iconphoto(False, tkinter.PhotoImage(file="C:\\Users\\crysis76\\Desktop\\exe py projects\\"
                                                "rock paper scissors\\main_Icon.png"))

# --------------------------------------------------
# GAME FRONTEND

HelloLabel = Label(window,
                   text="Здравствуйте, для начала игры выберите, \n"
                        "за кого будете играть:",
                   font=("Arial", 20))
HelloLabel.pack()

Button1 = Button(window,
                 text="Камень",
                 font=("Arial", 25),
                 command=choice1)
Button1.place(x=40, y=100)

Button2 = Button(window,
                 text="Ножницы",
                 font=("Arial", 25),
                 command=choice2)
Button2.place(x=215, y=100)

Button3 = Button(window,
                 text="Бумага",
                 font=("Arial", 25),
                 command=choice3)
Button3.place(x=420, y=100)

window.mainloop()
# --------------------------------------------------
