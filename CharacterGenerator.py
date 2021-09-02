from tkinter import * #Allows user interface creation
import tkinter #UI
import random #Allows randomly creating numbers
import Info #Subprogram
import csv #Read csv files
import math #Use math functions
import os #Used for printing  

window = Tk() #Create a tkinter window
window.title("Character Creator") #Set the title of the window
window.geometry("1280x950") #Sets the resolution of the window
window.resizable(width=False, height=False) #Make the window non resizable
window.iconbitmap('Sword.ico') #Sets the window icon
window["bg"] = "white" #Sets the background colour of the window
fonttype = "Piranesi It BT" #Sets the default font that I will use
fontsize = 18 #Sets the default font size

#------------[backgroundimage    ,ButtonColor, ActiveColor, Text, topleft
themes = [   ["ForestBackground.png","#4A4A25","#78783C", "white","black"],["PalaceGrassland.png","#626E55","#9CAA89","white","#29464A"],
             ["VolcanicLair.png","#893004","#E25006","white","#29464A" ],["MedievalCity.png","#235079","#4089C4", "white","black"],
             ["FlowerForest.png","#754579","#DD85E5", "white","black"],["MushroomVillage.png","#384d78","#6e87b4","white","#29464A"],
             ["IceDragon.png","#3b7d89","#64aab4", "white","black"] ]
#contains a list of preset resources and colours for when a random theme is picked

randomtheme = random.randint(0,(len(themes)-1)) #Picks a random number based on the number of items in the themes list

c_background = themes[randomtheme][0] #Sets the background to the picture chosen in the list
c_button = themes[randomtheme][1] #A variable containing a hex value that all buttons in the program wil have as their colour
c_active = themes[randomtheme][2] #A variable containing a hex value that all buttons will have as their active colour
c_text = themes[randomtheme][3] # A variable containing a hex value of what colour the text will be

#________________________________________________________
def proficiency(background,ypos): #Sets the proficiencies
    for child in window.winfo_children(): #Loops through all widgets
        if child.winfo_y() == ypos and child.winfo_x() == 15: #Verifys the widgets position
            child.configure(bg=c_active) #Changes background colour to active
        elif child.winfo_y() != ypos and child.winfo_x() == 15: 
            child.configure(bg=c_button) #Changes background colour to normal
    #Clearing--------------------
    while not backglist.get(0)=="": #While background list has something in
        backglist.delete(0) #Delete value in background list
    while not prolist.get(0)=="": #While proficiency list has something in
        prolist.delete(0) #Delete value in proficiency list 
    #----------------------------
    backglist.insert(END,background.split("-")[0]) #Insert name of background
    value1,value2 = Info.CheckProficiencies(background) #Set values as corresponding proficiencies
    prolist.insert(END,value1) #Insert values into proficiency list
    prolist.insert(END,value2)
    #---Sending to Equipment function---#
    StartingEquipment() #Call the Starting Equipment function

    
def StartingEquipment(): #Sets the default equipment
    backgroundvalue = str(backglist.get(0)) #Gets the background selected
    chosenclass = str(classlist.get(0)) #Gets class selected
    #Clearing--------------------
    while not equiplist.get(0)=="": #While equipment listbox has something in
        equiplist.delete(0) #Delete value in equipment listbox
    #----Background-----#
    if backgroundvalue: #If a background has been selected
        b_startingequip = Info.DefaultBackgroundEquipment(backgroundvalue[0:7])
         #Get the equipments for each background
        if b_startingequip != "": #If the background has equipment 
            for index in range(0,len(b_startingequip)): #Loop through the equipment
                if b_startingequip[index] != "":
                    equiplist.insert(END,b_startingequip[index]) #Add to listbox
    #-------Class-------#
    if chosenclass: #If a class has been selected
        c_startingequip = Info.DefaultClassEquipment(chosenclass.split(' ')[0])
        if c_startingequip: #If there is an equipment value
            for index in range(0,len(c_startingequip)): #Loop through equipment
              if c_startingequip[index] != "": 
                    equiplist.insert(END,c_startingequip[index]) #Add to listbox
    #------Chosen Equipment-------#
    for child in window.winfo_children(): #Loop through widgets
        if isinstance(child, tkinter.Button): #If widget is button
            if child.winfo_x() == 642 and child.cget('bg') == c_active: #If it is selected
                equiplist.insert(END,child.cget('text')) #Insert button's text to listbox



