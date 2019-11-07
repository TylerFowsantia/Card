from tkinter import *
from PIL import Image, ImageTk
import random
import os
import xlrd

root = Tk()
root.title('Blackjack')
root.geometry('1205x655')
card_entries = dict()  # Contains ('Image Name', number_value)
card_wb = xlrd.open_workbook('Card_Values.xlsx')
sheet = card_wb.sheet_by_index(0)
sheet.cell_value(0, 0)

for i in range(sheet.nrows):
    card_entries[sheet.cell_value(i, 0)] = sheet.cell_value(i, 1)  # Inputs key values for card_entries dict

objects = dict()  # Contains('Image Name', PhotoImage)

for item in card_entries:
    image_copy = Image.open("Card_Assets/"+item)  # Open Card PNGs
    image_copy = image_copy.resize((150, 185), Image.ANTIALIAS)  # Makes smaller images
    objects[item] = (ImageTk.PhotoImage(image_copy))  # Opens in PhotoImage

bg_img = ImageTk.PhotoImage(file='blackjack_background.png')  # Opens background image file in ImageTk
lose_img = ImageTk.PhotoImage(file='loser_screen.png')  # Opens lose screen image file in ImageTk
win_img = ImageTk.PhotoImage(file='winner_screen.png')  # Opens win screen image file in ImageTk
tie_img = ImageTk.PhotoImage(file='tie_screen.png')  # Opens tie screen image file in ImageTk
card_back_img = Image.open('blue_back.png')  # Opens back of card image file
card_back_img = card_back_img.resize((150, 185), Image.ANTIALIAS)  # Resizing back of card image
back_card = ImageTk.PhotoImage(card_back_img)  # Opens back of card image file in ImageTk

main_frame = Frame(root)
main_frame.pack(fill=BOTH, expand=YES)
main_frame.pack_propagate(False)

background_label = Label(main_frame, image=bg_img)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

counter = 0  # Counter counts times hit definement is pressed, to pull next player card
play_label = 0  # Shows start total for player before card values are added
deal_label = 0  # Shows start total for dealer before card values are added


def reset():  # Closes out program to reset after being met with a "play again" button
    python = sys.executable
    os.execl(python, python, * sys.argv)


def hit(click):  # Pulls new cards for player
    global counter
    global play_label
    global play_total_label
    global deal_total_label
    global lose_img
    counter += 1
    if counter == 1:
        randomizeP3 = random.choice(list(objects.keys()))  # Randomizes a 3rd card
        play_card3 = Label(main_frame, image=objects[randomizeP3])  # Finds key value and image of randomizer
        play_card3.pack()
        play_card3.place(x=595, y=330)   # Packs and places next to other cards
        play_label += card_entries[randomizeP3]  # Adds number value to total
        play_total_label.config(text='Your Total = {}'.format(play_label))  # Reformats total to display correct value
    elif counter == 2:
        randomizeP4 = random.choice(list(objects.keys()))  # Randomizes a 4th Card
        play_card4 = Label(main_frame, image=objects[randomizeP4])  # Finds key value and image of randomizer
        play_card4.pack()
        play_card4.place(x=760, y=330)  # Packs and places next to other cards
        play_label += card_entries[randomizeP4]  # Adds number value to total
        play_total_label.config(text='Your Total = {}'.format(play_label))  # Reformats total to display correct value
    else:
        randomizeP5 = random.choice(list(objects.keys()))  # Randomizes a 5th Card
        play_card5 = Label(main_frame, image=objects[randomizeP5])  # Finds key value and image of randomizer
        play_card5.pack()
        play_card5.place(x=350, y=410)  # Packs and places next to other cards
        hit_button.destroy()  # Prevents players from drawing more cards
        play_label += card_entries[randomizeP5]  # Adds number value to total
        play_total_label.config(text='Your Total = {}'.format(play_label))  # Reformats total to display correct value
    if play_label >= 22:  # Checks if player total is over 21, (Can be equal to 21 never over)
        background_label = Label(main_frame, image=lose_img)  # Replaces main screen with loser image screen
        background_label.place(relwidth=1, relheight=1)
        play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10, command=reset)
        play_agane.pack()
        play_agane.place(x=600, y=500)  # Play button is created with reset command and packed and place
        play_total_label = Label(text='Your Total = {}'.format(play_label))
        play_total_label.pack()
        play_total_label.place(x=300, y=400)  # Shows the player they are over 21
        deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
        deal_total_label.pack()
        deal_total_label.place(x=400, y=400)  # Shows presumed dealer value
    
    
