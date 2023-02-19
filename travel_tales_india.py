# Created by SST

# TRAVEL TALES
# MUSIC FOR DIE
# Player 2 and Player 1 image
# India map
# Start Page

import pygame
import random
import time
import pyttsx3
import tkinter as tk
from PIL import Image, ImageTk
import s1
import s2
import s3
import s4
import s5
import s6
import s7
import s8

WIDTH = 740
HEIGHT = 640
FPS = 30

pygame.init()
pygame.mixer.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Travel Tales")
clock = pygame.time.Clock()

engine = pyttsx3.init()
voices = engine.getProperty("voices")
engine.setProperty("voice", voices[1].id)
engine.setProperty("rate", 178)


def speak(audio):
    engine.say(audio)
    engine.runAndWait()


# background image
bckimg = pygame.image.load("board.jpg")
startimg = pygame.image.load("start.jpg")
startimg = pygame.transform.scale(startimg, (740, 640))
winbk = pygame.image.load("winbk.jpg")
winbk = pygame.transform.scale(winbk, (500, 500))
# roll dice image
dice_img = pygame.image.load("roll.png")
dice_img = pygame.transform.scale(dice_img, (60, 50))

# expand image
expand = pygame.image.load("expand.png")
expand = pygame.transform.scale(expand, (20, 20))

# hw to play
play = pygame.image.load("hwtoplay.jpg")
play = pygame.transform.scale(play, (740, 640))


def hwtoplay():
    screen.blit(play, (0, 0))


# pin
redpin = pygame.image.load("redpin.png")
redpin = pygame.transform.scale(redpin, (20, 20))
bluepin = pygame.image.load("bluepin.png")
bluepin = pygame.transform.scale(bluepin, (20, 20))

#font-player1 and player2
font1 = pygame.font.SysFont("comicsansms", 25)
font2 = pygame.font.SysFont("comicsansms", 20)
font3 = pygame.font.SysFont("timesnewroman", 30)
font4 = pygame.font.SysFont("timesnewroman", 50)

co_dict = {
    1: [185, 520], 2: [234, 520], 3: [283, 520], 4: [332, 520], 5: [381, 520],
    6: [430, 520], 7: [479, 520], 8: [528, 520], 9: [577, 520], 10: [626, 520],

    11: [626, 471], 12: [577, 471], 13: [528, 471], 14: [479, 471], 15: [430, 471],
    16: [381, 471], 17: [332, 471], 18: [283, 471], 19: [234, 471], 20: [185, 471],

    21: [185, 422], 22: [234, 422], 23: [283, 422], 24: [332, 422], 25: [381, 422],
    26: [430, 422], 27: [479, 422], 28: [528, 422], 29: [577, 422], 30: [626, 422],

    31: [626, 373], 32: [577, 373], 33: [528, 373], 34: [479, 373], 35: [430, 373],
    36: [381, 373], 37: [332, 373], 38: [283, 373], 39: [234, 373], 40: [185, 373],

    41: [185, 324], 42: [234, 324], 43: [283, 324], 44: [332, 324], 45: [381, 324],
    46: [430, 324], 47: [479, 324], 48: [528, 324], 49: [577, 324], 50: [626, 324],

    51: [626, 275], 52: [577, 275], 53: [528, 275], 54: [479, 275], 55: [430, 275],
    56: [381, 275], 57: [332, 275], 58: [283, 275], 59: [234, 275], 60: [185, 275],

    61: [185, 226], 62: [234, 226], 63: [283, 226], 64: [332, 226], 65: [381, 226],
    66: [430, 226], 67: [479, 226], 68: [528, 226], 69: [577, 226], 70: [626, 226],

    71: [626, 177], 72: [577, 177], 73: [528, 177], 74: [479, 177], 75: [430, 177],
    76: [381, 177], 77: [332, 177], 78: [283, 177], 79: [234, 177], 80: [185, 177],

    81: [185, 128], 82: [234, 128], 83: [283, 128], 84: [332, 128], 85: [381, 128],
    86: [430, 128], 87: [479, 128], 88: [528, 128], 89: [577, 128], 90: [626, 128],

    91: [626, 79], 92: [577, 79], 93: [528, 79], 94: [479, 79], 95: [430, 79],
    96: [381, 79], 97: [332, 79], 98: [283, 79], 99: [234, 79], 100: [185, 79],
}


