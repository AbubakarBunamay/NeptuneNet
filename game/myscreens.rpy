    #Game Machanics
screen murderscene ():
    imagemap:
        ground "images/murdersceneimage.png"
        hotspot (1, 0, 638, 498) action Jump ("headwound")
        hotspot ((646, 0, 623, 489)) action Jump ("bodybruise")
        hotspot ((1290, 7, 618, 473)) action Jump ("bloodstains")
        hotspot ((15, 597, 591, 455)) action Jump ("knockedcase")
        hotspot ((654, 599, 608, 463)) action Jump ("Guadycase")
        hotspot ((654, 599, 608, 463)) action Jump ("shoeprint")     

   




label headwound:
    "Headwound"
    jump second
label bodybruise:
    "bodybruise"
    jump second

    
label bloodstains:
    "bloodstains"
    jump second


label knockedcase:
    "Knockedcase"
    jump second

label Guadycase:
    "GaudyCase"
    jump second

label shoeprint:
    "shoeprint"
    jump second