def EquipmentChoice(choice,subindex,valueindex): #Allows user choice of equipment
    equipchoice = Info.ClassEquipment(classlist.get(0).split(" ")[0]) #Get equipment from subprogram
    
    for child in window.winfo_children():#Loop through widgets
        if isinstance(child, tkinter.Button): #If widget is a button
            if child.cget('text') == choice and child.winfo_x() == 642: #If button is the chosen equipment
                child.configure(bg=c_active) #Set to active
            elif (child.winfo_x() == 642) and (child.cget('text') in (equipchoice[subindex])) and (child.cget('text') != choice):
                #else if button's text is not chosen equipment
                child.configure(bg=c_button) #Set to normal colour
    StartingEquipment() #Call the startingequipment function
                        

def ChosenClass(playerclass,ypos): #When a class is chosen from the dropdown
    for child in window.winfo_children(): #Loops through widgets
        if child.winfo_y() == ypos and child.winfo_x() == 226: #If selected button is found
            child.configure(bg=c_active) #Set it to active
        elif child.winfo_y() != ypos and child.winfo_x() == 226: #else
            child.configure(bg=c_button) #Set it to normal
    #Clearing--------------------
    while not classlist.get(0)=="": #While class listbox isn't empty
        classlist.delete(0) #Delete contents
    #----------------------------
    classlist.insert(END,playerclass.split(" ")[0])  #Insert chosen class into listbox
    
    if topbuttons[3] == 0: #If the equipment menu is closed
        CreateNew("Equipment") #Call the Create New dropdown function
    elif topbuttons[3] == 1: #Else
        CreateNew("Equipment") #Close it
        CreateNew("Equipment") #Open it again with new values
    #---Sending to Equipment function---#
    StartingEquipment() #Call the starting equipment function

    classimgport = PhotoImage(file=playerclass.split(' ')[0]+"Portrait.png") #Set the portrait to the class name
    classportrait.config(image=classimgport) #Set the classportrait widget's image to the class portrait
    classportrait.image = classimgport 

def ChosenRace(race,ypos): #When a race is chosen from the dropdown
    for child in window.winfo_children(): #Loop through widgets
        if child.winfo_y() == ypos and child.winfo_x() == 432: #If button selected is found
            child.configure(bg=c_active) #Set to active
        elif child.winfo_y() != ypos and child.winfo_x() == 432 and child.winfo_y() < 500: #Else reset
                                                                    #and reset sub-race colours
            child.configure(bg=c_button) #Set to normal colour

        if child.winfo_y() >= 505 and child.winfo_x() == 432 or child.winfo_y() == 500 and child.winfo_x() == 428:
            child.destroy() #Destroy sub-races labels
        #if child.winfo_y() == 465  and child.winfo_x() == 1080:
    #Clearing--------------------
    while not racelist.get(0)=="": #While there is a race in the listbox        
        racelist.delete(0) #Delete it
    while not subracelist.get(0)=="": #While there is a subrace in the listbox       
        subracelist.delete(0) #Delete it
    #----------------------------
    racelist.insert(END,race.split(" ")[0]) #Insert the race into the listbox
    CalculateRaceMod() #Calls the calculate race mod function
    raceimgport = PhotoImage(file=race+"Portrait.png") #Sets the portrait to the race name
    raceportrait.config(image=raceimgport) #Sets the raceportrait widget's image to the race portrait
    raceportrait.image = raceimgport
    #--------------------------------------Creating Subraces------------------------------------------------#
    if not race.split(" ")[0] in ("Half-Elf","Half-Orc","Tiefling"): #If the race doesn't == those 3 subraces
        subracelistinfo = Info.SubRaceList(race.split(" ")[0]) #Retrieve the subraces for the race
        s_framebackpanel = Frame(window,bg="#000000",borderwidth=4) #Create a backpanel frame
        s_framebackpanel.place(x=428,y=500,relwidth=0.165,relheight=0.055*(len(subracelistinfo))   )
        for index in range(0,len(subracelistinfo)): #Loop through the subraces
            button = Button(window,bg=c_button,relief="sunken",fg=c_text,font=("Verdana",9),bd=2 #Create a subrace button
                                    ,text=subracelistinfo[index],justify="center",activebackground=c_active # for each
                                    ,command= lambda index=index:ChosenSubrace(subracelistinfo[index],505+(47*index))    )
            button.place(x=432,y=505+(47*index),relwidth=0.157,relheight=0.05)
    else: #if race == Half elf, half orc or tiefling"
        subracelist.insert(END,"N/A") #Set subrace to "N/A" as there are no subraces for them
            