def Bck():
    screen.blit(bckimg, (0, 0))
    screen.blit(dice_img, (25, 550))
    screen.blit(expand, (710, 7))


def players():
    msg1 = font1.render("Player 1", True, (255, 0, 0))
    msg2 = font1.render("Player 2", True, (0, 0, 255))
    msg3 = font3.render("TRAVEL", True, (0, 0, 0))
    msg4 = font3.render("INDIA", True, (0, 0, 0))
    screen.blit(msg1, (5, 200))
    screen.blit(msg2, (5, 300))
    screen.blit(msg3, (5, 20))
    screen.blit(msg4, (11, 60))


def pickNumber():
    die_num = random.randint(1, 6)
    if die_num == 1:
        die_img = pygame.image.load("d1.jpg")
    elif die_num == 2:
        die_img = pygame.image.load("d2.jpg")
    elif die_num == 3:
        die_img = pygame.image.load("d3.jpg")
    elif die_num == 4:
        die_img = pygame.image.load("d4.jpg")
    elif die_num == 5:
        die_img = pygame.image.load("d5.jpg")
    elif die_num == 6:
        die_img = pygame.image.load("d6.jpg")
    die_img = pygame.transform.scale(die_img, (60, 60))
    return (die_num, die_img)


def red_win_message():
    red_msg = font4.render("Player 1 wins", True, (255, 0, 0))
    screen.blit(red_msg, (285, 275))


def blue_win_message():
    blue_msg = font4.render("Player 2 wins", True, (0, 0, 255))
    screen.blit(blue_msg, (285, 275))


def rollr():
    msg3 = font2.render("Your Turn", True, (0, 0, 0))
    screen.blit(msg3, (5, 240))


def rollb():
    msg4 = font2.render("Your Turn", True, (0, 0, 0))
    screen.blit(msg4, (5, 340))


def startdisp():
    screen.blit(startimg, (0, 0))


def dispinloc(place, cord):
    msg5 = font2.render(place, True, (0, 0, 0))
    screen.blit(msg5, cord)


def dispin(pin, cord):
    screen.blit(pin, cord)


class Demo1:
    def __init__(self, master, pos):
        Demo1.main = self
        self.master = master
        self.master.geometry("500x500")
        self.master.minsize(500, 500)
        self.master.maxsize(500, 500)
        self.master.title("Travel Tales")
        self.master.configure(bg="black")
        self.pos_val = pos
        self.cnt = 0

        if self.pos_val == 1:
            self.info_dict = s1.info
        elif self.pos_val == 2:
            self.info_dict = s2.info
        elif self.pos_val == 3:
            self.info_dict = s3.info
        elif self.pos_val == 4:
            self.info_dict = s4.info
        elif self.pos_val == 5:
            self.info_dict = s5.info
        elif self.pos_val == 6:
            self.info_dict = s6.info
        elif self.pos_val == 7:
            self.info_dict = s7.info
        elif self.pos_val == 8:
            self.info_dict = s8.info

        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.image = Image.open(f"s{self.pos_val}.jpg")
        self.tk_img = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_img, anchor="nw")
        self.ans_button = tk.Button(fg="white", bg="black", text="Answer Quiz",
                                    command=self.new_window, anchor="s", font="Lucida 12 bold", pady=3, padx=10)
        self.ans_button_window = self.canvas.create_window(
            180, 490, anchor="sw", window=self.ans_button)

        self.no = random.randint(1, 5)
        self.master.update()
        for sentence in self.info_dict[f"g{self.no}"][0]:
            speak(sentence)

    def new_window(self):
        if self.cnt == 0:
            self.newWindow = tk.Toplevel(self.master)
            self.app = Demo2(self.newWindow, self.pos_val, self.no)
            self.cnt = 1

    def close_window(self):
        self.master.destroy()

    @classmethod
    def quit_window(cls):
        cls.main.close_window()


