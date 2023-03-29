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
        
        hotspot (1226, 299, 128, 146) action Jump ("headwound")
        hotspot (1527, 723, 94, 126) action Jump ("bodybruise")
        hotspot (1689, 739, 137, 141) action Jump ("bloodstains")
        hotspot (649, 867, 145, 153) action Jump ("knockedcase")
        hotspot (1359, 724, 165, 171) action Jump ("Guadycane")
        hotspot (896, 754, 99, 125) action Jump ("shoeprint")     
        hotspot (1484, 68, 414, 76) action If(not persistent.clicked_shoeprint, Jump("shoeprint_not_clicked"), Jump("first_murder"))

    add "my_img" as caret xpos 2024 ypos 150
    



label shoeprint_not_clicked:

    scene murder_bg

    #Ezekial Jones
    ej "Hey, Murphy, look at that shoe print."

    #Susan Murphy 
    sm "Hm. It doesn’t look expensive. One of the waiters, maybe?"
    
    jump shoeprint


label headwound:
   
    scene murder_bg
    
    #headwound
    show richard_headwound at right

    #Susan Murphy 
    voice "audio/day1/scene19_N3_sm.mp3"
    show susan at left 
    sm "This must be what killed him. Poor bastard. The bruising seems to say that it happened recently."
    hide susan 

    #Ezekiel Jones
    show ezekiel at left
    voice"audio/day1/scene19_N9_ej.mp3"
    ej "I've seen enough head wounds in my time. That's a deadly one." 
    hide ezekiel

    scene murder_bg

    menu headwound_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder
        

    

label bodybruise:
    
    scene murder_bg

    show richard_blood at right
    #Susan Murphy 
    show susan at left 
    voice "audio/day1/scene19_N3_sm2.mp3"
    sm "That body shot must've hurt."
    hide susan

    #Ezekiel Jones
    show ezekiel at left
    #voice"audio/day2/scene19_N9_ej2.mp3"
    ej "I got punched in the body during training a few times. I dropped to the ground like a sack of potatoes."
    hide ezekiel

    scene murder_bg

    menu bodybruise_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder        

    
label bloodstains:

    scene murder_bg

    show richard_blood at right

    #Susan Murphy 
    show susan at left
    voice"audio/day1/scene19_N5_sm_10.mp3"
    sm "Looks like he was beaten before he was killed."
    hide susan

    scene murder_bg


    menu hbloodstains_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":   
            jump first_murder


label knockedcase:

    scene murder_bg

    #Ezekiel Jones
    voice"audio/day1/scene19_N9_ej_6.mp3"
    ej "Seems like a struggle happened."
    
    #Susan Murphy 
    voice"audio/day1/scene19_N5_sm_7.mp3"
    sm "Did you think they talked before, or did he sneak up on him?"

    #Ezekiel Jones
    voice"audio/day1/scene19_n9_ej_7.mp3"
    ej "I don’t know, you tell me detective."

    #Susan Murphy 
    voice"audio/day1/scene19_N5_sm_9.mp3"
    sm "Well, there doesn’t seem to be any abrasion on the knuckles, or torn fingernails, so I’d say he was unconscious from the first hit."

    menu case_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder

label Guadycane:

    scene murder_bg

    show richard_cane at right

    #Susan Murphy 
    show susan at left
    voice"audio/day1/scene19_N5_sm5.mp3"
    sm "I think we've found our murder weapon."
    hide susan

    #Ezekiel Jones
    show ezekiel at left 
    voice "audio/day1/scene19_N9_ej5.mp3"
    ej "I think I saw Rachel carry that on board."
    hide ezekiel

    #Susan Murphy 
    show susan at left 
    voice"audio/day2/scene19_n5_sm_6.mp3"
    sm "Maybe there is something to what McQuaid said…"
    hide susan

    scene murder_bg


    menu gaudy_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder

