#Version 3.0: Changed the Tkinker to Streamlit
#####################################################################
#Import the required libaries
import os, sys, random
import streamlit as st
import pandas as pd

#####################################################################
#This section defins the functions. Each one is to create a different part of the loadout.
def getRandomMission():
    missionArry = ["Inferno", "Decapitation", "Vox Liberatis", "Reliquary", "Fall of Arteus", "Ballistic Engine", "Termination"]
    mission = random.choice(missionArry)
    return mission

#Get a random difficulty. Each difficutly is weighted slightly so that Substantial and Ruthless come up a bit more often
def getRandomDifficutly():
    difficutlyArry = ["Average", "Substantial", "Ruthless", "Lethal"]
    difficutly = str(random.choices(difficutlyArry, weights=(10,17,15,10))[0])
    return difficutly

#Get a random class
def getRandomClass():
    classArry = ["Tactical", "Assault", "Vanguard", "Bulwark", "Sniper", "Heavy"]
    single_class = random.choice(classArry) #I wanted to use class as the var name but that's a reserved term, so single_class it is
    return single_class

#Get a random primary weapon
def getRandomWeapon1(selectedClass):
    if(selectedClass == "Tactical"):
        primaryGunArry = ["Auto Bolt Rifle","Bolt Rifle","Heavy Bolt Rifle","Stalker Bolt Rifle","Bolt Carbine","Plasma Incinerator","Melta Rifle"] 
    elif(selectedClass =="Vanguard"):
        primaryGunArry = ["Instigator Bolt Carbine", "Bolt Carbine","Occulus Bolt Carbine","Melta Rifle"] 
    elif(selectedClass =="Sniper"):
        primaryGunArry = ["Stalker Bolt Rifle","Instigator Bolt Carbine","Bolt Sniper Rifle","Bolt Carbine","Las Fusil"] 
    elif(selectedClass =="Heavy"):
        primaryGunArry = ["Heavy Bolt Rifle", "Heavy Bolter","Heavy Plasma Incinerator", "Multi-Melta","Pyrecannon"]
    elif(selectedClass =="Techmarine"):
        primaryGunArry = ["Auto Bolt Rifle","Bolt Rifle","Heavy Bolt Rifle", "Heavy Plasma Incinerator","Occulus Bolt Carbine"]
    elif(selectedClass =="Assault" or selectedClass =="Bulwark"):
        primaryGunArry = ["None"]

    gun1 = random.choice(primaryGunArry)
    return gun1

#Get a random secondary weapon
def getRandomWeapon2(selectedClass):
    if(selectedClass =="Tactical"):
        secondaryGunArry = ["Bolt Pistol", "Heavy Bolt Pistol", "Plasma Pistol"]
    elif(selectedClass =="Assault"):
        secondaryGunArry = ["Bolt Pistol", "Heavy Bolt Pistol", "Plasma Pistol","Inferno Pistol","Neo-Volkite Pistol"]
    if(selectedClass =="Vanguard"):
        secondaryGunArry = ["Bolt Pistol", "Heavy Bolt Pistol", "Inferno Pistol","Neo-Volkite Pistol"]
    elif(selectedClass =="Bulwark"):
        secondaryGunArry = ["Bolt Pistol", "Heavy Bolt Pistol", "Plasma Pistol","Neo-Volkite Pistol"] 
    elif(selectedClass =="Sniper"):
        secondaryGunArry = ["Bolt Pistol","Heavy Bolt Pistol", "Inferno Pistol"]
    elif(selectedClass =="Heavy"):
        secondaryGunArry = ["Bolt Pistol", "Heavy Bolt Pistol", "Inferno Pistol"]
    elif(selectedClass =="Techmarine"):
        secondaryGunArry = ["Bolt Pistol", "Heavy Bolt Pistol", "Plasma Pistol", "Inferno Pistol", "Neo-Volkite Pistol"]


    gun2 = random.choice(secondaryGunArry)
    return gun2