class Demo2:
    def __init__(self, master, pos_val, no):
        self.master = master
        self.master.geometry("500x500")
        self.master.minsize(500, 500)
        self.master.maxsize(500, 500)
        self.master.title("Travel Tales")
        self.master.configure(bg="#FFC72C")
        self.pos_val = pos_val
        self.no = no
        self.user_choice = -1

        if self.pos_val == 1:
            self.info_dict = s1.info
        elif self.pos_val == 2:
            self.info_dict = s2.info
        elif self.pos_val == 3:
            self.info_dict = s3.info
        elif self.pos_val == 4:
            self.info_dict = s4.info
        elif self.pos_val == 5:
            self.info_dict = s5.info
        elif self.pos_val == 6:
            self.info_dict = s6.info
        elif self.pos_val == 7:
            self.info_dict = s7.info
        elif self.pos_val == 8:
            self.info_dict = s8.info

        self.var = tk.IntVar()
        self.var.set(-1)

        # Heading
        tk.Label(self.master, text="QUIZ", font="timesnewroman 14 bold",
                 justify="center", pady=20, bg="#FFC72C").pack()

        # Question
        tk.Label(self.master, text=self.info_dict[f"g{self.no}"][1], font="Lucida 12 bold",
                 justify="center", padx=14, pady=20, wraplength=400, bg="#FFC72C").pack()

        # option 1
        self.radio = tk.Radiobutton(
            self.master, text=self.info_dict[f"g{self.no}"][2], font="Lucida 12 bold", padx=34, pady=10, bg="#FFC72C", variable=self.var, value=1)
        self.radio.pack(anchor="w")

        # option 2
        self.radio = tk.Radiobutton(
            self.master, text=self.info_dict[f"g{self.no}"][3], padx=34, pady=10, font="Lucida 12 bold", bg="#FFC72C", variable=self.var, value=2)
        self.radio.pack(anchor="w")

        # option 3
        self.radio = tk.Radiobutton(
            self.master, text=self.info_dict[f"g{self.no}"][4], padx=34, pady=10, font="Lucida 12 bold", bg="#FFC72C", variable=self.var, value=3)
        self.radio.pack(anchor="w")

        # option 4
        self.radio = tk.Radiobutton(
            self.master, text=self.info_dict[f"g{self.no}"][5], padx=34, pady=10, font="Lucida 12 bold", bg="#FFC72C", variable=self.var, value=4)
        self.radio.pack(anchor="w")

        self.submitButton = tk.Button(self.master, text="Submit", font=(
            "Lucida 14 bold"), fg="white", bg="black", pady=3, padx=20, command=self.close_windows)
        self.submitButton.place(relx=0.35, rely=0.8)

    def close_windows(self):
        if self.info_dict[f"g{self.no}"][6] == self.var.get():
            Demo2.ans = True
        else:
            Demo2.ans = False
        self.master.destroy()
        Demo1.quit_window()


lad_ans = {1: "4312", 2: "2413", 3: "4321", 4: "4132", 5: "2431"}

fact = ["The interesting fact about its architecture is that the vimana of the temple does not cast a shadow at noon", "The main theme of Kathakali is mythological stories and various popular scenes taken from epics like Mahabharata Ramayana Bhagavat Purana other holy scriptures", "The shrine receives offerings from devotees in cash jewellery gold silver property deeds and Demat share transfers and the per day offering is around 22.5 million",
        "The flag a top the temple strangely always floats in the opposite direction of wind The flag floating in opposite direction brings your scientific reasoning to a halt and you just tend to believe that there is some force more powerful than science", "Hawal Mahal has 5 floors and there are no stairs to climb instead there are only ramps to reach the top floors"]

