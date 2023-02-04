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

    jump first_murder
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
        ground "images/windchime_murderscene.jpg"
        hotspot (1, 0, 638, 498) action Jump ("bareFeet")
        hotspot ((646, 0, 623, 489)) action Jump ("knife")
        hotspot ((1290, 7, 618, 473)) action Jump ("w_bloodstains")
        hotspot ((15, 597, 591, 455)) action Jump ("shoePrints") 

   

label bareFeet:

    scene BareFeet
    
    #Susan Murphy 
    sm "Looks like his shoes were removed."

    #Ezekiel Jones
    ej "Seems like it really was someone stealing his shoes."

    jump windchimescene_investigation

label knife:
    
    scene bodybruise

    #Susan Murphy 
    sm "Enough blood on that thing to feed Dracula for a month."

    #Ezekiel Jones
    ej "And judging by those stab wounds, it's certainly the murder weapon."

    jump windchimescene_investigation

    
label w_bloodstains:

    scene bloodstains

    #Ezekiel Jones
    ej "That blood's been there a while. See how it's crusted?"

    #Susan Murphy 
    sm "You're right. I'd put it a few hours old, around noon, I'd say."

    jump windchimescene_investigation


label shoePrints:

    scene shoePrints
    
    #Susan Murphy 
    sm "At a glance, those are a match for William's. Poor kid, murdered for his footwear."
    
    #Ezekiel Jones
    ej "Say, didn't he think that McQuaid or Dalton were the only others with access to his shoes?"
    
    jump windchimescene_investigation