#Get a random melee weapon
def getRandomMelee(selectedClass):
    if(selectedClass == "Tactical"):
        meleeArry = ["Chainsword", "Combat Knife"]
    elif(selectedClass == "Assault"):
        meleeArry = ["Chainsword", "Thunder Hammer", "Power Fist", "Power Sword", "Power Axe"] 
    elif(selectedClass =="Vanguard"):
        meleeArry = ["Chainsword","Combat Knife", "Power Axe"] 
    elif(selectedClass =="Bulwark"):
        meleeArry = ["Chainsword", "Thunder Hammer","Power Fist", "Power Sword","Power Axe"] 
    elif(selectedClass =="Sniper"):
        meleeArry = ["Combat Knife"] 
    elif(selectedClass =="Techmarine"):
        meleeArry = ["Combat Knife", "Power Sword", "Power Axe", "Omnissiah Axe"]
    elif(selectedClass =="Heavy" or selectedClass =="Bulwark"):
        meleeArry = ["None"]

    gun2 = random.choice(meleeArry)
    return gun2

#Get a random quote
def getRandomQuote():
    #An array full of quotes
    quotesArry = ["No Pity! No Remorse! No Fear! - Chaplain Grimaldus",
    "Only in death does duty end. - Imperium of Man",
    "The difference between heresy and treachery is ignorance. - Inquisition",
    "Knowledge is power, guard it well. - Inquisitor Kryptman",
    "To admit defeat is to blaspheme against the Emperor. - Imperial Guard",
    "Give me a hundred Space Marines. Or failing that, give me a thousand other troops. - Primarch Rogal Dorn",
    "Even in death, I still serve. - Space Marines",
    "Innocence proves nothing. - Inquisition",
    "There is no such thing as innocence, only degrees of guilt. - Inquisition",
    "Pain is an illusion of the senses, despair an illusion of the mind. - Legion of the Damned",
    "I am the hammer, I am the mail about His fist. I am the Spear in His hand. - Space Marines",
    "Hope is the first step on the road to disappointment. - Space Marines",
    "From the moment I understood the weakness of my flesh, it disgusted me. I craved the strength and certainty of steel. - Adeptus Mechanicus",
    "I have no fear, for I am fear incarnate. - Space Marines",
    "Walk softly, and carry a big gun. - Imperial Guard",
    "Brother I am pinned here! - Space Marines",
    "For the Emperor! - Space Marines",
    "An open mind is like a fortress with its gates unbarred and unguarded. - Blood Ravens Librarian",
    "Blessed is the mind too small for doubt. - Imperium of Man",
    "By His will alone is Terra kept safe. - Adeptus Custodes",
    "Ruthlessness is the kindness of the wise. - Lord Solar Macharius",
    "They shall be my finest warriors, these men who give of themselves to me. - The Emperor of Mankind",
    "Suffer not the unclean to live. - Inquisition",
    "What I cannot crush with words, I will crush with the tanks of the Imperial Guard! - Imperial Guard Commander",
    "Victory is but a prelude to the next battle. - Space Marines",
    "Only in death does duty end. - Imperium of Man",
    "Victory is achieved through mettle. Glory is achieved through metal. - Iron Hands Chapter"
    ]

    #Select a random quote, put it in a label
    quote= random.choice(quotesArry)
    return quote

#####################################################################
#This section calls all of the functions to generate the loadout
currentMission = getRandomMission()
currentDifficutly = getRandomDifficutly()
currentClass = getRandomClass()
currentPrimary = getRandomWeapon1(currentClass)
currentSecondary = getRandomWeapon2(currentClass)
currentMelee = getRandomMelee(currentClass)
currentQuote = getRandomQuote()

#####################################################################
#This section creates the streamlit site. First create the text at the top of the page.
st.set_page_config(page_title="Randomized Space Marine 2 Mission Selector") #Set the page title, icon, and layout
st.title("Randomized Space Marine 2 Mission Selector")

#Add the quote
st.markdown(currentQuote,width="stretch")

#Create the table that contains the loadout
loadoutTable = pd.DataFrame(
    {
        "Mission": [currentMission],
        "Difficulty": [currentDifficutly],
        "Class": [currentClass],
        "Primary Weapon": [currentPrimary],
        "Secondary Weapon": [currentSecondary],
        "Melee Weapon": [currentMelee],
    },
    index=["Your Orders:"],
)
st.dataframe(loadoutTable)


#Set up the button to re-roll
st.button("Click for another mission", key="reroll_button")  

# To Do:
# Make a custom font
# <link href="https://fonts.googleapis.com/css2?family=Manufacturing+Consent&display=swap" rel="stylesheet">
# https://fonts.google.com/selection/embed
# https://docs.streamlit.io/develop/tutorials/configuration-and-theming/external-fonts
#
# Get font wrapping working on the table
# This may be simmilar to how I did it for the amazon price tracker
# https://discuss.streamlit.io/t/text-rendering-with-word-wrapping/63517/2