headings = ["brihadeeswarar temple", "Kathkali",
            "Tirupati", "Jagannath temple", "Hawa Mahal"]


class Demo3:
    def __init__(self, master, pos):
        Demo3.main = self
        self.master = master
        self.master.geometry("500x500")
        self.master.minsize(500, 500)
        self.master.maxsize(500, 500)
        self.master.title("Travel Tales")
        self.master.configure(bg="black")
        self.pos_val = pos

        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.image = Image.open(f"crt{self.pos_val}.jpg")
        self.image = self.image.resize((600, 600), Image.ANTIALIAS)
        self.tk_img = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_img, anchor="nw")
        self.master.update()
        speak(headings[self.pos_val-1])
        time.sleep(5)
        self.image = Image.open(f"jum{self.pos_val}.jpg")
        self.image = self.image.resize((600, 600), Image.ANTIALIAS)
        self.tk_img = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_img, anchor="nw")
        self.master.update()
        time.sleep(5)
        self.master.destroy()
        ladquestion(self.pos_val)


class Demo4:
    ans = False

    def __init__(self, master, pos_val):
        self.master = master
        self.master.geometry("600x600")
        self.master.minsize(600, 600)
        self.master.maxsize(600, 600)
        self.master.title("Travel Tales")
        self.master.configure(bg="#FFC72C")
        self.pos_val = pos_val
        # Heading
        tk.Label(self.master, text="Answer", font="timesnewroman 21 bold",
                 justify="center", pady=20, bg="#FFC72C").place(relx=0.38, rely=0.1)

        self.valueb1 = tk.StringVar()
        self.valueb2 = tk.StringVar()
        self.valueb3 = tk.StringVar()
        self.valueb4 = tk.StringVar()

        self.entryb1 = tk.Entry(textvariable=self.valueb1)
        self.entryb2 = tk.Entry(textvariable=self.valueb2)
        self.entryb3 = tk.Entry(textvariable=self.valueb3)
        self.entryb4 = tk.Entry(textvariable=self.valueb4)

        self.entryb1.place(relx=0.1, rely=0.4, width=50, height=50)
        self.entryb2.place(relx=0.3, rely=0.4, width=50, height=50)
        self.entryb3.place(relx=0.5, rely=0.4, width=50, height=50)
        self.entryb4.place(relx=0.7, rely=0.4, width=50, height=50)

        self.submitButton = tk.Button(self.master, text="Submit", font=(
            "Lucida 14 bold"), fg="white", bg="black", pady=3, padx=20, command=self.close_windows)
        self.submitButton.place(relx=0.38, rely=0.8)

    def close_windows(self):
        print(self.valueb1.get()+self.valueb2.get() +
              self.valueb3.get()+self.valueb4.get())
        if (self.valueb1.get()+self.valueb2.get()+self.valueb3.get()+self.valueb4.get()) == lad_ans[self.pos_val]:
            Demo4.ans = True
        self.submitButton.destroy()
        self.canvas = tk.Canvas(self.master, width=500, height=500)
        self.canvas.pack()
        self.image = Image.open(f"ans{self.pos_val}.jpg")
        self.image = self.image.resize((600, 600), Image.ANTIALIAS)
        self.tk_img = ImageTk.PhotoImage(self.image)
        self.canvas.create_image(0, 0, image=self.tk_img, anchor="nw")
        self.master.update()
        speak(fact[self.pos_val-1])
        time.sleep(5)
        self.master.destroy()


def main(pos):
    root = tk.Tk()
    app = Demo1(root, pos)
    root.mainloop()


def ladmain(pos):
    root = tk.Tk()
    app = Demo3(root, pos)
    root.mainloop()


def ladquestion(pos):
    root = tk.Tk()
    app = Demo4(root, pos)
    root.mainloop()