def ChosenSubrace(subrace,ypos): #When a subrace is chosen from the dropdown
    for child in window.winfo_children(): #Loop through widgets
        if child.winfo_y() == ypos and child.winfo_x() == 432: # If button selected is found
            child.configure(bg=c_active)#Set to active
        elif child.winfo_y() != ypos and child.winfo_x() == 432 and child.winfo_y() > 500: #Else
            child.configure(bg=c_button) #Set to normal
    #Clearing--------------------
    while not subracelist.get(0)=="": #If subrace listbox is not empty
        subracelist.delete(0) #Delete contents
    #----------------------------
    subracelist.insert(END,subrace.split(" ")[0]) #insert subrace into listbox
    CalculateRaceMod() #Call calculate race mod function

def CalculateRaceMod(): #When the race chosen changes
    with open('racial bonus data.csv') as racesheet: #Open the racial bonuses csv file
        csv_reader = csv.reader(racesheet, delimiter=',') #Create a csv reader
        chosenline = [] 
        for row in csv_reader: #Loop through all the rows
            if subracelist.get(0) == "" or racelist.get(0) == "Dragonborn": #No subrace data
                if (row[0] == racelist.get(0)): #If the name field of the record is the race chosen
                    chosenline = row #Save the row
                    break
            else: #Subrace
                if (row[0] == racelist.get(0)+" ("+subracelist.get(0)+")"): #Get the race + (subrace)
                    chosenline = row #Save the row
                    break
        racialbonuslist = []  #Create a blank list
        for child in window.winfo_children(): #Loop through widgets
            if child.winfo_x() == 1082: #If widget has x position 1082
                racialbonuslist.append(child) #Add it to the racialbonuslist
        widgetindex = 1 #Set the index to start at 1
        for widget in racialbonuslist: #Loop through all widgets in the list
            widget.config(text=chosenline[widgetindex]) #Set the widget's text to the row's corresponding column
            if widget.cget('text') == "": #If the widget has text
                widget.config(text="0") #Set the text as 0
            widgetindex += 1 #Incremement the index by 1
    TotalPointsCalc("","","","","") #Call the total points calc function and send 5 empty parameters

def SkillPointCalc(value,attribute,ypos): #Calculates skill points
    #value = input (1 or -1) when pressing (+ or -)
    totalpoints = ""
    abscore = ""
    racebonus = ""
    
    for child in window.winfo_children(): #Loops through widgets
        if child.winfo_y() == ypos and child.winfo_x() == 1200: #If widget is at y=ypos and x=1200
            totalpoints = child #set totalpoints to widget
        if child.winfo_y() == ypos and child.winfo_x() == 1018: #if widget is at y=ypos and x=1018
            abscore = child ##ABILITY SCORE - + NOT ABILITY MODIFIER
        if child.winfo_y() == ypos and child.winfo_x() == 1082: #if widget is at y=ypos and x=1082
            racebonus = child #set racebonus to widget

    if ((int(abscore.cget('text'))+value) >= 8) and ((int(abscore.cget('text'))+value) <= 15):
        #if ability score is greater than 7 and less than 16
        pointcosts = {8:  1,  #Points vs costs
                      9:  1,
                      10: 1,
                      11: 1,
                      12: 1,
                      13: 1,
                      14: 2,
                      15: 2 }
        
        abilityscore = str((int(abscore.cget('text')))) #Set ability score to the ability score value as a string
        currentpointsleft = int(pointslabel.cget('text').split(':')[1].split('/')[0])
        cost = int(pointcosts.get((int(abilityscore))+value)) #Get the point cost for the ability score + input
        if value == -1: #If subtracting
            cost = int(pointcosts.get(int(abilityscore))) #Cost is the point cost for the ability score 
        if (currentpointsleft - cost >= 0) or value == -1: #If there are points left or a subtraction has been done
            abscore.configure(text= str((int(abscore.cget('text')))+value)) #Ability score is ability score + input
            pointslabel.configure(text= "Remaining Points:\n"+ str(currentpointsleft-(cost*value))+"/27")
            #Calculate the remaining points value
            TotalPointsCalc(attribute,ypos,totalpoints,abscore,racebonus)
            #Call the Total Points Calc function 

