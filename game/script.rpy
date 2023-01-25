# The Neptune script


#Characters are:
# Susan Murphy, Dr. Ezekial Jones, Richard Reed, Rachel Reed, Deborah White, Patricia White, Michael McQuaid, William Windchime, David Dalton, Lloyd Lewis.

#Characters will have initials as variable i.e Susan Murphy = sm but rar for the wife of reed

define sm = Character("Susan Murphy")
define ej = Character("Dr.Ezekial Jones")
define rr = Character("Richard Reed")
define rar = Character("Rachel Reed") 
define dw = Character("Deborah White")
define pw = Character("Patricia White")
define mm = Character("Michael McQuaid")
define ww = Character("William Windchime")
define dd = Character("David Dalton")
define ll = Character("Lloyd Lewis")

#For voice 
# naming as n(scene)(number) such as n11= naration scene 1 first. n = narrators sm=susan murphy etc

# The game starts here.

label start:

    ##Possible Splash Screen Here


    # Scene 1 - Susan’s house front door

    #scene BG
    scene susanfrontdoor 

    # Narrator voice
    #voice "audio/narrator/n01.mp3"
    "Coming home from her latest case, Susan Murphy, private eye, opens the door to her apartment."

    # Scene 2 - inside Susan’s front door, mail on the floor 

    #scene BG
    scene susanhomefloor
 
    # Narrator voice
    #voice "audio/narrator/n02.mp3"
    "Stepping inside, glancing down, she sees the expected bills and magazines slipped through the mail slot onto the floor."

    # Narrator voice

    "Among the pile is an ornate envelope, with an equally ornate invitation inside."

    # Scene 3 - an image of the envelope and invitation with text on them

    #scene BG
    scene invitation  

    #voice of mcquaid

    mm "Dear Susan Murphy, you have been cordially invited as a distinguished guest to ring in 1952 in style aboard the USS Neptune. We will be departing at 6:00 P.M. December 30th from Honolulu Harbour, and returning to the same location on January 3rd. I hope to see you there! - Michael McQuaid"

    # Susan thought voice 

    sm "McQuaid, McQuaid, where have I heard that name before? Oh right, I did a case for him. Well, I could use a vacation after today…Sure, why the heck not!"

    # Scene 4 - an image of the yacht on the water
    
    #Scene Bg 
    scene yatchonwater

    #Narrator Voice

    "A couple of weeks later, Susan readies to board the Neptune, admiring the lavish yacht."

    # Scene 5 - Inside Susan Cabin
    
    #scene BG
    scene susancabin

    #Narrator voice

    "As Susan sorts through her luggage, there is a knock at the door."

    #David Dalton

    dd "There will be a dinner for all the guests in the dining hall in 30 minutes."

    #Susan Murphy

    sm "Okay, thanks for the information."

    #Susan Murphy thought

    sm " Okay, time for me to get dolled up for dinner. I hope the food is going to be good."


    #Scene 6 - Navigating to dining room

    scene Navigation 



    "Navigation to Dining Room"


    #Scene 7 - The Dining Room

    #Scene BG
    scene dining room 

    #Narrator Voice

    "Susan enters the dining room and sees a well-dressed crowd sitting around the room at different tables."
    
    #Michael speaking as the player enters the room

    mm "Ah, and here’s our final guest arriving! Welcome, Susan. Please, take a seat. Now that we’re all here, the party can start!"

    mm "I know some of you are already acquainted with each other, but to help break the ice, why don’t we have a few introductions?"

    mm "First, we have Mr. Richard Reed, the CEO of Reed Industries, and his wife, Mrs. Rachel Reed."

    mm "Next, we have the illustrious Dr. Ezekiel Jones. The man’s service to our country and his patients' lives speaks for itself."

    mm "Then, We have the White sisters, Deborah and Patricia. True yin and yang if I’ve ever seen one."

    mm"Of course, the brilliant Susan Murphy, one of the great detectives of our time."
    
    mm "And finally, our talented captain, Lloyd Lewis! He’ll be navigating the boat for the next five days, so don’t expect to see much of him away from the helm"

    
    #Narrator voice of LLoyd Lewis
    #Seems deleted in main script, hiden for now.
    #ll "That’s my cue. Back to the helm, I go. Have a good meal, folks"

    #Voice of Michael McQuaid
    mm "Speaking of here’s dinner now!"

    #Susan Thoughts voice
    sm "Well, seems like McQuaid is in high spirits tonight. But why invite me? I stand out among these high-society types like a pebble among rhinestones. Hmm."

    #Narrator Voice Here
    "Just then, Susan hears a commotion from another table."

    #Richard Reed Voice
    rr"How dare you! Don’t you know who I am, boy?"

    #William Windchime
    ww "I-I’m so sorry, mister Reed, sir, I didn’t mean t-"

    #The Scene Here would still be in the room

    #Narrator Voice 
    "She turns to see one of the guests, Richard Reed covered in drink and screaming at the waitstaff."

    #Richard Reed Voice
    rr"I don’t care! Can’t you see how expensive this suit is! It’s worth more than your life, at the very least"

    #Richard Reed Voice
    rr "Michael, see to it that your server is disciplined! I’m going to go get changed out of this mess!"

    #Narator Voice Here
    "Richard leaves, muttering about having to replace a perfectly good suit."

    #Susan Murphy Thoughts
    sm "ell, Richard seems to be a very happy camper. I wonder if he’s always like this… Does the same go for his wife?"

    #Michael McQuaid Voice
    mm "William! Go wait in the kitchen. We’ll talk about this later!"

    #Narrator Voice Here
    "The waitstaff member leaves, looking abashed."

    #Ezekiel Jones
    ej "Don’t be too harsh on him, McQuaid. It was an honest mistake. The poor boy just tripped."

    #Michael McQuaid Voice Here
    mm "I expect a certain amount of professionalism, Doctor, and I’d thank you not to tell me my business. Now then, everyone, please continue to enjoy the party."

    #Narrator Voice 
    "The man sitting next to Susan turns toward her and starts talking to her quietly."

    #Ezekiel Jones Voice
    ej "Seems like that really got him going."

    #Susan Murphy Voice
    sm "Yeah,really got his goat. Seems very uptight. I don’t remember him being like this."

    #Ezekiel Jones Voice
    ej "If you worked for him, that’s why. He’s always nice until he’s not."

    #Susan Murphy Voice
    sm "Seems like you know our host quite a bit."

    #Ezekiel Jones Voice
    ej "If you worked for him, that’s why. He’s always nice until he’s not."

    #Susan Murphy Voice
    sm "Seems like you know our host quite a bit."

    #Ezekiel Jones Voice
    ej "Yeah, I know Michael, unfortunately. Hi, I’m Ezekiel."

    #Choice Menu

    menu:
        
        #Narrator 

        "How would you like to proceed"
        
        "Continue Path A":
            
            #Susan Murphy 

            sm "A pleasure to make your acquaintance. Well, Zeke, I think I’ll go mingle a bit. See you around."
            
        "Continue Path B":
            
            #Ezekiel Jones

            ej "Our host said you are an amazing private eye. Do you work for the police as a detective? You must have immensely high intelligence."

            #Susan Murphy 

            sm "Nonsense, I am smart. I have always had help. I always make sure to have criminals brought to justice."


            #Ezekiel Jones

            ej "That is very honourable of you. We are living in a tough time, so your job is very important. It may be weird to say this, but if there is anything I can help you with for any reason, don't hesitate to call me."

            #Susan Murphy 

            sm "Thank you, Ezekiel. You truly are a kind man. But enough about me, what about you? What do you do?"

            #Ezekiel Jones

            ej "I am a doctor. I help by prescribing the medication that my patients need."

            ej "After the war, my job has been rough because there are many people who need this medication to help them get better."

            #Susan Murphy 

            sm "Your job is no small feat. Your job is also as tough as mine, maybe even tougher."

            sm "Just as you said, if there is anything I can help you with, don't hesitate to ask."

            #Narrator

            "Ezekiel looked at Susan with a thankful smile. His smile was sincere and enough to move almost anyone."

            #Ezekiel Jones

            ej "Thank you for those kind words."

            #Susan Murphy 

            sm "I want to mingle a bit. Thank you for the talk."

            #Ezekiel Jones

            ej "The pleasure is mine, thank you."



    #Susan Murphy Voice
    sm "A pleasure to make your acquaintance. Well, Zeke, I think I’ll go mingle a bit. See you around."

    #Narrator Voice
    "Susan gets up and wanders the dining room. She comes to a table with three elegantly dressed women where Richard had been sitting"

    #Patricia White
    pw "Well, I don’t see why Richard had to go and make such a fuss! I mean, it was just booze!"

    #Rachel Reed Voice
    rr "Richard just gets easily upset when something happens to his things. I mean, that was a very expensive suit."

    #Deborah White
    dw "He’s a man who cares about his appearance. Can’t ask for much more than that these days."

    #Patricia White
    pw "Oh, if it isn’t “the brilliant Susan Murphy”? What’d you do for McQuaid to be called ‘brilliant’?"

    #Susan Murphy
    sm "I found a leak in his bank account for him. I’m sorry. I know McQuaid introduced us, but it went by a bit fast. Would you mind reminding me of your names?"

    #Deborah White
    dw "Oh, pardon me! I’m Deborah. This is my sister Patricia, and this is Rachel, the blowhard’s wife."

    #NRachel Reed
    rar "Hey!"

    #Narrator Voice
    "A ringing sound is heard, and Michael taps his glass with a spoon like he is making a toast."

    #Michael McQUiad
    mm "Everyone! I hope you've enjoyed your evening, but now it's time to get to business"

    #Narrator Voice
    "A hush settles over the room."

    #Michael Mcquaid Voice
    mm "You see, I may have told a little white lie on your invitations. The real reason you’re here is that each one of you has a secret. Something hidden that would ruin you if it were to get out."

    #Michael McQuaid Voice
    mm "I brought you all here so we could come to a little… arrangement. Over the next few days, I am sure you’ll find this to be in your best interest."

    #Michael McQuaid Voice
    mm "After all, who knows what would happen if your little secrets were no longer secret."

    #Susan Murphy Voice
    sm "What!"

    #Deborah White Voice
    dw "How dare you!"

    #Ezekiel Jones Voice
    ej "What on  Earth are you talking about"

    #Patricia White Voice
    pw "WHAT IN THE FLYING FUCK ARE YOU ON ABOUT!"

    #Rachel Reed Voice
    rar "Hrrk! I think I’m going to be sick."

    #Narrator Voice
    "Heads turn as Rachel runs from the room, sickened by Michael’s words."

    #Susan Murphy thoughts
    sm "He couldn’t mean… but how could he… No, that’s impossible."

    #Susan Murphy thoughts
    sm "He couldn’t mean… but how could he… No, that’s impossible."

    #Susan Murphy Thoughts
    sm "There’s no way he could know. What is this about? Hmm…"

    #Ezekiel Jones Voice
    ej "What do you want, McQuaid?"

    #Michael McQuaid Voice
    mm "The same I’ve always wanted, always deserved. Power. While you yucks have been going about your days with your crimes, I’ve been building a list on all of you."

    #Susan Murphy Thoughts
    sm "Building a list? Why would he possibly be building a list on me? *Sigh* I can’t ever get a vacation. I should probably check on Rachel. I wonder where she ran off too."

    #Scene 8 - The player Navigates the hallway 

    #Navigation

    scene navigatinghallway

    #Scene 9 - The Hallway

    #narrator voice
    "Susan leaves the room in search of Rachel. She is now in the Hallway."    

    #Susan Murphy
    sm "She said she was feeling sick. I should probably go and check the washroom."

    #Scene 10 - Navigating to the washroom    

    #Navigation

    scene navigatingtowashroom

    "Navigating to washroom"

    #scene 11 - The Washroom

    scene washroom

    #Narator Voice
    "Susan enters the washroom but finds no one."

    #Susan Murphy Voice
    sm "Drat, she’s not here. Where else would she be… their cabin!"

    #Scene 12 - Navigating to reed's Cabin

    #navigation 

    scene navigatetocabin

    "navigation to the cabin"


    #Scene 13 - Closer to the door

    scene reedscabindoor

    "When Susan arrives at the Reed's cabin, she finds the door slightly ajar"

    #Scene 14 - The player navigates to the Reed's cabin, opens the door and looks inside

    scene openreedscabindoor

    #Scene 15 - The Murder Scene in the cabin

    scene reedcabinmurder 

    #narrator Voice
    "As Susan opens the door, she is met with a horrific sight. Richard Reed, former CEO of Reed Industries, has been beaten bloody, and unmoving."

    menu:
        "Proceed to see murder"
        "Open the door full":
            scene murderroom
                #Susan Murphy Voice
                sm "Oh Shit. Is that Richard? Oh my God, I need to tell everyone about this."
                ++
        "It's enough":
            "Something here"
        



    #Scene 16 - Goes back to the dining room

    #Navigation 

    scene navigating to dining room
    
    "The player going navigating to living room"

    #Scene 17 - Dining Room 

    scene diningroom

    #Narrator
    "Susan sprints back to the dining room, bursting through the door, panting."

    #Susan Murphy
    sm "McQuaid! I thought you wanted us to do your bidding, not kill us"

    #Michael McQuaid
    mm "Pardon me, Ms. Murphy?"

    #Susan Murphy 
    sm "I went to look for Rachel because she was feeling a bit sick from your “news,” and I found Richard dead in their cabin. Explain yourself!"

    #Michael Mcquaid
    mm "Well, it wasn’t me. I was here the entire time? You said you went to find Rachel? What if she went to get rid of her dastardly husband?"

    #Susan Murphy
    sm "Oh, come on, that’s ridiculous."

    #Michael Mcquaid
    mm "As far as we know, you could have killed him." 

    #Ezekiel Jones
    ej "Hmm, he has a good point. We know nothing for sure. While you do seem like a lovely person Susan, you were out there alone."

    #Susan Murphy
    sm "You can’t be serious. You all saw me leave here a few seconds ago." 

    #Patricia White
    pw "Oh no, sis, are we gonna get murdered? I’m too pretty to get murdered."

    #Deborah White
    dw "Calm down, Patti. Nothing is gonna happen to you."

    #Patricia White
    pw "You don’t know that! I’m gonna die to a murderer onboard."

    #David Dalton
    dd "I don’t know if I want to work here if someone is murdering people. Someone tell the captain to turn thi - …"

    #Narrator
    "Indiscriminate chatter happens amongst the guests."

    #Michael Mcquaid
    mm "ALRIGHT, EVERYONE! Settle down. Let’s not lose our heads. Susan, you are a private eye, yeah? I think you have the qualifications to solve this."

    #Susan Murphy
    sm "What? You don’t suspect me anymore?"

    #Michael Mcquaid
    mm "I do. That’s why someone should be with you every second"

    #Ezekiel Jones
    ej "I’ll keep an eye on her"

    #Susan Murphy
    sm "Oh, please."

    #Michael Mcquaid
    mm "Perfect, the doctor and the eye. What a confidential relationship."

    #Patrica white
    pw "I wanna go look for Rachel! She could be in danger!"

    #Deborah White
    dw "Aren’t you afraid of getting murdered?"

    #Patrica White
    pw "Yes, but she was nice to me. Oh, please come with me, Debbie."

    #Deborah White
    dw "auughhh, fine. Let’s go look for her. Hey Michael! You heard?"

    #Michael Mcquaid
    mm "Loud and clear. The rest of us will stay here. Don’t want anyone else turning up dead now."

    #Narrator
    "Susan and Ezekiel left to go to the crime scene. Deborah and Patricia left moments after to try and find Rachel."

    #Scene 18 - Navigating to the murder scene

    #Navigation

    scene navigation



    #Narrator
    "While looking at a crime scene, click on points of interest around the area to find clues."

    #Narrator
    "Clues will be added to your detective board for easy viewing."

    #Scene 19 - Murder Scene Investigation 
    call screen murderscene
    

    #Mechanics in myscreen.rpy
    

    hide screen murderscene

