﻿# The Neptune script


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

image navigatetocabin = "hallway.jpg"
image reedscabin = "murderscene.jpg"


# The game starts here.

label start:

    #------------------------------------- START OF DAY 1 --------------------------------------------------------#
    
    # Scene 1 - Susan’s house front door

    #scene BG
    scene apartment 
    show susan
    #Susan's Apartment from door with mail slot (background)

    # Narrator 
    voice "audio/narrator/n01.mp3"
    "Coming home from her latest case, Susan Murphy, private eye, opens the door to her apartment."

    # Scene 2 - inside Susan’s front door, mail on the floor 

    #scene Bg
    scene mail
    #Inside Susan Apartment Mail on floor

    # Narrator 
    voice "audio/narrator/n02.mp3"
    "Stepping inside, glancing down, she sees the expected bills and magazines slipped through the mail slot onto the floor."

    # Narrator 

    "Among the pile is an ornate envelope, with an equally ornate invitation inside."

    # Scene 3 - Envelope 

    #Scene Bg - an image of the envelope and invitation with text on them
    scene envelope #inside The invitation 

    #voice of mcquaid
    #do we need this as text or would a graphic be enough?

    "Dear Susan Murphy, you have been cordially invited as a distinguished guest to ring in 1952 in style aboard the USS Neptune. We will be departing at 6:00 P.M. December 30th from Honolulu Harbour, and returning to the same location on January 3rd. I hope to see you there! - Michael McQuaid"

    # Susan thought  
    show susan
    sm "McQuaid, McQuaid, where have I heard that name before? Oh right, I did a case for him. Well, I could use a vacation after today…Sure, why the heck not!"

    # Scene 4 - Yatch

    #Scene Bg - an image of the yacht on the water
    scene yatchonwater

    #Narrator 

    "A couple of weeks later, Susan readies to board the Neptune, admiring the lavish yacht."

    # Scene 5 - Susan Cabin

    #scene bg - Inside Susan Cabin
    scene susancabin

    #Narrator 
    show susan
    "As Susan sorts through her luggage, there is a knock at the door."
    show susan at left

    #dalton 
    show david at right
    dd "There will be a dinner for all the guests in the dining hall in 30 minutes."

    #Susan Murphy
    sm "Okay, thanks for the information."
    hide david
    hide susan 
    
    #play sound susan cabin thought
    #thoughts screen maybe ( displaying that susan is thinking)
    show susan
    sm " Okay, time for me to get dolled up for dinner. I hope the food is going to be good."
    hide susan


    #choice scene
    #The player is given the ability to navigate the boat and makes their way to the dining room.
    scene navigation 

    "Navigation to Dining Room"

    #Scene Bg - Navigation Option screen


    #Scene 6 - Navigation 

    scene hallway

    "Walking your way to the dining hall"
    #Navigation here

    #Scene 7 - Dining Hall

    scene diningroom

    #Narrator 
    "Susan enters the dining room and sees a well-dressed crowd sitting around the room at different tables."
    
    #play sound/music with fade in here not voice
    #Michael speaking as the player enters the room
    show michael
    mm "Ah, and here’s our final guest arriving! Welcome, Susan. Please, take a seat. Now that we’re all here, the party can start!"

    mm "I know some of you are already acquainted with each other, but to help break the ice, why don’t we have a few introductions?"

    #Presenting the characters introducing them to the player ( IDEA: Unique BG, sounds etc)

    mm "First, we have Mr. Richard Reed, the CEO of Reed Industries, and his wife, Mrs. Rachel Reed."

    mm "Next, we have the illustrious Dr. Ezekiel Jones. The man’s service to our country and his patients' lives speaks for itself."

    mm "Then, We have the White sisters, Deborah and Patricia. True yin and yang if I’ve ever seen one."

    mm "Of course, the brilliant Susan Murphy, one of the great detectives of our time."
    
    mm "And finally, our talented captain, Lloyd Lewis! He’ll be navigating the boat for the next five days, so don’t expect to see much of him away from the helm"
    hide michael
    
    #LLoyd Lewis
    show lloyd
    ll "That’s my cue. Back to the helm, I go. Have a good meal, folks"
    hide lloyd

    #Michael McQuaid
    show michael 
    mm "Speaking of here’s dinner now!"
    hide michael
    
    #Susan Thoughts 
    show susan
    sm "Well, seems like McQuaid is in high spirits tonight. But why invite me? I stand out among these high-society types like a pebble among rhinestones. Hmm."
    hide susan
    

    #Narrator
    "Just then, Susan hears a commotion from another table."

    #Richard Reed
    show richard at right
    rr"How dare you! Don’t you know who I am, boy?"

    #William Windchime
    show william at left
    ww "I-I’m so sorry, mister Reed, sir, I didn’t mean t-"

    #The Scene Here would still be in the room

    #Narrator  
    "She turns to see one of the guests, Richard Reed covered in drink and screaming at the waitstaff."

    #Richard Reed 
    show richard
    rr"I don’t care! Can’t you see how expensive this suit is! It’s worth more than your life, at the very least"

    #Richard Reed 
    rr "Michael, see to it that your server is disciplined! I’m going to go get changed out of this mess!"
    hide richard
    hide william
    
    #Narator 
    "Richard leaves, muttering about having to replace a perfectly good suit."

    #Susan Murphy Thoughts
    show susan
    sm "ell, Richard seems to be a very happy camper. I wonder if he’s always like this… Does the same go for his wife?"
    hide susan

    #Michael McQuaid 
    show michael
    mm "William! Go wait in the kitchen. We’ll talk about this later!"
    hide michael

    #Narrator 
    "The waitstaff member leaves, looking abashed."

    #Ezekiel Jones
    show zeke at right
    ej "Don’t be too harsh on him, McQuaid. It was an honest mistake. The poor boy just tripped."

    #Michael McQuaid 
    show michael at left
    mm "I expect a certain amount of professionalism, Doctor, and I’d thank you not to tell me my business. Now then, everyone, please continue to enjoy the party."
    hide michael
    hide zeke 

    #Narrator  
    "The man sitting next to Susan turns toward her and starts talking to her quietly."
    
    #Ezekiel Jones 
    show zeke at right
    ej "Seems like that really got him going."

    #Susan Murphy 
    show susan at left
    sm "Yeah,really got his goat. Seems very uptight. I don’t remember him being like this."

    #Ezekiel Jones 
    ej "If you worked for him, that’s why. He’s always nice until he’s not."

    #Susan Murphy 
    sm "Seems like you know our host quite a bit."

    #Ezekiel Jones 
    ej "If you worked for him, that’s why. He’s always nice until he’s not."

    #Susan Murphy 
    sm "Seems like you know our host quite a bit."

    #Ezekiel Jones 
    ej "Yeah, I know Michael, unfortunately. Hi, I’m Ezekiel."

    hide zeke 
    hide susan

    menu scene_7_choice:
        "What are you looking to do?"
        "Go Mingle":

            jump mingle 

        "Get to know Ezekiel":

            #Susan Murphy 
            sm "A pleasure to make your acquaintance. Well, Zeke, I think I’ll go mingle a bit. See you around."

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

            jump mingle

label mingle:
    #Narrator 
    show susan
    "Susan gets up and wanders the dining room. She comes to a table with three elegantly dressed women where Richard had been sitting"
    

    scene switchtables

    #Patricia White 
    show patricia at right
    pw "Well, I don’t see why Richard had to go and make such a fuss! I mean, it was just booze!"

    #Rachel Reed 
    show rachel at left
    rar "Richard just gets easily upset when something happens to his things. I mean, that was a very expensive suit."
    

    #Deborah White
    hide rachel
    show deborah at left 
    dw "He’s a man who cares about his appearance. Can’t ask for much more than that these days."

    #Patricia White
    
    show patricia at right
    pw "Oh, if it isn’t “the brilliant Susan Murphy”? What’d you do for McQuaid to be called ‘brilliant’?"

    #Susan Murphy
    hide deborah
    show susan at left
    sm "I found a leak in his bank account for him. I’m sorry. I know McQuaid introduced us, but it went by a bit fast. Would you mind reminding me of your names?"

    #Deborah White
    hide patricia
    show deborah at right
    dw "Oh, pardon me! I’m Deborah. This is my sister Patricia, and this is Rachel, the blowhard’s wife."
    hide deborah
    hide susan

    #Rachel
    show rachel
    rar "Hey!"
    hide rachel

    #Narrator 
    "A ringing sound is heard, and Michael taps his glass with a spoon like he is making a toast."

    #Michael McQUiad
    show michael
    mm "Everyone! I hope you've enjoyed your evening, but now it's time to get to business"
    hide michael

    #Narrator 
    "A hush settles over the room."

    #Michael Mcquaid 
    show michael
    mm "You see, I may have told a little white lie on your invitations. The real reason you’re here is that each one of you has a secret. Something hidden that would ruin you if it were to get out."

    #Michael McQuaid 
    mm "I brought you all here so we could come to a little… arrangement. Over the next few days, I am sure you’ll find this to be in your best interest."

    #Michael McQuaid 
    mm "After all, who knows what would happen if your little secrets were no longer secret."
    hide michael 

    #Susan Murphy 
    show susan
    sm "What!"
    hide susan 

    #Deborah White 
    show deborah
    dw "How dare you!"
    hide deborah

    #Ezekiel Jones 
    show zeke
    ej "What on  Earth are you talking about"
    hide zeke

    #Patricia White 
    show patricia
    pw "WHAT IN THE FLYING FUCK ARE YOU ON ABOUT!"
    hide patricia

    #Rachel Reed 
    show rachel
    rar "Hrrk! I think I’m going to be sick."
    hide rachel

    #Narrator 
    "Heads turn as Rachel runs from the room, sickened by Michael’s words."

    #Susan Murphy thoughts
    show susan
    sm "He couldn’t mean… but how could he… No, that’s impossible."

    #Susan Murphy thoughts
    sm "He couldn’t mean… but how could he… No, that’s impossible."

    #Susan Murphy Thoughts
    sm "There’s no way he could know. What is this about? Hmm…"
    hide susan 

    #Ezekiel Jones 
    show zeke at left
    ej "What do you want, McQuaid?"

    #Michael McQuaid 
    show michael at right
    mm "The same I’ve always wanted, always deserved. Power. While you yucks have been going about your days with your crimes, I’ve been building a list on all of you."
    hide michael 
    hide zeke

    #Susan Murphy Thoughts
    show susan
    sm "Building a list? Why would he possibly be building a list on me? *Sigh* I can’t ever get a vacation. I should probably check on Rachel. I wonder where she ran off too."
    hide susan 

    #Scene 8 
    scene hallway

    "Navigating the hallway"
    
    #Navigate here to hallway

    #Scene 9 

    #narrator voice
    "Susan leaves the room in search of Rachel. She is now in the Hallway."    

    #Susan Murphy
    show susan
    sm "She said she was feeling sick. I should probably go and check the washroom."
    
    #Scene 10   
    #Navigating to the washroom

    scene navigatingtowashroom

    "Navigating to washroom"

    #Scene 11
    scene washroom

    #Narator Voice
    "Susan enters the washroom but finds no one."

    #Susan Murphy Voice
    show susan
    sm "Drat, she’s not here. Where else would she be… their cabin!"

    #Scene 12
    scene navigatetocabin

    "navigation to the cabin"

    #The player navigates to the Reed’s cabin, the door is slightly ajar

    #Scene 13

    #The Hallway Facing the Ajar Cabin Door
    scene hallwayfacingdoor

    #Narrator
    "When Susan arrives at the Reed's cabin, she finds the door slightly ajar."

    #Scene 14

    #The player navigates to the Reed's cabin, opens the door and looks inside
    scene reedscabin

    "Reaching the cabin, opening the door to look inside"

    #Scene 15 - First Murder   