def TotalPointsCalc(attribute,ypos,totalpoints,abscore,racebonus): #Calculate the total points values for each attribute
    if attribute == "": #do everything
        abilityscorelist = []
        racialbonuslist = []
        totalpointslist = []
        abmodlist = []
        for child in window.winfo_children(): #Loop through all widgets
            if child.winfo_x() == 1018: #if widget is an ability score label
                abilityscorelist.append(child) #Add to list
            if child.winfo_x() == 1082: #if widget is a racial bonus label
                racialbonuslist.append(child) #Add to list
            if child.winfo_x() == 1200: #if widget is a total points label
                totalpointslist.append(child) #Add to list
            if child.winfo_x() == 1140: #if widget is an ability modifier label
                abmodlist.append(child) #Add to list
        for index in range(len(abilityscorelist)): #Loop through length of ability score list 
            totalpointslist[index].config(text=str(int(abilityscorelist[index].cget('text'))+int(racialbonuslist[index].cget('text'))))
            #Total points = abilility score + racial bonus
            abmodlist[index].config(text = str(math.floor((int(totalpointslist[index].cget('text'))-10)/2)))
            #ability modifier = total points - 10 / 2 then rounded down
    else: #Specific attribute
        totalpoints.config(text= str( int(abscore.cget('text')) + int(racebonus.cget('text')) )  )
        #Total points = ability score + racial bonus
        for child in window.winfo_children(): #Loop through all widgets
            if child.winfo_x() == 1140 and child.winfo_y() == ypos: #if widget has x=1140 and y = ypos
                child.config(text = str(math.floor((int(totalpoints.cget('text'))-10)/2)))
                #Set widget text to total points - 10 / 2 then rounded
    return totalpointslist,abmodlist
        
                 
topbuttons = [0,0,0,0] #Sets a list of values that represent if the top buttons are active or not
def CreateNew(object): #Function for creating a dropdown
#________________________________
    if object == "Background": #1  #Creates a background dropdown
        if topbuttons[0] == 0: #If the 1st value in topbuttons is off
            topbuttons[0] = 1 #Set it on
            BackgroundInfo = Info.BackgroundInfoFunction() #Retrieve the info on backgrounds
            b_framebackpanel = Frame(window,bg="#000000",borderwidth=4)#Create a backpanel
            b_framebackpanel.place(x=10,y=65,relwidth=0.165,relheight=0.9)
            for index in range(0,len(BackgroundInfo)): #Loop through all of the background info entries
                button = Button(window,bg=c_button,relief="sunken",fg=c_text,font=("Verdana",9),bd=2 #Create a button
                                    ,text=BackgroundInfo[index],justify="center",activebackground=c_active
                                ,command= lambda index=index:proficiency(BackgroundInfo[index],70+(47*index))    )
                button.place(x=15,y=70+(47*index),relwidth=0.155,relheight=0.05) #Places the button
                if (BackgroundInfo[index]).split('-', 1)[0] == (backglist.get(0)): #If the button's background
                                                                   #is equal to the background selected
                    button.config(bg=c_active) #Make the background colour active
        else: #Close off
            topbuttons[0] = 0 #Set the 1st value in topbuttons off
            for child in window.winfo_children(): #Loop through all widgets
                if (child.winfo_x() == 15) or (child.winfo_class() == "Frame" and child.winfo_x() == 10):
                    #Checks if the button is at x position of 15, or is the backpanel
                    child.destroy() #Destroy the widget
#________________________________
    elif object == "Class": #2  #Creates a class dropdown
        if topbuttons[1] == 0: #If the 2nd value in topbuttons is off
            topbuttons[1] = 1 #Set it on
            ClassInfo = Info.ClassList() #Retrieve the info on classes
            c_framebackpanel = Frame(window,bg="#000000",borderwidth=4)
            c_framebackpanel.place(x=219,y=65,relwidth=0.165,relheight=0.605)
            for index in range(0,len(ClassInfo)): #Loop through all the class info entries
                button = Button(window,bg=c_button,relief="sunken",fg=c_text,font=("Verdana",9),bd=2
                                    ,text=ClassInfo[index],justify="center",activebackground=c_active
                                ,command= lambda index=index: ChosenClass(ClassInfo[index],70+(47*index)) ) 
                button.place(x=226,y=70+(47*index),relwidth=0.155,relheight=0.05) #Create a button
                if (ClassInfo[index]).split('-', 1)[0] == (classlist.get(0)):#If the button's class
                                                                   #is equal to the class selected
                    button.config(bg=c_active) #Set button colour to active
        else:
            topbuttons[1] = 0 #Set the value off
            for child in window.winfo_children():
                if (child.winfo_x() == 226) or (child.winfo_class() == "Frame" and child.winfo_x() == 219):
                    child.destroy() #Destroy if x = 226 or if is frame and x=219
