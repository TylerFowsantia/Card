from tkinter import *
from PIL import Image, ImageTk
import random
import math
import os
import xlrd

root = Tk()
root.title('Blackjack')
root.geometry('1200x650')

card_entries = dict()
card_wb = xlrd.open_workbook('Card_Values.xlsx')
sheet = card_wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    card_entries[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)

print(card_entries)
objects = []
counter = 0

bg_img = ImageTk.PhotoImage(file='blackjack_background.png')
card_back_img = Image.open('blue_back.png')
card_back_img = card_back_img.resize((150, 185), Image.ANTIALIAS)
back_card = ImageTk.PhotoImage(card_back_img)

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=YES)
main_frame.pack_propagate(False)

background_label = Label(main_frame, image=bg_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

for item in card_entries:
    image_copy = Image.open("Card_Assets/"+item)  # Open Card PNGs
    image_copy = image_copy.resize((150, 185), Image.ANTIALIAS)  # Makes smaller images
    objects.append((ImageTk.PhotoImage(image_copy))) # Opens in PhotoImage
      # Adds to randomize list


def hit(click):
    global counter
    global hit_button
    counter += 1
    if counter == 1:
        play_card3 = Label(main_frame, image=random.choice(objects))
        play_card3.pack()
        play_card3.place(x=595, y=330)
    elif counter == 2:
        play_card4 = Label(main_frame, image=random.choice(objects))
        play_card4.pack()
        play_card4.place(x=760, y=330)
    else:
        play_card5 = Label(main_frame, image=random.choice(objects))
        play_card5.pack()
        play_card5.place(x=350, y=410)
        hit_button.destroy()


def stand(click):
    hit_button.destroy()
    stand_button.destroy()
    deal_card2.config(image=random.choice(objects))


card_back = Label(main_frame, image=back_card)
card_back.pack()
card_back.place(x=857, y=90)

play_card1 = Label(main_frame, image=random.choice(objects))
play_card1.pack()
play_card1.place(x=265, y=330)
play_card2 = Label(main_frame, image=random.choice(objects))
play_card2.pack()
play_card2.place(x=430, y=330)

deal_card1 = Label(main_frame, image=random.choice(objects))
deal_card1.pack()
deal_card1.place(x=330, y=90)
deal_card2 = Label(main_frame, image=back_card)
deal_card2.pack()
deal_card2.place(x=485, y=90)

hit_button = Button(main_frame, text='Hit', bg='green', height=4, width=10)
hit_button.pack()
hit_button.place(x=180, y=450)
hit_button.bind('<Button-1>', hit)
stand_button = Button(main_frame, text='Stand', bg='red', height=4, width=10)
stand_button.pack()
stand_button.place(x=920, y=450)
stand_button.bind('<Button-1>', stand)

root.mainloop()