label first_murder:

    scene reedscabin

    #Narrator 
    "As Susan opens the door, she is met with a horrific sight. Richard Reed, former CEO of Reed Industries, has been beaten bloody, and unmoving."
    
    show screen reedscene_investigation

    
    hide screen reedscene_investigation
    #Susan Murphy 
    show susan
    sm "Oh Shit. Is that Richard? Oh my God, I need to tell everyone about this."
    hide susan

    #scene 16 

    #The player navigates back to the Dining Hall

    scene hallway

    "Navigating back to the dining hall"

    #scene 17
    scene diningroom

    #Narrator
    "Susan sprints back to the dining room, bursting through the door, panting."

    #Susan Murphy
    show susan at left 
    sm "McQuaid! I thought you wanted us to do your bidding, not kill us"

    #Michael McQuaid
    show michael at right
    mm "Pardon me, Ms. Murphy?"

    #Susan Murphy 
    sm "I went to look for Rachel because she was feeling a bit sick from your “news,” and I found Richard dead in their cabin. Explain yourself!"

    
    #Michael Mcquaid

    mm "Well, it wasn’t me. I was here the entire time? You said you went to find Rachel? What if she went to get rid of her dastardly husband?"


    #Susan Murphy
    
    sm "Oh, come on, that’s ridiculous."
    

    #Michael Mcquaid
    
    mm "As far as we know, you could have killed him." 
    hide michael

    #Ezekiel Jones
    show zeke at right 
    ej "Hmm, he has a good point. We know nothing for sure. While you do seem like a lovely person Susan, you were out there alone."

    #Susan Murphy
    
    sm "You can’t be serious. You all saw me leave here a few seconds ago." 
    
    #Patricia White
    hide zeke
    show patricia at right
    pw "Oh no, sis, are we gonna get murdered? I’m too pretty to get murdered."
    
    #Deborah White
    hide patricia
    show deborah at right
    dw "Calm down, Patti. Nothing is gonna happen to you."

    #Patricia White
    hide deborah
    show patricia at right
    pw "You don’t know that! I’m gonna die to a murderer onboard."

    #David Dalton
    hide patricia
    show david at right
    dd "I don’t know if I want to work here if someone is murdering people. Someone tell the captain to turn thi - …"
    hide david
    hide susan

    #Narrator
    "Indiscriminate chatter happens amongst the guests."

    #Michael Mcquaid
    show michael
    mm "ALRIGHT, EVERYONE! Settle down. Let’s not lose our heads. Susan, you are a private eye, yeah? I think you have the qualifications to solve this."

    #Susan Murphy
    show susan at left
    show michael at right
    sm "What? You don’t suspect me anymore?"


    #Michael Mcquaid
    mm "I do. That’s why someone should be with you every second."
    hide michael

    #Ezekiel Jones
    show zeke at right
    ej "I’ll keep an eye on her."
    
    #Susan Murphy
    sm "Oh, please."

    
    #Michael Mcquaid
    hide zeke
    show michael at right
    mm "Perfect, the doctor and the eye. What a confidential relationship."
    hide michael

    #Patrica white
    show patricia at right
    pw "I wanna go look for Rachel! She could be in danger!"
    hide patricia 

    #Deborah White
    show deborah at right
    dw "Aren’t you afraid of getting murdered?"
    hide deborah

    #Patrica White
    show patricia at right
    pw "Yes, but she was nice to me. Oh, please come with me, Debbie."
    hide patricia 

    #Deborah White
    show deborah at right
    dw "auughhh, fine. Let’s go look for her. Hey Michael! You heard?"
    hide deborah

    #Michael Mcquaid
    show michael at right
    mm "Loud and clear. The rest of us will stay here. Don’t want anyone else turning up dead now."
    hide michael
    hide susan

    #Narrator
    "Susan and Ezekiel left to go to the crime scene. Deborah and Patricia left moments after to try and find Rachel."

    #Scene 18 

    #Player navigates to the Murder 1 Scene Inside the Reed’s Cabin

    scene hallway

    "Navigating to the murder scene"

    #Scene 19

    #Investigating Richard's Murder Scene

    show reedscene_investigation

    #Narrator
    "While looking at a crime scene, click on points of interest around the area to find clues."

    #Narrator
    "Clues will be added to your detective board for easy viewing."

    #Clues are in slide 43 & 44
    #Code Mechanics Will be updated here

    #scene 20
    scene murderscene

    #scene 20
    scene murderscene

    #Susan Murphy
    show susan at left
    sm "I think that's all we can get from the crime scene. How about we go do some interviews?"


    #Ezekiel Jones 
    show zeke at right
    ej "I'm afraid everyone's probably going to be asleep, Murphy. Perhaps we should break for the night and pick up where we left off in the morning?"


    #Susan Murphy
    
    sm "As much as I hate to leave a case like this… you're right. Reconvene in the dining room tomorrow?"
    

    #Ezekiel Jones
    
    ej "Of course."

    #Narrator
    hide zeke
    hide susan
    "Susan and Ezekiel leave the crime scene and go to their separate rooms."


    #------------------------------------- END OF DAY 1 --------------------------------------------------------#

    #------------------------------------- START OF DAY 2 --------------------------------------------------------#
    

    #Day 2 
    #Scene 21
    scene daytwo

    "Day two"

    #NAVIGATION HERE
    #The player Navigates to the bathroom
    scene hallway
    "Navigating the hallway"
    
    #Scene 22
    scene hallway
    
    #Narrator
    "Susan is walking through the halls and hears some commotion coming from a bathroom."

    #Scene 23 
    #The player navigates to the Bathroom

    scene hallway
    "Navigating to the bathroom"

    #Scene 24
    scene insidebathroom

    #Narrator
    "Inside the bathroom, she sees the sisters, Patricia and Deborah White. Patricia is by the toilet, feeling sick to her stomach. Deborah is keeping her company."

    #Patrcia Sound Effect
    #Retches

    #Deborah
    show deborah
    dw "That's it, it's okay. Let it out."
    hide deborah

    #Susan Murphy
    show susan at left
    sm "Hello? Patricia, Deborah. You gals doing okay?"
    

    #Deborah White
    show deborah at right
    dw "Hey Susan, yea Patty's still a little shaken up. I thought it would be good to catch some sun and get some fresh air, but her stomach is still in knots." 
    hide deborah

    #Patricia White
    show patricia at right
    pw "Ughh, yea… at least this bathroom has a porthole. Though I'm not too fond of the sea smell."
    hide patricia

    #Deborah White
    show deborah at right
    dw "I'm just glad it seems to be helping calm you down. Back home, all she had to do was go outside for her worries to disappear naturally. Anyway, how are you doing, Susan?" 
    
    #Susan Murphy
    sm "About the same as everyone else, I guess. Can't I ever get a vacation?"

    #Deborah Murphy
    dw  "I hear you'. A working girl's work is never done."

    #Susan Murphy
    sm "Yea, speaking of, did you two find Rachel last night?"

    #Patricia White
    hide deborah
    show patricia at right
    pw "Yes, we did, *Hrph*"
    hide patricia

    #Deborah White
    show deborah at right
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
    hide deborah
    show patricia at right
    pw "We'll be just peachy, don't you worr– *Heaves*"
    hide patricia
    
    #Deborah White
    show deborah at right
    dw "We'll be fine. See you."
    hide deborah 
    hide susan

    #Scene 25

    #The player navigates to the Hallway
    
    scene hallway 
    "Navigating the hallway"

    #Scene 26
     
    #Narrator 
    "Susan leaves the White sisters in the bathroom."

    #Susan Thought 
    show susan
    sm "Thoughts: They say she broke down. It still doesn't excuse her totally. I have to keep looking for clues. Let's see how Rachel is actually doing."

    #Scene 27 

    #The player navigates to the dining room

    scene hallway
    "Navigating to dining room"

    #Scene 28 - The dining Hall

    #Narrator 
    "Susan now enters the Dining Hall. She sees Rachel with her head in her hands, Ezekiel trying to comfort her, and McQuaid is in the corner."

    #Ezekiel Jones
    show zeke
    ej "Ah, Susan, good morni-"
    hide zeke

    #Rachel Reed
    show rachel
    rar "Susan? SUSAN! You're the private eye. Right? Did you find out who did it? Did you find my husband's killer?"

    #Susan Murphy
    show susan at left
    show rachel at right
    sm "Not yet. I'm still working on it. I have gathered some clues, but I'm still working it all out."
    
    #Racheel Reed
    rar "So you have nothing? It's a Yacht! Someone here is responsible! They must be found and pay for what they've done!"
    hide rachel

    #Michael Mcquaid
    show michael at right 
    mm "Easy there. I'm sure Ms. Murphy is doing everything she can to solve this case."


    #Susan Murphy 

    sm "Don't think we've forgotten about you, McQuaid. Unfortunately, there are more pressing matters at hand."


    #Susan Murphy
 
    sm "But yes, I'll figure it out. Don't you worry about that! Rachel, I hope you don't mind, but I need to ask you some questions."

    hide michael
    #Rachel Reed
    show rachel at right 
    rar "What? Why me?"
    
    #Susan Murphy
    sm "Well, to be perfectly honest, you left the room last night and then Mr. Reed…you know."

    
    #Rachel Reed
    rar "You... You can't seriously be thinking I did this. He was my husband, for Christ's sake!"
    hide rachel

    #Ezekiel Jones
    show zeke at right
    ej "She isn't accusing you of anything, dear. She just needs to know where everyone was to paint the picture of what happened last night. Nothing more."


    #Susan Murphy

    sm "Exactly. Now please, if you may. Where did you go when you left the dining hall last night?"


    #Rachel Reed
    hide zeke 
    show rachel at right
    rar "Well, after the news, I felt nauseous. So I started to head to the bathroom. On my way there, I caught a draft of the ocean breeze and decided to go on the deck instead."

    #Susan Murphy
    
    sm "Did the ocean breeze help?"
    
    
    #Rachel Reed
    
    rar "A little. It did help to calm me down. I did hear something, but I thought it was just the party or something. Oh God, what if it was Richard? I could have done something to save him! He would have been alive if I had just stayed by his side."
    

    #Susan Murphy
    
    sm "Hey, don't do that. There's nothing you could have done to see this coming."
    

    #Ezekiel Jones
    hide rachel
    show zeke at right
    ej "Yea, take it from me. It doesn't help anything at all."
    hide zeke
    
    #Susan Murphy
    sm "Did you find your way back to the party?"

    #Rachel Reed
    show rachel at right
    rar "Yes, eventually the White sisters came to help but- *sobs* all they did was made me feel worse by telling me that I lost my Richard."
    

    #Susan Murphy
    
    sm "A couple more questions, okay? Do you know anyone that could've done this?"
    

    #Rachel Reed
    rar "*sniff* Richard always had enemies. Since we were back in school, he'd always been a bit...abrasive. They'd just never understood him. Oh, my Richard. I miss you so much.."


    #Ezekiel Jones
    hide rachel
    show zeke at right
    ej "Okay, that's enough. You should take some time to rest and grieve your loss."


    #Susan Murphy 

    sm "Yea, I'm sorry this happened."


    #Rachel reed
    hide zeke
    show rachel at right
    rar "Me too."
    hide rachel 
 
    #Susan Murphy 

    sm "McQuaid. What happened to the waitstaff member that had a squabble with Reed last night?"


    #Michael Mcquiad
    show michael at right
    mm "I sent him back to the kitchen to do some extra work. He should be there now if you want to talk to him."

    #Susan Murphy
    
    sm "Okay. We aren't done here either."
    

    #Michael Mcquiad
    
    mm "Oh, Ms. Murphy, where would I possibly go?"
    

    #Narrator
    "Susan looks at Ezekiel to confirm that he is coming with her, and then Susan leaves the Dining Hall."

    #Navigating the hallway
    scene hallway

    "Navigating hallway together"

    #Scene 30 - Ezekiel Jones (Hallway)

    sm "Ezekiel. I want to ask you a few questions."
            
    #Ezekiel Jones
    ej "I understand. I want this killer brought to justice, and I want to help you. I will answer any questions to the best of my ability."

    menu ezekiel_inv:
        "Choose path of investigation"
        "Ask About Footprint":
            
            #Scene 31 - Ezekiel Jones / Footprint (Hallway)

            #Susan Murphy 
            sm "I would like to check your shoes."
        
            #Ezekiel Jones
            ej "That is an unusual thing to ask. Is there a reason why?"

            #Susan Murphy 
            sm "Yes, there is. However, I can only say once I am certain of something."

            #Ezekiel Jones
            ej "I understand. I should mention I have multiple pairs of shoes. Would you like me to see them as well?"
                            
            #Susan Murphy 
            sm "Yes, if you have more, please take me to them. I need to check myself."

            #Ezekiel Jones
            ej "Okay, I will show you to them."

            #Scene 32 - Ezekiel Jones / Footprint (Ezekiel's Room)

            scene ezekielroom

            #Susan Murphy 
            sm "It is interesting how you have so many shoes and yet not a single match. Are you sure that is all of them, or are you hiding another pair?"

            #Ezekiel Jones
            ej "W-what? Is- is that r-really what you think of me? I-I I thought we were friends. I even told you I would help you if you needed anything."

            #Narrator
            "Pain was filling Susan up inside, but she kept a poker face to see his reaction."

            menu ezekiel_footprint:

                "Choose path of investigation"

                "Press Further":
                    
                    #Scene 33 - Ezekiel Jones / Footprint (Ezekiel's Room)
    
                    #Press further 
                    "Pressing Further" 

                    #Susan murphy
                    sm "From the sound of your reaction, it looks like you are hiding something. If there isn't anything to hide, look me in the eye and say it confidently."

                    sm "Do you have another pair of shoes that you are hiding?"

                    #Narrator
                    "Ezekiel Jones: had pain in his eyes of anger and sadness but also understanding. He calmed himself and took a deep breath."

                    #Susan Murphy Thoughts
                    sm "Okay, that rules him out in that part, at least. I am glad, it pains me, but I must do this to find the killer."

                    #Ezekiel Jones
                    ej "No, I don't have another pair of shoes. You are free to take a look around my room to check."

                    #Narrator
                    "Susan continued to check the room for anything that was hidden evidence but found nothing."

                    #Susan Murphy
                    sm "It seems like I was out of line. Thank you for bearing with me."

                    #Ezekiel Jones
                    ej  "It is okay. I apologize for my reaction as well. I understand all you want to do is find the killer."

                    ej "I realize you have another question. However, I want to clear my head. Meet me back at the dining hall, and we can talk there."

                    #Susan Murphy
                    sm "I understand. I will visit you in the dining hall to continue the conversation."

                #Menu Option - Calm him down
                "Calm him down":
                    
                    #Scene 34 - Ezekiel Jones / Footprint (Ezekiel's Room)

                    #Calming him down possible choice
                    "Calming him down"

                    #Susan Murphy 
                    sm  "Of course, we are friends, but you must understand that I am a detective. I can't leave any stone unturned."

                    sm  "If you genuinely have nothing, then you won't mind if I check your room. I view you as a friend and someone I trust."

                    sm  "To do my job, I must do this. Please help me."

                    #Ezekiel Jones
                    ej "Okay, I understand you may look around for anything that could help your investigation."

                    #Narrator
                    "Susan looked through Ezekiel's room and found nothing."

                    #Susan Murphy 
                    sm "Thank you for bearing with me through this."

                    #Ezekiel Jones
                    ej "It’s okay. I understand that you need to do your job. This is something you must do."

        "Ask about training":
            
            #Scene 35 - Ezekiel Jones / Training (Ezekiel's Room)

            #asking about training possible choice

            "Asking about Training"

            #Susan Murphy 
            sm "I just have a few more questions for you, Ezekiel."

            #Ezekiel Jones
            ej "Okay, what is it you need to ask me."

            #Susan Murphy 
            sm "When examining the body, you mentioned you did some training. What kind of training did you do?"

            #Ezekiel Jones
            ej "I was a combat medic during World War 2. I had to do combat training and help people recover during the War."

            #Susan Murphy
            sm "hmm... Interesting."

            #Susan Murphy Thoughts
            sm "I need to choose my words carefully here. One wrong question, and I could low the information I need."

            menu ezekiel_training:
                "Choose path of investigation"
                "Press Further":
                    
                    #Scene 36 - Ezekiel Jones / Training (Ezekiel's Room) 

                    #pressing further possible choice

                    "Pressing Further"
                    
                    #Susan Murphy 
                    sm "War is a harsh time. It can traumatize people. You may be suffering from this traumatic experience."

                    #Ezekeil Jones
                    ej "Are you stating that because I was in a War, it harmed me so much that I continued to kill people?!"

                    ej "I despise violence! I don't like harming people!"

                    #Susan Murphy 
                    sm "Yet you were in a War, and War involves killing."

                    #Ezekiel Jones
                    ej "It is true. I am suffering. Seeing innocent people die before your eyes is painful."

                    ej "No matter what, I joined this War because it is my duty! I wanted to help people, not kill them!"
                    
                    #Susan Murphy
                    sm "I apologize, Ezekiel. I know I was rough with asking questions."

                    #Narrator
                    "Ezekiel calms himself down."

                    #Ezekiel Jones
                    ej "It is okay. You are just doing your job."

                #Menu Option - Calm him down    
                "Calm him down":
                    ##Scene 37 - Ezekiel Jones / Footprint (Ezekiel's Room)

                    #Susan Murphy 
                    sm "Being a medic in the War is tough. You are not suffering from any mental trauma, are you?"

                    #Ezekiel Jones
                    ej "It really hurts me to see people die. While I do admit there might be some trauma that I am facing, I can't stop doing my job to help people."

                    ej "A friend of mine was on the front lines of World War 2, and he got shot. I did my best, everything I could do to save him."

                    ej "But no matter how hard I tried, it was not enough. He still died. It haunts me to this day."

                    #Susan Murphy 
                    "That sounds rough. I am sorry for your loss. If there is anything I can do to help, don't hesitate to ask."

                    #Ezekiel Jones
                    ej "Thank you, Susan. That means a lot."
                                        
                    menu ezekiel_calmhim:
                        "What's your next step?"
                        "Interrogate another passenger":
                            jump investigation_choice
                        "Quit for the day":
                            jump end_of_dayone                  
  
     
   
    #Scene 29 - choose to investigate

    scene hallway

    menu investigation_choice:
        "Choose who interrogate"
        "William Windchime":
            jump william_inv
        "David Dalton":
            jump dalton_inv
        "Michael McQuaid":
            jump michael_inv
        "Quit for the day":
            jump end_of_dayone

    