def chk_pos(val):
    if val == 4:
        ladmain(1)
        try:
            if Demo4.ans:
                val = 14
        except:
            val = 4
    elif val == 9:
        ladmain(2)
        try:
            if Demo4.ans:
                val = 31
        except:
            val = 9
    elif val == 17:
        main(1)
        try:
            if not Demo2.ans:
                val = 7
        except:
            val = 7
    elif val == 21:
        ladmain(3)
        try:
            if Demo4.ans:
                val = 42
        except:
            val = 21
    elif val == 33:
        ladmain(4)
        try:
            if Demo4.ans:
                val = 76
        except:
            val = 33
    elif val == 38:
        main(2)
        try:
            if not Demo2.ans:
                val = 19
        except:
            val = 19
    elif val == 50:
        main(3)
        try:
            if not Demo2.ans:
                val = 28
        except:
            val = 28
    elif val == 64:
        main(4)
        try:
            if not Demo2.ans:
                val = 60
        except:
            val = 60
    elif val == 67:
        main(5)
        try:
            if not Demo2.ans:
                val = 51
        except:
            val = 51
    elif val == 73:
        ladmain(5)
        try:
            if Demo4.ans:
                val = 92
        except:
            val = 73
    elif val == 94:
        main(6)
        try:
            if not Demo2.ans:
                val = 75
        except:
            val = 75
    elif val == 96:
        main(7)
        try:
            if not Demo2.ans:
                val = 78
        except:
            val = 78
    elif val == 98:
        main(8)
        try:
            if not Demo2.ans:
                val = 35
        except:
            val = 35
    return val