#________________________________
    elif object == "Race": #3  #Creates a race dropdown
        if topbuttons[2] == 0: #If the 3rd value in topbuttons is off
            topbuttons[2] = 1 #Set it on
            RaceInfo = Info.RaceList() #Retrieve the info on races
            r_framebackpanel = Frame(window,bg="#000000",borderwidth=4)
            r_framebackpanel.place(x=428,y=65,relwidth=0.165,relheight=0.457)
            for index in range(0,len(RaceInfo)): #Loop through all the race info entries
                button = Button(window,bg=c_button,relief="sunken",fg=c_text,font=("Verdana",9),bd=2
                                ,command=lambda index=index:ChosenRace(RaceInfo[index].split(' ', 1)[0],70+(47*index))
                                ,text=RaceInfo[index].split(' ',1)[0],justify="center",activebackground=c_active)
                button.place(x=432,y=70+(47*index),relwidth=0.157,relheight=0.05)#Create a button
                if (RaceInfo[index].split(' ', 1)[0]) == racelist.get(0) != "":#If the race's background
                                                                   #is equal to the race selected
                    button.config(bg=c_active) #Set button colour to active

        else:
            topbuttons[2] = 0 #Set the value off
            for child in window.winfo_children():
                if (child.winfo_x() == 428 and child.winfo_class() == "Frame") or child.winfo_x() == 432:
                    child.destroy() #Destroy if x = 428 or if is frame and x=432
            
#________________________________
    elif object == "Equipment": #4  #Creates a equipment dropdown
        if classlist.get(0) != "": #If a class has been selected
            if topbuttons[3] == 0: #If the 4th value in topbuttons is off
                topbuttons[3] = 1 #Set it on
                equipchoice = Info.ClassEquipment(classlist.get(0).split(" ")[0]) #Retrieve the info on equipment
                e_framebackpanel = Frame(window,bg="#000000",borderwidth=4) #Create a backpanel frame
                totaloffset = 0 #combined value of how much to offset from the top
                for sublistindex in range(0,len(equipchoice)): #Loop through all the equipment info entries
                    for valueindex in range(0,len(equipchoice[sublistindex])):
                        button = Button(window,bg=c_button,relief="sunken",fg=c_text,font=("Verdana",9),bd=2
                                ,text=equipchoice[sublistindex][valueindex],justify="center",activebackground=c_active
                                ,command=lambda sublistindex=sublistindex, valueindex=valueindex:EquipmentChoice(equipchoice[sublistindex][valueindex],sublistindex,valueindex) )
                        button.place(x=642,y=70+totaloffset,relwidth=0.157,relheight=0.05)
                        totaloffset += 47
                    totaloffset += 10
                e_framebackpanel.place(x=637,y=65,relwidth=0.165,height=totaloffset )
            else:   
                topbuttons[3] = 0 #Set the value off
                for child in window.winfo_children():
                    if (child.winfo_x() == 637 and child.winfo_class() == "Frame") or child.winfo_x() == 642:
                        child.destroy()


#-----------------    
img = PhotoImage(file=c_background)
backgroundimage = Label(window,width="0",height="0",bg="white",image = img)
backgroundimage.place(x=0,y=0,relwidth=1,relheight=1) #Creates and places a background image

t_background = Button(window,bg=c_button,fg="white",bd=4,relief="solid", #Creates and places the background button and connects it to a function
                text = "Background",font=(fonttype,fontsize,"bold"),activebackground=c_active,activeforeground="white", command= lambda:CreateNew("Background") )
t_background.place(x=10,y=19,relwidth = 0.165, relheight = 0.05)
t_class = Button(window,bg=c_button,fg="white",bd=4,relief="solid", #Creates and places the class button and connects it to a function
                text = "Class",font=(fonttype,fontsize,"bold"),activebackground=c_active,activeforeground="white", command=lambda:CreateNew("Class"))
t_class.place(x=219,y=19,relwidth = 0.165, relheight = 0.05)
t_race = Button(window,bg=c_button,fg="white",bd=4,relief="solid", #Creates and places the race button and connects it to a function
                text = "Race",font=(fonttype,fontsize,"bold"),activebackground=c_active,activeforeground="white",command=lambda:CreateNew("Race") )
t_race.place(x=428,y=19,relwidth = 0.165, relheight = 0.05)
t_equipment = Button(window,bg=c_button,fg="white",bd=4,relief="solid", #Creates and places the equipment button and connects it to a function
                text = "Equipment",font=(fonttype,fontsize,"bold"),activebackground=c_active,activeforeground="white",command=lambda:CreateNew("Equipment"))
t_equipment.place(x=637,y=19,relwidth = 0.165, relheight = 0.05)


#----Overview----------------------

overviewlabel = Label(window,width="14",height="1",bg=c_button,fg="white",borderwidth=4,relief="solid", #Creates an overview label
                              text="Character Overview",font=(fonttype,fontsize,"bold"),activebackground=c_active,activeforeground="white")
overviewlabel.place(x=860,y=19,relwidth = 0.3,relheight = 0.04) #Places the overview label

namelabel = Label(window,text="Name",font=(fonttype,fontsize,"bold"),bg=c_button,fg="white",borderwidth=3
                  ,relief="solid").place(x=880,y=70,relwidth=0.07,relheight=0.04) #Creates and places a name label