label dalton_inv:

    #Scene 38 - David Dalton (Kitchen)

    #keeping for alpha to provide flow to the game linear mechanics

    scene hallway

    "Navigating to Kitchen" 

    # ----------

    scene kitchen 

    #David Dalton 
    dd "Well, if it isn't the detective and her faithful Watson. Here to ask me a few questions, then?"

    #Susan Murphy 
    sm "Yes, actually. But first, I'm afraid I never caught your name…"

    #David Dalton 
    dd "Dalton. David Dalton."

    #Scene 39 - David Dalton / Footprint (kitchen)

    menu ask_dalton:
        "Choose your path of investigation"

        "Ask about footprint":
            
            #Asking about footprint 

            #Susan Murphy 
            sm "Dalton, can we see your shoes for a moment?"

            #Narrator
            "Dalton looks taken aback."

            #David Dalton 
            dd  "My shoes? Why would you ever need to see them?"

            #Susan Murphy 
            sm "Now that's a bit suspicious, Dalton. It would be a fairly innocuous request if you didn't do anything. Why not show us your shoes?"

            #Ezekiel Jones
            ej "Come now, Dalton, we found a shoe print at the crime scene, and we just want to verify whose shoe it was."

            #Susan Murphy Thoughts
            sm "Did Ezekiel really tell him that? He doesn't know the first thing about investigations!"

            #David Dalton 
            dd  "Oh, well, why didn't you say so?"

            #Narrator
            "Dalton removes his shoes and shows Susan the soles. They do not match the print found next to Richard's body."

            #Susan Murphy 
            sm "Well, that rules out that pair, at least. Do you have any other shoes, Dalton?"

            #David Dalton 
            dd "I do, but they're identical. I can go and grab them from my locker if you like."

            #Ezekiel Jones
            ej "We'd appreciate it, just to be thorough."

            #Narrator
            "Dalton steps through a door into the crew quarters."

            #Susan Murphy 
            sm "A thought occurs to me, Ezekiel. If all the staff lockers were in the same place,could Dalton have taken William's shoes?"

            #Ezekiel Jones
            ej "Well-"

            #Narrator
            "Dalton enters the room, carrying an identical pair of shoes to the ones he was wearing."

            #David Dalton
            dd "I could try, Miss Murphy, but the kid keeps a padlock on his locker. And why would I go through the effort in the first place?"

            menu dalton_footsteps:
                "What's your next step?"
                "Interrogate another passenger":
                    jump investigation_choice
                "Quit for the day":
                    jump end_of_dayone
                

        "Ask about whereabouts":
            
            #Scene 40 - David Dalton / Ask Whereabouts (kitchen)

            #Susan Murphy 
            sm "Where were you between 6:00 and 7:00 PM last night?"

            #David Dalton 
            dd "Well, I was in the Dining Hall until 6:30 when Mr. McQuaid asked me to come down here and get some more hors d'oeuvres, so I came in and got them, then went right back."

            #Susan Murphy 
            sm "Can anyone verify that?"

            #David Dalton 
            dd "Sure, Mr. McQuaid sent me, and William was here when I got down. Oh, and some of the guests might have heard the boss's order."

            #Susan Murphy 
            sm "And when did you get back to the Dining Hall?"

            #David Dalton 
            dd "Oh, 6:50, 6:55."

            #Ezekiel Jones
            ej "That seems like an awfully long time to get some appetizers. Sure you didn't take a little detour to murder a prick who insulted your co-worker?"

            #David Dalton 
            dd "Kill? For William? Oh please, I like the kid, but we ain't that close. We were out of appetizers, so I had to make more."

            #David Dalton 
            dd "Now, do you have anything else to ask, or can I get back to these dishes?"

            menu dalton_whereabouts:
                "Choose path of investigation"
                "Press Further":
                    #Scene 41 - David Dalton / Ask Whereabouts (kitchen)

                    #pressing further 

                    #Susan Murphy 
                    sm "You're sure that's all you did? It seems rather sloppy not to have spare hors d'oeuvres ready. And surely it would take less than 20 minutes."

                    #David Dalton 
                    dd "Well, I might've taken a moment to go to the washroom, but is that a crime?"

                    #Ezekiel Jones
                    ej "No, but murder is, so forgive us for wanting to know what you did in a mysterious 20-minute window."

                    #Susan Murphy 
                    sm "Can anyone corroborate this?"

                    #David Dalton 
                    dd "I'm not some schoolgirl going to the restroom in packs. Now, if you'll excuse me, I have some dishes to wash."

                    #Narrator 
                    "Dalton turns to the sink, and Susan turns to Ezekiel."

                    #Susan Murphy 
                    sm "Those wounds could definitely have been made in 20 minutes. Most fights don't take longer than a few moments, much less that long."

                    #Ezekiel Jones
                    ej "We'll have to keep an eye on him."

                    menu dalton_wherabouts_pressfurther:
                        "Choose path of the investigation"
                        "Interrrogate another passenger":
                            jump investigation_choice
                        "Quit for the day":
                            jump end_of_dayone


                "Leave it be":
                    jump end_of_dayone
                
                "Interrogate another passenger":
                    jump investigation_choice
                
                "Quit for the day":
                    jump end_of_dayone
                

            

                      
    
        

    
