#Game Machanics

screen reedscene_investigation():
    imagemap:
        ground "images/murdersceneimage.png"
        
        hotspot (6, 7, 619, 483) action Jump ("headwound")
        hotspot (659, 14, 603, 473) action Jump ("bodybruise")
        hotspot (1302, 22, 599, 458) action Jump ("bloodstains")
        hotspot (19, 601, 601, 462) action Jump ("knockedcase")
        hotspot (657, 593, 608, 477) action Jump ("Guadycane")
        hotspot (1306, 599, 598, 464) action Jump ("shoeprint")     
        hotspot (12, 501, 1888, 69) action Jump ("first_murder")


label headwound:
   
    scene headwound
    
    #Susan Murphy 
    sm "This must be what killed him. Poor bastard. The bruising seems to say that it happened recently."

    #Ezekiel Jones
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
    sm "That body shot must've hurt."

    #Ezekiel Jones
    ej "I got punched in the body during training once. I dropped to the ground like a sack of potatoes."
        
    menu bodybruise_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder        

    
label bloodstains:

    scene bloodstains

    #Susan Murphy 
    sm "Looks like he was beaten before he was killed."

    menu hbloodstains_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder


label knockedcase:

    #Ezekiel Jones

    ej "Seems like a struggle happened"
    
    #Susan Murphy 

    sm "Did you think they talked before, or did he sneak up on him?"

    menu case_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder

label Guadycane:

    scene gaudycane
    #Susan Murphy 
    sm "I think we've found our murder weapon."

    #Ezekiel Jones
    ej "I think I saw Rachel carry that on board."

    #Susan Murphy 

    sm "Maybe there is something to what McQuaid said…"

    menu gaudy_inv:
        "What's your next step"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder

label shoeprint:

    scene shoeprint
    
    #Ezekiel Jones

    ej "Any bright ideas about that shoe print?"

    #Susan Murphy 

    sm "Doesn't look like something expensive. Perhaps one of the waiters?"

    menu shoe_inv:
        "Say Statement"
        "Continue Investigating":
            call screen reedscene_investigation
        "Done Investigating":
            jump first_murder
        


screen windchimescene_investigation():

    imagemap:
        ground "images/windchine_scene.jpg"
        hotspot (19, 95, 919, 317) action Jump ("bareFeet")
        hotspot (1120, 157, 612, 234) action Jump ("knife")
        hotspot (61, 588, 831, 434) action Jump ("w_bloodstains")
        hotspot (1142, 597, 622, 441) action Jump ("shoePrints")
        hotspot (91, 462, 1713, 123) action Jump ("third") 

   

label bareFeet:

    scene BareFeet
    
    #Susan Murphy 
    sm "Looks like his shoes were removed."

    #Ezekiel Jones
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
    sm "Enough blood on that thing to feed Dracula for a month."

    #Ezekiel Jones
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
    ej "That blood's been there a while. See how it's crusted?"

    #Susan Murphy 
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
    sm "At a glance, those are a match for William's. Poor kid, murdered for his footwear."
    
    #Ezekiel Jones
    ej "Say, didn't he think that McQuaid or Dalton were the only others with access to his shoes?"
    
    menu chime_shoeprint_inv:
        "What's your next step"
        "Continue Investigating":
            call screen windchimescene_investigation
        "Done Investigating":
            jump third 

screen patriciascene_investigation():

    imagemap:
        ground "images/white_murder_scene.jpg"
        hotspot (109, 356, 705, 358) action Jump ("handprint")
        hotspot (1017, 356, 869, 305) action Jump ("bruising")
        hotspot (928, 0, 41, 1079) action Jump ("thirdmurder")
   

label handprint:

    scene handprint
    
    #Susan Murphy 
    sm "Looks like his shoes were removed."

    #Ezekiel Jones
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
    sm "Enough blood on that thing to feed Dracula for a month."

    #Ezekiel Jones
    ej "And judging by those stab wounds, it's certainly the murder weapon."

    menu white_bruising_inv:
        "What's your next step"
        "Continue Investigating":
            call screen patriciascene_investigation
        "Done Investigating":
            jump thirdmurder 