nameentry = Entry(window,bg=c_button,bd=3,fg="white",font=("Verdana",fontsize)) #Creates an entry box for name input
nameentry.place(x=970,y=70,relwidth=0.185,relheight=0.04) #Places the entry box

genderlabel = Label(window,text="Gender",font=(fonttype,fontsize,"bold"),bg=c_button,fg="white" #Creates and places a "gender" label
                 ,borderwidth=3,relief="solid").place(x=880,y=105,relwidth=0.07,relheight=0.04)
genderentry = Text(window,bg=c_button,bd=3,fg="white",font=("Verdana",fontsize)) #Creates a text box for age input
genderentry.place(x=970,y=105,relwidth=0.185,relheight=0.04) #Places the text box

agelabel = Label(window,text="Age",font=(fonttype,fontsize,"bold"),bg=c_button,fg="white" #Creates and places an "age" label
                 ,borderwidth=3,relief="solid").place(x=880,y=140,relwidth=0.07,relheight=0.04)
ageentry = Text(window,bg=c_button,bd=3,fg="white",font=("Verdana",fontsize)) #Creates a text box for age input
ageentry.place(x=970,y=140,relwidth=0.185,relheight=0.04) #Places the text box

prolistlabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="Skill Proficiencies",borderwidth=3).place(x=880,y=185,relwidth=0.256,relheight=0.03)
prolist = Listbox(window,width="20",height="25",bg=c_button,highlightcolor=c_active,borderwidth=4,relief="solid", #Creates a list box for skill proficiencies
                  fg="white",highlightthickness=0,font=("Verdana",14),selectbackground=c_active) 
prolist.place(x=880,y=210,relwidth=0.256,relheight=0.1) #Places the list box

chosenbackgroundlabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="Background",borderwidth=3)
chosenbackgroundlabel.place(x=880,y=310,relwidth=0.135,relheight=0.03) #Creates a background label
backglist = Listbox(window,width="20",height="25",bg=c_button,justify="center",highlightcolor=c_active,borderwidth=3,
                    relief="solid",fg="white",highlightthickness=0,font=("Verdana",15),selectbackground=c_button)
backglist.place(x=880,y=335,relwidth =0.135,relheight = 0.035) #Places the background listbox

chosenclasslabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="Class",borderwidth=3)
chosenclasslabel.place(x=1060,y=310,relwidth=0.115,relheight=0.03) #Creates a class label
classlist = Listbox(window,width="20",height="25",bg=c_button,justify="center",highlightcolor=c_active,borderwidth=3,
                    relief="solid",fg="white",highlightthickness=0,font=("Verdana",15),selectbackground=c_button)
classlist.place(x=1060,y=335,relwidth =0.115,relheight = 0.035) #Places the class listbox

equipmentlabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="Equipment",borderwidth=3)
equipmentlabel.place(x=880,y=375,relwidth=0.15,relheight=0.03) #Creates an equipment label
equiplist = Listbox(window,width="20",height="25",bg=c_button,justify="center",highlightcolor=c_active,borderwidth=3,
                    relief="solid",fg="white",highlightthickness=0,font=("Verdana",12),selectbackground=c_button)
equiplist.place(x=880,y=400,relwidth =0.15,relheight = 0.18) #Places the equipment listbox

chosenracelabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="Race",borderwidth=3)
chosenracelabel.place(x=1080,y=375,relwidth=0.1,relheight=0.03) #Creates a race label
racelist = Listbox(window,width="20",height="25",bg=c_button,justify="center",highlightcolor=c_active,borderwidth=3,
                   relief="solid",fg="white",highlightthickness=0,font=("Verdana",15),selectbackground=c_button)
racelist.place(x=1080,y=400,relwidth =0.1,relheight = 0.035) #Creates a race input box

chosensubracelabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="Sub-race",borderwidth=3)
chosensubracelabel.place(x=1080,y=440,relwidth=0.1,relheight=0.03) #Creates a Sub-race label
subracelist = Listbox(window,width="20",height="25",bg=c_button,justify="center",highlightcolor=c_active,borderwidth=3,
                      relief="solid",fg="white",highlightthickness=0,font=("Verdana",13),selectbackground=c_button)
subracelist.place(x=1080,y=465,relwidth =0.1,relheight = 0.035) #Creates a subrace input box

pointslabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",10),text="Remaining Points:\n27/27",borderwidth=3)
pointslabel.place(x=1080,y=505,relwidth=0.1,relheight=0.06) #Creates a points remaining label