label william_inv:
    #Scene 42 - William Windchime 

    #Narrator
    "William Windchime walks into the kitchen"
    
    #Susan Murphy 
    sm "Hello, William. We want to ask you a few questions if you don't mind."


    #William Windchime
    ww "Oh. Um. I guess not. It's about the murder, right?"

    #Ezkeiel Jones
    ej "Yes, it is. Now son, make sure to answer truthfully. We just want to get to the bottom of this."

    menu windchime_inv:
        "Choose path of investigation"

        "Asking about footprint":
    
            #Scene 43 - William Windchime / Footprint (kitchen)

            #Susan Murphy 
            sm "Can we see your shoes?"

            #William Windchime
            ww "What? Why?"

            #Ezekiel Jones
            ej "We found a shoe print at the scene of the crime, and we're trying to narrow down whose it was. Now come on, show us. "

            #William Windchime
            ww "Well, hold on, wait a minute-"

            #Susan Murphy 
            sm "What's the problem, kid? If you didn't do it, you've got nothing to hide."

            #William Windchime
            ww "Well- but- okay…"

            #Narrator 
            "William takes off his shoe and shows it to Susan. It matches the shoe print."

            #Susan Murphy 
            sm "It's a match!"

            #William Windchime
            ww "I swear it's not me! Someone stole them last night!"

            #Ezekiel Jones
            ej "Right, sure they did. I'm sure they took them right off your feet. "

            #William Windchime
            ww "No, no. I have a second pair that I was wearing. Please, it wasn't me!"

            menu windchime_footprint:

                "Choose path of investigation"

                "Press further":
                    #Scene 44 - William Windchime / Footprint (Kitchen)

                    #Pressing Further Possible Choice

                    "Pressing Further"

                    #Susan Murphy 
                    sm "Right. Someone stole your spare pair of shoes, committed murder, and then returned them to you."

                    sm "Because that sounds entirely plausible. Who would even do that?"

                    #William Windchime
                    ww "W-w-well, Dalton and I share a locker. It could have been him!"

                    #Ezekiel Jones
                    ej "You have to admit, this seems awfully suspicious. Especially with how rude Richard was to you last night."

                    ej  "Now, I'm sure that others have been rude to you in the past, but maybe you finally had enough, eh?"

                    #William Windchime
                    ww "I don't have to stand here and take this! If you'll excuse me, there are things I need to do."

                    #Narrator 
                    "William storms off."

                    #Susan Murphy
                    sm "Damn, there he goes." 

                    menu windchime_press:
                        "What's your next step?"

                        "Interrogate another passenger":
                            jump investigation_choice

                        "Quit for Day":
                            jump end_of_dayone
                        

                        "Interrogate another passenger":
                            jump investigation_choice
                        
                        "Quit for the day":
                            jump end_of_dayone
                
        "Asking about wherabouts":

                #Scene 45 William Windchime / Whereabouts (kitchen)
   
                #Susan Murphy 
                sm "Where were you around 6:30 last night?"

                #William Windchime
                ww "I was here, in the kitchen. I spilled that soup, and then Mr. McQuaid yelled at me, and I didn't want to cause more trouble, so I came right down."

                #Ezekiel Jones
                ej "Can anybody corroborate that story?"

                #William Windchime
                ww "W-well, Dalton was in here around 6:50, and Mr. McQuaid sent me-"

                #Susan Murphy 
                sm  "So no."

                #William Windchime
                ww "I… I guess not. But it wasn't me, I swear! I was cleaning up the kitchen, that's all!"

                #Ezkeiel Jones
                ej "Sure, kid, sure."

                menu windchime_whereabouts:

                    "Choose path of investigation"

                    "Press Further":
                        #Scene 46 William Windchime / Whereabouts (kitchen)

                        #Pressing Further Possible Option 

                        "Pressing Further"
                        
                        #Susan Murphy 
                        sm "You're positive that no one could vouch for your whereabouts? No one came down for a snack, and you didn\'t go to the washroom or leave?"

                        #William Windchime
                        ww "No, ma'am. Mister McQuaid told me to stay down here, so… I did."

                        #Ezkeiel Jones
                        ej "Well, no one will fault you for loyalty, but you've got to admit how suspicious this sounds."

                        #William Windchime
                        ww "Well.. yes, but I swear, it wasn't me!"

                        menu windchime_further:

                            "Choose path of investigation"

                            "Interrogate another passenger":
                                jump investigation_choice

                            "Quit for day":
                                jump end_of_dayone
                            

                    "Investigate Motive":
                        
                        #Scene 47 William Windchime / Whereabouts (kitchen)

                        #Susan Murphy 
                        sm "Alright, William, I have another question for you. When you spilled that soup on Richard, he shouted at you, right? That must have made you angry."

                        #William Windchime
                        ww "Well, yes, but not enough to... to- "

                        #Ezkeiel Jones
                        ej "To what? To murder someone? Someone who humiliated you in front o- "

                        #William Windchime
                        ww "Yes! Of course, I was angry! You'd be, too, if some rich asshole screamed at you for an accident! But I'm not some loon to kill somebody over something like that!"

                        #Susan Murphy 
                        sm "Easy, kid, we're just covering our bases. Say, how did you end up here, anyways? You don't strike me as the type to go for a service position."

                        #Narrator
                        "William grows visibly nervous."

                        #William Windchime
                        ww "Well- um-"

                        #Narrator
                        "William sighs."

                        #William Windchime
                        ww  "You're right. I'm not really cut out for this sort of work. What I really want is to travel, to see the world, but…"

                        ww "Well, it's a little embarrassing, but I'm out of money. I had quite a bit from my parents, but it didn't… last as long as I thought it would."

                        ww "Why am I even telling you this? I have to go. I've got things to do."

                        #Narrator
                        "William walks off in a huff."

                        #Ezekiel Jones
                        ej  "Is it just me, or did he sound… resentful? Do you think he could have killed Richard to humiliate his employer?"
                        
                        #Susan Murphy 
                        sm "It's certainly possible but unlikely."

                        menu windchime_motive:

                            "What's your next step?"

                            "Interrogate another passenger":
                                jump investigation_choice
                            "Quit for the day":
                                jump end_of_dayone
                            
                    

label michael_inv:

    #Narrator 
    "Susan and Ezekiel leave for the Dining Hall."

    #Navigating to the DIning Hall 
    scene hallway 

    "Navigating to the Dining Hall"

    #Scene 48 - Michael McQUaid (Dining Hall)

    scene dininghall

    #Michael Mcquaid
    mm "Well, well, well, if it isn't our very own Ms. Holmes and Dr. Watson. Any luck out there?"

    #Susan Murphy
    sm "We're looking at a few avenues of investigation, and I was hoping to pick your brain about some of the people here."

    #Michael Mcquaid
    mm "Of course! I'm all ears."

    menu mcquaid_inv:
        "Choose your path of investigation"
        "The Reeds":
            
            #Scene 49 - Michael McQUaid / The Reeds (Dining Hall)

            #Ask About Reeds possible option

            #Susan Murphy
            sm "Did Richard or his wife have any enemies? Particularly among those aboard?"

            #Michael Mcquaid
            mm "Oh, no shortage! How do you think I was going to blackmail him? But the people on this boat?"

            #Narrator
            "The party's host hesitates for a moment."

            #Michael Mcquaid
            mm "Not that I know of."

            #Susan Murphy
            sm "Care to elaborate on that?"

            #Michael Mcquaid
            mm "Richard was… involved, shall we say, with quite a few shady dealings. He took a lot of money from a lot of people."

            mm "Besides that, you saw how abrasive he was with poor William? He was like that with everyone except his beloved Rachel."

            mm  "That sort of behaviour earned him no few enemies. But as far as I know, none of them are on this boat."

            #Susan Murphy
            sm "Speaking of the blackmail… What exactly is it that you have on me?"

            #Michael Mcquaid
            mm "Oh, I think you know exactly what I have on you, Murphy. Now. Do you have any questions that I'll actually answer?"


            #Scene 50 - Michael McQUaid / The Reeds (Dining Hall)

            #Susan Murphy
            sm "Yes, actually. Is there any chance that Rachel murdered her husband?"

            #Michael Mcquaid
            mm "No. Whatever else they were, they loved each other more than anything."

            menu mcquaid_reeds:
                "Choose path of investigation"
                "Interrogate another passenger":
                    jump investigation_choice
                "Quit for the day":
                    jump end_of_dayone
                
        "William Windchime":
            
            #Scene 50 - Michael McQUaid / Asking about windchime (Dining Hall)

            #Possible choice of asking about William Windchime

            #Scene 51 - Michael McQUaid / Asking about windchime (Dining Hall)

            #Susan Murphy
            sm "What can you tell us about the kid, Windchime?"

            #Narrator
            "Michael shakes his head sadly."

            #Michael Mcquaid
            mm "Sad story, that one. He's worked for me for a few months now. He hasn't said much, but I've looked into him."

            mm "The kid's heir to one of the biggest lawn-decoration companies in the country, but he never wanted that."

            mm "It seems he wanted to travel, but the money dried up when he got to Hawaii. I asked him why he didn't just ask his parents for more money, but…"

            mm "Well, he always gives me a sad look when I ask."

            #Susan Murphy
            sm "And what can you tell us about your other waiter?"

            #Michael Mcquaid
            mm "Oh. Dave's worked for me for quite a while. I trust him to take care of the things I don't want to do around the boat."

            #Ezekiel Jones
            ej "High praise for a simple waiter."

            #Michael Mcquaid
            mm "Oh, he's more of a jack of all trades. He's a dab hand with a wrench and a decent cook."

            #Susan Murphy
            sm "When did you hire him?"

            #Michael Mcquaid
            mm "Oh, four, five years ago now. He'd fallen on some hard times and needed work. So I took him on, and now he's here!"

            #Susan Murphy
            sm "Do you know what he did before he fell on these ‘hard times’?"

            #Michael Mcquaid
            mm "Y'know, I'm not quite sure. Whenever I asked, he would always say he doesn't like talking about it."

            mm "Personally, I suspect it was some trade or other, but I never got answers out of him"

            #Ezekiel Jones
            ej "Would he have any reason to kill Richard?"

            #Michael Mcquaid
            mm "None that I can think of. Do you have any more questions for me? "

            menu mcquaid_chime:
                "Choose path of investigation"
                "Interrogate another passenger":
                    jump investigation_choice
                "Quit for the day":
                    jump end_of_dayone


 



label end_of_dayone:

    #Navigating to the Cabin

    scene hallway

    "Navigating to the cabin"

    #Scene 52 - Susan Cabin 

    scene susansabin 

    #Narrator
    "After a long day of talking to everyone on board and finding clues about what happened to Richard Reed, Susan enters her room to go to sleep when suddenly…"

    #Scream sound
    "A scream will be heard here"

    #Navigating to the Hallway 
    
    "Going to the hallway"

    #Scene 53 - Hallway
    
    scene hallway

    #Narrator 
    "...she is jolted back into action and rushes toward the sounds of commotion. As Susan is runningin the direction of the scream, she sees a female member of the waitstaff coming out of the kitchen sobbing with her hands covering her eyes. As Susan enters the kitchen"

    #Scene 54 - Kitchen 

    #Narrator
    "she is met by Michael McQuaid and some wait staff members surrounding a new murder scene."

    #Susan Murphy 
    sm "McQuaid? What happened here?"

    #Narrator
    "Susan now sees what the commotion was all about."

    #Seeing the scne

    "Going to see the scene"

    #Scene 55 - Kitchen / SUsan Face 

    #Narrator
    "Lying there, dead, is William Windchime. Just as Susan sees the body, Ezekiel comes rushing in."

    #Ezekiel Jones
    ej "What happen- oh.."

    #Susan Murphy 
    sm  "*sighs Looks like the mystery continues."

    #Michael Mcquaid
    mm "Okay, the detectives are here. Let's let them do their work."

    #Susan Murphy 
    sm "Wait, where is the girl that found him here?"

    #Michael Mcquaid
    mm "I'll go out and look for her. We'll be close by."

    #Ezekiel Jones
    ej "Well, time to go to work. Again."

    #Narator
    "While looking at a crime scene, click on points of interest around the area to find clues."
    
    #Scene 56 - Murder Scene in kitchen
    
    show screen windchimescene_investigation 




