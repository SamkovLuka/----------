from tkinter import*

bomb  = 100
score = 0
best_score = 0

press_return = True

def start(event):
    global press_return
    global bomb
    global score
    if not press_return:
       pass
    else:
       bomb = 100
       score = 0
       label.config(text="")
       update_bomb()
       update_score()
       update_display()
       press_return = False

    pass

def update_display():
    global bomb
    global score
    global best_score
    if bomb > 50:
       bomb_label.config(image=normal_photo)
    elif 0 < bomb < 50:
       bomb_label.config(image=no_photo)
    else:
       bomb_label.config(image=bang_photo)
    fuse_label.config(text="Fuse: " +str(bomb))
    score_label.config(text="Score: " +str(score))
    best_score_label.config(text="Best score: "+str(best_score))
    fuse_label.after(100,update_display)
    pass

def update_bomb():
   global bomb
   bomb - 50
   if is_alive():
      fuse_label.after(400,update_bomb)
   pass

def update_score():
    global score
    global best_score
    score += 1
    if is_alive():
       score_label.after(2000, update_score)
       best_score_file = open("best_score.txt","w+")
       best_score_label.config(text="Best score: "+str(score))
       best_score_file.write(f"best score: {str(score)}")
       best_score_label.config(text=f"Best score: "+str(best_score))
       bs = best_score_file.read()
       best_score_label.config(text=f"Best score: "+str(bs))
    pass


def update_best_score():
   global score
   global best_score
   if score>best_score:
      best_score_file = open("best_score.txt","w+")
      best_score_label.config(text=f"Best score: "+ best_score_file.read())
      
      
def click():
  global bomb
  if is_alive():
     bomb+=1
  pass

def is_alive():
   global bomb
   global press_return
   if bomb<=0:
      label.config(text="Bang!Bang!Bang!")
      press_return = True
      return False
   else:
      return True
   pass

root = Tk()
root.title("Bang Bang")
root.geometry("500x550")


label = Label(root,text="Press [Enter] to start the game",font=("Comic Sans MS",12))
label.pack()

fuse_label = Label(root, text="Fuse: " + str(bomb), font=("Comic Sans MS",14))
fuse_label.pack()
score_label = Label(root, text="Score: " + str(score), font=("Comic Sans MS",14))
score_label.pack()


best_score_label  = Label(root,text="Best score: "+str(best_score),font=("Comic Sans MS",14))
best_score_label.pack()

no_photo = PhotoImage(file="img/bomb_no.gif")
normal_photo = PhotoImage(file="img/bomb_normal.gif")
bang_photo = PhotoImage(file="img/pow.gif")


bomb_label = Label(root, image=normal_photo)
bomb_label.pack()



click_button = Button(root, text="Click me",bg="#000000",fg="#ffffff",width=15,font=("Comic Sans MS",14),command=click)
click_button.pack()



root.bind("<Return>",start)
root.mainloop()