label shoeprint:
    $ persistent.clicked_shoeprint = True

    scene murder_bg
    
    show richard_footprint at right 

    #Ezekiel Jones
    show ezekiel at left
    voice"audio/day2/scene19_n9_ej_3.mp3" 
    ej "Any bright ideas about that shoe print?"
    hide ezekiel

    #Susan Murphy 
    show susan at left 
    voice "audio/day1/scene19_N3_sm4.mp3"
    sm "Doesn't look like something expensive. Perhaps one of the waiters?"
    hide susan

    #Ezekiel Jones
    #voice"audio/day2/scene19.mp3" 
    show ezekiel at left
    ej "Richard was awfully rude to that William kid."
    hide ezekiel

    scene murder_bg

    menu shoe_inv:
        "Say Statement"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder
        


screen windchimescene_investigation():

    imagemap:
        ground "images/windchime_murderscene.png"
        hotspot (1034, 940, 109, 124) action Jump ("bareFeet")
        hotspot (273, 959, 127, 106) action Jump ("knife")
        hotspot (418, 786, 145, 124) action Jump ("w_bloodstains")
        hotspot (1785, 813, 128, 133) action Jump ("shoePrints")
        hotspot (243, 728, 70, 86) action Jump ("cloth")
        hotspot (1597, 87, 323, 83) action Jump ("third") 

    add "my_img" as caret xpos 2024 ypos 150

label bareFeet:

    scene murder_bg
    
    #Susan Murphy 
    voice "audio/day2/scene56_N5_sm_1.mp3"
    sm "Looks like his shoes were removed."

    #Ezekiel Jones
    voice "audio/day2/scene56_N9_ej_1.mp3"
    ej "Seems like it really was someone stealing his shoes."

    menu chime_barefeet_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 

label knife:
    
    scene murder_bg

    #Susan Murphy 
    voice "audio/day2/scene56_N5_sm_2.mp3"
    sm "Enough blood on that thing to feed Dracula for a month."

    #Susan Murphy
    voice "audio/day2/scene56_N5_sm_3.mp3"
    sm "And judging by those stab wounds, it's certainly the murder weapon."

    menu chime_knife_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 

    
label w_bloodstains:

    scene murder_bg

    #Ezekiel Jones
    voice "audio/day2/scene56_N9_ej_2.mp3"
    ej "That blood's been there a while. See how it's crusted?"

    #Susan Murphy 
    voice "audio/day2/scene56_N5_sm_4.mp3"
    sm "You're right. I'd put it a few hours old, around noon, I'd say."

    menu chime_stains_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 


label shoePrints:

    scene murder_bg
    
    #Susan Murphy 
    voice "audio/day2/scene56_N5_sm_5.mp3"
    sm "At a glance, those are a match for William's. Poor kid, murdered for his footwear."
    
    #Ezekiel Jones
    voice "audio/day2/scene56_N9_ej_3.mp3"
    ej "Say, didn't he say that McQuaid or Dalton were the only others with access to his shoes?"
    
    menu chime_shoeprint_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 

label cloth:

    scene murder_bg

    #Susan Murphy
    voice "audio/day2/scene56_N5_sm_6.mp3"
    sm "Looks like a piece of a shirt. He must have put up a fight, torn his attacker’s clothes"

    jump third


screen patriciascene_investigation():

    imagemap:
        ground "images/white_murderscene.png"
        hotspot (109, 356, 705, 358) action Jump ("handprint")
        hotspot (1537, 814, 70, 73) action Jump ("bruising")
        hotspot (1533, 66, 387, 102) action Jump ("thirdmurder")
    
    add "my_img" as caret xpos 2024 ypos 150


label handprint:

    scene murder_bg
    
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
    
    scene murder_bg

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

#Envelope Invitation Screen
screen envelope():
    
    imagemap:
        ground "images/envelope.png"

        hotspot (0, 0, 1920, 1080) action Jump ("cont_env")


#Day Screens
screen day_one():
    
    imagemap:
        ground "images/dayone.png"
        
        hotspot (0, 0, 1920, 1080) action Jump ("dayone")