def stand(click):  # Standing prevents players from drawing allowing dealer(AI) to draw and match
    global deal_label
    global deal_total_label
    global play_total_label
    global background_label
    hit_button.destroy()  # Prevents player phase
    stand_button.destroy()  # Prevents player phase
    randomizeD2 = random.choice(list(objects.keys()))  # Dealer reveals hidden 2nd card
    deal_card2.config(image=objects[randomizeD2])
    deal_label += card_entries[randomizeD2]  # Adds number value to dealer total
    deal_total_label.config(text='Dealer Total = {}'.format(deal_label))
    if play_label > deal_label:  # Checks if player value is still higher after reveal of 2nd card
        randomizeD3 = random.choice(list(objects.keys()))  # Draws for a 3rd card
        deal_card3 = Label(main_frame, image=objects[randomizeD3])
        deal_card3.pack()
        deal_card3.place(x=640, y=90)  # Finds image key and pack and places card
        deal_label += card_entries[randomizeD3]  # Adds number value to dealer total
        deal_total_label.config(text='Dealer Total = {}'.format(deal_label))  # Reformats dealer value
        if deal_label >= 22:  # After drawing 3rd card, checks if dealer is over 21
            background_label = Label(main_frame, image=win_img)  # Replaces main screen with win image screen
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10, command=reset)
            play_agane.pack()
            play_agane.place(x=600, y=500)
            play_total_label = Label(text='Your Total = {}'.format(play_label))
            play_total_label.pack()
            play_total_label.place(x=300, y=400)
            deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
            deal_total_label.pack()
            deal_total_label.place(x=400, y=400)
        elif play_label > deal_label:  # However if dealer is still under 21 and under player value player win and reset
            background_label = Label(main_frame, image=win_img) # Replaces main screen with win image screen
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10, command=reset)
            play_agane.pack()
            play_agane.place(x=600, y=500)
            play_total_label = Label(text='Your Total = {}'.format(play_label))
            play_total_label.pack()
            play_total_label.place(x=300, y=400)
            deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
            deal_total_label.pack()
            deal_total_label.place(x=400, y=400)
        elif play_label < deal_label: # If after 3rd card and dealer outmatches player, dealer win and reset
            background_label = Label(main_frame, image=lose_img)  # Replaces main screen with loser image screen
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10, command=reset)
            play_agane.pack()
            play_agane.place(x=500, y=500)
            play_total_label = Label(text='Your Total = {}'.format(play_label))
            play_total_label.pack()
            play_total_label.place(x=400, y=400)
            deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
            deal_total_label.pack()
            deal_total_label.place(x=600, y=400)
        else:  # In any other case; player and dealer have equal value and tie and reset
            background_label = Label(main_frame, image=tie_img)  # Replaces main screen with tie image screen
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10, command=reset)
            play_agane.pack()
            play_agane.place(x=550, y=500)
            play_total_label = Label(text='Your Total = {}'.format(play_label))
            play_total_label.pack()
            play_total_label.place(x=500, y=400)
            deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
            deal_total_label.pack()
            deal_total_label.place(x=600, y=400)
    elif play_label < deal_label:  # If dealer value already higher than player after 2nd card reveal dealer win and reset 
        background_label = Label(main_frame, image=lose_img)
        background_label.place(relwidth=1, relheight=1)
        play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10, command=reset)
        play_agane.pack()
        play_agane.place(x=500, y=500)
        play_total_label = Label(text='Your Total = {}'.format(play_label))
        play_total_label.pack()
        play_total_label.place(x=400, y=400)
        deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
        deal_total_label.pack()
        deal_total_label.place(x=600, y=400)
        if deal_label > 22:  # Checks if dealer was higher than 21 after 2nd card, player win
            background_label = Label(main_frame, image=win_img)
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='gray', height=4, width=10, command=reset)
            play_agane.pack()
            play_agane.place(x=600, y=500)
            play_total_label = Label(text='Your Total = {}'.format(play_label))
            play_total_label.pack()
            play_total_label.place(x=300, y=400)
            deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
            deal_total_label.pack()
            deal_total_label.place(x=400, y=400)
        elif play_label == deal_label:  # If dealer total is equal to player total after 2nd card, tie and reset
            background_label = Label(main_frame, image=tie_img)
            background_label.place(relwidth=1, relheight=1)
            play_agane = Button(main_frame, text='Play Again', fg='White', bg='steelblue2', height=4, width=10, command=reset)
            play_agane.pack()
            play_agane.place(x=550, y=500)
            play_total_label = Label(text='Your Total = {}'.format(play_label))
            play_total_label.pack()
            play_total_label.place(x=500, y=400)
            deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
            deal_total_label.pack()
            deal_total_label.place(x=600, y=400)
    elif play_label == deal_label:  # In all other cases player and dealer tie and reset
        background_label = Label(main_frame, image=tie_img)
        background_label.place(relwidth=1, relheight=1)
        play_agane = Button(main_frame, text='Play Again', fg='White', bg='steelblue2', height=4, width=10, command=reset)
        play_agane.pack()
        play_agane.place(x=550, y=500)
        play_total_label = Label(text='Your Total = {}'.format(play_label))
        play_total_label.pack()
        play_total_label.place(x=500, y=400)
        deal_total_label = Label(text='Dealer Total = {}'.format(deal_label))
        deal_total_label.pack()
        deal_total_label.place(x=600, y=400)