raceimgport = PhotoImage(file = "") #Creates a new photoimage variable
raceportrait = Label(window,bg=c_button,bd=3,relief="solid",activebackground=c_button,activeforeground=c_button
                ,image=raceimgport) #Sets the portrait image as the raceportrait image
raceportrait.place(x=1125,y=800,width=85,height=85) #Places the race portrait 

classimgport = PhotoImage(file = "") #Creates a new photoimage variable
classportrait = Label(window,bg=c_button,bd=3,relief="solid",activebackground=c_button,activeforeground=c_button
                ,image=classimgport) #Sets the portrait as the classimgport image
classportrait.place(x=1035,y=800,width=85,height=85) #Places the class portrait
#----Skill Points Columns-----#
attributecol = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",10),text="Attributes",borderwidth=3)
attributecol.place(x=880,y=575,relwidth=0.09,relheight=0.04) #Creates a column called "Attributes"

abscorecol = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",10),text="Ability\nScore",borderwidth=3)
abscorecol.place(x=1000,y=575,relwidth=0.052,relheight=0.04)#Creates a column called "Ability Score"

racialbonuscol = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",10),text="Racial\nBonus",borderwidth=3)
racialbonuscol.place(x=1070,y=575,relwidth=0.04,relheight=0.04)#Creates a column called "Racial Bonus"

abilitymodcol = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",10),text="Ability\nModifier",borderwidth=3)
abilitymodcol.place(x=1124,y=575,relwidth=0.05,relheight=0.04)#Creates a column called "Ability Modifier"

totalscorecol = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",10),text="Total\nScore",borderwidth=3)
totalscorecol.place(x=1192,y=575,relwidth=0.035,relheight=0.04)#Creates a column called "Total Score"

#--------Skill Points--------------#
attributeslist = ["Strength","Dexterity","Constitution","Intelligence","Wisdom","Charisma"]

for attindex in range(len(attributeslist)): #Loops through the attributelist list and creates labels and buttons for them
    ypos = 620 + (attindex*28) #Sets the y position as starting from 620 and increases by 28
    attributelabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text=attributeslist[attindex],borderwidth=3)
    attributelabel.place(x=880,y=ypos,relwidth=0.09,relheight=0.03)#Creates a label with the attributeslist value
    minusbutton = Button(window,bg=c_button,fg="white",bd=3,relief="raised",text = "-",font=(fonttype,fontsize)
                        ,activebackground=c_active,activeforeground="white",command=lambda attindex=attindex, ypos=ypos:SkillPointCalc(-1,attributeslist[attindex],ypos))
    minusbutton.place(x=1000,y=ypos,relwidth=0.015,relheight=0.03) #Creates a minus button 
    abscorelabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="8",borderwidth=2)
    abscorelabel.place(x=1018,y=ypos,relwidth=0.023,relheight=0.03) #Creates the ability score label
    plusbutton = Button(window,bg=c_button,fg="white",bd=3,relief="raised",text = "+",font=(fonttype,fontsize)
                        ,activebackground=c_active,activeforeground="white",command=lambda attindex=attindex, ypos=ypos:SkillPointCalc(1,attributeslist[attindex],ypos))
    plusbutton.place(x=1047,y=ypos,relwidth=0.015,relheight=0.03) #Creates a plus button
    bonuslabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="0",borderwidth=3)
    bonuslabel.place(x=1082,y=ypos,relwidth=0.02,relheight=0.03) #Creates a racial bonus label
    abmodlabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="-1",borderwidth=3)
    abmodlabel.place(x=1140,y=ypos,relwidth=0.025,relheight=0.03) #Creates an ability modifier label
    totscorelabel = Label(window,bg=c_button,relief="solid",fg="white",font=("Verdana",12),text="8",borderwidth=3)
    totscorelabel.place(x=1200,y=ypos,relwidth=0.025,relheight=0.03) #Creates a total scores label
#----------------------------------#

