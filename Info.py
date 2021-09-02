def BackgroundInfoFunction():
    BackgroundInfo = ["Acolyte -Spend their lives in\nservice of a religious temple",
                        "Charlatan -A trickster that\nhas a way with people",
                        "Criminal -Has a history of\nbreaking the law and the\n criminal underworld",
                        "Entertainer -Thrives infront\nof a live audience",
                        "Folk Hero -Regarded as a \n champion by commonfolk\n and village-people",
                        "Gladiator -Battle for the\nentertainment of crowds",
                        "Guild Artisan -Skilled in a\ncertain field as an apprentice",
                        "Guild Merchant -Sells and\ntrades goods for profit",
                        "Hermit -Live in seclusion\n away from others",
                        "Knight -The lowest of the\n nobles, but on a path to \n higher status",
                        "Noble -Your family owns land\n and has significant political\n influence",
                        "Outlander -Grew up in the \nwild, away from towns and \ncivilization",
                        "Pirate -Spent a life on the\nhigh seas and sent enemies\n to their grave ",
                        "Sage -Scoured manuscripts,\nstudied scrolls and is\n a master in this field of study",
                        "Sailor -Sailed on a vessel\nfor years and faced storms\n and monsters of the deep",
                        "Soldier -War has been\n their life for as long as they\n can remember",
                        "Spy -Practised their abilities\nas an espionage agent to\nretrieve important information",
                        "Urchin -Grew up on the\nstreets, alone orphaned\nand poor "]
    return BackgroundInfo



def CheckProficiencies(action):
    value1 = ""
    value2 = ""
    
    BackgroundProficiencies = {
        "Acolyte": ["Insight (WIS)","Religion (INT)"],
        "Charlat": ["Deception (CHA)","Sleight of Hand (DEX)"],
        "Crimina": ["Deception (CHA)","Stealth (DEX)"],
        "Enterta": ["Acrobatics (DEX)","Performance (CHA)"],
        "Folk He": ["Animal Handling (WIS)","Survival (WIS)",],
        "Gladiat": ["Acrobatics (DEX)","Performance (CHA)"],
        "Guild A": ["Insight (WIS)","Persuasion (CHA)"],
        "Guild M": ["Insight (WIS)","Persuasion (CHA)"],
        "Hermit ": ["Medicine (WIS)","Religion (INT)"],
        "Knight ": ["History (INT)","Persuasion (CHA)"],
        "Noble -": ["History (INT)","Persuasion (CHA)"],
        "Outland": ["Athletics (STR)","Survival (WIS)"],
        "Pirate ": ["Athletics (STR)","Perception (WIS)"],
        "Sage -S": ["Arcana (INT)","History (INT)"],
        "Sailor ": ["Athletics (STR)","Perception (WIS)"],
        "Soldier": ["Athletics (STR)","Intimidation (CHA)"],
        "Spy -Pr": ["Deception (CHA)","Stealth (DEX)"],
        "Urchin ": ["Sleight of Hand (DEX)","Stealth (DEX)"],
        }
    value1 = BackgroundProficiencies.get(action[0:7])[0]
    value2 = BackgroundProficiencies.get(action[0:7])[1]

    return value1,value2

def ClassList():
    ClassInfo = ["Barbarian -A fierce warrior\nof primitive background who\ncan enter a battle rage",
                 "Bard -An inspiring magician\nwhose power echoes the \nmusic of creation",
                 "Cleric -A priestly champion\n who wields divine magic\n in service of a higher power",
                 "Druid -A priest wielding the\npowers of nature- moonlight,\nplant growth, fire and lightning ",
                 "Fighter -A master of martial\ncombat, skilled with varieties\nof weapons and armour",
                 "Monk -A master of martial arts,\nharnessing the power of the\n body",
                 "Paladin -A holy warrior \n bound to a sacred oath",
                 "Ranger -A warrior who uses\n martial prowess and nature \nmagic to combat threats",
                 "Rogue -A scoundrel who uses\n stealth + trickery to overcome\nobstacles and enemies",
                 "Sorcerer -A spellcaster who\n draws on inherent magic from\n a gift or bloodline",
                 "Warlock -A wielder of magic\nderived from a bargain with an \n extraplanar entity",
                 "Wizard -A scholarly magic user\n capable of manipulating the\n structures of reality"]
    return ClassInfo


def RaceList():
    RaceInfo = ["Dwarf",
                "Elf",
                "Halfling",
                "Human",
                "Dragonborn",
                "Gnome",
                "Half-Elf",
                "Half-Orc",
                "Tiefling"]
    return RaceInfo



def SubRaceList(race):
    SubRaceInfo = {"Dwarf":     ["Hill","Mountain"],
                   "Elf":       ["Wood","Drow"],
                   "Halfling":  ["Lightfoot","Stout"],
                   "Human":     ["Calishite","Chondathan","Damaran","Illuskan","Mulan","Rashemi","Shou","Tethyrian","Turami"],
                   "Dragonborn":["Black","Blue","Bronze","Copper","Gold","Green","Red","Silver","White"],
                   "Gnome":     ["Forest","Rock"],
                   "Half-Elf":  [],
                   "Half-Orc":  [],
                   "Tiefling":  []
                    }
    subracevalue = SubRaceInfo.get(race)
    return subracevalue

