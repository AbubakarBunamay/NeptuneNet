    #Game Machanics
screen murderscene ():
    imagemap:
        ground "images/murdersceneimage.png"
        hotspot (1, 0, 638, 498) action Jump ("headwound")
        hotspot ((646, 0, 623, 489)) action Jump ("bodybruise")
        hotspot ((1290, 7, 618, 473)) action Jump ("bloodstains")
        hotspot ((15, 597, 591, 455)) action Jump ("knockedcase")
        hotspot ((654, 599, 608, 463)) action Jump ("Guadycane")
        hotspot ((654, 599, 608, 463)) action Jump ("shoeprint")     

   




label headwound:
    
    #Susan Murphy 
    sm "This must be what killed him. Poor bastard. The bruising seems to say that it happened recently."

    #Ezekiel Jones
    ej "I've seen enough head wounds in my time. That's a deadly one." 

    jump second

label bodybruise:
    
    #Susan Murphy 
    sm "That body shot must've hurt."

    #Ezekiel Jones
    ej "I got punched in the body during training once. I dropped to the ground like a sack of potatoes."
    jump second

    
label bloodstains:

    #Susan Murphy 
    sm "Looks like he was beaten before he was killed."

    jump second


label knockedcase:

    scene headwound
    #Ezekiel Jones

    ej "Seems like a struggle happened"
    
    #Susan Murphy 

    sm "Did you think they talked before, or did he sneak up on him?"

    jump second

label Guadycane:

    scene gaudycane
    #Susan Murphy 
    sm "I think we've found our murder weapon."

    #Ezekiel Jones
    ej "I think I saw Rachel carry that on board."

    #Susan Murphy 

    sm "Maybe there is something to what McQuaid said…"

    jump second

label shoeprint:

    scene shoeprint
    
    #Ezekiel Jones

    ej "Any bright ideas about that shoe print?"

    #Susan Murphy 

    sm "Doesn't look like something expensive. Perhaps one of the waiters?"

    jump second
