# Name: Venus Chandra
# UPI: vcha997
import turtle, tkinter as tk, random, sys
from tkinter import *
from turtle import *
def spiral_graphics(event):
    screen = turtle.Screen()
    screen.bgcolor('black')
    screen.title("Let's play!")
    index = 0
    turtle.forward(30)
    edge_index_list = [273, 260, 291, 290]
    colors = ['#FF3030', '#FF8000', '#FFFF00', '#00FF00', '#03A89E',
              '#AB82FF']
    for i in range(298):
        if index == 6:
            index = 0
        turtle.speed("fastest")
        turtle.pencolor(colors[index])
        if i == 297:
            turtle.forward(i)
            turtle.forward(50)
        if i != 297:
            turtle.forward(i)
            turtle.right(75)
        if i > 272 and i < 297:
            index2 = 0
            for number in range(4):
                if index2 == 6:
                    index2 = 0
                pensize(4)
                turtle.pencolor(colors[index])
                turtle.speed("fastest")
                turtle.forward(30)
                turtle.left(90)
                index2 += 1
            pensize(0)
        index += 1
    turtle.color('#00FF7F')
    style = ('Courier', 30, 'italic')
    turtle.write('Welcome to Solitaire!', font = style, align = 'center')
    turtle.hideturtle()
    turtle.done()
    


