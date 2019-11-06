from tkinter import *
from PIL import Image, ImageTk
import random
import math
import os
import xlrd

root = Tk()
root.title('Blackjack')
root.geometry('1200x650')

card_entries = dict()  # Contains ('Image Name', number_value)
card_wb = xlrd.open_workbook('Card_Values.xlsx')
sheet = card_wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    card_entries[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)

objects = dict()  # Contains('Image Name', PhotoImage)

for item in card_entries:
    image_copy = Image.open("Card_Assets/"+item)  # Open Card PNGs
    image_copy = image_copy.resize((150, 185), Image.ANTIALIAS)  # Makes smaller images
    objects[item] = (ImageTk.PhotoImage(image_copy))  # Opens in PhotoImage

print(card_entries)
print(objects)

bg_img = ImageTk.PhotoImage(file='blackjack_background.png')
lose_img = ImageTk.PhotoImage(file='loser_screen.png')
card_back_img = Image.open('blue_back.png')
card_back_img = card_back_img.resize((150, 185), Image.ANTIALIAS)
back_card = ImageTk.PhotoImage(card_back_img)

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=YES)
main_frame.pack_propagate(False)

background_label = Label(main_frame, image=bg_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

counter = 0
play_label = 0
deal_label = 0


def hit(click):
    global counter
    global play_label
    global play_total_label
    counter += 1
    if counter == 1:
        randomizeP3 = random.choice(list(objects.keys()))
        play_card3 = Label(main_frame, image=objects[randomizeP3])
        play_card3.pack()
        play_card3.place(x=595, y=330)
        play_label += card_entries[randomizeP3]
        play_total_label.config(text='Your Total = {}'.format(play_label))
        if play_label >= 22:
            background_label = Label(main_frame, image=lose_img)
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10)
            play_agane.pack()
            play_agane.place(x=600, y=500)
    elif counter == 2:
        randomizeP4 = random.choice(list(objects.keys()))
        play_card4 = Label(main_frame, image=objects[randomizeP4])
        play_card4.pack()
        play_card4.place(x=760, y=330)
        play_label += card_entries[randomizeP4]
        play_total_label.config(text='Your Total = {}'.format(play_label))
        if play_label >= 22:
            background_label = Label(main_frame, image=lose_img)
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10)
            play_agane.pack()
            play_agane.place(x=600, y=500)
    else:
        randomizeP5 = random.choice(list(objects.keys()))
        play_card5 = Label(main_frame, image=objects[randomizeP5])
        play_card5.pack()
        play_card5.place(x=350, y=410)
        hit_button.destroy()
        play_label += card_entries[randomizeP5]
        play_total_label.config(text='Your Total = {}'.format(play_label))
        if play_label >= 22:
            background_label = Label(main_frame, image=lose_img)
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10)
            play_agane.pack()
            pplay_agane.place(x=600, y=500)


def stand(click):
    global deal_label
    global deal_total_label
    hit_button.destroy()
    stand_button.destroy()
    randomizeD2 = random.choice(list(objects.keys()))
    deal_card2.config(image=objects[randomizeD2])
    deal_label += card_entries[randomizeD2]
    deal_total_label.config(text='Dealer Total = {}'.format(deal_label))


card_back = Label(main_frame, image=back_card)
card_back.pack()
card_back.place(x=857, y=90)

randomizeP1 = random.choice(list(objects.keys()))
randomizeP2 = random.choice(list(objects.keys()))
play_card1 = Label(main_frame, image=objects[randomizeP1])
play_card1.pack()
play_card1.place(x=265, y=330)
play_card2 = Label(main_frame, image=objects[randomizeP2])
play_card2.pack()
play_card2.place(x=430, y=330)

play_label += card_entries[randomizeP1] + card_entries[randomizeP2]
play_total_label = Label(main_frame, text='Your Total = {}'.format(play_label), font=('Comic Sans MS', 8))
play_total_label.pack()
play_total_label.place(x=550, y=550)

randomizeD1 = random.choice(list(objects.keys()))
deal_card1 = Label(main_frame, image=objects[randomizeD1])
deal_card1.pack()
deal_card1.place(x=330, y=90)
deal_card2 = Label(main_frame, image=back_card)
deal_card2.pack()
deal_card2.place(x=485, y=90)

deal_label += card_entries[randomizeD1]
deal_total_label = Label(main_frame, text='Dealer Total = {}'.format(deal_label), font=('Comic Sans MS', 8))
deal_total_label.pack()
deal_total_label.place(x=175, y=175)

hit_button = Button(main_frame, text='Hit', bg='green', height=4, width=10)
hit_button.pack()
hit_button.place(x=180, y=450)
hit_button.bind('<Button-1>', hit)
stand_button = Button(main_frame, text='Stand', bg='red', height=4, width=10)
stand_button.pack()
stand_button.place(x=920, y=450)
stand_button.bind('<Button-1>', stand)

root.mainloop()