#####################################################################
#This section will fill out the left column. The first step is to create a dictionary with key value pairs. They key is the name of the variable and the value is what the lable with be shown.
#left_label_texts = {
#    "mission_Label":"Your mission is:", 
#    "difficulty_Label":"Your difficulty is:",
#    "class_Label":"Your class is:",
#    "weapon1_Label": "Your primary weapon is:",
#    "weapon2_Label": "Your secondary weapon is:",
#    "weapon3_Label": "Your melee weapon is:"
#}

#For loop that loops through each dictornay value and creates label bassed of each
#for i, (key, text) in enumerate(left_label_texts.items()):  #For each item in the dict reach each key/value
#    label = ttk.Label(window, text=text, font=("Dubai",12), background="#362d3c", foreground="white")    #Create a new label with the info for the current object
#    label.grid(row=i+1, column=0,  padx=5, pady=5, sticky=tk.W) #Put the label on a grid 

#####################################################################
#This section creates the button at the bottom which lets your re-roll your setup.

#button = tk.Button(window, text="Click for another mission", font=("Dubai",12))    #Create a new button with the info for the current object
#button['font'] = 12
#button.grid(column=0, row=7, columnspan=3, padx=5, pady=5) #Put the label on a grid 

#This creates blank arays that will be used in button_press(event) to clear out the loadout and quote 
#resetRightColumnArry = []
#quoteLableArry = []

#####################################################################
#This section creates the check boxes in the right column. It first creates variables for the status of the box, then it creates the box, finally it adds it ot the grid. 
#mission_Check_state = tk.IntVar()
#difficulty_Check_state = tk.IntVar()
#class_Check_state = tk.IntVar()

#check_Box_Mission = tk.Checkbutton(window, text="Mission", variable=mission_Check_state, onvalue=1, offvalue=0, font=("Dubai",12), background="#362d3c", foreground="white")
#check_Box_Difficulty = tk.Checkbutton(window, text="Difficulty", variable=difficulty_Check_state, onvalue=1, offvalue=0, font=("Dubai",12), background="#362d3c", foreground="white")
#check_Box_Class = tk.Checkbutton(window, text="Class", variable=class_Check_state, onvalue=1, offvalue=0, font=("Dubai",12), background="#362d3c", foreground="white")

#check_Box_Mission.grid(column=2, row=1, columnspan=1, padx=5, pady=5) 
#check_Box_Difficulty.grid(column=2, row=2, columnspan=1, padx=5, pady=5)
#check_Box_Class.grid(column=2, row=3, columnspan=1, padx=5, pady=5) 

#####################################################################

#This function adds the loadout to the GUI. It is called on first load and whenever the reroll button is clicked
#def loadCenterText(currentItems):
#    for index, item in enumerate(currentItems):
#        label = ttk.Label(window, text=item, font=("Dubai",12), anchor='w', background="#362d3c", foreground="white")    #Create a new label with the info for the current object
#        label.grid(row=index+1, column=1,  padx=5, pady=5) #Put the label on a grid 
#        resetRightColumnArry.append(label)

#Add the loadout and quote to the grid. This only triggers on first load.
#loadCenterText(center_label_texts)
#currentQuote = getRandomQuote()
#####################################################################
#This will re-roll everything when the re-roll button is pressed
#def button_press(event):
#    print("Button Pressed")

    #These for loops clear out whatever is in the 
 #   for e in resetRightColumnArry:
  #      e.config(text="")

   # for f in quoteLableArry:
    #    f.config(text="")

    #if mission_Check_state.get() == 0:
     #   global currentMission
     #   currentMission = getRandomMission()

   # if difficulty_Check_state.get() == 0:
   #     global currentDifficutly
   #     currentDifficutly = getRandomDifficutly()

   # if class_Check_state.get() == 0:
   #     global currentClass, currentPrimary, currentSecondary, currentMelee
   #     currentClass = getRandomClass()
   #     currentPrimary = getRandomWeapon1(currentClass)
   #     currentSecondary = getRandomWeapon2(currentClass)
   #     currentMelee = getRandomMelee(currentClass)

   # new_center_label_texts = [currentMission, currentDifficutly, currentClass, currentPrimary, currentSecondary,currentMelee]
   # loadCenterText(new_center_label_texts)

    #randomquote()