def display_rules(event):
    window.destroy()
    window1 = tk.Tk()
    window1.title('Overview & Rules')
    var = StringVar()
    window1['background'] = "black"
    rules = Message(window1, textvariable=var, relief=RIDGE,
                    font = ("Courier", 14),
                    cursor = "arrow", width = 1000, bg = "black",
                    fg = "green", justify = 'center')
    
    var.set("Overview Of Solitaire:\n\n ⁍ The aim of the game is to \
arrange the cards in a pile in descending order numerically (i.e no suits \
(♠️♥♣️♦️️) are used). The first card in a pile (excluding pile 0) is the \
highest number and the card after that will be 1 less than the first card \
and so on. Inorder to win, you will need to arrange all cards in decreasing \
order within the number of rounds generated. But there is a twist! \
(」°ロ°)」. For every fourth round, you will have to guess a number between 1 \
and 2, as the program randomly generates a number between 1 and 2. If you \
guess incorrectly, you will lose that round, reducing the chances of you \
winning. Are you up for the challenge? \n\nHere Are The Rules:\n\n♣ The \
first pile (pile 0) will contain all of the cards that will be required \
to be arranged. You will only be able to see the first card on top of pile \
0 and the rest will be hidden with an asteric (*). You will be able to see \
cards in other piles \n♣ You can fill an empty pile with any card. You can \
move a pile to another pile as long as it's in descending order, except \
for pile 0, it can not be moved nor used to sort the cards \
\n♣ You can move a card to any of the piles but (1) the moving card must \
be from the top of pile 0 and (2) whichever pile you decide the moving \
card will go into must be one less than the last card on the desired pile \
\n♣ If you don't want to put the first card of pile 0 into the other \
piles, you can move that card to the back of pile 0 which is an option \
given by the prompt. Hence, you will be able to see the next card in \
pile 0 however, it will still take up a round \n♣ Last but not least, \
you must have fun! ＼(^o^)／\n\n\
⠘ ⢿⣿⣆⠀⠀⠀⠀⢀⣴⣿⡿⠃⠀⠀⢀⣾⣿⣿⣦⠀⠀⠀⠘⢿⣿⣦⡀⠀⠀⠀⠀⣴⣿⡟⠀⠀⠀⠀⣿⣿\n\
 ⣠⠤ ⠹⣿⣷⡄⠀⣠⣿⡿⠋⠀⠀⠀⢠⣿⡿⠋⠻⣿⣷⡀⠀⠀⠀⠹⣿⣷⣄⠀⣠⣾⡿⠋⠀⠀⠀⠀⠀⣿⣿⠇\n\
⡞⣠⠌⠩⠑⣻⣦⠀⠀⠀⠀⠈⠿⣿⣾⣿⠟⠁⠀⠀⠀⣠⣿⡿⠁⠀⠀⠹⣿⣷⡄⠀⠀⠀⠈⢻⣿⣷⣿⠟⠀⠀⠀⠀⠀⠀⠀⣿⣿⠀⣐⡒⠄⠀⠀⠸\n\
⢻⡳⢻⣟⠢⢤⣹⠆⠀⠀⠀⠀⠀⢹⣿⡇⠀⠀⠀⠀⣰⣿⡿⠿⠿⠿⠿⠿⠿⣿⣿⣄⠀⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠀⠿⠿⢿⣡⠤⢒⣂⠀⡼\n\
⠙⣼⡜⠳⠿⠁⠀⠀⠀⠀⠀⠀⠀⢼⣿⡇⠀⠀⠀⣼⣿⠟⠀⠀⠀⠀⠀⠀⠀⠈⢿⣿⣦⠀⠀⠀⣿⣿⡇⠀⠀⠀⠀⠀⠀⠀⠰⣶⣷⡎⠳⠶⠋⣼⡞⠁\n\
⠸⠿⢀⣀⣀⠀⠀⠀⠀⠀⠠⢴⠂⠲⣒⠒⠒⠲⠶⢀⣈⣁⠩⠿⠿⠿⠿⠋⠉⠉⠉⠫⠉⣁⣀⡀⠶⠒⠒⠒⣲⠶⢦⠤⠤⠤⠠⠄⠀⠀⣀⡀⠸⠏⠀⠀\n\
⠈⢯⠷⡄⠀⠀⠀⠀⠀⠀⠈⢧⠀⢈⣳⡤⠖⠊⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠒⠤⣶⣍⡀⢀⡞⠁⠀⠀⠀⠀⠀⠀⡴⢽⠇⠀⠀\n\
⠀⠈⠳⡈⢢⡀⠀⠀⠀⠀⠀⣨⣟⣹⣏⣀⣀⣀⣀⣀⣀⣀⣀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣀⣀⣀⣀⣀⣯⣍⣛⢄⠀⠀⣀⠀⢀⣠⢊⣴⠃⠀⠀⠀⠀\n\
⣴⠭⠁⠈⠀⣠⢔⡲⠛⠋⠉⠁⠀⠀⠀⠀⠀⠀⠀⠀⠈⠙⡆⠀⠀⠀⣖⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠉⠉⠑⠻⢖⡢⣌⠉⠀⠉⠑⡆⠀⠀⠀⠀\n\
⠈⠹⢶⣄⠈⣿⣾⣤⣤⣀⣀⣀⣀⣀⣀⡀⣀⣤⣤⠤⣤⣴⣷⠛⠉⢷⣿⣦⣤⣤⣤⣤⣄⣀⣀⣀⣀⣀⣀⣀⣠⣤⣷⣿⢀⡠⠖⠋⠀⠀⠀⠀⠀\n\
    ⠉⠻⣿⣿⣭⣅⣀⣤⣤⣤⣤⣀⣁⣥⣴⣾⣿⠟⠁⠀⠀⠀⠙⠿⣿⣿⣿⣿⣏⣭⣥⢨⣤⣤⣀⢀⣤⣼⣿⠟⠁⠀⠀⠀⠀⠀⠀⠀\n\
    ⠀⣀⠔⣇⢹⣿⠿⡿⠛⠛⣛⣛⣛⣉⡉⠉⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⣉⣛⣛⣛⠛⠛⢿⠿⣿⡿⣸⠐⠢⣄⠀⠀⠀⠀⠀⠀⠀\n\
   ⠀⠊⠀⠀⠸⡌⢯⢲⢵⡀⠀⢻⠀⠀⠀⠀⢹⠉⠉⠉⠉⠉⠩⠉⠉⠉⠉⠉⡏⠀⠀⠀⠀⡇⠀⢀⡮⣔⡿⢁⠃⣀⠀⠀⠙⣦⠀⠀⠀⠀⠀\n\
   ⠦⢤⡤⠤⠀⣹⣦⣿⣦⡈⣿⠘⠓⢤⠤⠄⢸⣄⡀⠀⠀⠀⠀⠀⠀⠀⠀⣀⡅⠠⠤⡤⠚⠃⣸⢁⣴⢿⠷⠦⠐⠒⠒⠃⠂⠉⠀⠀⠀⠀⠀\n\
           ⠈⣿⠛⠻⠦⠄⢸⣄⠀⠀⠈⡆⠀⠀⠀⠀⠀⠀⠀⢰⠁⠀⢀⣰⣁⠠⠴⠛⠉⠘⢇⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
            ⡏⠀⠀⢑⡶⠤⣄⣭⣙⣉⣉⠒⠒⠒⠒⠒⠒⠒⠋⢉⣉⣩⣤⡤⠒⠛⠢⡀⠀⠸⡆⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀\n\
            ⢧⣀⣐⡥⠴⠒⠈⠁⠀⠈⠹⣿⡉⠉⠁⠀⠀⣼⠋⠁⠀⠀⠀⠈⠉⠒⠶⠬⠵⠴⠃")
    button = tk.Button(text = "Click here to proceed\nwith the game (｡◕‿◕｡)",
                   width = 20, height = 10,
                   bg = "black", fg = "green", relief = SUNKEN)
    button.bind("<Button-1>", spiral_graphics)
    rules.pack()
    button.pack()
    window1.mainloop()
    
window = tk.Tk()
window['background'] = "black"
frame_a = tk.Frame()
frame_b = tk.Frame()
greeting = tk.Label(master = frame_a, relief = SUNKEN,
                    text= "Would you like to play Solitare?", fg = "green",
                    bg = 'black', font = "italic")
button = tk.Button(master = frame_b, text = "Click here to continue (｡◕‿◕｡)",   
                   width = 40, height = 20,
                   bg = "black", fg = "green", relief = RAISED)
button.bind("<Button-1>", display_rules)
greeting.pack()
frame_a.pack()
frame_b.pack()
button.pack()
window.title('Hello there!')
window.geometry("300x200+10+20")
window.mainloop()

def win_print():
    print("🎉 YOU WON WELL DONE! 🎉")
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠿⠟⢛⣛⣛⣛⣛⣛⣛⠻⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\
⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⢛⣉⣥⣴⠶⠾⠟⣋⣉⣩⣹⣿⣿⣻⡿⠷⠶⣶⣬⣍⡛⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠟⢉⣤⡶⠟⣉⣡⣶⣶⣿⣿⣿⠿⠛⠛⠛⠿⠿⣿⣿⣶⣶⣭⣉⠻⢷⣦⣍⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣤⡶⠛⢩⣶⣾⣿⣿⣿⣿⣿⡇⢀⣀⣀⣀⣀⡀⠀⠠⠙⠻⣿⣿⣿⣿⣶⣌⠻⣷⣬⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⡿⠋⣀⠞⠀⠐⠘⢘⣿⣿⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣿⣷⣦⣄⣸⣿⣿⣿⣿⣿⣷⣬⡛⢿⣦⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⠟⠠⠂⠀⣀⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⡂⠻⣿⣄⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⠃⣰⠀⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⢿⣿⣦⡈⢿⣧⠘⣿⣩⣍⠻⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⠃⣤⠅⢠⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⠉⠙⠻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢹⣿⣿⣆⠻⣷⠈⣿⣿⣷⠹⣿⣿⡿⠿⢿⣿\n\
⣿⣿⠇⣴⣿⢰⣿⣿⣿⡟⠛⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⠀⠀⠀⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣆⢹⣿⣿⣆⠙⣇⢸⣿⣿⡄⣿⣿⢰⣴⡌⢿\n\
⣿⡟⢰⣿⡏⣿⣿⣿⠏⠀⠀⠀⠈⢿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⢻⣿⣿⣦⠙⠀⣿⣿⡇⢿⡏⣾⣿⡇⢸\n\
⣿⠃⣾⣿⣿⣿⣿⣿⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣧⠀⠈⡇⠀⠀⢠⣿⣿⣿⣿⣿⣿⣿⣿⠟⢛⣛⣛⡛⠻⠷⡈⢿⣿⣿⡆⠀⣿⣿⡇⣾⡇⣿⣿⠇⣾\n\
⡏⢠⣿⣿⣿⣿⣿⣿⣆⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣿⣧⠀⠀⠀⢀⣾⣿⣿⣿⣿⣿⣿⢁⣴⣿⣿⣿⣿⣿⣿⣷⡆⢸⣿⣿⡇⠀⣿⣿⡇⣿⠀⣿⡿⢸⣿\n\
⡇⢸⣿⣿⣿⣿⣿⣿⣿⣄⠀⢀⣰⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣾⣿⣿⣿⣿⣿⣿⡿⠷⠈⠻⠿⠿⠿⠿⠿⢿⣿⣿⣾⣿⣿⣧⣤⡿⣿⠁⠏⣾⣿⠃⣼⣿\n\
⡇⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡏⢰⣾⣷⡄⢠⣴⣶⣶⣦⡀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣀⣠⣿⡿⢰⣿⣿\n\
⣇⠘⣿⣻⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⠀⠘⣿⣿⣿⡌⢻⣿⣿⣿⣿⡆⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣿⣿⣿\n\
⣿⡄⣿⣿⣿⣿⡏⠀⠙⠛⠛⠻⠿⠿⠿⠿⠿⠿⠿⠛⠛⠛⢛⣛⣉⣥⣤⣴⣶⣾⣿⠃⡀⢿⣿⣿⣷⡘⢿⣿⡿⠛⣡⣼⣿⣿⣿⣿⣿⣿⣿⣿⣿⡟⣸⣿⣿⣿\n\
⣿⣧⠘⣿⣿⣿⡇⢇⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠚⠉⢀⡇⠘⢿⣿⣿⣿⣶⣶⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢁⣿⣿⣿⣿\n\
⣿⣿⡄⢸⣿⣿⣷⡈⡄⠈⠙⠛⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠛⠋⠉⠁⠀⠀⠀⢀⣾⣿⣄⠈⢻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠃⣾⣿⣿⣿⣿\n\
⣿⣿⣿⡀⠻⣿⣿⣷⡈⢆⠀⢠⠠⠶⣶⣶⣶⣶⣶⣶⣶⣶⣶⡾⠞⠓⠁⠀⠀⢠⣾⣿⣿⣿⣧⠀⠹⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠁⣴⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⡄⠻⣿⣿⣿⣦⡳⢄⠀⠠⣄⣈⣀⣉⣉⣉⣉⣩⣥⣴⣶⣶⠞⢁⣴⣿⣿⣿⣿⣿⣿⣷⣄⠈⠙⠿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣀⣾⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣦⠙⢿⣿⣿⣿⣮⣝⣦⣬⣙⠛⠻⠿⠿⠿⠟⠛⢋⣩⣴⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣦⣄⠀⠈⠉⠉⠀⣠⣤⣤⣶⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣷⣄⠛⣿⣿⣿⣿⣿⣿⣾⣿⣿⣿⣿⣿⣭⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡷⠂⢠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣷⣄⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣠⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣤⣉⠛⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠿⠛⣉⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣬⣉⡙⠿⠿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠿⠛⠋⣉⣤⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⣶⣶⣤⣭⣭⣭⣭⣭⣭⣬⣴⣶⣶⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿")
    sys.exit()
    
def lose_print():
    print("⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠟⢉⣤⣤⡙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠋⣴⣿⣿⣿⣷⠘⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⡿⠟⣋⣡⣤⣶⣶⣶⣶⣶⣶⣤⣭⣁⡛⠿⣿⠿⠟⠛⠻⢿⣿⣿⣿\n\
⣿⣿⣿⠟⢉⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣤⡒⢿⣿⣷⠈⣿⣿⣿\n\
⣿⣿⢋⣴⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣦⡙⡿⢠⣿⣿⣿\n\
⣿⠁⣾⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣷⡄⢺⣿⣿⣿\n\
⡇⣸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡄⠻⠿⣿\n\
⠁⣿⣿⠟⠛⠛⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠛⠛⠻⣿⣿⣿⣿⣿⣿⣇⢸⣶⠈\n\
⠀⣿⣏⠀⠀⠀⢨⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⠘⢋⣴\n\
⠀⣿⣿⡇⣤⡔⣿⣿⡟⣋⣭⣍⢻⣿⣿⣿⣿⢢⣤⡞⣿⣿⣿⣿⣿⣿⡏⢰⣿⣿\n\
⡇⢻⣿⡇⢿⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⢸⣿⡇⣿⣿⣿⣿⣿⣿⢃⠻⣿⣿\n\
⣿⡌⢻⣿⢸⡇⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡆⣿⡇⣿⣿⣿⣿⡿⢃⣾⡇⢸⣿\n\
⣿⣿⣦⡙⠈⢷⢸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⣿⣷⢸⣿⠿⢋⣠⣭⣥⣴⣿⣿\n\
⣿⣿⣿⣿⣷⣤⣁⡛⠛⠿⠿⢿⣿⣿⣿⣿⠿⠷⠸⢛⠈⣥⣶⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⠏⣸⣿⣖⠶⣶⣶⣶⠖⣲⣾⣿⡈⠠⣿⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⢠⣯⣙⣛⣃⣽⣿⣇⣚⣛⣫⣽⣧⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⠇⠘⢠⣌⣭⢻⣿⣿⣿⢫⣍⣥⠘⠿⠀⣀⣈⠉⢹⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣄⠻⡿⣿⣿⢨⣿⣿⣿⢸⣻⡟⣿⠃⣠⣿⡿⠗⣸⣿⣿⣿⣿⣿\n\
⣿⣿⣿⣿⣿⣿⣿⣦⡉⣓⣋⡘⠛⠛⠛⠂⠓⢚⣡⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿")
    sys.exit()
    

class Solitaire:
    def __init__(self, cards):
        self.piles = []
        self.num_cards = len(cards)
        self.num_piles = (self.num_cards // 8) + 3
        self.max_num_moves = self.num_cards * 2
        for i in range(self.num_piles):
            self.piles.append(CardPile())
        for i in range(self.num_cards):
            self.piles[0].add_bottom(cards[i])
            
    def get_pile(self, i):
        return self.piles[i]

    def display(self):
        for i in range(0, self.num_piles):
            if self.piles[i].items != []:
                print(str(i) + ":", end = " ")
                self.piles[i].print_all(i)
            else:
                print(str(i) + ":")

    def move(self, p1, p2):
        if p1 == 0 and p2 == 0 and self.piles[p1].items != []:
            moving_card = self.piles[p1].remove_top()
            self.piles[p1].add_bottom(moving_card)
        elif p1 == 0 and p2 > 0 and self.piles[p1].items != []:
            moving_card = self.piles[p1].items[0]
            if self.piles[p2].items == []:
                self.piles[p1].remove_top()
                self.piles[p2].add_bottom(moving_card)
            else:
                valid_card = self.piles[p2].items[-1] - 1
                if self.piles[p2].items != [] and moving_card == valid_card:
                    self.piles[p1].remove_top()
                    self.piles[p2].add_bottom(moving_card)
        elif (p1 > 0 and p2 > 0 and self.piles[p1].items != [] and
        self.piles[p2].items != []):
            for i in range(len(self.piles[p1].items)):
                moving_card = self.piles[p1].items[0]
                valid_card = self.piles[p2].items[-1] - 1
                if moving_card == valid_card:
                    self.piles[p1].remove_top()
                    self.piles[p2].add_bottom(moving_card)
    
       
    def is_complete(self):
        if self.piles[0].items != []:
            return False
        piles_with_cards = 0
        pile = 0
        for i in range(0, self.num_piles):
            if self.piles[i].items != []:
                piles_with_cards += 1
                pile = i
        if piles_with_cards != 1:
            return False
        previous_card = 100
        for current_card in self.piles[pile].items:
            if current_card < previous_card:
                previous_card = current_card
            elif current_card > previous_card:
                return False
        return True
            
    def play(self):
        print("********************** NEW GAME *****************************") 
        move_number = 1 
        while move_number <= self.max_num_moves and not self.is_complete(): 
            self.display()
            random_number = random.randint(1, 2)
            if move_number % 4 == 0:
                guess = int(input("\nTake a guess - 1 or 2?: "))
            if move_number % 4 == 0 and guess == random_number:
                print("Nice! You guessed correctly! \( ﾟヮﾟ)/")
                print()
                print("Round", move_number, "out of", self.max_num_moves,
                      end = ": ") 
                row1 = int(input("Move from pile no.: "),10) 
                print("Round", move_number, "out of", self.max_num_moves,
                      end = ": ")
                row2 = int(input("Move to pile no.: "),10) 
                if (row1 >= 0 and row2 >= 0 and row1 < self.num_piles and
                    row2 < self.num_piles): 
                    self.move(row1, row2) 
            elif move_number % 4 != 0:
                print("Round", move_number, "out of", self.max_num_moves,
                      end = ": ") 
                row1 = int(input("Move from pile no.: "),10) 
                print("Round", move_number, "out of", self.max_num_moves,
                      end = ": ")
                row2 = int(input("Move to pile no.: "),10) 
                if (row1 >= 0 and row2 >= 0 and row1 < self.num_piles and
                    row2 < self.num_piles): 
                    self.move(row1, row2)
            elif guess != random_number:
                print(f"You've lost round {move_number}. Better luck \
next time! >_<")
                print()
            move_number += 1
        if self.is_complete(): 
            print("You Win in", move_number - 1, "steps!\n")
            win_print()
        else: 
            print("You Lose!\n")
            lose_print()
            

class CardPile:
    def __init__(self):
        self.items = []
        
    def add_top(self, item):
        self.items.insert(0, item)
        
    def add_bottom(self, item):
        self.items.append(item)
        
    def remove_top(self):
        return self.items.pop(0)
        
    def remove_bottom(self):
        return self.items.pop()
        
    def size(self):
        return len(self.items)
    
    def peek_top(self):
        return self.items[0]
    
    def peek_bottom(self):
        return self.items[-1]
    
    def print_all(self, index):
        if index == 0:
            items_to_be_printed = []
            print(self.items[0], end = " ")
            for i in range(1, self.size()):
                items_to_be_printed.append("*")
            print(" ".join(items_to_be_printed))
        else:
            items_to_be_printed = []
            for char in self.items:
                items_to_be_printed.append(str(char))
            print(" ".join(items_to_be_printed))

	
cards = [5, 9, 8, 7, 1, 2, 0, 3, 4, 6]
game = Solitaire(cards)
game.play()	

