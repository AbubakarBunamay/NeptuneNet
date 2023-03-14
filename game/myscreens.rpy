#Game Machanics
init:
    $ style.input.caret = "my_img"
image my_img:
    "start.png"
    xalign 1.5
    yalign 1.5
    linear 1.0 alpha 1.0
    linear 1.0 alpha 0.0
    repeat



screen title_screen():
    
    imagemap:
        ground "images/title_screen.png"
        
        hotspot (0, 0, 1920, 1080) action Jump ("to_main_menu")

    add "my_img" as caret xpos 680 ypos 800

    image "gui/name_title.png" xpos 220 ypos 550
        
        
   

label to_main_menu():
    $ MainMenu(confirm=False)()

screen reedscene_investigation():
    imagemap:
        ground "images/richard_murderscene.png"
        
        hotspot (1215, 467, 101, 54) action Jump ("headwound")
        #hotspot (1464, 723, 188, 174) action Jump ("bodybruise")
        hotspot (1302, 22, 599, 458) action Jump ("bloodstains")
        hotspot (19, 601, 601, 462) action Jump ("knockedcase")
        hotspot (429, 982, 237, 67) action Jump ("Guadycane")
        hotspot (837, 774, 201, 132) action Jump ("shoeprint")     
        hotspot (1484, 68, 414, 76) action Jump ("first_murder")

    add "my_img" as caret xpos 2024 ypos 150

label headwound:
   
    scene headwound
    
    #Susan Murphy 
    #voice "audio/day1/scene19_N3_sm.mp3"
    sm "This must be what killed him. Poor bastard. The bruising seems to say that it happened recently."

    #Ezekiel Jones
    #voice"audio/day2/scene19_N9_ej.mp3"
    ej "I've seen enough head wounds in my time. That's a deadly one." 

    menu headwound_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder
        

    

label bodybruise:
    
    scene bodybruise

    #Susan Murphy 
    #voice"audio/day2/scene19_N3_sm2.mp3"
    sm "That body shot must've hurt."

    #Ezekiel Jones
    #voice"audio/day2/scene19_N9_ej2.mp3"
    ej "I got punched in the body during training a few times. I dropped to the ground like a sack of potatoes."
        
    menu bodybruise_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder        

    
# label bloodstains:

#     scene bloodstains

    #Susan Murphy 
    #voice"audio/day2/scene19_N3_sm3.mp3"
    sm "Looks like he was beaten before he was killed."

#     menu hbloodstains_inv:
#         "What's your next step"
#         "Continue Investigating":
#             call screen reedscene_investigation
#         "Done Investigating":
#             jump first_murder


label knockedcase:

    #Ezekiel Jones
    #voice"audio/day2/scene19_N9_ej6.mp3"
    ej "Seems like a struggle happened"
    
    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "Did you think they talked before, or did he sneak up on him?"

    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "I don’t know, you tell me detective"

    #Susan Murphy 
    #voice"audio/day2/scene19_N5_sm9.mp3"
    sm "Well, there doesn’t seem to be any abrasion on the knuckles, or torn fingernails, so I’d say he was unconscious from the first hit."

    menu case_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder

label Guadycane:

    scene gaudycane
    #Susan Murphy 
    #voice"audio/day2/scene19_N5_sm5.mp3"
    sm "I think we've found our murder weapon."

    #Ezekiel Jones
    #voice"audio/day2/scene19_N9_ej5.mp3"
    ej "I think I saw Rachel carry that on board."

    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "Maybe there is something to what McQuaid said…"

    #Susan Murphy 
    sm "That body shot must've hurt."

    #Ezekiel Jones
    ej "I got punched in the body during training a few times. I dropped to the ground like a sack of potatoes."

    menu gaudy_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder

label shoeprint:

    scene shoeprint
    
    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "Any bright ideas about that shoe print?"

    #Susan Murphy 
    #voice"audio/day2/scene19_N3_sm4.mp3"
    sm "Doesn't look like something expensive. Perhaps one of the waiters?"

    menu shoe_inv:
        "Say Statement"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder
        


screen windchimescene_investigation():

    imagemap:
        ground "images/windchime_murderscene.png"
        hotspot (788, 985, 366, 90) action Jump ("bareFeet")
        hotspot (251, 996, 203, 49) action Jump ("knife")
        hotspot (418, 786, 145, 124) action Jump ("w_bloodstains")
        hotspot (1702, 792, 211, 112) action Jump ("shoePrints")
        hotspot (1597, 87, 323, 83) action Jump ("third") 

    add "my_img" as caret xpos 2024 ypos 150

label bareFeet:

    scene BareFeet
    
    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "Looks like his shoes were removed."

    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "Seems like it really was someone stealing his shoes."

    menu chime_barefeet_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 

label knife:
    
    scene knife

    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "Enough blood on that thing to feed Dracula for a month."

    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "And judging by those stab wounds, it's certainly the murder weapon."

    menu chime_knife_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 

    
label w_bloodstains:

    scene bloodstains

    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "That blood's been there a while. See how it's crusted?"

    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "You're right. I'd put it a few hours old, around noon, I'd say."

    menu chime_stains_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 


label shoePrints:

    scene shoePrints
    
    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "At a glance, those are a match for William's. Poor kid, murdered for his footwear."
    
    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "Say, didn't he say that McQuaid or Dalton were the only others with access to his shoes?"
    
    menu chime_shoeprint_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 

screen patriciascene_investigation():

    imagemap:
        ground "images/white_murderscene.png"
        hotspot (109, 356, 705, 358) action Jump ("handprint")
        hotspot (1537, 814, 70, 73) action Jump ("bruising")
        hotspot (1533, 66, 387, 102) action Jump ("thirdmurder")
    
    add "my_img" as caret xpos 2024 ypos 150


label handprint:

    scene handprint
    
    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "Looks like his shoes were removed."

    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "Seems like it really was someone stealing his shoes."

    menu white_handprint_inv:
        "What's your next step"
        "Continue Investigating":
            call screen patriciascene_investigation
        "Done Investigating":
            jump thirdmurder 

label bruising:
    
    scene bruising

    #Susan Murphy 
    #voice"audio/day2/scene19.mp3"
    sm "Enough blood on that thing to feed Dracula for a month."

    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3"
    ej "And judging by those stab wounds, it's certainly the murder weapon."

    menu white_bruising_inv:
        "What's your next step"
        "Continue Investigating":
            call screen patriciascene_investigation
        "Done Investigating":
            jump thirdmurder 