class Player(pygame.sprite.Sprite):
    win = False
    count = 0

    def __init__(self, img_name, distance, colour):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load(img_name)
        self.image = pygame.transform.scale(self.image, (36, 36))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = distance
        self.start = 0
        self.end = 0
        self.answer_flag = 0
        self.colour = colour
        self.distance = distance
        self.num = 0

    def control(self, start, end):
        self.start = start
        self.end = end
        self.flag = 0
        self.answer_flag = 0

    def update(self):
        if self.end != 0 and self.start < 100 and self.flag == 0 and Player.win == False:
            if self.start < self.end:
                self.start += 1
                self.rect.x, self.rect.y = co_dict[self.start]
                pygame.mixer.music.load("piece.mp3")
                pygame.mixer.music.set_volume(0.7)
                pygame.mixer.music.play(loops=1)
            elif self.start == self.end and self.flag == 0:
                self.num = chk_pos(self.start)
                self.rect.x, self.rect.y = co_dict[self.num]
                self.start = self.num
                self.flag = 1
                self.answer()

        if self.start == 100:
            if self.colour == "red":
                # pygame.draw.rect(screen,(191,239,255),pygame.Rect(178,66,500,500))
                screen.blit(winbk, (178, 67))
                red_player.rect.x, red_player.rect.y = red_player.distance
                blue_player.rect.x, blue_player.rect.y = blue_player.distance
                red_win_message()
                pygame.display.update()
                if Player.count == 0:
                    speak("Player 1 wins")
                    Player.count += 1
            else:
                # pygame.draw.rect(screen,(191,239,255),pygame.Rect(178,66,500,500))
                screen.blit(winbk, (178, 67))
                red_player.rect.x, red_player.rect.y = red_player.distance
                blue_player.rect.x, blue_player.rect.y = blue_player.distance
                blue_win_message()
                pygame.display.update()
                if Player.count == 0:
                    speak("Player 2 wins")
                    Player.count += 1
            # pygame.mixer.music.load("winsound.mpeg")
            # pygame.mixer.music.set_volume(0.7)
            # pygame.mixer.music.play(loops=1)
            Player.win = True

    def answer(self):
        self.answer_flag = 1
        return self.num

    @classmethod
    def location(class_name):
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(620, 27, 100, 90))
        msg1 = font1.render("Player 1", True, (255, 0, 0))
        msg2 = font1.render("Player 2", True, (0, 0, 255))
        screen.blit(msg1, (623, 29))
        screen.blit(msg2, (623, 69))

    def locate(self, t):
        if self.num > 0:
            t.left(60)
            t.circle(40, 45)
            # t.circle(-20,90)
            t.write("Tamil Nadu")
        if self.num > 4:
            t.left(40)
            t.forward(28)
            t.write("Kerala")
        if self.num > 9:
            t.right(45)
            t.circle(-40, 45)
            t.forward(20)
            t.write("Karnataka")
        if self.num > 17:
            t.forward(35)
            t.write("Andhra Pradesh")
        if self.num > 21:
            t.forward(50)
            t.write("Telengana")
            t.right(20)
            t.forward(70)
            t.write("Odhisha")
            t.circle(20, 90)
            t.left(45)
        if self.num > 33:
            t.left(20)
            t.forward(100)
            t.write("Maharashtra")
        if self.num > 38:
            t.circle(5, 20)
            t.right(45)
            t.circle(-20, 90)
            t.right(30)
            t.forward(50)
            t.write("Madhya Pradesh")
        if self.num > 50:
            t.right(60)
            t.circle(5, 20)
            t.forward(150)
            t.write("West Bengal")

    """def locate(self,t):
    t.left(90)
    t.forward(30)"""

    @classmethod
    def locplayers(class_name):
        if red_player.num in range(0, 5):
            dispin(redpin, (382, 460))
            dispinloc("Tamil Nadu", (355, 435))
        elif red_player.num in range(5, 10):
            dispin(redpin, (343, 470))
            dispinloc("Kerala", (323, 450))
        elif red_player.num in range(10, 18):
            dispin(redpin, (336, 427))
            dispinloc("Karnataka", (316, 407))
        elif red_player.num in range(18, 22):
            dispin(redpin, (390, 414))
            dispinloc("Andhra Pradesh", (370, 394))
        elif red_player.num in range(22, 34):
            dispin(redpin, (466, 326))
            dispinloc("Odhisa", (446, 306))
        elif red_player.num in range(34, 39):
            dispin(redpin, (338, 376))
            dispinloc("Maharashtra", (308, 356))
        elif red_player.num in range(39, 51):
            dispin(redpin, (348, 313))
            dispinloc("Madhya Pradesh", (328, 293))
        elif red_player.num in range(51, 65):
            dispin(redpin, (382, 460))
            dispinloc("West Bengal", (355, 435))
        elif red_player.num in range(65, 68):
            dispin(redpin, (502, 292))
            dispinloc("Uttar Pradesh", (482, 272))
        elif red_player.num in range(68, 74):
            dispin(redpin, (302, 254))
            dispinloc("Rajasthan", (282, 234))
        elif red_player.num in range(74, 95):
            dispin(redpin, (283, 321))
            dispinloc("Gujarat", (263, 301))
        elif red_player.num in range(95, 99):
            dispin(redpin, (332, 198))
            dispinloc("Punjab", (312, 178))
        elif red_player.num in range(99, 101):
            dispin(redpin, (339, 140))
            dispinloc("Jammu and Kashmir", (319, 120))

        if blue_player.num in range(0, 5):
            dispin(bluepin, (382, 460))
            dispinloc("Tamil Nadu", (355, 435))
        elif blue_player.num in range(5, 10):
            dispin(bluepin, (343, 470))
            dispinloc("Kerala", (323, 450))
        elif blue_player.num in range(10, 18):
            dispin(bluepin, (336, 427))
            dispinloc("Karnataka", (316, 407))
        elif blue_player.num in range(18, 22):
            dispin(bluepin, (390, 414))
            dispinloc("Andhra Pradesh", (370, 394))
        elif blue_player.num in range(22, 34):
            dispin(bluepin, (466, 326))
            dispinloc("Odhisa", (446, 306))
        elif blue_player.num in range(34, 39):
            dispin(bluepin, (338, 376))
            dispinloc("Maharashtra", (308, 356))
        elif blue_player.num in range(39, 51):
            dispin(bluepin, (348, 313))
            dispinloc("Madhya Pradesh", (328, 293))
        elif blue_player.num in range(51, 65):
            dispin(bluepin, (382, 460))
            dispinloc("West Bengal", (355, 435))
        elif blue_player.num in range(65, 68):
            dispin(bluepin, (502, 292))
            dispinloc("Uttar Pradesh", (482, 272))
        elif blue_player.num in range(68, 74):
            dispin(bluepin, (302, 254))
            dispinloc("Rajasthan", (282, 234))
        elif blue_player.num in range(74, 95):
            dispin(bluepin, (283, 321))
            dispinloc("Gujarat", (263, 301))
        elif blue_player.num in range(95, 99):
            dispin(bluepin, (332, 198))
            dispinloc("Punjab", (312, 178))
        elif blue_player.num in range(99, 101):
            dispin(bluepin, (339, 140))
            dispinloc("Jammu and Kashmir", (319, 120))

    def reddispmap(self):
        import turtle
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()
        wn = turtle.Screen()
        t.color("red")
        t.penup()
        t.goto(-98, -250)
        t.pendown()
        t.write("Kanyakumari")
        t.forward(1)
        wn.bgpic("indmap.gif")
        self.locate(t)
        wn.exitonclick()

    def bluedispmap(self):
        import turtle
        turtle.TurtleScreen._RUNNING = True
        t = turtle.Turtle()
        wn = turtle.Screen()
        t.color("blue")
        t.penup()
        t.goto(-98, -250)
        t.pendown()
        t.write("Kanyakumari")
        t.forward(1)
        wn.bgpic("indmap.gif")
        self.locate(t)
        wn.exitonclick()

    def redlocate(self, val):
        if val == 0:
            pass


