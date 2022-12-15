from tkinter import *
from tkinter import ttk

inventory=[]

def livingroom():
  for widget in frm.winfo_children():
    widget.destroy()
  ttk.Label(frm, text="You are now in the living room. The room is dimly lit, but you can make out your surroundings and see a few pieces of furniture around you. On your left is a large leather couch, and to the right you see a small desk with a few drawers. There is a large oriental rug, but overall the room seems to be lacking much decor. Everything looks untouched, as if frozen in a moment in time. While taking in the room, you notice a mysterious safe in the corner, which seems to be locked. In addition, there is a lock on the door which will not budge unless opened with a code. You can't seem to quite remember how you got here, but it seems all you can do know is to escape.",wraplength=300).grid(column=0, row=0, columnspan=3)
  but4 = ttk.Button(frm, text="Look under couch", command=couch).grid(column=0,row=2)
  but5 = ttk.Button(frm, text="Look in drawer", command=drawer).grid(column=0,row=3)
  but6 = ttk.Button(frm, text="Open safe", command=safe1).grid(column=0,row=4)
  but7 = ttk.Button(frm, text="Open lock", command=lock1).grid(column=0,row=5)
  but8 = ttk.Button(frm, text="Give up", command=end).grid(column=1,row=3)
  but13 = ttk.Button(frm, text="Look in dead light bulb", command=deadlightbulb).grid(column=0,row=6)
  but14 = ttk.Button(frm, text="Look behind painting", command=painting).grid(column=0,row=7)
  but100 = ttk.Button(frm, text="Show Inventory", command=inventoryfunc).grid(column=1,row=5)

def inventoryfunc():
  print(inventory)

def end():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You did not escape",wraplength=300).grid(column=0, row=0)

def couch():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You crouch down on your knees to become level with the floor. You look under the couch, but all you see is cobwebs and dust",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but3 = ttk.Button(frm, text="Living Room", command=livingroom).grid(column=0,row=2)
  

def drawer():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You look around the room and notice drawers, you looks through all of the drawers. In one you find a key!",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but3 = ttk.Button(frm, text="Living Room", command=livingroom).grid(column=0,row=2)
  if "Key1" not in inventory:
    but9 = ttk.Button(frm, text="Take Key", command=key1).grid(column=2,row=4)

def key1():
  if "Key1" not in inventory:
    inventory.append("Key1")