label second:

    #Scene 20- Post Murder Scene Inestigation 

    scene donemurderinvestigation

    #Susan Murphy
    sm "I think that's all we can get from the crime scene. How about we go do some interviews?"

    #Ezekiel Jones 
    ej "I'm afraid everyone's probably going to be asleep, Murphy. Perhaps we should break for the night and pick up where we left off in the morning?"

    #Susan Murphy
    sm "As much as I hate to leave a case like this… you're right. Reconvene in the dining room tomorrow?"

    #Ezekiel Jones
    ej "Of course."

    #Narrator
    "Susan and Ezekiel leave the crime scene and go to their separate rooms."

    #Day 2 

    #Scene 21 - The player to navigate to the hallway 

    #Navigation 

    scene navigatinghall 

    #Scene 22- Hallway 

    scene hallway 

    "Susan is walking through the halls and hears some commotion coming from a bathroom."

    #Scene 23 - The player Navigates to the bathroom 

    #Navigation 
    scene navigatingtobathroom

    #Scene 24 - Inside the bathroom 
     
    #Narrator
    "Inside the bathroom, she sees the sisters, Patricia and Deborah White. Patricia is by the toilet, feeling sick to her stomach. Deborah is keeping her company."
    scene insidebathroom

    #Patrcia Sound Effect
    pw "Retches"

    #Deborah
    dw "That's it, it's okay. Let it out."

    #Susan Murphy
    sm "Hello? Patricia, Deborah. You gals doing okay?"

    #Deborah White
    dw "Hey Susan, yea Patty's still a little shaken up. I thought it would be good to catch some sun and get some fresh air, but her stomach is still in knots." 

    #Patricia White
    pw "Ughh, yea… at least this bathroom has a porthole. Though I'm not too fond of the sea smell."

    #Deborah White
    dw "I'm just glad it seems to be helping calm you down. Back home, all she had to do was go outside for her worries to disappear naturally. Anyway, how are you doing, Susan?" 

    #Susan Murphy
    sm "About the same as everyone else, I guess. Can't I ever get a vacation?"

    #Deborah Murphy
    dw  "I hear you'. A working girl's work is never done."

    #Susan Murphy 
    sm "Yea, speaking of, did you two find Rachel last night?"

    #Patricia White
    pw "Yes, we did, *Hrph*"

    #Deborah White
    dw  "Yea, we found her. Thank goodness she was okay. Physically."

    #Susan Murphy
    sm "Where was she?"

    #Deborah White
    dw "On the deck, trying to catch herself. She left because she was feeling dizzy. I guess she was trying to catch some air herself."

    #Susan Murphy
    sm "Did you tell her?"

    #Deborah White
    dw "What choice did we have? Poor thing, she immediately broke down over that man. Seems to me like she really loved him. Even if he was a piece of work."

    #Susan Murphy
    sm "Hmm, okay. Well, I'll try to go and find her."

    #Deborah White
    dw "I think she's in the Dining Hall. When I saw her last, she was still distressed, and McQuaid was with her."

    #Susan Murphy 
    sm "Thanks. Will you two be okay?"

    #Patricia White
    pw "We'll be just peachy, don't you worr- *Heaves*"

    #Deborah White
    dw "We'll be fine. See you."

    #scene 25 - The player navigating to the hallway 
    
    #Navigation 
    scene navigatinghallway
 

    #Narrator 
    "Susan leaves the White sisters in the bathroom."

    #Susan Thought 
    sm "Thoughts: They say she broke down. It still doesn't excuse her totally. I have to keep looking for clues. Let's see how Rachel is actually doing."

    #scene 27 - The player navigates to the dining room
    
    #NAVIGATION
    
    scene navigatingdiningroom

    #scene 28 - The Dining Room 

    scene diningroom

    #Narrator 
    "Susan now enters the Dining Hall. She sees Rachel with her head in her hands, Ezekiel trying to comfort her, and McQuaid is in the corner."

    #Ezekiel Jones
    ej "Ah, Susan, good morni-"

    #Rachel Reed
    rar "Susan? SUSAN! You're the private eye. Right? Did you find out who did it? Did you find my husband's killer?"

    #Susan Murphy
    sm "Not yet. I'm still working on it. I have gathered some clues, but I'm still working it all out."

    #Racheel Reed
    rar "So you have nothing? It's a Yacht! Someone here is responsible! They must be found and pay for what they've done!"

    #Michael Mcquaid
    mm "Easy there. I'm sure Ms. Murphy is doing everything she can to solve this case."

    #Susan Murphy 
    sm "Don't think we've forgotten about you, McQuaid. Unfortunately, there are more pressing matters at hand."

    #Susan Murphy 
    sm "But yes, I'll figure it out. Don't you worry about that! Rachel, I hope you don't mind, but I need to ask you some questions."

    #Rachel Reed
    rar "What? Why me?"

    #Susan Murphy
    sm "Well, to be perfectly honest, you left the room last night and then Mr. Reed…you know."

    #Rachel Reed
    rar "You... You can't seriously be thinking I did this. He was my husband, for Christ's sake!"

    #Ezekiel Jones
    ej "She isn't accusing you of anything, dear. She just needs to know where everyone was to paint the picture of what happened last night. Nothing more."

    #Susan Murphy
    sm "Exactly. Now please, if you may. Where did you go when you left the dining hall last night?"

    #Rachel Reed
    rar "Well, after the news, I felt nauseous. So I started to head to the bathroom. On my way there, I caught a draft of the ocean breeze and decided to go on the deck instead."

    #Susan Murphy
    sm "Did the ocean breeze help?"

    #Rachel Reed
    rar "A little. It did help to calm me down. I did hear something, but I thought it was just the party or something. Oh God, what if it was Richard? I could have done something to save him! He would have been alive if I had just stayed by his side."

    #Susan Murphy
    sm "Hey, don't do that. There's nothing you could have done to see this coming."

    #Ezekiel Jones
    ej "Yea, take it from me. It doesn't help anything at all."

    #Susan Murphy
    sm "Did you find your way back to the party?"
    
    #Rachel Reed
    rar "Yes, eventually the White sisters came to help but- *sobs* all they did was made me feel worse by telling me that I lost my Richard."

    #Susan Murphy
    sm "A couple more questions, okay? Do you know anyone that could've done this?"

    #Rachel Reed
    rar "*sniff* Richard always had enemies. Since we were back in school, he'd always been a bit...abrasive. They'd just never understood him. Oh, my Richard. I miss you so much.."

    #Ezekiel Jones
    ej "Okay, that's enough. You should take some time to rest and grieve your loss."

    #Susan Murphy 
    sm "Yea, I'm sorry this happened."

    #Rachel reed
    rar "Me too."

    #Susan Murphy 
    sm "McQuaid. What happened to the waitstaff member that had a squabble with Reed last night?"

    #Michael Mcquiad
    mm "I sent him back to the kitchen to do some extra work. He should be there now if you want to talk to him."

    #Susan Murphy
    sm "Okay. We aren't done here either."

    #Michael Mcquiad
    mm "Oh, Ms. Murphy, where would I possibly go?"

    #Narrator
    "Susan looks at Ezekial to confirm that he heard where she was going, and then Susan left."

    










    return