all_sprites = pygame.sprite.Group()
red_player = Player("red_piece.png", (6, 140), "red")
blue_player = Player("blue_piece.png", (60, 140), "blue")
all_sprites.add(red_player)
all_sprites.add(blue_player)

# Creating button
button = pygame.Rect(25, 550, 40, 40)
# expand
button2 = pygame.Rect(710, 7, 20, 20)
# player1-expand
button3 = pygame.Rect(618, 27, 100, 40)
# player2-expand
button4 = pygame.Rect(622, 73, 100, 40)
# start
button5 = pygame.Rect(180, 265, 100, 50)
# quit
button6 = pygame.Rect(480, 270, 100, 50)
# location on board
button7 = pygame.Rect(180, 75, 490, 490)
# hwtoplay
button8 = pygame.Rect(335, 366, 97, 46)
# game specific variables
running = True
turn = "red"
red_val = 0
blue_val = 0
red_dup_val = 0
blue_dup_val = 0
speak_flag = 0
expandclick = False
startpage = True
piece_count = 0


def hw_play():
    root = tk.Tk()
    root.minsize(740, 640)
    root.maxsize(740, 640)
    image = Image.open("hwtoplay.jpg")
    photo = ImageTk.PhotoImage(image)
    l = tk.Label(image=photo)
    l.pack()
    root.mainloop()