def PrintVerification(): #Checks if there are any boxes that need input
    for child in window.winfo_children(): #Loop through all widgets
        if child.cget('bg') == "red": #If the widget has a red background
            child.config(bg = c_button) #Set it back to normal colour
            
    #------Check if nothing is blank----#
    done = True
    #----Name
    if nameentry.get() == "": #Check if there is a name inputted
        nameentry.config(bg = "red")
        done = False #Sets it to false to signal there are still
         #boxes that need input
    #----Gender    
    if genderentry.get("1.0",END) == "":
        genderentry.config(bg = "red")
        done = False
    #----Age
    if ageentry.get("1.0",END) == "":
        ageentry.config(bg = "red")
        done = False

    #----Background
    if backglist.get(0) == "":
        done = False
        backglist.config(bg = "red")
    #----Class
    if classlist.get(0) == "":
        done = False
        classlist.config(bg = "red")
    #----Equipment
    if equiplist.get(0) == "":
        done = False
        equiplist.config(bg = "red")
    #----Race
    if racelist.get(0) == "":
        done = False
        racelist.config(bg = "red")    
    #----Subrace
    if subracelist.get(0) == "":
        done = False
        subracelist.config(bg = "red")
    #----Skill points
    if pointslabel.cget('text') != "Remaining Points:\n0/27":
        #Checks if there are exactly 0 remaining points
        pointslabel.config(bg = "red")

    if done == True: #If there are no empty inputs
        print("Submit")
        file = open('CharacterOverview.html','w') #Creates a new html file that is writable
        file.write("<h1>Character Overview </h1><strong> Name: </strong>"+nameentry.get()+"<br><strong>Gender:</strong> "
                    +genderentry.get("1.0",END)+"<br> <strong>Age: </strong>"+ageentry.get("1.0",END)+"<br><br><strong> Background: </strong>"
                   +backglist.get(0)+"<br><strong>Class: </strong>"+classlist.get(0)+"<br><strong>Race: </strong>"+racelist.get(0)+
                   "<br><strong>Subrace: </strong>"+subracelist.get(0))
        #Writes all the string infos onto the html file with formatting
        file.write("<br><img src="+racelist.get(0)+"Portrait.png><img src="+classlist.get(0)+"Portrait.png> ")
        #Adds the portrait images onto the file
        
        file.write("<br><br><strong><font size=4>Proficiencies:</font></strong><br>")
        #Adds a Proficiencies title
        for index, item in enumerate(prolist.get(0, END)): #Loops through the proficiency values
            file.write(item+"<br>") #Adds the proficiency with a new line after it
            
        file.write("<br><strong><font size=4>Equipment:</font></strong><br>")
        #Adds an Equipment title
        for index, item in enumerate(equiplist.get(0, END)): #Loops through the equipment values
            file.write(item+"<br>") #Adds the equipment with a new line after it

        #-------------------------------Skill Points------------------------------#
        attributes = ["Strength&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;",
                      "Dexterity&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;",
                      "Constitution&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;",
                      "Intelligence&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;",
                      "Wisdom&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;",
                      "Charisma&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;"]
        file.write("<br><strong><font size=4>Attributes:&emsp;&nbsp;&nbsp;Total Score:&emsp;&nbsp;&nbsp;Ability Modifier:</font></strong><br>")
        #Adds an Attributes title
        totalpointslist,abilitymodlist = TotalPointsCalc("","","","","")
        #Retrieve the list of total points widgets and ability modifier widgets
        for index in range(len(attributes)): #Loops through the attributes values
            file.write(attributes[index]) #Adds the attribute name
            file.write(totalpointslist[index].cget('text')) #Adds the total points value
            file.write("&emsp;&emsp;&emsp;&emsp;&emsp;&emsp;&nbsp;&nbsp;&nbsp;&nbsp;") #Adds spaces
            file.write(abilitymodlist[index].cget('text')) #Adds the ability modifier value
            file.write("<br>") #Breaks onto the next value
        #------------------------------------------------------------------------#
        file.close()
        #os.startfile("CharacterOverview.html", "print")
 ##           file.write("\nProficiencies: ")            
##            for index, item in enumerate(prolist.get(0, END)): #Proficiencies
##                file.write("\n"+item)
##
##            file.write("\n\nEquipment: ")
##            for index, item in enumerate(equiplist.get(0, END)): #Equipment
##                file.write("\n"+item)
##
##            pointnames = ["Strength    ","Dexterity   ","Constitution","Intelligence","Wisdom      ","Charisma    "]
##            file.write("\n\nAttributes        Total Score        Ability Modifier")
##            for item in range(0,len(totalpointslist)): #Points
##                print(pointnames[item])
##                print(totalpointslist[item].cget('text'))
##                file.write("\n"+str(pointnames[item]) +"           "+str(totalpointslist[item].cget('text'))+"              "+str(abmodlist[item].cget('text')) )
##            file.close()

    
        
    #---------------------------------------------------------------------------------------------------------------------------------------------
   


printbutton = Button(window,bg=c_button,relief="raised",fg=c_text,font=("Verdana",16),bd=3,text="Print"
                                    ,justify="center",activebackground=c_active,command = lambda:PrintVerification() )
printbutton.place(x=900,y=856,relwidth=0.08,relheight=0.03)
#Creates a print button and links it to PrintVerification()


#__________________________________________________________________________________________________________
window.mainloop() #Initiates the entire tkinter window