def DefaultBackgroundEquipment(background):
    StartingBackgroundEquipment = {
        "Acolyte": [""],
        "Charlat": ["Disguise Kit","Forgery Kit"],
        "Crimina": ["Gaming Set","Thieves' Tools"],
        "Enterta": ["Disguise Kit","Musical Instrument"],
        "Folk He": ["Artisan's Tools","Vehicle (Land)"],
        "Gladiat": ["Disguise Kit","Unusual Weapon"],
        "Guild A": ["Artisan's Tools"],
        "Guild M": ["Navigator's Tools"],
        "Hermit ": ["Herbalism Kit"],
        "Knight ": ["Gaming Set"],
        "Noble " : ["Gaming Set"],
        "Outland": ["Musical Instrument"],
        "Pirate ": ["Navigator's Tools","Vehicle (Water)"],
        "Sage -S": [""],
        "Sailor ": ["Navigator's Tools","Vehicle (Water)"],
        "Soldier": ["Gaming Set","Vehicle (Land)"],
        "Spy -Pr": ["Gaming Set","Theives' Tools"],
        "Urchin ": ["Disguise Kit","Thieves' Tools"],
    }
    return StartingBackgroundEquipment.get(background)

def DefaultClassEquipment(chosenclass):
    StartingClassEquipment = {
        "Barbarian" : ["Explorer's Pack","4 Javelins"],
        "Bard"      : ["Leather Armour","Dagger"],
        "Cleric"    : ["1 Shield","Holy Symbol"],
        "Druid"     : ["Leather Armour","Explorer's Pack","Druidic Focus"],
        "Monk"      : ["10 Darts"],
        "Paladin"   : ["Chain Mail","Holy Symbol"],
        "Ranger"    : ["Longbow","Quiver + 20 Arrows"],
        "Rogue"     : ["Leather Armour","2 Daggers","Theives' Tools"],
        "Sorcerer"  : ["2 Daggers"],
        "Warlock"   : ["Leather Armour","Simple Weapon","2 Daggers"],
        "Wizard"    : ["Spellbook"],
        }
    return StartingClassEquipment.get(chosenclass)


def ClassEquipment(classchosen):
    ChosenEquipment = { "Barbarian" :  [  ["Greataxe","Martial Melee Weapon"]           ,["2 Handaxes","Simple Weapon"]                  ,["Explorer's Pack","4 Javelins"] ],
                        "Bard"      :  [  ["Rapier","Longsword","Simple Weapon"]        ,["Diplomat's Pack","Entertainer's Pack"]          ,["Lute","Musical Instrument"]  ],
                        "Cleric"    :  [  ["Mace","Warhammer"]                          ,["Scale Mail","Leather Armour","Chain Mail"]    ,["Light Crossbow","Simple Weapon"] ],
                        "Druid"     :  [  ["Wooden Shield","Simple Weapon"]             ,["Scimitar","Martial Melee Weapon"]                                                              ],
                        "Fighter"   :  [  ["Chainmail","Longbow + 20 Arrows"]           ,["Martial Weapon + Shield","2 Martial Weapons"]   ,["Light Crossbow + 20 Bolts","2 Handaxes"]  ],
                        "Monk"      :  [  ["Shortsword","Simple Weapon"]                ,["Dungeoneer's Pack","Explorer's Pack"]   ],
                        "Paladin"   :  [  ["Martial Weapon+Shield","2 Martial Weapons"] ,["5 Javelins","Simple Melee Weapon"]             ,["Priest's Pack","Explorer's Pack"]    ],
                        "Ranger"    :  [  ["Scalemail","Leather Armour"]                ,["2 Shortswords","2 Melee Weapons"]       ,["Dungeoneer's Pack","Explorer's Pack"]  ],
                        "Rogue"     :  [  ["Rapier","Shortsword"]                       ,["Shortbow + 20 Arrows","Simple Melee Weapon"]   ,["Burglar's Pack","Dungeoneer's Pack","Explorer's Pack"]  ],
                        "Sorcerer"  :  [  ["Light Crossbow + 20 Bolts","Simple Weapon"] ,["Component Pouch","Arcane Focus"]               ,["Dungeoneer's Pack","Explorer's Pack"] ],
                        "Warlock"   :  [  ["Light Crossbow + 20 Bolts","Simple Weapon"] ,["Component Pouch","Arcane Focus"]               ,["Scholar's Pack","Dungeoneer's Pack"] ],
                        "Wizard"    :  [  ["Quarterstaff","Dagger"]                     ,["Component Pouch","Arcane Focus"]               ,["Scholar's Pack","Explorer's Pack"] ]
                    }
    return ChosenEquipment.get(classchosen)
        