def safe1():
  for widget in frm.winfo_children():
    widget.destroy()
  if "Key1" in inventory:
    ttk.Label(frm, text="Once you get the key you try to find a something that this key could open. You find a safe, you turn the key and the safe door swings open. You pull out a piece of paper from the safe, you flip it over and find a code.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    if "Code1" not in inventory:
        but11 = ttk.Button(frm, text="Take Code", command=code1).grid(column=2,row=4)
    but3 = ttk.Button(frm, text="Back to Living Room", command=livingroom).grid(column=0,row=3)
  else:
    ttk.Label(frm, text="You must find a key to unlock this safe",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but3 = ttk.Button(frm, text="Back to Living Room", command=livingroom).grid(column=0,row=3)
  but100 = ttk.Button(frm, text="Show Inventory", command=inventoryfunc).grid(column=2,row=2)

def code1():
    if "Code1" not in inventory:
      inventory.append("Code1")

def lock1():
  for widget in frm.winfo_children():
    widget.destroy()
  if "Code1" in inventory:
    ttk.Label(frm, text="You find a lock on a door with numbers that can be entered in. You enter the code from the safe. You pull down on the lock and it pops open. You open the door which leads to the bedroom.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but3 = ttk.Button(frm, text="Back to Living Room", command=livingroom).grid(column=0,row=2)
    but3 = ttk.Button(frm, text="Enter Bedroom", command=bedroom).grid(column=0,row=3)
  else:
    ttk.Label(frm, text="You must find a code to unlock this safe",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but3 = ttk.Button(frm, text="Back to Living Room", command=livingroom).grid(column=0,row=3)
  but100 = ttk.Button(frm, text="Show Inventory", command=inventoryfunc).grid(column=2,row=2)

def deadlightbulb():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You notice a dead light bulb hanging from the center of the room. Curious, you unscrew it to look for clues. However, there seems to be nothing inside.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but3 = ttk.Button(frm, text="Living Room", command=livingroom).grid(column=0,row=2)


def painting():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You see a painting on one of the walls in the room. It seems to be hanging somehwhat sideways",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but3 = ttk.Button(frm, text="Return to living Room", command=livingroom).grid(column=0,row=2)
    but17 = ttk.Button(frm, text="Inspect the painting", command=inspectpainting).grid(column=0,row=3)

def inspectpainting():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You look behind the painting and notice a switch. You flip it, not sure what it does. Intrigued, you hear what seems like a shift in the wall. It seems the bookcase has moved",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but3 = ttk.Button(frm, text="Living Room", command=livingroom).grid(column=0,row=2)
  but15 = ttk.Button(frm, text="Look behind Bookcase", command=bookcase).grid(column=0,row=3)
  
def bookcase():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You walk over to the bookcase, their appears to be a door behind the book case. You open the door and enter what seems to be an office.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but3 = ttk.Button(frm, text="Living Room", command=livingroom).grid(column=0,row=2)
  but18 = ttk.Button(frm, text="Office", command=office).grid(column=0,row=3)

def bedroom():
  for widget in frm.winfo_children():
    widget.destroy()
  ttk.Label(frm, text="Congragulations, you have found a way out of the livint room. You are now in the bedroom. As you look around, you make note of a large banaster queen bed in the center of the room, and see a closet as wel as a dresser off on one side of the wall. Above the dresser, yu see your reflection staring back at you in a hanging mirror. As you make your way around the room, you hear the sound of creaky floorboards, as if some have recently been moved slightly out of place. As you take a minute to think of where to go next, you are met with the weird sensation that makes you feel like someone is watching you. Warning, be careful - trying to open locks may be more difficult, and you should think twce before trying to unlock something you do not think you have the code for.",wraplength=300).grid(column=0, row=0, columnspan=3)
  but19 = ttk.Button(frm, text="Look under bed", command=livingroom).grid(column=0,row=2)
  but20 = ttk.Button(frm, text="Look under floorboards", command=livingroom).grid(column=0,row=3)
  but21 = ttk.Button(frm, text="Look behind Mirror", command=livingroom).grid(column=0,row=4)
  but22 = ttk.Button(frm, text="Open lock", command=lock1).grid(column=0,row=5)
  but8 = ttk.Button(frm, text="Give up", command=end).grid(column=1,row=3)
  but100 = ttk.Button(frm, text="Show Inventory", command=inventoryfunc).grid(column=1,row=5)

def office():
  for widget in frm.winfo_children():
    widget.destroy()
  ttk.Label(frm, text="Congragulations, you have found a way out of the living room. You have now entered the office. As you look around, you see a large mahogany desk near the center of the room. There is a chair next to it, and a large high-tech computer on top. The only other thing in the room is a mysterious door in the corner, which seems to have no purpose.",wraplength=300).grid(column=0, row=0, columnspan=3)
  but28 = ttk.Button(frm, text="Look under desk", command=underdesk).grid(column=0,row=2)
  but29 = ttk.Button(frm, text="Log into computer", command=computer).grid(column=0,row=3)
  but8 = ttk.Button(frm, text="Give up", command=end).grid(column=1,row=3)
  but100 = ttk.Button(frm, text="Show Inventory", command=inventoryfunc).grid(column=1,row=5)

def underdesk():
  for widget in frm.winfo_children():
    widget.destroy()
  ttk.Label(frm, text="You quickly walk over to the desk in hopes to get out of this place as fast as possible. Their are several drawers but nothing in them. You kneel on the groud to see if their is anything else under the desk and you find a button. You press the button and it releases some kind of password.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but26 = ttk.Button(frm, text="Office", command=office).grid(column=0,row=2)
  if "password1" not in inventory:
        but27 = ttk.Button(frm, text="Take password", command=code1).grid(column=2,row=4)
    
def computer():
   for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You sit down on the desk thinking to yourself what this password can open, then suddenly a window on the computer appears asking for a password. You enter the password and it opens the computer! Their are several tabs open on the computer that you click through, hoping they would help you escape this mansion. None of them seem to be useful, but you finally get to the last tab and find a blueprint.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but26 = ttk.Button(frm, text="Office", command=office).grid(column=0,row=2)
    but32 = ttk.Button(frm, text="Inspect blueprint", command=blueprint).grid(column=0,row=3)

def blueprint():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You look through the blueprint and see that their is a secret door under the carpet in the office.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but26 = ttk.Button(frm, text="Office", command=office).grid(column=0,row=2)
    but30 = ttk.Button(frm, text="Inspect Carpet", command=carpet).grid(column=0,row=3)

def carpet():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You pull the carpet off to the side and find a rusted door.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but26 = ttk.Button(frm, text="Office", command=office).grid(column=0,row=2)
    but30 = ttk.Button(frm, text="Open door", command=behinddoor).grid(column=0,row=3)

def behinddoor():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="Through the door is an underground tunnel. You hop into the pitch black tunnel grasping to the sides of the walls afraid you are going to fall. At the end of the tunnel you find a door nailed shut and a hammer next to it. You start to pull the nails off the door, once you finished you open the door.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but33 = ttk.Button(frm, text="Grab the hammer", command=hammer).grid(column=0,row=2)

def hammer():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You use the hammer to pull the nails off the door one by one. But it is taking you a while since you can't see where they are, you have to use your hands to find each nail. Finally you pull all the nails off.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but33 = ttk.Button(frm, text="Look behind door", command=behinddoor2).grid(column=0,row=2)

def behinddoor2():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You grab the rusted handle and look around. All you see is a necklace with a locket and a safe.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but36 = ttk.Button(frm, text="Inspect safe", command=inspectsafe2).grid(column=0,row=2)
  but37 = ttk.Button(frm, text="Inspect Necklace", command=necklace).grid(column=0,row=3)
  but100 = ttk.Button(frm, text="Show Inventory", command=inventoryfunc).grid(column=2,row=2)

def necklace():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="You open the locket to find a key inside. You bring the key over to the safe.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but3 = ttk.Button(frm, text="Back to Room", command=behinddoor2).grid(column=0,row=2)
  if "locketkey" not in inventory:
    but41 = ttk.Button(frm, text="Take Key", command=locketkey).grid(column=2,row=4)

def locketkey():
  if "locketkey" not in inventory:
    inventory.append("locketkey")

def inspectsafe2():
  for widget in frm.winfo_children():
    widget.destroy()
  if "locketkey" in inventory:
    ttk.Label(frm, text="You look back over to the safe, possibly this key could open the safe.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but42 = ttk.Button(frm, text="Open Safe", command=insidesafe2).grid(column=0,row=2)
  else:
    ttk.Label(frm, text="You try to open the safe but it won't budge, their seems to be a key hole. You may need a key to open this safe.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)
    but30 = ttk.Button(frm, text="Back to Room", command=behinddoor2).grid(column=0,row=3)
  but100 = ttk.Button(frm, text="Show Inventory", command=inventoryfunc).grid(column=2,row=2)
    

def locketkey():
  if "locketkey" not in inventory:
    inventory.append("locketkey")

def insidesafe2():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="There is nothing inside the safe except for some dusted cob webs crowded in the corner. This path seems to be a dead end.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but30 = ttk.Button(frm, text="Back to tunnel", command=tunnel).grid(column=0,row=2)

def tunnel():
  for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="Infuriated by th edead end, you walk back into the tunnel trying to see if their was anything you missed when walking through the tunnel before. Again you grasp to the sides but this time you feel a lever on the side.",wraplength=300).grid(column=0, row=0)
  ttk.Label(frm).grid(column=0, row=1)
  but33 = ttk.Button(frm, text="Pull lever", command=lever).grid(column=0,row=2)

def lever():
   for widget in frm.winfo_children():
    widget.destroy()
    ttk.Label(frm, text="The lever opens a door to a boiler room.",wraplength=300).grid(column=0, row=0)
    ttk.Label(frm).grid(column=0, row=1)


 

root = Tk()
frm = ttk.Frame(root, padding=10)
frm.grid()
ttk.Label(frm, text="Rules:  To play this game, you or a group of people can collaborate to escape the mansion. In order to escape the mansion, you must solve puzzles in order to exit each room and move forward. Make sure to inspect different things in order to discover keys, find codes, and make your way out. If you find something you think will aid you in your goal, make sure to take it in order to add it to your inventory. In order to acess your inventory at any point, click show inventory, and you will be able to see what things you have already picked up. If at any point you are unable to proceed, you may give up, exiting the game, and failing to escape the mansion. Now, good luck escaping the mansion, you will need it.",wraplength=300).grid(column=0, row=0)
ttk.Label(frm).grid(column=0, row=1)
ttk.Label(frm, text="Goal: Escape The mansion by finding keys, unlocking codes, and discovering different rooms",wraplength=300).grid(column=0, row=4)
ttk.Label(frm).grid(column=0, row=5)
ttk.Label(frm, text="Intro: You wake up in a room that you have never seen before. Disoriented you try and remember how you got here, but nothing comes to mind. Their seems to be no direct way to get out, all of the doors are locked. In a panic you came to the conlsuion that you are going to have to try to escape.",wraplength=300).grid(column=0, row=6)
ttk.Label(frm).grid(column=0, row=7)
ttk.Label(frm, text="Would you like to proceed?",wraplength=300).grid(column=0, row=8)
ttk.Label(frm).grid(column=0, row=9)
but1 = ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=11)
but2 = ttk.Button(frm, text="Enter Living Room", command=livingroom).grid(column=0,row=10)
root.mainloop()
print ("You failed to escape the mansion")