#!/usr/bin/env python3
# Written by Treebug842

import os
import sys
from tkinter import *
from PIL import ImageTk,Image
import numpy as np

root = Tk()
root.title("Tick Tack Toe")
root.iconbitmap("icon.ico")

global board
board = np.array([[0,0,0],
	[0,0,0],
	[0,0,0]])

global L1
global L2
L1 = 0
L2 = 0

global player
player = 1

def end_popup(outcome):
	def stop_game():
		sys.exit()

	def restart_game():
		os.startfile('Tick-Tack-Toe.exe')
		sys.exit()

	root.withdraw()
	popup = Tk()
	popup.wm_title("Match Ended")
	popup.iconbitmap("icon.ico")
	if outcome == 0:
		message = Label(popup, text="Match was a Draw!", font='Helvetica 18 bold', pady=30)
	elif outcome == 1:
		message = Label(popup, text="Player 1 Wins!", font='Helvetica 18 bold', pady=30)
	elif outcome == 2:
		message = Label(popup, text="Player 2 Wins!", font='Helvetica 18 bold', pady=30)

	exit_button = Button(popup, text="Exit", padx=100, font='Helvetica 15 bold', borderwidth=10, command=stop_game)
	reset_button = Button(popup, text="Play Again", padx=68, font='Helvetica 15 bold', borderwidth=10, command=restart_game)

	message.pack()
	exit_button.pack(padx=10)
	reset_button.pack(padx=10, pady=10)

	popup.mainloop()

x_icon = ImageTk.PhotoImage(Image.open("x_icon.png"))
button1 = Button(root, image=x_icon)
button2 = Button(root, image=x_icon)
button3 = Button(root, image=x_icon)
button4 = Button(root, image=x_icon)
button5 = Button(root, image=x_icon)
button6 = Button(root, image=x_icon)
button7 = Button(root, image=x_icon)
button8 = Button(root, image=x_icon)
button9 = Button(root, image=x_icon)

o_icon = ImageTk.PhotoImage(Image.open("o_icon.png"))
button1 = Button(root, image=o_icon)
button2 = Button(root, image=o_icon)
button3 = Button(root, image=o_icon)
button4 = Button(root, image=o_icon)
button5 = Button(root, image=o_icon)
button6 = Button(root, image=o_icon)
button7 = Button(root, image=o_icon)
button8 = Button(root, image=o_icon)
button9 = Button(root, image=o_icon)

def win(x):
	end_popup(x)

def check_score():
	for x in range(1, 3):
		for i in range(0, 3):
			if board[i][0] == x and board[i][1] == x and board[i][2] == x:
				win(x)
		for i in range(0, 3):
			if board[0][i] == x and board[1][i] == x and board[2][i] == x:
				win(x)
		if board[0][0] == x and board[1][1] == x and board[2][2] == x:
			win(x)
		if board[2][0] == x and board[1][1] == x and board[0][2] == x:
			win(x)
	if np.all(board != 0):
		end_popup(0)

def change_player():
	global player
	player += 1
	if player == 3:
		player = 1
	if player == 1:
		player_tag = Label(root, text="Player 1", fg="red", font='Helvetica 18 bold')
		player_tag.grid(row=4, column=1)
	elif player == 2:
		player_tag = Label(root, text="Player 2", fg="blue", font='Helvetica 18 bold')
		player_tag.grid(row=4, column=1)
	check_score()

def button_press1():
	if board[0][0] == 0:
		if player == 1:
			button1 = Button(root, image=x_icon)
			button1.grid(row=0, column=0)
		elif player == 2:
			button1 = Button(root, image=o_icon)
			button1.grid(row=0, column=0)
		board[0][0] = player
		change_player()

def button_press2():
	if board[0][1] == 0:
		if player == 1:
			button2 = Button(root, image=x_icon)
			button2.grid(row=0, column=1)
		elif player == 2:
			button2 = Button(root, image=o_icon)
			button2.grid(row=0, column=1)
		board[0][1] = player
		change_player()
	
def button_press3():
	if board[0][2] == 0:
		if player == 1:
			button3 = Button(root, image=x_icon)
			button3.grid(row=0, column=2)
		elif player == 2:
			button3 = Button(root, image=o_icon)
			button3.grid(row=0, column=2)
		board[0][2] = player
		change_player()

def button_press4():
	if board[1][0] == 0:
		if player == 1:
			button4 = Button(root, image=x_icon)
			button4.grid(row=1, column=0)
		elif player == 2:
			button4 = Button(root, image=o_icon)
			button4.grid(row=1, column=0)
		board[1][0] = player
		change_player()

def button_press5():
	if board[1][1] == 0:
		if player == 1:
			button5 = Button(root, image=x_icon)
			button5.grid(row=1, column=1)
		elif player == 2:
			button5 = Button(root, image=o_icon)
			button5.grid(row=1, column=1)
		board[1][1] = player
		change_player()

def button_press6():
	if board[1][2] == 0:
		if player == 1:
			button6 = Button(root, image=x_icon)
			button6.grid(row=1, column=2)
		elif player == 2:
			button6 = Button(root, image=o_icon)
			button6.grid(row=1, column=2)
		board[1][2] = player
		change_player()

def button_press7():
	if board[2][0] == 0:
		if player == 1:
			button7 = Button(root, image=x_icon)
			button7.grid(row=2, column=0)
		elif player == 2:
			button7 = Button(root, image=o_icon)
			button7.grid(row=2, column=0)
		board[2][0] = player
		change_player()

def button_press8():
	if board[2][1] == 0:
		if player == 1:
			button8 = Button(root, image=x_icon)
			button8.grid(row=2, column=1)
		elif player == 2:
			button8 = Button(root, image=o_icon)
			button8.grid(row=2, column=1)
		board[2][1] = player
		change_player()

def button_press9():
	if board[2][2] == 0:
		if player == 1:
			button9 = Button(root, image=x_icon)
			button9.grid(row=2, column=2)
		elif player == 2:
			button9 = Button(root, image=o_icon)
			button9.grid(row=2, column=2)
		board[2][2] = player
		change_player()

player_tag = Label(root, text="Player 1", fg="red", font='Helvetica 18 bold')
blank_icon = ImageTk.PhotoImage(Image.open("blank.png"))
button1 = Button(root, image=blank_icon, command=button_press1)
button2 = Button(root, image=blank_icon, command=button_press2)
button3 = Button(root, image=blank_icon, command=button_press3)
button4 = Button(root, image=blank_icon, command=button_press4)
button5 = Button(root, image=blank_icon, command=button_press5)
button6 = Button(root, image=blank_icon, command=button_press6)
button7 = Button(root, image=blank_icon, command=button_press7)
button8 = Button(root, image=blank_icon, command=button_press8)
button9 = Button(root, image=blank_icon, command=button_press9)

def start_board():
	button1.grid(row=0, column=0)
	button2.grid(row=0, column=1)
	button3.grid(row=0, column=2)
	button4.grid(row=1, column=0)
	button5.grid(row=1, column=1)
	button6.grid(row=1, column=2)
	button7.grid(row=2, column=0)
	button8.grid(row=2, column=1)
	button9.grid(row=2, column=2)  
	player_tag.grid(row=4, column=1)

start_board()

root.mainloop()