label third:

    #Scene 57 - Post Murder in Kitchen

    scene murderscene_kitchen

    #Susan Murphy 
    sm "That seems to be all there is to find here."

    #Ezekiel Jones
    ej "And it looks like the day is over. Any point in holding interrogations right now?"

    #Susan Murphy 
    sm "I don't think so. We should retire for the night and pick back up tomorrow."

    #Narrator
    "The pair go to their rooms and sleep a restless night."

    
    #------------------------------------- END OF DAY 2 --------------------------------------------------------#


    #------------------------------------- START OF DAY 3 --------------------------------------------------------#

    scene day3

    "Day 3"

    #Scene 58 - Michael MCquiad 

    scene dininghall

    #Susan Murphy 
    sm "McQuaid."
    voice"scene58_N5_sm_1.mp3"

    #Michael Mcquaid
    mm "Murphy. How goes the investigation? Any luck finding who killed poor William?"
    voice "scene58_N2_mm_1.mp3"

    #Susan Murphy 
    sm "We've got a few leads that we're following."
    voice "scene58_N5_sm_2.mp3"

    #Michael Mcquaid
    mm "That sounds like stalling, detective. Are you sure you know what you're doing?"
    voice "scene58_N2_mm_2.mp3"

    #Susan Murphy Thoughts
    sm "Yeah, yeah. Rub it in, why don't you?"
    voice "scene58_N5_sm_3.mp3"

    #Michael Mcquaid
    mm "Or maybe you're misleading us. Maybe you know exactly who the killer is and are just trying to protect yourself."
    voice "scene58_N2_mm_3.mp3"

    #Ezekiel Jones
    ej "Don't be ridiculous, man! I was with Susan the whole time yesterday. She couldn't have murdered William."
    voice "scene58_N9_ej_1.mp3"

    #Michael Mcquaid
    mm "If you say so, faithful Watson. Now, do you have any questions for me?"
    voice "scene58_N2_mm_4.mp3"

    #Scene 59 - Michael McQuaid / Ezekiel Jones

    #Asking About Ezekiel Possible Choice

    "Asking about Ezekiel"
 
    #Susan Murphy 
    sm "Ezekiel, would you mind leaving for a moment?"
    voice "scene59_N5_sm_1.mp3"

    #Narrator
    "Ezekiel looks at you, mildly confused, but obeys."
    voice "scene59_N1_1.mp3"

    #Ezekiel Jones
    ej "Sure…"
    voice "scene59_N9_ej_1.mp3"

    #Susan Murphy 
    sm "Why is he here, McQuaid?"
    voice "scene59_N5_sm_3.mp3"

    #Michael Mcquaid
    mm "What?"
    voice "scene59_N2_mm_1.mp3"

    #Susan Murphy 
    sm "Why is Ezekiel here? Compared to all your other guests, he seems like a saint. What possible secrets could he have?"
    voice "scene59_N5_sm_3.mp3"

    #Narrator
    "Michael laughs in her face."
    voice "scene59_N1_2.mp3"

    #Michael Mcquaid
    mm "Oh, my dear detective, you think the good doctor is a saint? Oh, what a laugh. I won't tell but believe me when I say that man has more than enough secrets for blackmail."
    voice "scene59_N2_mm_2.mp3"

    mm "Now, do you have anything else I can do for you?"
    voice "scene59_N2_mm_3.mp3"

    #Scene 60 - Michael McQuaid / White Sisters

    #Asking About Ezekiel Possible Choice

    #Susan Murphy 
    sm "What can you tell me about the Whites?"
    voice "scene60_N5_sm_1.mp3"

    #Michael Mcquaid
    mm "Oh, not much. Wealthy socialites who started from the bottom now they're where they are."
    voice "scene60_N2_mm_1.mp3"

    #Susan Murphy 
    sm "Did they have any prior relationship with either of the deceased?"
    voice "scene60_N5_sm_2.mp3"

    #Michael Mcquaid
    mm "Certainly not with William, but they move in the same circles as Rachel. If you're asking if they had the motive or even means to murder either one."
    voice "scene60_N2_mm_2.mp3"

    mm "They may not be entirely honest, but they're certainly not murderers. At least, not ones that would beat a man to death or stab one."
    voice "scene60_N2_mm_3.mp3"

    #Susan Murphy 
    sm "What do you mean by that, McQuaid?"
    voice "scene60_N5_sm_3.mp3"

    #Michael Mcquaid
    mm "Let's just say that they didn't exactly come by all that money, honestly. Though I'm not sure, Patty has the wits to know where their money came from."
    voice "scene60_N2_mm_4.mp3"

    mm "Now, I'm sure you have more important things to do. Catch us a murderer, Ms. Holmes!"
    voice "scene60_N2_mm_5.mp3"

    #Narrator
    "Susan walks out of the dining and sees Deborah White."
    voice "scene60_N1_1.mp3"

    #Scene 61 - Deborah White 

    #Going to question deborah white possible choice

    "Going to question deborah white"

    #Susan Murphy 
    sm "Hey Deborah, can I ask you a couple of questions?"
    voice "scene61_N5_sm_1.mp3"

    #Deborah White
    dw "Sure. What would you like to know?"
    voice "scene61_N12_dw_1.mp3"

    #Susan Murphy 
    sm "Do you know where I can find Patty?"
    voice "scene61_N5_sm_2.mp3"

    #Scene 62 - Debeorah White / Where is patty 

    #asking where is patty possible choice

    "asking where is patty"

    #Susan Murphy 
    sm "It's unusual to see you without your sister. Where is she?"
    voice "scene62_N5_sm_1.mp3"

    #Deborah White
    dw "I don't know. I've been worried sick looking for her all morning."
    voice "scene62_N12_dw_1.mp3"

    #Susan Murphy 
    sm "Does she usually go off on her own?"
    voice "scene62_N5_sm_2.mp3"

    #Deborah White
    dw "When we are home, she usually does her own thing, but she always checks in with me." 
    voice "scene62_N12_dw_2.mp3"

    #Susan Murphy 
    sm "Hmm, and she didn't tell you anything this time?"
    voice "scene62_N5_sm_3.mp3"

    #Deborah White
    dw "Nothing, I woke up, and she was already gone. Maybe she got seasick again and went out for some air, but I would have found her by now. I hope she's okay."
    voice "scene62_N12_dw_3.mp3"

    #Susan Murphy 
    sm "Well, I'm walking around a lot today so if I find her, I will let you know."
    voice "scene62_N5_sm_4.mp3"

    #Deborah White
    dw "Thanks, Susan."
    voice "scene62_N12_dw_4.mp3"

    #Scene 63 - Debeorah White / Rachel Reaction

    #asking abour rachel reaction possible choice

    "asking abour rachel reaction"

    #Susan Murphy 
    sm "You girls went looking for Rachel on the first night, right? When you found her, how was she?"
    voice "scene63_N5_sm_1.mp3"

    #Deborah White
    dw "Yea, Patty and I went to look for her and found her on the deck. She was okay, just catching some air. Don't you remember? I told you this."
    voice "scene63_N12_dw_1.mp3"

    #Susan Murphy 
    sm "Yea, just needed a recap. When you found her and told her, how did she react?"
    voice "scene63_N5_sm_2.mp3"

    #Deborah White
    dw "About the same as anyone would react. She didn't believe me at first, but eventually, she broke down crying. Patty was doing her best to try and console her."
    voice "scene63_N12_dw_2.mp3"

    #Susan Murphy 
    sm "Oh really?"
    voice "scene63_N5_sm_3.mp3"

    #Deborah White
    dw "Yea, she seemed like she was out there a little while because she was shivering. After she accepted what we were telling her wasn't a lie, she turned pale—like all the blood left her face."
    voice "scene63_N12_dw_3.mp3"

    dw "After she broke down, she immediately rushed back to the dining hall. We went   along with her as well."
    voice "scene63_N12_dw_4.mp3"

    #Susan Murphy 
    sm "Hmm, okay. Thanks for sharing"
    voice "scene63_N5_sm_4.mp3"

    #Deborah White
    dw "Is that all you had to ask me?"
    voice "scene63_N12_dw_5.mp3"

    #Susan Murphy 
    sm "For now, yes. I'll keep looking around for Patty. Good luck."
    voice "scene63_N5_sm_5.mp3"

    #Deborah White
    dw "Thanks, Susan, you're such a God send!"
    voice "scene63_N12_dw_6.mp3"

    #Narrator
    "Susan goes to the bedrooms to go and check on Rachel."
    voice "scene_N1_1.mp3"

    #navigating to Rachel Cabin

    scene hallway

    "Navigating to Rachel Cabin"

    #Scene 64 - Rachel Reed 

    scene rachelcabin

    #Narator
    "A very sad looking Rachel opens the cabin door for Susan."
    voice "scene64_N1_1.mp3"

    #Susan Murphy 
    sm "Hey Rachel, just coming to check up on you. How are you?"
    voice "scene64_N5_sm_1.mp3"

    #Rachel Reed
    rar "I lost my husband. I'm miserable."

    #Susan Murphy 
    sm "Yea, no one can blame you for that. I just wanted to ask a couple of questions. Is that okay?"
    voice "scene64_N5_sm_2.mp3"

    #Narator
    "Rachel Shrugs"
    voice "scene64_N1_2.mp3"

    #Rachel Reed
    rar "I guess."
    voice "scene64_N11_rar_1.mp3"

    #Scene 65 - Rachel Reed / Diamond Cane

    #Asking about Diamond Cane Possible Choice

    "Asking about Cane"

    #Susan Murphy 
    sm "You were seen carrying a Diamond Cane. Where did you get it from?"
    voice "scene65_N5_sm_1.mp3"

    #Rachel Reed
    rar "From Richard. He bought it for me as an anniversary present. Sure, it cost a lot of money, but he bought it to apologize for being a little extra mean back then. Business wasn't good, but it got better."
    voice "scene65_N11_rar_1.mp3"

    #Rachel Reed
    rar "The gesture meant more to me than the stupid cane."
    voice "scene65_N11_rar_2.mp3"

    #Susan Murphy 
    sm "Did you misplace it at any time?"
    voice "scene65_N5_sm_2.mp3"

    #Rachel Reed
    rar "No. As soon as we boarded, we went to the room and changed for dinner. I left it there."
    voice "scene65_N11_rar_3.mp3"

    #Susan Murphy 
    sm "Oh, okay."
    voice "scene65_N5_sm_3.mp3"

    #Scene 66 - Rachel Reed / About Richard

    #Asking about Richard

    "Asking about Richard"

    #Susan Murphy 
    sm "Is it okay if I ask about Richard?"
    voice "scene66_N5_sm_1.mp3"

    #Rachel Reed
    rar "*Nods* Hmm-hmm."
    voice "scene66_N11_rar_1.mp3"

    #Susan Murphy 
    sm "How long have you known each other?"
    voice "scene66_N5_sm_2.mp3"

    #Rachel Reed
    rar "Since primary school. He's truly the same person, just a bit more refined now… or was anyway..."
    voice "scene66_N11_rar_2.mp3"

    #Susan Murphy 
    sm "Does he have a lot of enemies?"
    voice "scene66_N5_sm_3.mp3"

    #Rachel Reed
    rar "Yes, unfortunately. For better or worse, he acted very loudly and was a very proud man. Which made him an acquired taste."
    voice "scene66_N11_rar_3.mp3"

    #Susan Murphy 
    sm "I'm guessing more people didn't like the taste as opposed to the few that did."
    voice "scene66_N5_sm_4.mp3"

    #Rachel Reed
    rar "That's why you're the detective."
    voice "scene66_N11_rar_4.mp3"

    rar "Are we done yet? I would like to go and lay back down again."
    voice "scene66_N11_rar_5.mp3"

    #Susan Murphy 
    sm "Sure, that's all I wanted to ask."
    voice "scene66_N5_sm_5.mp3"

    #Rachel Reed
    rar "Bye.."
    voice "scene66_N11_rar_6.mp3"

    #Narrator
    "Rachel closes the door on Susan."
    voice "scene66_N1_1.mp3"

    "Susan heads up on deck for a breath of fresh air."
    voice "scene66_N1_2.mp3"

    #navgating to the desk

    scene hallway

    "Navigating to the Deck"

    #The Deck

    scene deck

    #Scene 67 - Ezekiel Jones

    #Narrator
    "Susan spotted Ezekiel the moment she walks out on the deck."
    voice "scene67_N1_1.mp3"

    #Susan Murphy 
    sm "Good afternoon Mr. Jones."
    voice "scene67_N5_sm_1.mp3"

    #Ezekiel Jones
    ej "Good afternoon Ms. Murphy."
    voice "scene67_N9_ej_1.mp3"

    #Susan Murphy 
    sm "I need to ask you a few questions."
    voice "scene67_N5_sm_2.mp3"

    #Ezekiel Jones
    ej "Okay... What do you need to know?"
    voice "scene67_N9_ej_2.mp3"

    #Scene 68 - Ezekiel Jones / Whereabouts

    #Asking About Whereabouts Possible Choice

    "Asking About Whereabout"

    #Narrator
    "Susan asks Ezekiel about his whereabouts during the time of the murder."

    #Ezekiel Jones
    ej "This is an unusual question. I was with you for most of the day. Remember I was helping you."
    voice "scene68_N9_ej_1.mp3"

    #Susan Murphy thoughts
    sm "That is correct. However, there were a few times when we might have separated."
    voice "scene68_N3_smt_1.mp3"

    #Susan Murphy 
    sm "There were a few times we separated. Where did you go during those times?"
    voice "scene68_N5_sm_1.mp3"

    #Ezekiel Jones
    ej "I just separated to use the bathroom, go to bed, or help give you information if it involved us finding the murderer."
    voice "scene68_N9_ej_2.mp3"

    #Scene 69 - Ezekiel Jones / whereabouts
    
    #Pressing Further Possible Choice

    "Pressing Further"

    #Susan Murphy 
    sm "Yes. However, there was one time when we separated. It is suspicious how it was only a few minutes, but it could have been enough time to find information before you kill someone."
    voice "scene69_N5_sm_1.mp3"

    #Ezekiel Jones
    ej "We have gone over this before. I am not the killer. You can ask a few people on the boat to prove it to you."
    voice "scene69_N9_ej_1.mp3"

    ej "I have been talking to them to gather information. I have nothing to hide."
    voice "scene69_N9_ej_2.mp3"

    #Susan Murphy 
    sm "I understand. Apologies for questioning your trust."
    voice "scene69_N5_sm_2.mp3"

    #Narrator
    "Ezekiel calms himself down."
    voice "scene69_N1_1.mp3"

    #Ezekiel Jones
    ej "Think nothing of it. If at any point you suspect me, I shall answer any questions truthfully."
    voice "scene69_N9_ej_3.mp3"

    #Scene 70 - Ezekiel Jones / Motive

    #Probe for motive possible choice

    "Probe for motive"

    #Susan Murphy 
    sm "Did you notice any changes in behaviour from William?"
    voice "scene70_N5_sm_1.mp3"

    #Ezekiel Jones
    ej "I have not noticed much from him. He seemed normal."
    voice "scene70_N9_ej_1.mp3"

    #Susan Murphy 
    sm "In the brief moments when we separated, had you spotted him?"
    voice "scene70_N5_sm_2.mp3"

    #Ezekiel Jones
    ej "Yes, I had."
    voice "scene70_N9_ej_2.mp3"

    #Scene 71 - Ezekiel Jones / Motive

    #Pressing further possible choice

    "Pressing Further"

    #Susan Murphy 
    sm "It seems suspicious that you did meet him, and in those brief moments when we weren't together, he turns up dead the next day."
    voice "scene71_N5_sm_1.mp3"

    #Ezekiel Jones
    ej "It is suspicious. I can confirm that I have an alibi and some important information."
    voice "scene71_N9_ej_1.mp3"

    #Susan Murphy 
    sm "Oh, and what might that be?"
    voice "scene71_N5_sm_2.mp3"

    #Ezekiel Jones
    ej "I can confirm that I was not the last person to see him that day. It was, in fact, (player to insert name here). I have not seen him since"
    voice "scene71_N9_ej_2.mp3"

    #Susan Murphy Thoughts
    sm "That is some important information."
    voice "scene71_N3_smt_1.mp3"

    #Susan Murphy
    sm "Thank you."
    voice "scene71_N5_sm_3.mp3"

    #Ezekiel Jones
    ej "You're Welcome."
    voice "scene71_N9_ej_3.mp3"

    #Scene 72 - Ezekiel Jones / Motive

    #Calm him down possible choice

    "Calming him down"

    #Susan Murphy
    sm " It is not my intention to anger you. I just need to know what you have against him."
    voice "scene72_N5_sm_1.mp3"

    #Ezekiel Jones
    ej "Why I have nothing against him. While I have seen him recently, I have no reason or motive to go against him."
    voice "scene72_N9_ej_1.mp3"

    #Susan Murphy
    sm "Were you the last to see him?"
    voice "scene72_N5_sm_2.mp3"

    #Ezekiel Jones
    ej "I can confirm that I was not the last person to see him that day. It was, in fact, (the player asked to insert name here). I have not seen him since."
    voice "scene72_N9_ej_2.mp3"

    #Susan Murphy Thoughts
    sm "That is an important piece of information."
    voice "scene72_N5_sm_3.mp3"

    #Susan Murphy
    sm "Thank you, Ezekiel."
    voice "scene72_N5_sm_4.mp3"

    #Ezekiel Jones
    ej "My pleasure."
    voice "scene72_N9_ej_3.mp3"

    #Narrator
    "Susan turns and catches David Dalton’s eye."
    voice "scene72_N1_1.mp3"

    #Scene 73 - David Dalton

    #Go to speak david possible option

    "Going to talk to David"

    #David Dalton
    dd "More questions, Ms. detective? Haven't I proven my innocence to you?"
    voice "scene73_N4_dd_1.mp3"

    #Ezekiel Jones
    ej "Well, William didn't make the footprints that lead away from his own body."
    voice "scene73_N9_ej_1.mp3"

    #Susan Murphy
    sm "We're just covering our bases, Dalton. We have two dead bodies on this boat, and the odds of there being two separate murderers are laughable."
    voice "scene73_N5_sm_1.mp3"

    #Susan Murphy
    sm "Now, we do have a couple more questions."
    voice "scene73_N5_sm_2.mp3"

    menu dalton_pathIvestigation:
        "Choose Path of Investigation"

        #Scene 74 - David Dalton / Whereabouts 

        "Ask About Whereabouts":
            
            #Susan Murphy
            sm "Where were you around the time of William's murder?"
            voice "scene74_N5_sm_1.mp3"

            #David Dalton
            dd "I was here, taking a smoke break. And before you ask, Mr. McQuaid can confirm it. I asked him for permission."
            voice "scene74_N4_dd_1.mp3"

            #Susan Murphy
            sm "Is McQuaid the only one who can verify that?"
            voice "scene74_N5_sm_2.mp3"

            #David Dalton
            dd "I beg your pardon?"
            voice "scene74_N4_dd_2.mp3"

            #Susan Murphy
            sm "Well, it's awfully convenient that the one person on the boat you have a prior relationship with, someone who speaks of you very highly, is the person you point to as your witness."
            voice "scene74_N5_sm_3.mp3"

            sm "Convenient enough that it beggars' belief, some might say."
            voice "scene74_N5_sm_4.mp3"

            #Ezekiel Jones
            ej "What she's trying to say is that it's suspicious that your boss is the only one who saw you."
            voice "scene74_N9_ej_1.mp3"

            #Susan Murphy
            sm "I think he got the point." 
            voice "scene74_N5_sm_5.mp3"

            #David Dalton
            dd "I can't help if people aren't out and about with a murderer on the boat! In any case, ask around. Someone else probably saw me up here."
            voice "scene74_N4_dd_3.mp3"

            dd "It's not like I was exactly hiding."
            voice "scene74_N4_dd_4.mp3"

            menu daltonchoice_whereabouts:
                "Choose your path of investigation"

                #Scene 75 - David Dalton - whereabouts - Press further
                "Press Further":
                    
                    #Susan Murphy
                    sm "Especially coupled with yesterday's 20-minute window…"
                    voice "scene75_N5_sm_1.mp3"
                    #Narrator
                    "Annoyance at being questioned quickly turns to a wave of quiet anger on Dalton's face."

                    #David Dalton
                    dd "Are you accusing me of murder, detective?"
                    voice "scene75_N4_dd_1.mp3"

                    #Susan Murphy
                    sm "No, no! I'm just trying to eliminate possibilities!"
                    voice "scene75_N5_sm_2.mp3"

                    #David Dalton
                    dd "Are you sure you're a real detective? It sure seems you're trying to pin it on the butler…"
                    voice "scene75_N4_dd_2.mp3"

                    #Susan Murphy Thoughts
                    sm "Wait, could he…? No, that's impossible. Would McQuaid have told him?"
                    voice "scene75_N3_smt_1.mp3"

                    #Susan Murphy
                    sm "I assure you that's not the case. I simply want to be sure that I catch the right person."
                    voice "scene75_N5_sm_3.mp3"

                    #Narrator
                    "Dalton gives Susan a dark look."
                    voice "scene75_N1_1.mp3"

                    #David Dalton
                    dd "Sure, whatever you say, look, my break is about ove-"
                    voice "scene75_N4_dd_3.mp3"

                    #Narrator
                    "A scream echoes from the depths of the ship. You turn to Ezekiel, nod, and run toward it."
                    voice "scene75_N1_2.mp3"

                    #----------------- End of Convo

                    #Narrator 
                    "Susan and Ezekiel rocket down the hallway… "
                    voice "scene75_N1_3.mp3"

                    jump fourth

                "probe motive":
                    #Jump to the Scene 76 - David Dalton / Motive 
                    jump probemotive
                

        #Scene 76 - David Dalton / Motive 

        "Probe for motive":
            
            #Jump to the scene
            jump probemotive

            