# Game loop
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    screen.fill((0, 255, 195))

    if startpage == True:
        startdisp()
        if speak_flag < 3:
            speak_flag += 1
        if speak_flag == 2:
            speak("Welcome to travel tales ")
            speak("your journey leads to knowledge")
            speak("Learn about indian culture in a fun way")
    else:
        Bck()
        players()
        if turn == "red":
            rollr()
        else:
            rollb()
    # Process input (events)
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            running = False
        elif startpage == True and event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if button5.collidepoint(mouse_pos):
                startpage = False
            elif button8.collidepoint(mouse_pos):
                hw_play()
            elif button6.collidepoint(mouse_pos):
                running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and Player.win == False:
            mouse_pos = pygame.mouse.get_pos()
            if button.collidepoint(mouse_pos):
                die_num, die_img = pickNumber()
                screen.blit(die_img, (30, 450))
                # pygame.mixer.music.load("roll.mp3")
                # pygame.mixer.music.set_volume(0.7)
                # pygame.mixer.music.play(loops=1)
                if turn == "red":
                    turn = "blue"
                    red_dup_val = red_val
                    if die_num == 6 and red_val == 0:
                        turn = "red"
                        red_val = 4
                        # red_val=4
                        red_player.control(red_dup_val, red_val)
                    elif red_val == 95:
                        if die_num <= 5:
                            red_val += die_num
                            red_player.control(red_dup_val, red_val)
                        else:
                            turn = "red"
                    elif red_val == 96:
                        if die_num <= 4:
                            red_val += die_num
                            red_player.control(red_dup_val, red_val)
                        elif die_num == 6:
                            turn = "red"
                    elif red_val == 97:
                        if die_num <= 3:
                            red_val += die_num
                            red_player.control(red_dup_val, red_val)
                        elif die_num == 6:
                            turn = "red"
                    elif red_val == 98:
                        if die_num <= 2:
                            red_val += die_num
                            red_player.control(red_dup_val, red_val)
                        elif die_num == 6:
                            turn = "red"
                    elif red_val == 99:
                        if die_num == 1:
                            red_val += die_num
                            red_player.control(red_dup_val, red_val)
                        elif die_num == 6:
                            turn = "red"
                    elif red_val != 0:
                        red_val += die_num
                        if die_num == 6:
                            turn = "red"
                        red_player.control(red_dup_val, red_val)
                else:
                    turn = "red"
                    blue_dup_val = blue_val
                    if die_num == 6 and blue_val == 0:
                        turn = "blue"
                        blue_val = 4
                        # blue_val=4
                        blue_player.control(blue_dup_val, blue_val)
                    elif blue_val == 95:
                        if die_num <= 5:
                            blue_val += die_num
                            blue_player.control(blue_dup_val, blue_val)
                        else:
                            turn = "blue"
                    elif blue_val == 96:
                        if die_num <= 4:
                            blue_val += die_num
                            blue_player.control(blue_dup_val, blue_val)
                        elif die_num == 6:
                            turn = "blue"
                    elif blue_val == 97:
                        if die_num <= 3:
                            blue_val += die_num
                            blue_player.control(blue_dup_val, blue_val)
                        elif die_num == 6:
                            turn = "blue"
                    elif blue_val == 98:
                        if die_num <= 2:
                            blue_val += die_num
                            blue_player.control(blue_dup_val, blue_val)
                        elif die_num == 6:
                            turn = "blue"
                    elif blue_val == 99:
                        if die_num == 1:
                            blue_val += die_num
                            blue_player.control(blue_dup_val, blue_val)
                        elif die_num == 6:
                            turn = "blue"
                    elif blue_val != 0:
                        blue_val += die_num
                        if die_num == 6:
                            turn = "blue"
                        blue_player.control(blue_dup_val, blue_val)
            elif button2.collidepoint(mouse_pos):
                Player.location()
                expandclick = True
            elif button3.collidepoint(mouse_pos) and expandclick == True and (red_player.answer_flag == 1 or red_val == 0):
                red_player.reddispmap()
                expandclick = False
            elif button4.collidepoint(mouse_pos) and expandclick == True:
                blue_player.bluedispmap()
                expandclick = False
            elif button7.collidepoint(mouse_pos):
                Player.locplayers()

        # Update
    all_sprites.update()

    if red_player.answer_flag == 1:
        red_val = red_player.answer()

    if blue_player.answer_flag == 1:
        blue_val = blue_player.answer()

    if piece_count >= 3:
        all_sprites.draw(screen)

    if startpage == False:
        piece_count += 1
        
    pygame.display.update()
    time.sleep(1.1)
    pygame.display.flip()

pygame.quit()