card_back = Label(main_frame, image=back_card)
card_back.pack()
card_back.place(x=857, y=90)  # Places 'deck' in spot

randomizeP1 = random.choice(list(objects.keys()))  # Randomizes 1st starter card for player
randomizeP2 = random.choice(list(objects.keys()))  # Randomizes 2nd starter card for player
play_card1 = Label(main_frame, image=objects[randomizeP1])  # Finds image key for 1st player card
play_card1.pack()
play_card1.place(x=265, y=330)  # Places the image
play_card2 = Label(main_frame, image=objects[randomizeP2])  # Finds image key for 2nd player card
play_card2.pack()
play_card2.place(x=430, y=330)  # Places the image

play_label += card_entries[randomizeP1] + card_entries[randomizeP2]  # Adds number value of card1 and card2 for player
play_total_label = Label(main_frame, text='Your Total = {}'.format(play_label), font=('Comic Sans MS', 8))
play_total_label.pack()
play_total_label.place(x=550, y=550)  # Places label and displays player total

randomizeD1 = random.choice(list(objects.keys()))  # Randomizes 1st starter card for dealer
deal_card1 = Label(main_frame, image=objects[randomizeD1])  # Finds image key for 1st dealer card
deal_card1.pack()
deal_card1.place(x=330, y=90)
deal_card2 = Label(main_frame, image=back_card)  # In blackjack, dealer's 2nd card is not displayed until player stands
deal_card2.pack()
deal_card2.place(x=485, y=90)

deal_label += card_entries[randomizeD1]  # Adds number value to dealer total
deal_total_label = Label(main_frame, text='Dealer Total = {}'.format(deal_label), font=('Comic Sans MS', 8))
deal_total_label.pack()
deal_total_label.place(x=175, y=175)

hit_button = Button(main_frame, text='Hit', bg='green', height=4, width=10)  # Hit button to draw player cards
hit_button.pack()
hit_button.place(x=180, y=450)
hit_button.bind('<Button-1>', hit)  # Binds button to left click with definement 'hit'
stand_button = Button(main_frame, text='Stand', bg='red', height=4, width=10)  # Stand button to initiate dealer phase
stand_button.pack()
stand_button.place(x=920, y=450)
stand_button.bind('<Button-1>', stand)  # Binds button to left click with definement 'stand'

root.mainloop()