label probemotive:
    #Susan Murphy
            sm "Before he died, did you notice any changes in behaviour from William?"
            voice "scene76_N5_sm_1.mp3"

            #David Dalton
            dd "What do you mean, Ms. Murphy?"
            voice "scene76_N4_dd_1.mp3"

            #Susan Murphy
            sm "Anything. Did he seem more blue than usual, or perhaps aggressive? Maybe you had some odd conversation with him. Anything, really."
            voice "scene76_N5_sm_2.mp3"

            #David Dalton
            dd "Well… he was asking about our lockers last night. He seemed really bothered about the idea of someone getting into his."
            voice "scene76_N4_dd_2.mp3"

            dd "Do we have to worry about a thief, as well as a murderer, on this boat?"
            voice "scene76_N4_dd_3.mp3"

            #Susan Murphy
            sm "Hopefully not. We've got enough to deal with."
            voice "scene76_N5_sm_3.mp3"

            #Choice during motive

            menu dalton_motive_choice:
                "Proceed with"

                #Scene 77 - David Dalton / Motive - Confortation

                "Asking About confrontation":
                    
                    #Susan Murphy
                    sm "This conversation, did he… accuse you of anything?"
                    voice "scene77_N5_sm_1.mp3"

                    #Narrator
                    "Dalton's eyes flick between you and Ezekiel, filled with suspicion."
                    voice "scene77_N1_1.mp3"

                    #David Dalton
                    dd "No, he didn't. Did he say something to you? I mean. I wouldn't steal from the kid. If that's what you're asking."
                    voice "scene77_N4_dd_1.mp3"

                    dd "Why? Did he say something?"
                    voice "scene77_N4_dd_2.mp3"

                    #Susan Murphy
                    sm "No, it's just-"
                    voice "scene77_N5_sm_2.mp3"

                    #Narrator
                    "A scream echoes from the depths of the ship. You turn to Ezekiel, nod, and run toward it."
                    voice "scene77_N1_2.mp3"

                    #----------- End of convo

                    "A scream will be heard" 

                    #Narrator
                    "Susan and Ezekiel rocket down the hallway… "
                    voice "scene77_N1_3.mp3"

                    jump fourth

                #Scene 78 - David Dalton / Motive - Confortation

                "Press for details":
                    
                    #Susan Murphy
                    sm "Did William mention being suspicious of anyone in particular during this conversation?"
                    voice "scene78_N5_sm_1.mp3"

                    #David Dalton
                    dd "Not as such, but he did seem concerned about the lock he was using. Apparently, the boss gave it to him when he asked about the security of the lockers."
                    voice "scene78_N4_dd_1.mp3"

                    #Ezekiel Jones
                    ej "What do you mean \"concerned\" ?"
                    voice "scene78_N9_ej_1.mp3"

                    #David Dalton
                    dd "I don't really know. He seemed to think that Mr. McQuaid might have a copy of the key, but what he'd want in William's locker…"
                    voice "scene78_N4_dd_2.mp3"

                    dd "Wait, weren't the two of you asking about shoes yesterday? Something about a shoeprint? Was William the murderer?"
                    voice "scene78_N4_dd_3.mp3"

                    #Ezekiel Jones
                    ej "Unlikely, since he's kicked the bucket."
                    voice "scene78_N9_ej_2.mp3"

                    #David Dalton
                    dd "Maybe there was only one murder he wanted to commit. Couldn\'t he have?"
                    voice "scene78_N4_dd_4.mp3"

                    #Narrator
                    "You interrupt Dalton."
                    voice "scene78_N1_1.mp3"

                    #Susan Murphy
                    sm "He wasn't the killer, Dalton. There's too much evidence that conflicts with that."
                    voice "scene78_N5_sm_2.mp3"

                    #David Dalton
                    dd "Alright, but maybe it was Mr. McQuaid? After all, he gave William the lock and invited you all here to blackmail you."
                    voice "scene78_N4_dd_5.mp3"

                    #Ezekiel Jones
                    ej "That's unlikely. He was with everyone else at the time of the first murder."
                    voice "scene78_N9_ej_3.mp3"

                    #Susan Murphy
                    sm "As Ezekiel says, it's unlikely that-"
                    voice "scene78_N5_sm_3.mp3"

                    #Narrator
                    "A scream echoes from the depths of the ship. You turn to Ezekiel, nod, and run toward it."
                    voice "scene78_N1_2.mp3"

                    #----------------- End of Convo

                    #Narrator 
                    "Susan and Ezekiel rocket down the hallway… "
                    voice "scene78_N1_3.mp3"

                    jump fourth

label fourth:

    #Scene 79 - The scream

    #Narrator 
    "…letting themselves into the Neptune's finely appointed washroom, they find the hunched form of Deborah White, crying over the newly deceased Patricia White."
    voice "scene79_N1_1.mp3"

    #Ezekiel Jones
    ej "Oh, Patty…"
    voice "scene79_N9_ej_1.mp3"

    #Susan Murphy
    sm "Deborah, what happened here?"
    voice "scene79_N5_sm_1.mp3"

    #Deborah White
    dw "I couldn't find Patty anywhere, and I looked around the boat all day for her."
    voice "scene79_N12_dw_1.mp3"

    #Narrator
    "Deborah's words start to slur together as her panic lends speed to her mouth. By the time she becomes intelligible again, all she says is:"
    voice "scene79_N1_2.mp3"

    #Deborah White
    dw "And now she's dead!"
    voice "scene79_N12_dw_2.mp3"

    #Susan Murphy
    sm "It'll be alright, Deborah. I'll catch the one who did this. Ezekiel, could you…"
    voice "scene79_N5_sm_2.mp3"

    #Ezekiel Jones
    ej "Of course. Debbie, please, come with me."
    voice "scene79_N9_ej_2.mp3"

    #Narrator
    "Ezekiel leads the weeping White sister out of the bathroom, leaving Susan alone with a finely dressed corpse."
    voice "scene79_N1_3.mp3"

    #Susan Murphy Thoughts
    sm "Well, time to get to work."
    voice "scene79_N5_sm_3.mp3"

    #Entering the 3rd Crime Scene

    #Scene 80 - 3rd Murder in the bathroom 

    show screen patricia_murderscene

    #Scene 81 - Murder Scene 

    #Susan Murphy 
    sm "Not much to go by. I need some rest, and we can reconvene tomorrow morning."
    voice "scene81_N5_sm_1.mp3"

    #------------------------- End of day 3

    #------------------------- Start of day 4

    scene day 4

    "Day 4"

    #Scene 82 - Susan's Cabin

    #Narrator
    "Susan awakes in her room, feeling blissfully well rested for a moment, before remembering the situation she's in."
    voice "scene82_N1_1.mp3"

    #Susan Murphy Thoughts
    sm "God, we need to catch this maniac. There aren't that many of us left."
    voice "scene82_N3_smt_1.mp3"

    sm "Okay, think, what do I know? The killer finds Richard in his suite and beats him, to death, with his wife's cane, apparently wearing William's shoes."
    voice "scene82_N3_smt_2.mp3"

    #Susan Murphy
    sm "So they're smart enough to cover his tracks, to confuse whoever investigates. Clearly, whoever did it wanted us to think it was one of those two."
    voice "scene82_N5_sm_1.mp3"

    sm "Then the next day, William is murdered after we ask about his shoes and cause him to panic. Maybe he asked around and stumbled upon the real killer."
    voice "scene82_N5_sm_2.mp3"

    sm "So he ends up dead… in the kitchen. Who else would have been in the kitchen with William?"
    voice "scene82_N5_sm_3.mp3"

    sm "And the next day, poor Patty ends up dead in the bathroom, strangled by a left-handed man."
    voice "scene82_N5_sm_4.mp3"

    sm "Left-handed man… in the kitchen."
    voice "scene82_N5_sm_5.mp3"

    sm "That's it I have figured out! I know who it is!"
    voice "scene82_N5_sm_6.mp3"

    sm "I need to call everyone to the dining hall!"
    voice "scene82_N5_sm_7.mp3"

    #To the Dining Hall

    scene hallway

    "Navigating to the dining hall"

    #Scene 83- The Dining Hall

    #Narrator
    "After calling everyone to the dining hall Susan starts explaining why everyone is in the room."
    voice "scene83_N1_1.mp3"

    #Susan Murphy
    sm "I have figured out who the Murderer is."
    voice "scene83_N5_sm_1.mp3"

    #Narrator 
    "The entire dining hall became silent soon with whispers and murmurs filling the area."
    voice "scene83_N1_2.mp3"

    #Susan Murphy
    sm "But first, McQuaid, I have a question."
    voice "scene83_N5_sm_2.mp3"

    #Michael McQuaid
    mm "What, another? Surely you have everything you need, Ms. Murphy if you know who the killer is."
    voice "scene83_N2_mm_1.mp3"

    #Susan Murphy
    sm "Indulge me. You brought us here. You owe us that much."
    voice "scene83_N5_sm_3.mp3"

    #Michael McQuaid
    mm "Fine, ask your question."
    voice "scene83_N2_mm_2.mp3"

    #Susan Murphy
    sm "Why?"
    voice "scene83_N5_sm_4.mp3"

    #Michael McQuaid
    mm "Excuse me, detective?"
    voice "scene83_N2_mm_3.mp3"

    #Susan Murphy
    sm "Why invite us here at all? Other than blackmail, I mean. You could have asked us to your home or just sent letters, for God's sake!"
    voice "scene83_N5_sm_5.mp3"

    sm "So why invite us here? Hell, I'm just a detective. Why invite me?"
    voice "scene83_N5_sm_6.mp3"

    #Michael McQuaid
    mm "You want to know why Murphy? The great detective can't figure it out? Fine. I'll tell you why."
    voice "scene83_N2_mm_4.mp3"

    mm "Each of you is here for a different reason. I invited Richard and Rachel simply because that Reed Industries is a direct competitor, and I want it gone."
    voice "scene83_N2_mm_5.mp3"

    mm "The Whites, on the other hand, are a little bit more complicated. They're rich, yes, but they're also well-connected. Deborah knows people, knows how to get what she wants."
    voice "scene83_N2_mm_6.mp3"

    mm "And Patty, well, she had her own connections of a more intimate nature."
    voice "scene83_N2_mm_7.mp3"

    mm  "The good doctor? He's performed certain procedures at my behest that I wouldn't want to be known to the public."
    voice "scene83_N2_mm_8.mp3"

    mm "And then there's you. Tell me, lady Holmes, how did you first meet me?"
    voice "scene83_N2_mm_9.mp3"

    #Susan Murphy
    sm "You hired me. You hired me to find a corporate spy who had stolen some important documents."
    voice "scene83_N5_sm_7.mp3"

    #Michael McQuaid
    mm "I-"
    voice "scene83_N2_mm_10.mp3"

    #Narrator
    "McQuaid gives Susan a long, hard look. After a moment, he rests his head in his hands."
    voice "scene83_N1_3.mp3"

    #Michael McQuaid
    mm "You don't know?"
    voice "scene83_N2_mm_11.mp3"

    #Susan Murphy
    sm "What don't I know, McQuaid?"
    voice "scene83_N5_sm_8.mp3"

    #Michael McQuaid
    mm "And here I thought you were one of the great detectives. He wasn't a corporate spy!"
    voice "scene83_N2_mm_12.mp3"

    mm "He was a federal agent. And those documents? Some damning evidence. I thought you knew! I thought that you'd take me down any day now!"
    voice "scene83_N2_mm_13.mp3"

    mm "That's why I invited you along, detective. I thought you were actually good at your job. But, unfortunately, it seems I was mistaken."
    voice "scene83_N2_mm_14.mp3"

    mm "And I went through all the trouble of finding blackmail for you too. Now tell us, little miss detective, who's the killer?"
    voice "scene83_N2_mm_15.mp3"

    menu killer_choice:

        "Choose the killer"

        "David Dalton":
            
            #Scene 84 - David dalton Killer

            #Susan Murphy
            sm "David Dalton, of course. David Dalton, who was mysteriously absent for 20 minutes around thetime of Richard's murder."
            voice "scene84_N5_sm_1.mp3"

            sm "David Dalton, who would have been a normal sight in the kitchen for William. David Dalton, who served drinks with his left hand."
            voice "scene84_N5_sm_2.mp3"

            #Narrator
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            voice "scene84_N5_sm_1.mp3"

            #David Dalton 
            dd "Very clever, a regular Sherlock we have in our midsts. It's too bad that all of that deductive power will end up at the bottom of the ocean."
            voice "scene84_N4_dd_1.mp3"

            #Michael McQuaid
            mm "Dalton? What are you saying?"
            voice "scene84_N2_mm_1.mp3"

            #David Dalton 
            dd "I've put a bomb on the boat, 'boss.' If I can't have the satisfaction of killing you all with my bare hands, then this will have to do."
            voice "scene84_N4_dd_2.mp3"

            #Michael McQuaid
            mm "What? That wasn't the deal! You were supposed to get rid of them, not me!"
            voice "scene84_N2_mm_2.mp3"

            #David Dalton 
            dd "Did you really think you were exempt, McQuaid? You. All of you have made my life a living hell!"
            voice "scene84_N4_dd_3.mp3"

            #Ezekeil Jones
            ej "What the hell are you talking about? I've never even met you before!"
            voice "scene84_N9_ej_1.mp3"

            #David Dalton 
            dd "Oh sure, you haven't. Of course, you and your rich friends haven't been laughing behind my back while I suffered!"
            voice "scene84_N4_dd_4.mp3"

            dd "I was supposed to have the life that all of you have! I worked hard, and I earned it! Instead, you all just lied, cheated your way through, and then ensured that I couldn't follow!"
            voice "scene84_N4_dd_5.mp3"

            dd "I waited for this for years! And finally, finally, I have my chance! Did you really think I'd leave you alive, McQuaid? After everything you did to me?"
            voice "scene84_N4_dd_6.mp3"

            dd "And now it's ruined! Ruined by a fake detective!"
            voice "scene84_N4_dd_7.mp3"

            #Susan Murphy Thoughts
            sm "Damn."
            voice "scene84_N3_smt_1.mp3"

            #Narrator
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            voice "scene84_N5_sm_2.mp3"

            #David Dalton 
            dd "That's right, the woman you all trusted with your lives didn't earn her position! Just like all of you, she cheated her way to the top!"
            voice "scene84_N4_dd_8.mp3"

            jump finale

        "Michael Mcquiad":
            
            #Scene 85 - Michael Killer

            #Susan Murphy 
            sm "Why, it’s Michael McQuaid, of course!"
            voice "scene85_N5_sm_1.mp3"

            #Narrator
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            voice "scene85_N1_1.mp3"

            #David Dalton 
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            voice "scene85_N4_dd_1.mp3"

            #Susan Murphy Thoughts
            sm "Damn."
            voice "scene85_N3_smt_1.mp3"

            #Narrator
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            voice "scene85_N1_2.mp3"

            #David Dalton 
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            voice "scene85_N4_dd_2.mp3"

            #Michael McQuaid
            mm "Dalton? What's the meaning of this?"
            voice "scene85_N2_mm_1.mp3"

            #David Dalton 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            voice "scene85_N4_dd_3.mp3"

            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            voice "scene85_N4_dd_4.mp3"

            jump finale

        "Ezekiel Jones":
            
            #Scene 86 - Ezekiel Killer

            #Susan Murphy 
            sm "Why, it’s Ezekiel Jones, of course!"
            voice "scene86_N5_sm_1.mp3"

            #Narrator
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            voice "scene86_N1_1.mp3"

            #David Dalton 
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            voice "scene86_N4_dd_1.mp3"

            #Susan Murphy Thoughts
            sm "Damn."
            voice "scene86_N3_smt_1.mp3"

            #Narrator
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            voice "scene86_N1_2.mp3"

            #David Dalton 
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            voice "scene86_N4_dd_2.mp3"

            #Michael McQuaid
            mm "Dalton? What's the meaning of this?"
            voice "scene86_N2_mm_1.mp3"

            #David Dalton 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            voice "scene86_N4_dd_3.mp3"

            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            voice "scene86_N4_dd_4.mp3"

            jump finale

        "Deborah White":
            
            #Scene 87 - Deborah Killer
            
            #Susan Murphy 
            sm "Why, it’s Deborah White, of course!"
            voice "scene87_N5_sm_1.mp3"

            #Narrator
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            voice "scene_N1_1.mp3"

            #David Dalton 
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            voice "scene87_N4_dd_1.mp3"

            #Susan Murphy Thoughts
            sm "Damn."
            voice "scene87_N3_smt_1.mp3"

            #Narrator
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            voice "scene_N1_2.mp3"

            #David Dalton 
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            voice "scene87_N4_dd_2.mp3"

            #Michael McQuaid
            mm "Dalton? What's the meaning of this?"
            voice "scene87_N2_mm_1.mp3"

            #David Dalton 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            voice "scene87_N4_dd_3.mp3"

            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            voice "scene87_N4_dd_4.mp3"

            jump finale

        "Rachel Reed":
            
            #Scene 88 - Rachel Reed
            
            #Susan Murphy 
            sm "Why, it’s Rachel Reed, of course!"
            voice "scene88_N5_sm_1.mp3"

            #Narrator
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            voice "scene88_N1_1.mp3"

            #David Dalton 
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            voice "scene88_N4_dd_1.mp3"

            #Susan Murphy Thoughts
            sm "Damn."
            voice "scene88_N5_sm_2.mp3"

            #Narrator
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            voice "scene88_N1_2.mp3"

            #David Dalton 
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            voice "scene88_N4_dd_2.mp3"

            #Michael McQuaid
            mm "Dalton? What's the meaning of this?"
            voice "scene88_N2_mm_1.mp3"

            #David Dalton 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            voice "scene88_N4_dd_3.mp3"

            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            voice "scene88_N4_dd_4.mp3"

            jump finale


label finale:

    #Scene 89 - Killer cont

    scene dininghall

    #Susan Murphy 
    sm "And there's the question we've all been asking. The motive. Every person on this boat has been laughing at you, Dalton? The first time I met you was three days ago!"
    voice "scene89_N5_sm_1.mp3"

    #David Dalton 
    dd " Liar! You cheated your way to the top, just like them! And now, you'll all find yourselves at the bottom of the ocean!"
    voice "scene89_N4_dd_1.mp3"

    dd "Finally, I will have my revenge!"
    voice "scene89_N4_dd_2.mp3"

    #Narrator
    "With that, the intercom dies."
    voice "scene89_N1_1.mp3"

    #Susan Murphy 
    sm "Ezekiel, Deborah, Rachel, had any of you ever heard of Dalton before this trip?"
    voice "scene89_N5_sm_2.mp3"

    #Ezekiel Jones
    ej "He might have come to my practice once or twice, years ago, but I'm not sure."
    voice "scene89_N9_ej_1.mp3"

    #Deborah White
    dw "Never. I would have remembered him."
    voice "scene89_N12_dw_1.mp3"

    #Rachel Reed
    "Not as far as I can remember. Richard might have known him, though."
    voice "scene89_N11_rar_1.mp3"

    #Susan Murphy 
    sm "Alright, so he's crazy. If you wanted to sink a ship, where would you put a bomb?"
    voice "scene89_N5_sm_3.mp3"

    #Ezekiel Jones
    "Either the hold or the engine room. I doubt we have the time to visit both."
    voice "scene89_N9_ej_2.mp3"

    #Michael McQuaid
    mm "I, er, have an elegant solution to that one. The boat's hold and engine room are the same place. Just take the stairs at the end of the hall."
    voice "scene89_N2_mm_1.mp3"

    #Susan Murphy 
    sm "All right. Ezekiel, follow me."
    voice "scene89_N5_sm_4.mp3"

    #Scene 90 - The Bomb

    scene bomblocation

    #Narrator
    "Susan and Ezekiel sprint down the hall and practically fly down the stairs into the hold, where they discover a bomb strapped to the engine."
    voice "scene90_N1_1.mp3"

    #Susan Murphy 
    sm "There it is!"
    voice "scene90_N5_sm_1.mp3"

    #Narrator
    "Ezekiel examines the bomb closely, flinching as it ticks."
    voice "scene90_N1_1.mp3"

    #Scene 91 - The password

    scene holdingbomb

    #Ezekiel Jones
    ej "We must be able to defuse it. See those three lights? It looks like we have three choices."
    voice "scene91_N9_ej_1.mp3"

    #Susan Murphy 
    sm "Come on, think! What would Dalton make the password? How are we supposed to know this?"
    voice "scene91_N5_sm_1.mp3"

    #Ezekiel Jones
    ej "He must have given us a hint in that long winded speech of his."
    voice "scene91_N9_ej_2.mp3"

    #Susan Murphy 
    sm "The password must be his motive… hmm."

    menu defuse_bomb:

        "Choose Wisely"

        "Avenge":
           
            #Scene 92 - Explosion

            #Susan Murphy 
            sm "No, wait-"
            voice "scene92_N5_sm_1.mp3"

            #Narrator
            "An explosion rips through the Neptune, a roaring inferno over the water. Many on the boat are killed outright, while others…"
            voice "scene92_N1_1.mp3"

            #Narrator
            "Others are drowned, caught in Neptune's Net."
            voice "scene92_N1_2.mp3"

            #Narrator
            "With them died the knowledge of what happened on this five-day cruise and any evidence that the passengers were anything less than upstanding members of the community."
            voice "scene92_N1_3.mp3"

            scene game_over

            "Game over"

            return


        "Revenge":
            
            #Scene 93 - Accepted

            scene passwordaccepted

            #Susan Murphy 
            sm "That's it! Now, to find Dalton. Ezekiel, you stay here. Grab him if he comes back."
            voice "scene93_N5_sm_1.mp3"

            #Ezekiel Jones
            ej "Right."
            voice "scene93_N9_ej_1.mp3"

            #Scene 94 - The hallway 

            scene hallway 

            #Narrator
            "Susan dashes off, finding herself in the hallway."
            voice "scene94_N1_1.mp3"

            #Susan Murphy 
            sm "Where would he be? He was on the intercom earlier. What rooms would have a microphone for the intercom."
            voice "scene94_N5_sm_1.mp3"

            #Susan Murphy 
            sm "The helm. He must be at the helm."
            voice "scene94_N5_sm_2.mp3"

            #Scene 95 - the helm

            scene helm

            #Narrator 
            "Susan makes her way to the ship's helm, stepping cautiously inside."
            voice "scene95_N1_1.mp3"

            #David Dalton 
            dd "You're too late, Ms. Holmes. The boat will explode, taking us to the bottom, where you all belong!"
            voice "scene95_N4_dd_1.mp3"

            #Susan Murphy 
            sm "I'm afraid that's incorrect, Dalton. We've already defused the bomb. Come quietly, and this can all be over."
            voice "scene95_N5_sm_1.mp3"

            #David Dalton 
            dd "Why should I? You all laughed at me! Even if I'm not sent to the chair, you all will make sure that I never get another job!"
            voice "scene95_N4_dd_2.mp3"

            dd "You've all conspired against me. Why should I trust your word now?"
            voice "scene95_N4_dd_3.mp3"

            #Susan Murphy 
            sm "There was never a conspiracy, Dalton. McQuaid's used you, pinned your failure on us."
            voice "scene95_N5_sm_2.mp3"

            #David Dalton 
            dd "No! You're lying! Just like you lied about being a detective, I can't trust anything you say! If my bomb doesn't do it, I'll kill you myself. "
            voice "scene95_N4_dd_4.mp3"

            #Narrator
            "Dalton lunges for Susan, but before he can act, Susan has her gun drawn and aimed."
            voice "scene95_N1_1.mp3"

            #Susan Murphy 
            sm "Is this worth your life, Dalton? Now come quietly. Please, I don't want to hurt you. Just come with me."
            voice "scene95_N5_sm_3.mp3"

            #Narrator 
            "Dalton hesitates for a moment."
            voice "scene95_N1_2.mp3"

            #David Dalton 
            dd "You know if you arrest me, I will reveal all your dirty little secrets. Even if I can't kill you, I'll ruin you."
            voice "scene95_N4_dd_5.mp3"

            #Susan Murphy 
            sm "As attempts to make me drop my guard, that one's weak. Now come with me."
            voice "scene95_N5_sm_4.mp3"

            #Narrator 
            "Susan escorts her captive to the dining hall."
            voice "scene95_N1_3.mp3"

            #Scene 96 - Ending | Dining Hall

            scene dininghall

            #Susan Murphy 
            sm "And here we have him, ladies and gentlemen. Our killer. One of you, go get Ezekiel from the hold."
            voice "scene96_N5_sm_1.mp3"

            #Narrator
            "Deborah nods and leaves to get Ezekiel."
            voice "scene96_N1_1.mp3"

            #Michael McQuaid
            mm "You little traitor! After everything I've done for you, you start killing my guests! Why I should-"
            voice "scene96_N2_mm_1.mp3"

            #Susan Murphy 
            sm "Hold it right there, McQuaid. I seem to remember you mentioning a deal with Dalton here. What might the terms of that deal be?"
            voice "scene96_N5_sm_2.mp3"

            #Narrator 
            "Michael becomes pale."
            voice "scene96_N1_2.mp3"

            #David Dalton 
            dd "I can tell you exactly what that deal was. Blackmail wasn't enough for you, eh McQuaid? No, you wanted them gone."
            voice "scene96_N4_dd_1.mp3"

            dd "So he found me with my vendetta, a perfect patsy! The deal, Murphy, was for me to kill you, and then he would protect me from the authorities."
            voice "scene96_N4_dd_2.mp3"

            dd "Brave enough to order a death, but not enough to do it himself."
            voice "scene96_N4_dd_3.mp3"

            #Narrator
            "Ezekiel walks in with Deborah."
            voice "scene96_N1_3.mp3"

            #Ezekiel Jones
            ej "Ah, I see you've found him. What shall we do with him?"
            voice "scene96_N9_ej_1.mp3"

            #Susan Murphy 
            sm "Is there anywhere on the ship that can be locked from the outside?"
            voice "scene96_N5_sm_3.mp3"

            #Ezekiel Jones
            ej "There were a couple of doors leading out from the hold that seemed to have locks."
            voice "scene96_N9_ej_2.mp3"

            #Susan Murphy 
            sm "Those'll do. Put him in one and our illustrious host in the other. Then when we get back to Honolulu, we can hand them over to the authorities."
            voice "scene96_N5_sm_4.mp3"

            #Ezekiel Jones
            ej "Alright. I'll keep an eye on them, just in case."
            voice "scene96_N9_ej_3.mp3"

            #Scene 97 - THE END

            scene theend

            #Narrator
            "The two culprits were put in their makeshift cells while a course was charted back to the harbour. After a nerve-wracking day, they finally returned."
            voice "scene97_N1_1.mp3"

            "Michael McQuaid and David Dalton were handed over to the authorities. Before the trial, secrets were spilled, and lives ruined."
            voice "scene97_N1_2.mp3"

            "They may have escaped Neptune's Net, but the lives of those on board would never be the same again."
            voice "scene97_N1_3.mp3"

            return 


        "Change":

            #Scene 92 - Explosion

            #Susan Murphy 
            sm "No, wait-"
            voice "scene92_N5_sm_1.mp3"

            #Narrator
            "An explosion rips through the Neptune, a roaring inferno over the water. Many on the boat are killed outright, while others…"
            voice "scene92_N1_1.mp3"

            #Narrator
            "Others are drowned, caught in Neptune's Net."
            voice "scene92_N1_2.mp3"

            #Narrator
            "With them died the knowledge of what happened on this five-day cruise and any evidence that the passengers were anything less than upstanding members of the community."
            voice "scene92_N1_3.mp3"

            scene game_over

            "Game over"

            return
        









    return