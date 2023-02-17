# The Neptune script
init python:
    persistent.investigation_choices_viewed = []
#Characters are:
# Susan Murphy, Dr. Ezekial Jones, Richard Reed, Rachel Reed, Deborah White, Patricia White, Michael McQuaid, William Windchime, David Dalton, Lloyd Lewis.

#Characters will have initials as variable i.e Susan Murphy = sm but rar for the wife of reed

define sm = Character("Susan Murphy")
define smt = Character("Susan Murphy (Thoughts)")
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
    voice "audio/Character voices/Character voices/Narrator-1-Scene-2-2.mp3"
    "Among the pile is an ornate envelope, with an equally ornate invitation inside."

    # Scene 3 - Envelope 

    #Scene Bg - an image of the envelope and invitation with text on them
    scene envelope #inside The invitation 

    #voice of mcquaid
    #do we need this as text or would a graphic be enough?
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 3.mp3"
    "Dear Susan Murphy, you have been cordially invited as a distinguished guest to ring in 1952 in style aboard the USS Neptune. We will be departing at 6:00 P.M. December 30th from Honolulu Harbour, and returning to the same location on January 3rd. I hope to see you there! - Michael McQuaid"

    # Susan thought  
    show susan
    voice "audio/Character Voices/Character Voices/Narrator 3 - scene 3.mp3"
    smt "McQuaid, McQuaid, where have I heard that name before? Oh right, I did a case for him. Well, I could use a vacation after today…Sure, why the heck not!"

    # Scene 4 - Yatch

    #Scene Bg - an image of the yacht on the water
    scene yatchonwater

    #Narrator 
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 4.mp3"
    "A couple of weeks later, Susan readies to board the Neptune, admiring the lavish yacht."

    # Scene 5 - Susan Cabin

    #scene bg - Inside Susan Cabin
    scene susancabin

    #Narrator 
    show susan
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 5-1.mp3"
    "As Susan sorts through her luggage, there is a knock at the door."
    show susan at left

    #dalton 
    show david at right
    voice "audio/Character Voices/Character Voices/Narrator 4 - Scene 5-2.mp3"
    dd "There will be a dinner for all the guests in the dining hall in 30 minutes."

    #Susan Murphy
    voice "audio/Character Voices/Character Voices/Narrator 5 - scene 5-3.mp3"
    sm "Alright, thank you."
    hide david
    hide susan 
    
    #play sound susan cabin thought
    show susan
    voice "audio/Character Voices/Character Voices/Narrator 3 - scene 5.mp3"
    smt " Okay, time for me to get dolled up for dinner. I hope the food is going to be good."
    hide susan


    #Scene Bg - Navigation Option screen


    #Scene 6 - Navigation 

    scene hallway
    #Footsteps here?  
    "Walking your way to the dining hall"
    #Navigation here

    #Scene 7 - Dining Hall

    scene diningroom

    #Narrator 
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 6.mp3"
    "Susan enters the dining room and sees a well-dressed crowd sitting around the room at different tables."
    
    #play sound/music with fade in here not voice
    #Michael speaking as the player enters the room
    show michael
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 6.mp3"
    mm "Ah, and here comes our final guest of the evening! Welcome, Susan. Please, take a seat. Now that we’re all here, the party can start!"

    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-3-1.mp3"
    mm "I know some of you are already acquainted with each other, but to help break the ice, why don’t we have a few introductions?"
    hide michael
    #Presenting the characters introducing them to the player ( IDEA: Unique BG, sounds etc)
    show richard at left
    show rachel at right
    voice "audio/Character Voices/Character Voices/Narrator 2 - Scene 7-3.mp3"
    mm "First, we have Mr. Richard Reed, the CEO of Reed Industries, and his wife, Mrs. Rachel Reed."
    hide richard
    hide rachel
    show zeke
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-4.mp3"
    mm "Next, we have the illustrious Dr. Ezekiel Jones. The man’s service to our country and his patients' lives speaks for itself."
    hide zeke
    show deborah at right
    show patricia at left 
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-5.mp3"
    mm "Then, We have the White sisters, Deborah and Patricia. True yin and yang if I’ve ever seen one."
    hide deborah
    hide patricia
    show susan
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-6.mp3"
    mm "Of course, the brilliant Susan Murphy, one of the great detectives of our time."
    hide susan

    #Michael McQuaid
    show michael 
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-8.mp3"
    #Utensil coming in sound?
    mm "Ah, and here’s dinner now!"
    hide michael
    
    #Susan Thoughts 
    show susan
    voice "audio/Character Voices/Character Voices/Narrator 3 - scene 7-2.mp3"
    smt "Well, seems like McQuaid is in high spirits tonight. But why invite me? I stand out among these high-society types like a pebble among rhinestones. Hmm."
    hide susan
    

    #Narrator
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7-3.mp3"
    "Just then, Susan hears a commotion from another table."

    #Richard Reed
    show richard at right
    voice "audio/Character Voices/Character Voices/Narrator 7 - scene 7.mp3"
    rr"How dare you! Don’t you know who I am, boy?"

    #William Windchime
    show will at left
    voice "audio/Character Voices/Character Voices/Narrator 8 - scene 7.mp3"
    ww "I-I’m so sorry, mister Reed, sir, I didn’t mean t-"

    #The Scene Here would still be in the room

    #Narrator  
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7-4.mp3" 
    "She turns to see one of the guests, Richard Reed covered in drink and screaming at the waitstaff."

    #Richard Reed 
    show richard
    voice "audio/Character Voices/Character Voices/Narrator 7 - scene 7-2.mp3"
    rr"I don’t care! Can’t you see how expensive this suit is! It’s worth more than your life, at the very least"

    #Richard Reed 
    voice "audio/Character Voices/Character Voices/Narrator 7 - scene 7-3.mp3"
    rr "Michael, see to it that your server is disciplined! I’m going to get changed out of this mess!"

    hide richard
    hide will
    
    #Narator 
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7-5.mp3"
    "Richard leaves, muttering about having to replace a perfectly good suit."

    #Susan Murphy Thoughts
    show susan
    voice "audio/Character Voices/Character Voices/Narrator 3 - scene 7-3.mp3"
    smt "Well, Richard seems to be a very happy camper. I wonder if he’s always like this… Does the same go for his wife?"
    hide susan

    #Michael McQuaid 
    show michael
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-9.mp3"
    mm "William! Go wait in the kitchen. We’ll talk about this later!"
    hide michael

    #Narrator 
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7-6.mp3"
    "The waitstaff member leaves, looking abashed."

    #Narrator  
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7-7.mp3" 
    "The man sitting next to Susan turns toward her and starts talking to her quietly."
    
    #Ezekiel Jones 
    show zeke at right
    voice "audio/Character Voices/Character Voices/Narrator 9 - scene 7-2.mp3"
    ej "Seems like that really got him going."

    #Susan Murphy 
    show susan at left
    voice "audio/Character Voices/Character Voices/Narrator 5 - Scene 7-2.mp3"
    sm "Yeah,really got his goat. Seems very uptight. I don’t remember him being like this."
    
    #Ezekiel Jones
    show zeke at right
    voice "audio/Character Voices/Character Voices/Narrator 9 - scene 7.mp3"
    ej "Don’t be too harsh on him, McQuaid. It was an honest mistake. The poor boy just tripped."
    hide susan

    #Michael McQuaid 
    show michael at left
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-10.mp3"
    mm "I expect a certain amount of professionalism, Doctor, and I’d thank you not to tell me how to run my business. Now then, everyone, please continue to enjoy the party."

    hide michael
    hide zeke 


    #Ezekiel Jones 
    show zeke at right
    voice "audio/Character Voices/Character Voices/Narrator 9 - scene 7-3.mp3"
    ej "You just haven’t known him long enough. He’s always nice until he’s not."

    #Susan Murphy 
    show susan at left
    voice "audio/Character Voices/Character Voices/Narrator 5 - scene 7-3.mp3"
    sm "Seems like you know our host quite a bit."

    #Ezekiel Jones
    voice "audio/Character Voices/Character Voices/Narrator 9 - scene 7-4.mp3" 
    ej "Yeah, I know Michael, unfortunately. Hi, I’m Ezekiel."

    hide zeke 
    hide susan

    menu scene_7_choice:
        "What are you looking to do?"
        #Go mingle Choice    
        "Go Mingle":

            #Susan Murphy 
            show susan
            voice "audio/Character Voices/Character Voices/Narrator 5 - scene 7-4.mp3"
            sm "A pleasure to make your acquaintance. Well, Ezekiel, I think I’ll go mingle a bit. See you around."
            hide susan

            jump mingle 


        #Get to ezekiel 
        "Get to know Ezekiel":

            #Ezekiel Jones
            show zeke at right          
            ej "Our host said you are an amazing private eye. That kind of job takes brains."

            #Susan Murphy
            show susan at left 
            sm "Oh, I’m just as smart as anyone, and besides, I have always had help. But, I always manage to catch my crooks."

            #Ezekiel Jones
            ej "I don’t envy the job, but I’m glad there’s someone doing it. If there is anything I can help you with for any reason, don't hesitate to call me."

            #Susan Murphy 
            sm "Thank you, Ezekiel. You’re a good man. But enough about me, what about you? What do you do?"

            #Ezekiel Jones
            ej "I am a doctor. I help by prescribing the medication that my patients need."

            ej "After the war, my job has been rough because there are so many people who need my help."

            #Susan Murphy 
            sm "Your job is no small feat. Your job is as tough as mine, maybe even tougher."

            sm "Just as you said, if there is anything I can help you with, don't hesitate to ask."

            #Narrator
            "Ezekiel looked at Susan with a thankful smile. His smile was sincere and enough to move almost anyone."
            
            #Ezekiel Jones
            ej "Thank you for those kind words."

            #Susan Murphy
            sm "I want to mingle a bit. Thank you for the talk."

            #Ezekiel Jones
            ej "The pleasure is mine, thank you."
            hide zeke
            hide susan

            jump mingle

label mingle:
    
    #Narrator 
    show susan
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7-8.mp3"
    "Susan gets up and wanders the dining room. She comes to a table with three elegantly dressed women where Richard had been sitting"
    

    scene switchtables

    #Patricia White 
    show patricia at right
    pw "Well, I don’t see why Richard had to go and make such a fuss! I mean, it was just booze!"

    #Rachel Reed 
    show rachel at left
    voice "audio/Character Voices/Character Voices/Narrator 11 - scene 7.mp3"
    rar "Richard just gets easily upset when something happens to his things. I mean, that was a very expensive suit."
    

    #Deborah White
    hide rachel
    show deborah at left 
    voice "audio/Character Voices/Character Voices/Narrator 12 - scene 7.mp3"
    dw "He’s a man who cares about his appearance. Can’t ask for much more than that these days."

    #Patricia White
    
    show patricia at right
    voice "audio/Character Voices/Character Voices/Narrator 10 - scene 7-2.mp3"
    pw "Oh, if it isn’t “the brilliant Susan Murphy”? What’d you do for McQuaid to be called ‘brilliant’?"

    #Susan Murphy
    hide deborah
    show susan at left
    voice "audio/Character Voices/Character Voices/Narrator 5 - scene 7.mp3"
    sm "I found a leak in his bank account for him. I’m sorry. I know McQuaid introduced us, but it went by a bit fast. Would you mind reminding me of your names?"

    #Deborah White
    hide patricia
    show deborah at right
    voice "audio/Character Voices/Character Voices/Narrator 12 - scene 7-2.mp3"
    dw "Oh, pardon me! I’m Deborah. This is my sister Patricia, and this is Rachel, the blowhard’s wife."
    hide deborah
    hide susan

    #Rachel
    show rachel
    voice "audio/Character Voices/Character Voices/Narrator 11 - scene 7-2.mp3"
    rar "Hey!"
    hide rachel

    #Narrator 
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7.mp3"
    "A ringing sound is heard, and Michael taps his glass with a spoon as if making a toast."

    #Michael McQUiad
    show michael
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7.mp3"
    mm "Everyone! I hope you've enjoyed your evening, but now it's time to get to business"
    hide michael

    #Narrator 
    voice "audio/Character Voices/Character Voices/Narrator 1 - scene 7-2.mp3"
    "A hush settles over the room."

    #Michael Mcquaid 
    show michael
    voice "audio/Character Voices/Character Voices/Narrator 2 - scene 7-2.mp3"
    mm "You see, I may have told a little white lie on your invitations. The real reason you’re here is that each one of you has a secret. Something hidden that would ruin you if it were to get out."

    #Michael McQuaid 
    mm "I brought you all here so we could come to a little… arrangement. Over the next few days, I am sure you’ll find this to be in your best interest."

    #Michael McQuaid 
    mm "After all, who knows what would happen if your little secrets were no longer secret."
    hide michael 

    #Susan Murphy 
    show susan
    voice "audio/Character Voices/Narrator5Scene7Step14.mp3"
    sm "What!"
    hide susan 

    #Deborah White 
    show deborah
    voice "audio/Character Voices/Narrator12Scene7Step15.mp3"
    dw "How dare you!"
    hide deborah

    #Ezekiel Jones 
    show zeke
    voice "audio/Character Voices/Narrator9Scene7Step16.mp3"
    ej "What on  Earth are you talking about"
    hide zeke

    #Patricia White 
    show patricia
    voice "audio/Character Voices/Narrator10Scene7Step17.mp3"
    pw "WHAT IN THE FLYING FUCK ARE YOU ON ABOUT!"
    hide patricia

    #Rachel Reed 
    show rachel
    voice "audio/Character Voices/Narrator11Scene7Step18.mp3"
    rar "Hrrk! I think I’m going to be sick."
    hide rachel

    #Narrator
    voice "audio/Character Voices/Narrator1Scene7Step19.mp3" 
    "Heads turn as Rachel runs from the room, sickened by Michael’s words."

    #Susan Murphy thoughts
    voice "audio/Character Voices/Narrator3Scene7Step20.mp3"
    smt "He couldn’t mean… but how could he… No, that’s impossible."

    #Susan Murphy Thoughts
    voice "audio/Character Voices/Narrator3Scene7Step21.mp3"
    sm "There’s no way he could know. What is this about? Hmm…"
    hide susan 

    #Ezekiel Jones 
    show zeke at left
    voice "audio/Character Voices/Narrator9Scene7Step22.mp3"
    ej "I don’t believe you, McQuaid. You’re bluffing."

    #Michael McQuaid 
    show michael at right
    voice "audio/Character Voices/Narrator2Scene7Step23.mp3"
    mm "Really Ezekiel? Then you wouldn’t mind me telling all these fine people about that missing shipment of drugs" 

    #Narrator
    "As the crowd’s eyes turn towards him, Ezekiel pales."

    #Ezekiel Jones 
    show zeke at left
    voice "audio/Character Voices/Narrator9Scene7Step22.mp3"
    ej "What do you want, McQuaid?"

    #Michael McQuaid 
    show michael at right
    voice "audio/Character Voices/Narrator2Scene7Step23.mp3"
    mm "The same I’ve always wanted, always deserved. Power. While you yucks have been going about your days with your crimes, I’ve been building a list on all of you."
    hide michael 
    hide zeke

    #Susan Murphy Thoughts
    show susan
    voice "audio/Character Voices/Narrator3Scene7Step24.mp3"
    smt "Building a list? Why would he possibly be building a list on me? *Sigh* I can’t ever get a vacation. I should probably check on Rachel. I wonder where she ran off too."
    hide susan 

    #Scene 9 

    #narrator voice
    voice"audio/Character Voices/Narrator1Scene8Step1.mp3"
    "Susan leaves the room in search of Rachel. She is now in the Hallway."

    #Scene 8 
    scene hallway

    "Navigating the hallway"
    
    #Navigate here to hallway

        

    #Susan Murphy
    show susan
    voice"audio/Character Voices/Narrator5Scene8Step2.mp3"
    sm "She said she was feeling sick. I should probably go and check the washroom."
    
    #Scene 10   
    #Navigating to the washroom

    scene navigatingtowashroom

    "Navigating to washroom"

    #Scene 11
    scene washroom

    #Narator Voice
    voice"audio/Character Voices/Narrator1Scene9Step3.mp3"
    "Susan enters the washroom but finds no one there."

    #Susan Murphy Voice
    show susan
    voice"audio/Character Voices/Narrator5Scene9Step4.mp3"
    sm "Drat, she’s not here. Where else would she be… their cabin!"

    #Scene 12
    scene navigatetocabin

    "navigation to the cabin"

    #The player navigates to the Reed’s cabin, the door is slightly ajar

    #Scene 13

    #The Hallway Facing the Ajar Cabin Door
    scene hallwayfacingdoor

    #Narrator
    voice"audio/Character Voices/Character Voices/Narrator1-Scene_10-31.mp3"
    "When Susan arrives at the Reed's cabin, she finds the door slightly ajar."
    #voice "scene13_N1_1.mp3"

    #Scene 14

    #The player navigates to the Reed's cabin, opens the door and looks inside
    scene reedscabin

    "Reaching the cabin, opening the door to look inside"

    #Scene 15 - First Murder   



    scene reedscabin

    #Narrator 
    voice "audio/Character Voices/Narrator1Scene10Step1.mp3"
    "As Susan opens the door, she is met with a horrific sight. Richard Reed, former CEO of Reed Industries, has been beaten bloody, and unmoving."
    #voice "scene15_N1_1.mp3"

    #Susan Murphy 
    show susan
    voice "audio/Character Voices/Narrator5Scene11Step2.mp3"
    sm "Oh Shit. Is that Richard? Oh my God, I need to tell everyone about this."
    
    hide susan

    hide susan       

    #scene 16 

    #The player navigates back to the Dining Hall

    scene hallway

    "Navigating back to the dining hall"

    #scene 17
    scene diningroom

    #Narrator
    voice"audio/Character Voices/Narrator1Scene12Step25.mp3"
    "Susan sprints back to the dining room, bursting through the door, panting."
    #voice "scene17_N1_1.mp3"

    #Susan Murphy
    show susan at left 
    voice"audio/Character Voices/Narrator5Scene12Step26.mp3"
    sm "McQuaid! I thought you wanted us to do your bidding, not kill us"
    voice "scene17_N5_sm_1.mp3"

    #Michael McQuaid
    show michael at right
    voice"audio/Character Voices/Narrator2Scene12Step27.mp3"
    mm "Pardon me, Ms. Murphy?"
    voice "scene17_N2_mm_1.mp3"

    #Susan Murphy 
    voice"audio/Character Voices/Narrator5Scene12Step28.mp3"
    sm "I went to look for Rachel because she was feeling a bit sick from your “news,” and I found Richard dead in their cabin. Explain yourself!"
    voice "scene17_N5_sm_2.mp3"
    
    #Michael Mcquaid
    voice"audio/Character Voices/Narrator2Scene12Step29.mp3"
    mm "Well, it wasn’t me. I was here the entire time! You said you went to find Rachel? What if she went to get rid of her dastardly husband?"
    voice "scene17_N2_mm_2.mp3"

    #Susan Murphy
    voice"audio/Character Voices/Character Voices/Narrator5_Scene12-35.mp3"
    sm "Oh, come on, that’s ridiculous."
    voice "scene17_N5_sm_3.mp3"

    #Michael Mcquaid
    voice"audio/Character Voices/Character Voices/Narrator 2 - Scene 12-35.mp3"
    mm "As far as we know, you could have killed him!" 
    hide michael
    voice "scene17_N2_mm_3.mp3"

    #Ezekiel Jones
    show zeke at right 
    voice"audio/Character Voices/Character Voices/Narrator 9 - Scene12-35.mp3"
    ej "Hmm, he has a good point. We know nothing for sure. While you do seem like a lovely person Susan, you were out there alone."
    voice "scene17_N9_ej_1.mp3"

    #Susan Murphy
    voice"audio/Character Voices/Character Voices/Narrator 5 - Scene12-36.mp3"
    sm "You can’t be serious! You all saw me leave here a few seconds ago!" 
    voice "scene17_N5_sm_4.mp3"

    #Patricia White
    hide zeke
    show patricia at right
    voice"audio/Character Voices/Character Voices/Narrator 10 - Scene12-36.mp3"
    pw "Oh no, sis, are we gonna get murdered? I’m too pretty to get murdered!"
    voice "scene17_N10_pw_1.mp3"

    #Deborah White
    hide patricia
    show deborah at right
    voice"audio/Character Voices/Character Voices/Narrator 12- Scene12- 36.mp3"
    dw "Calm down, Patty. Nothing is gonna happen to you."
    voice "scene17_N12_dw_1.mp3"

    #Patricia White
    hide deborah
    show patricia at right
    voice"audio/Character Voices/Character Voices/Narrator 10 - Scene12-37.mp3"
    pw "You don’t know that! I’m gonna die to a murderer onboard."
    voice "scene17_N10_pw_2.mp3"

    #David Dalton
    hide patricia
    show david at right
    voice"audio/Character Voices/Character Voices/Narrator 4 - Scene12-37.mp3"
    dd "I don’t know if I want to work here if someone is murdering people. Someone tell the captain to turn thi - …"
    voice "scene17_N4_dd_1.mp3"

    hide david
    hide susan

    #Narrator
    voice"audio/Character Voices/Character Voices/Narrator 1 - Scene12-37.mp3"
    "Indiscriminate chatter happens amongst the guests."
    voice "scene17_N1_2.mp3"

    #Michael Mcquaid
    show michael
    voice"audio/Character Voices/Character Voices/Narrator 2 - Scene12-38.mp3"
    mm "ALRIGHT, EVERYONE! Settle down. Let’s not lose our heads. Susan, you are a private eye, yeah? I think you have the qualifications to solve this."
    voice "scene17_N2_mm_4.mp3"

    #Susan Murphy
    show susan at left
    show michael at right
    voice"audio/Character Voices/Character Voices/Narrator 5 - Scene12-38.mp3"
    sm "What? You don’t suspect me anymore?"
    voice "scene17_N5_sm_5.mp3"

    #Michael Mcquaid
    voice"audio/Character Voices/Character Voices/Narrator 2 - Scene12-38-2nd_line.mp3"
    mm "I do. That’s why someone should be with you every second."
    voice "scene17_N2_mm_5.mp3"

    hide michael

    #Ezekiel Jones
    show zeke at right
    voice"audio/Character Voices/Character Voices/Narrator 9 - Scene12-38.mp3"
    ej "I’ll keep an eye on her."
    voice "scene17_N9_ej_2.mp3"

    #Susan Murphy
    voice"audio/Character Voices/Narrator5Scene12Slide39Step1.mp3"
    sm "Oh, please."
    voice "scene17_N5_sm_6.mp3"
    
    #Michael Mcquaid
    hide zeke
    show michael at right
    voice"audio/Character Voices/Narrator2Scene12Slide39Step1.mp3"
    mm "Perfect, the doctor and the eye. What a confidential relationship."
    voice "scene17_N2_mm_6.mp3"

    hide michael

    #Patrica White
    show patricia at right
    voice"audio/Character Voices/Narrator10Scene12Slide39Step1.mp3"
    pw "I wanna go look for Rachel! She could be in danger!"
    hide patricia 
    voice "scene17_N10_pw_3.mp3"

    #Deborah White
    show deborah at right
    voice"audio/Character Voices/Narrator12Scene12Slide40Step1.mp3"
    dw "Aren’t you afraid of getting murdered?"
    hide deborah
    voice "scene17_N12_dw_2.mp3"

    #Patrica White
    show patricia at right
    voice"audio/Character Voices/Narrator10Scene12Slide40Step1.mp3"
    pw "Yes, but she was nice to me. Oh, please come with me, Debbie."
    voice "scene17_N10_pw_4.mp3"

    hide patricia 

    #Deborah White
    show deborah at right
    voice"audio/Character Voices/Narrator12Scene12Slide40Step2.mp3"
    dw "auughhh, fine. Let’s go look for her. Hey Michael! You heard?"
    voice "scene17_N12_dw_3.mp3"

    hide deborah

    #Michael Mcquaid
    show michael at right
    voice"audio/Character Voices/Narrator2Scene12Slide41Step1.mp3"
    mm "Loud and clear. The rest of us will stay here. Don’t want anyone else turning up dead now."
    voice "scene17_N2_mm_7.mp3"

    hide michael
    hide susan

    #Narrator
    voice"audio/Character Voices/Narrator1Scene12Slide41Step1.mp3"
    "Susan and Ezekiel leave to go to the crime scene. Deborah and Patricia leave moments after to try and find Rachel."

    #voice "scene17_N1_3.mp3"

    #Scene 18 

    #Player navigates to the Murder 1 Scene Inside the Reed’s Cabin

    scene hallway

    "Navigating to the murder scene"

    #voice "scene18_N1_1.mp3"

    #Scene 19

    #Investigating Richard's Murder Scene

    call screen reedscene_investigation

    #Narrator
    voice"audio/Character Voices/Character Voices/Narrator 1_scene13-Line1-42.mp3"
    "While looking at a crime scene, click on points of interest around the area to find clues."

    hide screen reedscene_investigation
    
label first_murder:   

    #scene 20
    scene murderscene

    #scene 20
    scene murderscene

    #Susan Murphy
    show susan at left
    voice"audio/Character Voices/Character Voices/Narrator 5_Scene13-Line-1-45.mp3"
    sm "I think that's all we can get from the crime scene. How about we go do some interviews?"
    #voice "scene20_N5_sm_1.mp3"

    #Ezekiel Jones 
    show zeke at right
    voice"audio/Character Voices/Character Voices/Narrator 9_Scene13-45-line1.mp3"
    ej "I'm afraid everyone's probably gone to sleep, Murphy. Perhaps we should break for the night and pick up where we left off in the morning?"
 
    #voice "scene20_N9_ej_1.mp3"

    #Susan Murphy
    voice"audio/Character Voices/Character Voices/Narrator 5_Scene13-45-Line 2.mp3"
    sm "As much as I hate to leave a case like this… you're right. Reconvene in the dining room tomorrow?"
    #voice "scene20_N5_sm_2.mp3"

    #Ezekiel Jones
    voice"audio/Character Voices/Character Voices/Narrator 9_Scene13-45-Line 2.mp3"
    ej "Of course."
    #voice "scene20_N9_ej_2.mp3"

    #Narrator
    hide zeke
    hide susan
    voice"audio/Character Voices/Character Voices/Narrator 1_Scene13-45.mp3"
    "Susan and Ezekiel leave the crime scene and go to their separate rooms."
    #voice "scene20_N1_1.mp3"

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
    "Susan is walking through the halls and hears some commotion coming from the bathroom."

    #Scene 23 
    #The player navigates to the Bathroom

    scene hallway
    "Navigating to the bathroom"

    #Scene 24
    scene insidebathroom

    #Narrator
    "Inside the bathroom, she sees the sisters, Patricia and Deborah White. Patricia is by the toilet, feeling sick to her stomach. Deborah is keeping her company."

    #Patrcia Sound Effect Retches
    show patricia
    pw "Retches"
    hide patricia

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
    pw "Yes, ma'am, Hrph"
    hide patricia

    #Deborah White
    show deborah at right
    dw  "Yea, we found her. Thank goodness she was okay. Physically, at least."

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
    dw "I think she's in the Dining Hall. When I saw her last, she was still distressed, and Michael was with her"

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
    smt "They said she broke down. It still doesn't excuse her totally. I have to keep looking for clues. Let's see how Rachel is actually doing."

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
    rar "sigh"
    
    #Rachel Reed
    rar "Well, after the news, I felt nauseous. So I started to head to the bathroom. On my way there, I caught a draft of the ocean breeze and decided to go on the deck instead."

    #Susan Murphy
    
    sm "Did the ocean breeze help?"
    
    
    #Rachel Reed
    
    rar "A little. It helped to calm me down. I did hear something, but I thought it was just the party or something. Oh God, what if it was Richard? I could have done something to save him! He would have been alive if I had just stayed by his side."
    

    #Susan Murphy
    
    sm "Hey, don't do that. There's nothing you could have done to see this coming."
    

    #Ezekiel Jones
    hide rachel
    show zeke at right
    ej "Yeah, take it from me. It doesn't help anything at all."
    hide zeke
    
    #Susan Murphy
    show rachel at right
    sm "Did you find your way back to the party?"

    #Rachel Reed
    rar "Yes, eventually the White sisters came to help but-"

    rar "*sobs*"
    
    rar "all they did was made me feel worse by telling me that I lost my Richard."

    #Susan Murphy
    
    sm "A couple more questions, okay? Do you know anyone that could've done this?"
    

    #Rachel Reed
    rar "*sniff*"

    rar "Richard always had enemies. Since we were back in school, he'd always been a bit...abrasive. They'd just never understood him. Oh, my Richard. I miss you so much.."
    hide rachel

    #Ezekiel Jones
    
    show zeke at right
    ej "Okay, that's enough. You should take some time to rest and grieve your loss."


    #Susan Murphy 

    sm "Yes, I'm sorry this happened."


    #Rachel reed
    hide zeke
    show rachel at right
    rar "Me too."
    hide rachel 
 
    #Susan Murphy 
    show michael at right
    sm "McQuaid. What happened to the waitstaff member that had a squabble with Reed last night?"


    #Michael Mcquiad
    mm "I sent him back to the kitchen to do some extra work. He should be there now if you want to talk to him."

    #Susan Murphy
    
    sm "Okay. We aren't done here either."
    

    #Michael Mcquiad
    
    mm "Oh, Ms. Murphy, where would I possibly go?"
    

    #Narrator
    "Susan looks at Ezekiel to confirm he is coming with her, and then Susan leaves."

    #Navigating the hallway
    scene hallway
    show susan at left
    show zeke at right

    "Navigating hallway together"

    #Scene 30 - Ezekiel Jones (Hallway)

    sm "Ezekiel, I want to ask you a few questions."
            
    #Ezekiel Jones
    ej "I understand. I want this killer brought to justice, and I want to help you. I will answer any questions to the best of my ability."
    hide zeke
    hide susan

    menu ezekiel_inv:
        "Choose path of investigation"
        "Ask About Footprint":
            
            #Scene 31 - Ezekiel Jones / Footprint (Hallway)

            #Susan Murphy 
            show susan at left
            show zeke at right
            sm "I would like to check your shoes."
        
            #Ezekiel Jones
            ej "Because of the footprint, right? Do you think it’s me?"

            #Susan Murphy 
            sm "No, I just have to be certain. Better safe than sorry, right?"

            #Ezekiel Jones
            ej "I understand. I should mention I have multiple pairs of shoes. Would you like me to see them as well?"
                            
            #Susan Murphy 
            sm "Yes, if you have more, please take me to them. I need to check them myself"

            #Ezekiel Jones
            ej "Okay, I will show you to them."
            hide zeke
            hide susan

            #Scene 32 - Ezekiel Jones / Footprint (Ezekiel's Room)

            scene ezekielroom

            #Susan Murphy 
            show susan at left
            show zeke at right
            sm "It is interesting how you have so many shoes and yet not a single match. Are you sure that is all of them, or are you hiding another pair?"

            #Ezekiel Jones
            ej "W-what? Is- is that r-really what you think of me? I-I I thought we were friends. I even told you I would help you if you needed anything."

            #Narrator
            "Pain was filling Susan up inside, but she kept a poker face to see his reaction."
            hide zeke
            hide susan
            menu ezekiel_footprint:

                "Choose path of investigation"

                "Press Further":
                    
                    #Scene 33 - Ezekiel Jones / Footprint (Ezekiel's Room)

                    #Susan murphy
                    show susan at left
                    show zeke at right
                    sm "From the sound of your reaction, it almost seems like you’re hiding something. If there isn't anything to hide, look me in the eye and say it confidently"

                    sm "Do you have another pair of shoes that you are hiding?"

                    #Narrator
                    "Ezekiel Jones had pain in his eyes of anger and sadness but also understanding. He calmed himself and took a deep breath."

                    #Susan Murphy Thoughts
                    sm "Okay, that rules him out in that part, at least. I am glad, it pains me, but I must do this to find the killer."

                    #Ezekiel Jones
                    ej "No, I don't have another pair of shoes. Feel free to take a look around my room to check."

                    #Narrator
                    "Susan continued to check the room for anything that was hidden but found nothing."

                    #Susan Murphy
                    sm "It seems like I was out of line. Thank you for bearing with me."

                    #Ezekiel Jones
                    ej  "It’s okay. I apologize for my reaction as well. I understand all you want to do is find the killer."

                    ej "I realize you have another question. However, I need to clear my head. Meet me back at the dining hall, and we can talk there."

                    #Susan Murphy
                    sm "I understand. I will visit you in the dining hall to continue the conversation."
                    hide zeke
                    hide susan

                #Menu Option - Calm him down
                "Calm him down":
                    
                    #Scene 34 - Ezekiel Jones / Footprint (Ezekiel's Room)

                    #Susan Murphy 
                    show susan at left
                    show zeke at right
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
                    hide zeke
                    hide susan
                    jump training
                    jump cont_ezekiel_inv

        "Ask about training":
            jump cont_ezekiel_inv

label cont_ezekiel_inv:

    #Scene 35 - Ezekiel Jones / Training (Ezekiel's Room)

    #Susan Murphy 
    show susan at left
    show zeke at right
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
    hide zeke
    hide susan
    menu ezekiel_training:
        "Choose path of investigation"
        "Press Further":
            
            #Scene 36 - Ezekiel Jones / Training (Ezekiel's Room) 

            #pressing further possible choice

            "Pressing Further"
            
            #Susan Murphy 
            show susan at left
            show zeke at right
            sm "War is a harsh time. It can traumatize people. You may be suffering from this traumatic experience."

            #Ezekeil Jones
            ej "Are you stating that because I was in a War, it harmed me so much that I continued to kill people?!"

            ej "I despise violence! I don't like harming people!"

            #Susan Murphy 
            sm "Yet you were in a War, and War involves killing."

            #Ezekiel Jones
            ej "It is true. I am suffering. Seeing innocent people die before your eyes is painful."

            ej "No matter what, I joined the War because it is my duty! I wanted to help people, not kill them!"
            
            #Susan Murphy
            sm "I apologize, Ezekiel. I know I was rough with asking questions."

            #Narrator
            "Ezekiel tries to calm himself down."

            #Ezekiel Jones
            ej "It’s okay. You’re just doing your job."
            hide zeke
            hide susan

        #Menu Option - Calm him down    
        "Calm him down":
            ##Scene 37 - Ezekiel Jones / Footprint (Ezekiel's Room)

            #Susan Murphy 
            show susan at left 
            show zeke at right
            sm "Being a medic in the War is tough. You are not suffering from any mental trauma, are you?"

            #Ezekiel Jones
            ej "It really hurts me to see people die. While I do admit there might be some trauma that I am facing, I can't stop doing my job to help people."

            ej "A friend of mine was on the front lines of World War 2, and he got shot. I did my best, everything I could do to save him."

            ej "But no matter how hard I tried, it wasn’t enough. He still died. It haunts me to this day."

            #Susan Murphy 
            "That sounds rough. I am sorry for your loss. If there is anything I can do to help, don't hesitate to ask."

            #Ezekiel Jones
            ej "Thank you, Susan. That means a lot."
            hide zeke
            hide susan

            menu ezekiel_calmhim:
                "What's your next step?"
                "Interrogate another passenger":
                    jump investigation_choice
                "Quit for the day":
                    jump end_of_dayone                  
  
     
   
    #Scene 29 - choose to investigate

    scene hallway


    menu investigation_choice:
        "Choose who to interrogate"
        "William Windchime" if "william" not in persistent.investigation_choices_viewed:
            $ persistent.investigation_choices_viewed.append("william")
            jump william_inv
        "David Dalton" if "david" not in persistent.investigation_choices_viewed:
            $ persistent.investigation_choices_viewed.append("david")
            jump dalton_inv
        "Michael McQuaid" if "michael" not in persistent.investigation_choices_viewed:
            $ persistent.investigation_choices_viewed.append("michael")
            jump michael_inv
        "Quit for the day":
            jump end_of_dayone


    

label dalton_inv:
    $ persistent.investigation_choices_viewed.append("David Dalton")
    #Scene 38 - David Dalton (Kitchen)

    #keeping for alpha to provide flow to the game linear mechanics

    scene hallway

    "Navigating to Kitchen" 

    # ----------

    scene kitchen 

    #David Dalton 
    show david
    dd "Well, if it isn't the detective and her faithful Watson. Here to ask me a few questions, then?"

    #Susan Murphy
    show susan at left
    show david at right
    sm "Yes, actually. But first, I'm afraid I never caught your name…"

    #David Dalton 
    dd "Dalton. David Dalton."
    hide susan
    hide david

    #Scene 39 - David Dalton / Footprint (kitchen)

    menu ask_dalton:
        "Choose your path of investigation"

        "Ask about footprint":
            
            #Asking about footprint 

            #Susan Murphy 
            show susan 
            sm "Dalton, can we see your shoes for a moment?"

            #Narrator
            hide susan
            show david 
            "Dalton looks taken aback."

            #David Dalton
            dd  "My shoes? Why would you ever need to see them?"

            #Susan Murphy
            show susan at left 
            show david at right 
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
            hide susan 
            hide david

            menu dalton_footsteps:
                "What's your next step?"
                "Interrogate another passenger":
                    jump investigation_choice
                "Quit for the day":
                    jump end_of_dayone
                

        "Ask about whereabouts":
            
            #Scene 40 - David Dalton / Ask Whereabouts (kitchen)

            #Susan Murphy 
            show susan
            sm "Where were you between 6:00 and 7:00 PM last night?"

            #David Dalton
            hide susan
            show david 
            dd "Well, I was in the Dining Hall until 6:30 when Mr. McQuaid asked me to come down here and get some more hors d'oeuvres, so I came in and got them, then went right back."

            #Susan Murphy
            show susan at left
            show david at right 
            sm "Can anyone verify that?"

            #David Dalton 
            dd "Sure, Mr. McQuaid sent me, and William was here when I got down. Oh, and some of the guests might have heard the boss's order."

            #Susan Murphy 
            sm "And when did you get back to the Dining Hall?"

            #David Dalton 
            dd "Oh, 6:50, 6:55."

            #Ezekiel Jones
            hide susan
            hide david
            show zeke
            ej "That seems like an awfully long time to get some appetizers. Sure you didn't take a little detour to murder a prick who insulted your co-worker?"
            hide zeke

            #David Dalton 
            show david
            dd "Kill? For William? Oh please, I like the kid, but we ain't that close. We were out of appetizers, so I had to make more."

            #David Dalton 
            dd "Now, do you have anything else to ask, or can I get back to these dishes?"
            hide david

            menu dalton_whereabouts:
                "Choose path of investigation"
                "Press Further":
                    #Scene 41 - David Dalton / Ask Whereabouts (kitchen)

                    #pressing further 

                    #Susan Murphy 
                    show susan
                    sm "You're sure that's all you did? It seems rather sloppy not to have spare hors d'oeuvres ready. And surely it would take less than 20 minutes."
                    hide susan

                    #David Dalton
                    show david 
                    dd "Well, I might've taken a moment to go to the washroom, but is that a crime?"
                    hide david

                    #Ezekiel Jones
                    show zeke
                    ej "No, but murder is, so forgive us for wanting to know what you did in a mysterious 20-minute window."
                    hide zeke

                    #Susan Murphy
                    show susan 
                    sm "Can anyone corroborate this?"
                    hide susan

                    #David Dalton 
                    show david
                    dd "I'm not some schoolgirl going to the restroom in packs. Now, if you'll excuse me, I have some dishes to wash."

                    #Narrator 
                    "Dalton turns to the sink, and Susan turns to Ezekiel."

                    #Susan Murphy 
                    hide david
                    show susan
                    sm "Those wounds could definitely have been made in 20 minutes. Most fights don't take longer than a few moments, much less that long."
                    hide susan

                    #Ezekiel Jones
                    show zeke
                    ej "We'll have to keep an eye on him."
                    hide zeke

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
    $ persistent.investigation_choices_viewed.append("William Windchime")
    #Narrator
    show will
    "William Windchime walks into the kitchen"
    hide will

    #Susan Murphy 
    show susan
    sm "Hello, William. We want to ask you a few questions if you don't mind."
    hide susan

    #William Windchime
    show will 
    ww "Oh. Um. I guess not. It's about the murder, right?"
    hide will

    #Ezkeiel Jones
    show zeke
    ej "Yes, it is. Now son, make sure to answer truthfully. We just want to get to the bottom of this."
    hide zeke

    menu windchime_inv:
        "Choose path of investigation"

        "Asking about footprint":
    
            #Scene 43 - William Windchime / Footprint (kitchen)

            #Susan Murphy 
            show susan
            sm "Can we see your shoes?"
            hide susan

            #William Windchime
            show will
            ww "What? Why?"
            hide will

            #Ezekiel Jones
            show zeke
            ej "We found a shoe print at the scene of the crime, and we're trying to narrow down whose it was. Now come on, show us. "
            hide zeke

            #William Windchime
            show will
            ww "Well, hold on, wait a minute-"
            hide will

            #Susan Murphy 
            show susan
            sm "What's the problem, kid? If you didn't do it, you've got nothing to hide."
            hide susan

            #William Windchime
            show will
            ww "Well- but- okay…"
            hide will

            #Narrator 
            "William takes off his shoe and shows it to Susan. It matches the shoe print."

            #Susan Murphy
            show susan 
            sm "It's a match!"
            hide susan

            #William Windchime
            show will
            ww "I swear it's not me! Someone stole them last night!"
            hide will

            #Ezekiel Jones
            show zeke
            ej "Right, sure they did. I'm sure they took them right off your feet. "
            hide zeke

            #William Windchime
            show will
            ww "No, no. I have a second pair that I was wearing. Please, it wasn't me!"
            hide will

            menu windchime_footprint:

                "Choose path of investigation"

                "Press further":
                    #Scene 44 - William Windchime / Footprint (Kitchen)

                    #Pressing Further Possible Choice

                    "Pressing Further"

                    #Susan Murphy 
                    show susan at left
                    show will at right
                    sm "Right. Someone stole your spare pair of shoes, committed murder, and then returned them to you."

                    sm "Because that sounds entirely plausible. Who would even do that?"
                    
                    #William Windchime
                    ww "W-w-well, Dalton and I share a locker. It could have been him!"

                    #Ezekiel Jones
                    hide susan
                    show zeke at left
                    ej "You have to admit, this seems awfully suspicious. Especially with how rude Richard was to you last night."

                    ej  "Now, I'm sure that others have been rude to you in the past, but maybe you finally had enough, eh?"

                    #William Windchime
                    ww "I don't have to stand here and take this! If you'll excuse me, there are things I need to do."
                    hide will
                    show zeke at right
                    show susan at left 

                    #Narrator 
                    "William storms off."

                    #Susan Murphy
                    sm "Damn, there he goes." 
                    hide susan
                    hide zeke

                    menu windchime_press:
                        "What's your next step?"

                        "Interrogate another passenger":
                            jump investigation_choice

                        "Quit for Day":
                            jump end_of_dayone

                "Interrogate another passenger":
                    jump investigation_choice
                
                "Quit for Day":
                    jump end_of_dayone
                       
                        
                
        "Asking about wherabouts":

            #Scene 45 William Windchime / Whereabouts (kitchen)
   
            #Susan Murphy 
            show susan at left
            show will at right
            sm "Where were you around 6:30 last night?"

            #William Windchime
            ww "I was here, in the kitchen. I spilled that soup, and then Mr. McQuaid yelled at me, and I didn't want to cause more trouble, so I came right down."

            #Ezekiel Jones
            hide susan
            show zeke at left
            ej "Can anybody corroborate that story?"

            #William Windchime
            ww "W-well, Dalton was in here around 6:50, and Mr. McQuaid sent me-"

            #Susan Murphy
            hide zeke
            show susan at left 
            sm  "So no."

            #William Windchime
            ww "I… I guess not. But it wasn't me, I swear! I was cleaning up the kitchen, that's all!"

            #Ezkeiel Jones
            hide susan
            show zeke at left
            ej "Sure, kid, sure."
            hide zeke
            hide will

            menu windchime_whereabouts:

                "Choose path of investigation"

                "Press Further":
                    #Scene 46 William Windchime / Whereabouts (kitchen)

                    #Pressing Further Possible Option 

                    "Pressing Further"
                        
                    #Susan Murphy 
                    show susan at left
                    show will at right
                    sm "You're positive that no one could vouch for your whereabouts? No one came down for a snack, and you didn\'t go to the washroom or leave?"

                    #William Windchime
                    ww "No, ma'am. Mister McQuaid told me to stay down here, so… I did."

                    #Ezkeiel Jones
                    hide susan
                    show zeke at left
                    ej "Well, no one will fault you for loyalty, but you've got to admit how suspicious this sounds."

                    #William Windchime
                    ww "Well.. yes, but I swear, it wasn't me!"
                    hide zeke 
                    hide will

                    menu windchime_further:

                        "Choose path of investigation"

                        "Interrogate another passenger":
                            jump investigation_choice

                        "Quit for day":
                            jump end_of_dayone
                                    

                "Investigate Motive":
                        
                    #Scene 47 William Windchime / Whereabouts (kitchen)

                    #Susan Murphy 
                    show susan at left
                    show will at right
                    sm "Alright, William, I have another question for you. When you spilled that soup on Richard, he shouted at you, right? That must have made you angry."

                    #William Windchime
                    ww "Well, yes, but not enough to... to- "

                    #Ezkeiel Jones
                    hide susan
                    show zeke at left
                    ej "To what? To murder someone? Someone who humiliated you in front o- "

                    #William Windchime
                    ww "Yes! Of course, I was angry! You'd be, too, if some rich asshole screamed at you for an accident! But I'm not some loon to kill somebody over something like that!"

                    #Susan Murphy
                    hide zeke
                    show susan at left 
                    sm "Easy, kid, we're just covering our bases. Say, how did you end up here, anyways? You don't strike me as the type to go for a service position."
                    hide susan
                    hide will
                    show will
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
                    hide will
                    #Ezekiel Jones
                    show zeke at right
                    show susan at left
                    ej  "Is it just me, or did he sound… resentful? Do you think he could have killed Richard to humiliate his employer?"
                    #Susan Murphy 
                    sm "It's certainly possible but unlikely."
                    hide susan
                    hide zeke

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
    show michael
    mm "Well, well, well, if it isn't our very own Ms. Holmes and Dr. Watson. Any luck out there?"
    hide michael

    #Susan Murphy
    show susan
    sm "We're looking at a few avenues of investigation, and I was hoping to pick your brain about some of the people here."
    hide susan

    #Michael Mcquaid
    show michael
    mm "Of course! I'm all ears."
    hide michael

    menu mcquaid_inv:
        "Choose your path of investigation"
        "The Reeds":
            
            #Scene 49 - Michael McQUaid / The Reeds (Dining Hall)

            #Ask About Reeds possible option

            #Susan Murphy
            show susan at left
            show michael at right
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
            hide michael 
            hide susan

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
            show susan at left
            show michael at right
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
            hide susan
            show zeke at left
            ej "High praise for a simple waiter."

            #Michael Mcquaid
            mm "Oh, he's more of a jack of all trades. He's a dab hand with a wrench and a decent cook."

            #Susan Murphy
            hide zeke
            show susan at left
            sm "When did you hire him?"

            #Michael Mcquaid
            mm "Oh, four, five years ago now. He'd fallen on some hard times and needed work. So I took him on, and now he's here!"

            #Susan Murphy
            sm "Do you know what he did before he fell on these ‘hard times’?"

            #Michael Mcquaid
            mm "Y'know, I'm not quite sure. Whenever I asked, he would always say he doesn't like talking about it."

            mm "Personally, I suspect it was some trade or other, but I never got answers out of him"

            #Ezekiel Jones
            hide susan
            show zeke at left
            ej "Would he have any reason to kill Richard?"

            #Michael Mcquaid
            mm "None that I can think of. Do you have any more questions for me? "
            hide zeke
            hide michael

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

    scene kitchen

    #Narrator
    "She is met by Michael McQuaid and some wait staff members surrounding a new murder scene."

    #Susan Murphy 
    show susan
    sm "McQuaid? What happened here?"

    #Narrator
    "Susan now sees what the commotion was all about."

    #Seeing the scne

    "Going to see the scene"

    #Scene 55 - Kitchen / SUsan Face 

    #Narrator
    "Lying there, dead, is William Windchime. Just as Susan sees the body, Ezekiel comes rushing in."

    #Ezekiel Jones
    show susan at left
    show zeke at right
    ej "What happen- oh.."

    #Susan Murphy 
    sm  "*sighs Looks like the mystery continues."

    #Michael Mcquaid
    hide zeke
    show michael at right
    mm "Okay, the detectives are here. Let's let them do their work."

    #Susan Murphy 
    sm "Wait, where is the girl that found him here?"

    #Michael Mcquaid
    mm "I'll go out and look for her. We'll be close by."

    #Ezekiel Jones
    hide michael
    show zeke at right
    ej "Well, time to go to work. Again."

    
    #Scene 56 - Murder Scene in kitchen
    
    call screen windchimescene_investigation 


    hide screen windchimescene_investigation

label third:

    #Scene 57 - Post Murder in Kitchen

    scene murderscene_kitchen

    #Susan Murphy 
    show susan
    sm "That seems to be all there is to find here."
    hide susan

    #Ezekiel Jones
    show zeke
    ej "And it looks like the day is over. Any point in holding interrogations right now?"
    hide zeke

    #Susan Murphy 
    show susan
    sm "I don't think so. We should retire for the night and pick back up tomorrow."
    hide susan 

    #Narrator
    "The pair go to their rooms and sleep a restless night."

    
    #------------------------------------- END OF DAY 2 --------------------------------------------------------#


    #------------------------------------- START OF DAY 3 --------------------------------------------------------#

    scene day3

    "Day 3"

    #Scene 58 - Michael MCquiad 

    scene dininghall

    #Susan Murphy 
    voice "audio/scene58_N5_sm_1.mp3"
    show susan
    sm "McQuaid."
    

    #Michael Mcquaid
    voice "audio/scene58_N2_mm_1.mp3"
    show susan at left
    show michael at right
    mm "Murphy. How goes the investigation? Any luck finding who killed poor William?"
    

    #Susan Murphy
    voice "audio/scene58_N5_sm_2.mp3" 
    sm "We've got a few leads that we're following."
    

    #Michael Mcquaid
    voice "audio/scene58_N2_mm_2.mp3"
    mm "That sounds like stalling, detective. Are you sure you know what you're doing?"
    

    #Susan Murphy Thoughts
    #voice "audio/scene58_N5_sm_3.mp3"
    sm "Yeah, yeah. Rub it in, why don't you?"
    

    #Michael Mcquaid
    voice "audio/scene58_N2_mm_3.mp3"
    mm "Or maybe you're misleading us. Maybe you know exactly who the killer is and are just trying to protect yourself."
    

    #Ezekiel Jones
    hide susan 
    show zeke at left
    voice "audio/scene58_N9_ej_1.mp3"
    ej "Don't be ridiculous, man! I was with Susan the whole time yesterday. She couldn't have murdered William."
    

    #Michael Mcquaid
    voice "audio/scene58_N2_mm_4.mp3"
    mm "If you say so, faithful Watson. Now, do you have any questions for me?"
    

    #Scene 59 - Michael McQuaid / Ezekiel Jones
 
    #Susan Murphy 
    voice "audio/scene59_N5_sm_1.mp3"
    hide zeke
    show susan at left
    sm "Ezekiel, would you mind leaving for a moment?"
    

    #Narrator
    hide susan
    show zeke at left
    voice "audio/scene59_N1_1.mp3"
    "Ezekiel looks at Susan, mildly confused, but obeys."
    

    #Ezekiel Jones
    voice "audio/scene59_N9_ej_1.mp3"
    ej "Sure…"
    hide zeke

    #Susan Murphy
    show susan at left 
    voice "audio/scene59_N5_sm_3.mp3"
    sm "Why is he here, McQuaid?"
    

    #Michael Mcquaid
    voice "audio/scene59_N2_mm_1.mp3"
    mm "What?"
    

    #Susan Murphy
    voice "audio/scene59_N5_sm_3.mp3" 
    sm "Why is Ezekiel here? Compared to all your other guests, he seems like a saint. What possible secrets could he have?"
    

    #Narrator
    voice "audio/scene59_N1_2.mp3"
    "Michael laughs in her face."
    

    #Michael Mcquaid
    voice "audio/scene59_N2_mm_2.mp3"
    mm "Oh, my dear detective, you think the good doctor is a saint? Oh, what a laugh. I won't tell but believe me when I say that man has more than enough secrets for blackmail."
    
    voice "audio/scene59_N2_mm_3.mp3"
    mm "Now, do you have anything else I can do for you?"
    

    #Scene 60 - Michael McQuaid / White Sisters

    #Asking About Ezekiel Possible Choice

    #Susan Murphy
    voice "audio/scene60_N5_sm_1.mp3" 
    sm "What can you tell me about the Whites?"
    

    #Michael Mcquaid
    voice "audio/scene60_N2_mm_1.mp3"
    mm "Oh, not much. Wealthy socialites who started from the bottom now they're where they are."
    

    #Susan Murphy
    voice "audio/scene60_N5_sm_2.mp3" 
    sm "Did they have any prior relationship with either of the deceased?"
    

    #Michael Mcquaid
    voice "audio/scene60_N2_mm_2.mp3"
    mm "Certainly not with William, but they move in the same circles as Rachel. If you're asking if they had the motive or even means to murder either one."
    
    voice "audio/scene60_N2_mm_3.mp3"
    mm "They may not be entirely honest, but they're certainly not murderers. At least, not ones that would beat a man to death or stab one."
    

    #Susan Murphy
    voice "audio/scene60_N5_sm_3.mp3" 
    sm "What do you mean by that, McQuaid?"
    

    #Michael Mcquaid
    voice "audio/scene60_N2_mm_4.mp3"
    mm "Let's just say that they didn't exactly come by all that money, honestly. Though I'm not sure Patty has the wits to know where their money came from."
    
    voice "audio/scene60_N2_mm_5.mp3"
    mm "Now, I'm sure you have more important things to do. Catch us a murderer, Ms. Holmes!"
    hide susan
    hide michael

    #Narrator
    voice "audio/scene60_N1_1.mp3"
    "Susan walks out of the dining and sees Deborah White."
    

    #Scene 61 - Deborah White 

    #Going to question deborah white possible choice

    "Going to question deborah white"

    #Susan Murphy
    show susan
    voice "audio/scene61_N5_sm_1.mp3" 
    sm "Hey Deborah, can I ask you a couple of questions?"
    

    #Deborah White
    show susan at left
    show deborah at right
    voice "audio/scene61_N12_dw_1.mp3"
    dw "Sure. What would you like to know?"
    

    #Susan Murphy
    voice "audio/scene61_N5_sm_2.mp3" 
    sm "Do you know where I can find Patty?"
    

    #Scene 62 - Debeorah White / Where is patty 

    #Susan Murphy 
    voice "audio/scene62_N5_sm_1.mp3"
    sm "It's unusual to see you without your sister. Where is she?"
    

    #Deborah White
    voice "audio/scene62_N12_dw_1.mp3"
    dw "I don't know. I've been worried sick looking for her all morning."
    

    #Susan Murphy
    voice "audio/scene62_N5_sm_2.mp3" 
    sm "Does she usually go off on her own?"
    

    #Deborah White
    voice "audio/scene62_N12_dw_2.mp3"
    dw "When we are home, she usually does her own thing, but she always checks in with me." 
    

    #Susan Murphy 
    voice "audio/scene62_N5_sm_3.mp3"
    sm "Hmm, and she didn't tell you anything this time?"
    

    #Deborah White
    voice "audio/scene62_N12_dw_3.mp3"
    dw "Nothing, I woke up, and she was already gone. Maybe she got seasick again and went out for some air, but I would have found her by now. I hope she's okay."
    

    #Susan Murphy
    voice "audio/scene62_N5_sm_4.mp3" 
    sm "Well, I'm walking around a lot today so if I find her, I will let you know."
    

    #Deborah White
    voice "audio/scene62_N12_dw_4.mp3"
    dw "Thanks, Susan."
    

    #Scene 63 - Debeorah White / Rachel Reaction

    #Susan Murphy
    voice "audio/scene63_N5_sm_1.mp3" 
    sm "You girls went looking for Rachel on the first night, right? When you found her, how was she?"
    

    #Deborah White
    voice "audio/scene63_N12_dw_1.mp3"
    dw "Yeah, Patty and I went to look for her and found her on the deck. She was okay, just catching some air. Don't you remember? I told you this."
    

    #Susan Murphy
    voice "audio/scene63_N5_sm_2.mp3" 
    sm "Yeah, just needed a reminder. When you found her and told her, how did she react?"
    

    #Deborah White
    voice "audio/scene63_N12_dw_2.mp3"
    dw "About the same as anyone would react. She didn't believe me at first, but eventually, she broke down crying. Patty was doing her best to try and console her."
    

    #Susan Murphy 
    voice "audio/scene63_N5_sm_3.mp3"
    sm "Oh really?"
    

    #Deborah White
    voice "audio/scene63_N12_dw_3.mp3"
    dw "Yea, she seemed like she was out there a little while because she was shivering. After she accepted what we were telling her wasn't a lie, she turned pale—like all the blood left her face."
    
    voice "audio/scene63_N12_dw_4.mp3"
    dw "After she broke down, she immediately rushed back to the dininghall. Wewentalong with her."
    

    #Susan Murphy
    voice "audio/scene63_N5_sm_4.mp3" 
    sm "Hmm, okay. Thanks for sharing"
    

    #Deborah White
    voice "audio/scene63_N12_dw_5.mp3"
    dw "Is that all you had to ask me?"
    

    #Susan Murphy
    voice "audio/scene63_N5_sm_5.mp3" 
    sm "For now, yes. I'll keep looking around for Patty. Good luck."
    

    #Deborah White
    voice "audio/scene63_N12_dw_6.mp3"
    dw "Thanks, Susan, you're such a gift!"
    
    hide susan 
    hide deborah

    #Narrator
    #voice "audio/scene_N1_1.mp3"
    "Susan goes to the bedrooms to go and check on Rachel."
    

    #navigating to Rachel Cabin

    scene hallway

    "Navigating to Rachel Cabin"

    #Scene 64 - Rachel Reed 

    scene rachelcabin

    #Narator
    voice "audio/scene64_N1_1.mp3"
    "A very sad looking Rachel opens the cabin door for Susan."
    

    #Susan Murphy 
    show susan
    voice "audio/scene64_N5_sm_1.mp3"
    sm "Hey Rachel, just coming to check up on you. How are you?"
    

    #Rachel Reed
    show susan at left
    show rachel at right
    rar "I just lost my husband. I'm miserable."
    
    

    #Susan Murphy 
    voice "audio/scene64_N5_sm_2.mp3"
    sm "Yea, that's fair. I just wanted to ask a couple of questions. Is that okay?"
    

    #Narator
    voice "audio/scene64_N1_2.mp3"
    "Rachel Shrugs"
    

    #Rachel Reed
    voice "audio/scene64_N11_rar_1.mp3"
    rar "I guess."
    

    #Scene 65 - Rachel Reed / Diamond Cane

    #Susan Murphy
    voice "audio/scene65_N5_sm_1.mp3" 
    sm "You were seen carrying a Diamond Cane. Where did you get it from?"
    

    #Rachel Reed
    voice "audio/scene65_N11_rar_1.mp3"
    rar "From Richard. He bought it for me as an anniversary present. Sure, it cost a lot of money, but he bought it to apologize for being a little extra mean back then. Business wasn't good, but it got better."
    

    #Rachel Reed
    voice "audio/scene65_N11_rar_2.mp3"
    rar "The gesture meant more to me than the stupid cane."
    

    #Susan Murphy
    voice "audio/scene65_N5_sm_2.mp3" 
    sm "Did you misplace it at any time?"
    

    #Rachel Reed
    voice "audio/scene65_N11_rar_3.mp3"
    rar "No. As soon as we boarded, we went to the room and changed for dinner. I left it there."
    

    #Susan Murphy 
    voice "audio/scene65_N5_sm_3.mp3"
    sm "I, see."
    

    #Scene 66 - Rachel Reed / About Richard

    #Susan Murphy
    voice "audio/scene66_N5_sm_1.mp3" 
    sm "Is it okay if I ask about Richard?"
    

    #Rachel Reed
    voice "audio/scene66_N11_rar_1.mp3"
    rar "*Nods* Hmm-hmm."
    

    #Susan Murphy 
    voice "audio/scene66_N5_sm_2.mp3"
    sm "How long have you known each other?"
    

    #Rachel Reed
    voice "audio/scene66_N11_rar_2.mp3"
    rar "Since primary school. He's truly the same person, just a bit more refined now… or was anyway..."
    

    #Susan Murphy
    voice "audio/scene66_N5_sm_3.mp3" 
    sm "Did he have a lot of enemies?"
    

    #Rachel Reed
    voice "audio/scene66_N11_rar_3.mp3"
    rar "Yes, unfortunately. For better or worse, he acted very loudly and was a very proud man. Which made him an acquired taste."
    

    #Susan Murphy
    voice "audio/scene66_N5_sm_4.mp3" 
    sm "I'm guessing more people didn't like the taste."
    

    #Rachel Reed
    voice "audio/scene66_N11_rar_4.mp3"
    rar "That's why you're the detective."
    
    voice "audio/scene66_N11_rar_5.mp3"
    rar "Are we done yet? I would like to go and lay back down again."
    

    #Susan Murphy 
    voice "audio/scene66_N5_sm_5.mp3"
    sm "Sure, that's all I wanted to ask."
    

    #Rachel Reed
    voice "audio/scene66_N11_rar_6.mp3"
    rar "Bye.."
    

    #Narrator
    voice "audio/scene66_N1_1.mp3"
    "Rachel closes the door on Susan."
    hide rachel
    show susan
    voice "audio/scene66_N1_2.mp3"
    "Susan heads up on deck for a breath of fresh air."
    hide susan

    #navgating to the desk

    scene hallway

    "Navigating to the Deck"

    #The Deck

    scene deck

    #Scene 67 - Ezekiel Jones

    #Narrator
    voice "audio/scene67_N1_1.mp3"
    "Susan spots Ezekiel the moment she walks out on the deck."
    

    #Susan Murphy 
    show susan
    voice "audio/scene67_N5_sm_1.mp3"
    sm "Good afternoon Mr. Jones."
    

    #Ezekiel Jones
    show susan at left
    show zeke at right
    voice "audio/scene67_N9_ej_1.mp3"
    ej "Good afternoon Ms. Murphy."
    

    #Susan Murphy 
    voice "audio/scene67_N5_sm_2.mp3"
    sm "I need to ask you a few questions."
    

    #Ezekiel Jones
    voice "audio/scene67_N9_ej_2.mp3"
    ej "Okay... What do you need to know?"
    hide susan
    hide zeke
    

    menu deck_inv:
        "Choose path of investigation"
        "Ask About Whereabout":
            #Scene 68 - Ezekiel Jones / Whereabouts

            #Narrator
            show susan at left
            show zeke at right
            "Susan asks Ezekiel about his whereabouts during the time of the murder."

            #Susan Murphy
            sm "Where were you when William was murdered?"

            #Ezekiel Jones
            voice "audio/scene68_N9_ej_1.mp3"
            ej "This is an unusual question. I was with you for most of the day. Remember I was helping you."
            

            #Susan Murphy thoughts
            voice "audio/scene68_N3_smt_1.mp3"
            #sm "That is correct. However, there were a few times when we might have separated."
            

            #Susan Murphy 
            sm "There were a few times we separated. Where did you go during those times?"

            #Ezekiel Jones
            ej "I just separated to use the bathroom, go to bed, or help give you information if it involved us finding the murderer."
            hide susan
            hide zeke
            #Scene 69 - Ezekiel Jones / whereabouts
            
            #Pressing Further Possible Choice

            "Pressing Further"

            #Susan Murphy 
            sm "Yes. However, there was one time when we separated. It is suspicioushowitwasonly a few minutes, but it could have been enough time for you kill someone."
            show susan at left
            show zeke at right

            #Ezekiel Jones
            ej "We’ve have gone over this before. I am not the killer. You can ask anyone on the boat to prove it to you"

            ej "I’ve been talking to them to gather information. I have nothing to hide."

            #Susan Murphy 
            sm "I understand. Apologies for questioning your trust."

            #Narrator
            "Ezekiel calms himself down."

            #Ezekiel Jones
            ej "Think nothing of it. If at any point you suspect me, I will answer anyquestionstruthfully."
            hide susan
            hide zeke
            

            #Narrator
            "Susan turns and catches David Dalton’s eye."

        "Probe for motive":
            #block of code to run
            #Scene 70 - Ezekiel Jones / Motive

            #Susan Murphy 
            show susan at left
            show zeke at right
            sm "Did you notice any changes in behaviour from William?"

            #Ezekiel Jones
            ej "I have not noticed much from him. He seemed normal."

            #Susan Murphy 
            sm "In the brief moments when we separated, had you spotted him?"

            #Ezekiel Jones
            ej "Yes, I had."
            hide susan
            hide zeke

            menu motive_inv:
                "Choose path of investigation"
                "Press Further":
                    #Scene 71 - Ezekiel Jones / Motive

                    #Susan Murphy 
                    show susan at left
                    show zeke at right
                    sm "It seems suspicious that you did meet him, and in those brief moments when we weren't together, he turns up dead the next day."

                    #Ezekiel Jones
                    ej "It is suspicious. I can confirm that I have an alibi and some important information."

                    #Susan Murphy 
                    sm "Oh, and what might that be?"

                    #Ezekiel Jones
                    ej "I can confirm that I was not the last person to see him that day. It was, in fact, (player to insert name here). I have not seen him since"

                    #Susan Murphy Thoughts
                    sm "That is some important information."
                    #Susan Murphy
                    sm "Thank you."

                    #Ezekiel Jones
                    ej "You're Welcome."
                    hide susan
                    hide zeke

                    #Narrator
                    "Susan turns and catches David Dalton’s eye."

                "Calm him down":
                    #Scene 72 - Ezekiel Jones / Motive

                    #Susan Murphy
                    show susan at left
                    show zeke at right
                    sm " It is not my intention to anger you. I just need to know what you have against him."

                    #Ezekiel Jones
                    ej "Why I have nothing against him. While I have seen him recently, I have no reason or motive to go against him."

                    #Susan Murphy
                    sm "Were you the last to see him?"

                    #Ezekiel Jones
                    ej "I can confirm that I was not the last person to see him that day. It was, in fact, (the player asked to insert name here). I have not seen him since."

                    #Susan Murphy Thoughts
                    sm "That is an important piece of information."

                    #Susan Murphy
                    sm "Thank you, Ezekiel."

                    #Ezekiel Jones
                    ej "My pleasure."
                    hide susan
                    hide zeke        

                    #Narrator
                    "Susan turns and catches David Dalton’s eye."
            
  
   
    #Narrator
    show susan
    voice "audio/scene72_N1_1.mp3"
    "Susan turns and catches David Dalton’s eye."
    

    #Scene 73 - David Dalton

    #Go to speak david possible option

    "Going to talk to David"

    #David Dalton
    show susan at left
    show david at right
    voice "audio/scene73_N4_dd_1.mp3"
    dd "More questions, Ms. detective? Haven't I proven my innocence to you?"
    

    #Ezekiel Jones
    hide susan
    show zeke at left
    voice "audio/scene73_N9_ej_1.mp3"
    ej "Well, William didn't make the footprints that lead away from his own body."
    

    #Susan Murphy
    hide zeke
    show susan at left
    voice "audio/scene73_N5_sm_1.mp3"
    sm "We're just covering our bases, Dalton. We have two dead bodies on this boat, and the odds of there being two separate murderers are laughable."
    

    #Susan Murphy
    voice "audio/scene73_N5_sm_2.mp3"
    sm "Now, we do have a couple more questions."
    

    menu dalton_pathIvestigation:
        "Choose Path of Investigation"
        #Scene 74 - David Dalton / Whereabouts 
        "Ask About Whereabouts":
            
            #Susan Murphy
            voice "audio/scene74_N5_sm_1.mp3"
            sm "Where were you around the time of William's murder?"
            

            #David Dalton
            voice "audio/scene74_N4_dd_1.mp3"
            dd "I was here, taking a smoke break. And before you ask, Mr. McQuaid can confirm it. I asked him for permission."
            

            #Susan Murphy
            voice "audio/scene74_N5_sm_2.mp3"
            sm "Is McQuaid the only one who can verify that?"
            

            #David Dalton
            voice "audio/scene74_N4_dd_2.mp3"
            dd "I beg your pardon?"
            

            #Susan Murphy
            voice "audio/scene74_N5_sm_3.mp3"
            sm "Well, it's awfully convenient that the one person on the boat you have a prior relationship with, someone who speaks of you very highly, is the person you point to as your witness."
            
            voice "audio/scene74_N5_sm_4.mp3"
            sm "Convenient enough that it beggars' belief, some might say."
            

            #Ezekiel Jones
            hide susan
            show zeke at left
            voice "audio/scene74_N9_ej_1.mp3"
            ej "What she's trying to say is that it's suspicious that your boss is the only one who saw you."
            

            #Susan Murphy
            hide zeke
            show susan at left
            voice "audio/scene74_N5_sm_5.mp3"
            sm "I think he got the point." 
            

            #David Dalton
            voice "audio/scene74_N4_dd_3.mp3"
            dd "I can't help if people aren't out and about with a murderer on the boat! In any case, ask around. Someone else probably saw me up here."
            

            dd "It's not like I was exactly hiding."

            menu daltonchoice_whereabouts:
                "Choose your path of investigation"

                #Scene 75 - David Dalton - whereabouts - Press further
                "Press Further":
                    
                    #Susan Murphy
                    sm "Especially coupled with yesterday's 20-minute window…"

                    #Narrator
                    "Annoyance at being questioned quickly turns to a wave of quiet anger on Dalton's face."

                    #David Dalton
                    dd "Are you accusing me of murder, detective?"

                    #Susan Murphy
                    sm "No, no! I'm just trying to eliminate possibilities!"

                    #David Dalton
                    dd "Are you sure you're a real detective? It sure seems you're trying to pin it on the butler…"

                    #Susan Murphy Thoughts
                    sm "Wait, could he…? No, that's impossible. Would McQuaid have told him?"

                    #Susan Murphy
                    sm "I assure you that's not the case. I simply want to be sure that I catch the right person."

                    #Narrator
                    "Dalton gives Susan a dark look."

                    #David Dalton
                    dd "Sure, whatever you say, look, my break is about ove-"

                    #Narrator
                    "A scream echoes from the depths of the ship. You turn to Ezekiel, nod, and run toward it."
                    
                    #----------------- End of Convo

                    #Narrator 
                    "Susan and Ezekiel rocket down the hallway."

                    jump fourth


                "Probe for motive":
            
                    #Jump to the scene
                    jump probemotive

            


label probemotive:

    #Susan Murphy
    voice "audio/scene76_N5_sm_1.mp3"
    sm "Before he died, did you notice any changes in behaviour from William?"
    

    #David Dalton
    voice "audio/scene76_N4_dd_1.mp3"
    dd "What do you mean, Ms. Murphy?"
    

    #Susan Murphy
    voice "audio/scene76_N5_sm_2.mp3"
    sm "Anything. Did he seem more blue than usual, or perhaps aggressive? Maybe you had some odd conversation with him. Anything, really."
    

    #David Dalton
    voice "audio/scene76_N4_dd_2.mp3"
    dd "Well… he was asking about our lockers last night. He seemed really bothered about the idea of someone getting into his."
    
    voice "audio/scene76_N4_dd_3.mp3"
    dd "Do we have to worry about a thief, as well as a murderer, on this boat?"
    

    #Susan Murphy
    voice "audio/scene76_N5_sm_3.mp3"
    sm "Hopefully not. We've got enough to deal with."
    

    #Choice during motive

    menu dalton_motive_choice:
        "Proceed with"

        #Scene 77 - David Dalton / Motive - Confortation

        "Asking About confrontation":
            
            #Susan Murphy
            voice "audio/scene77_N5_sm_1.mp3"
            sm "This conversation, did he… accuse you of anything?"
            

            #Narrator
            voice "audio/scene77_N1_1.mp3"
            "Dalton's eyes flick between you and Ezekiel, filled with suspicion."
            

            #David Dalton
            voice "audio/scene77_N4_dd_1.mp3"
            dd "No, he didn't. Did he say something to you? I mean. I wouldn't steal from the kid. If that's what you're asking."
            
            voice "audio/scene77_N4_dd_2.mp3"
            dd "Why? Did he say something?"
            

            #Susan Murphy
            voice "audio/scene77_N5_sm_2.mp3"
            sm "No, it's just-"
            

            #Narrator
            voice "audio/scene77_N1_2.mp3"
            "A scream echoes from the depths of the ship. You turn to Ezekiel, nod, and run toward it."
            

            #----------- End of convo

            "A scream will be heard" 

            #Narrator
            voice "audio/scene77_N1_3.mp3"
            "Susan and Ezekiel rocket down the hallway."
            

            jump fourth

        #Scene 78 - David Dalton / Motive - Confortation

        "Press Further":
            
            #Susan Murphy
            voice "audio/scene78_N5_sm_1.mp3"
            sm "Did William mention being suspicious of anyone in particular during this conversation?"
            

            #David Dalton
            voice "audio/scene78_N4_dd_1.mp3"
            dd "Not as such, but he did seem concerned about the lock he was using. Apparently, the boss gave it to him when he asked about the security of the lockers."
            

            #Ezekiel Jones
            hide susan
            show zeke at left
            voice "audio/scene78_N9_ej_1.mp3"
            ej "What do you mean \"concerned\" ?"
            

            #David Dalton
            voice "audio/scene78_N4_dd_2.mp3"
            dd "I don't really know. He seemed to think that Mr. McQuaid might have a copy of the key, but what he'd want in William's locker…"
            
            voice "audio/scene78_N4_dd_3.mp3"
            dd "Wait, weren't the two of you asking about shoes yesterday? Something about a shoeprint? Was William the murderer?"
            

            #Ezekiel Jones
            voice "audio/scene78_N9_ej_2.mp3"
            ej "Unlikely, since he's kicked the bucket."
            

            #David Dalton
            voice "audio/scene78_N4_dd_4.mp3"
            dd "Maybe there was only one murder he wanted to commit. Couldn\'t he have?"
            

            #Narrator
            voice "audio/scene78_N1_1.mp3"
            "You interrupt Dalton."
            

            #Susan Murphy
            hide zeke
            show susan at left
            voice "audio/scene78_N5_sm_2.mp3"
            sm "He wasn't the killer, Dalton. There's too much evidence that conflicts with that."
            

            #David Dalton
            voice "audio/scene78_N4_dd_5.mp3"
            dd "Alright, but maybe it was Mr. McQuaid? After all, he gave William the lock and invited you all here to blackmail you."
            

            #Ezekiel Jones
            voice "audio/scene78_N9_ej_3.mp3"
            ej "That's unlikely. He was with everyone else at the time of the first murder."
            

            #Susan Murphy
            voice "audio/scene78_N5_sm_3.mp3"
            sm "As Ezekiel says, it's unlikely that-"
            

            #Narrator
            voice "audio/scene78_N1_2.mp3"
            "A scream echoes from the depths of the ship. You turn to Ezekiel, nod, and run toward it."
            hide susan 
            hide zeke
            hide david

            #----------------- End of Convo

            #Narrator 
            voice "audio/scene78_N1_3.mp3"
            "Susan and Ezekiel rocket down the hallway."
            

            jump fourth

label fourth:

    #Scene 79 - The scream

    #Narrator 
    voice "audio/scene79_N1_1.mp3"
    "They let themselves into the Neptune's finely appointed washroom, and find the hunchedformofDeborah White, crying over the newly deceased Patricia White."
    

    #Ezekiel Jones
    show zeke
    voice "audio/scene79_N9_ej_1.mp3"
    ej "Oh, Patty…"
    

    #Susan Murphy
    hide zeke 
    show susan
    voice "audio/scene79_N5_sm_1.mp3"
    sm "Deborah, what happened here?"
    

    #Deborah White
    susan at left
    show deborah at right
    voice "audio/scene79_N12_dw_1.mp3"
    dw "I couldn't find Patty anywhere, and I looked around the boat all day for her."
    

    #Narrator
    voice "audio/scene79_N1_2.mp3"
    "Deborah's words start to slur together as her panic lends speed to her mouth. By the time she becomes intelligible again, all she says is:"
    

    #Deborah White
    voice "audio/scene79_N12_dw_2.mp3"
    dw "And now she's dead!"
    

    #Susan Murphy
    voice "audio/scene79_N5_sm_2.mp3"
    sm "It'll be alright, Deborah. I'll catch the one who did this. Ezekiel, could you…"
    

    #Ezekiel Jones
    hide susan
    show zeke
    voice "audio/scene79_N9_ej_2.mp3"
    ej "Of course. Debbie, please, come with me."
    

    #Narrator
    voice "audio/scene79_N1_3.mp3"
    "Ezekiel leads the weeping White sister out of the bathroom, leaving Susan alone with a finely dressed corpse."
    

    #Susan Murphy Thoughts
    hide zeke
    hide deborah
    show susan
    voice "audio/scene79_N5_sm_3.mp3"
    sm "Well, time to get to work."
    
    #Narrator
    "While looking at a crime scene, click on points of interest around the area to find clues."

    #Entering the 3rd Crime Scene

    #Scene 80 - 3rd Murder in the bathroom 

    call screen patriciascene_investigation


label thirdmurder:

    #Scene 81 - Murder Scene 

    #Susan Murphy
    show susan
    voice "audio/scene81_N5_sm_1.mp3" 
    sm "Not much to go by. I need some rest, and we can reconvene tomorrow morning."
    hide susan
    

    #------------------------- End of day 3

    #------------------------- Start of day 4

    scene day 4

    "Day 4"

    #Scene 82 - Susan's Cabin

    #Narrator
    #voice "audio/scene82_N1_1.mp3"
    "Susan awakes in her room, feeling blissfully well rested for a moment, before remembering the situation she's in."
    

    #Susan Murphy Thoughts
    #voice "audio/scene82_N3_smt_1.mp3"
    sm "God, we need to catch this maniac. There aren't that many of us left."
    
    #voice "audio/scene82_N3_smt_2.mp3"
    sm "Okay, think, what do I know? The killer finds Richard in his suite and beats him, to death, with his wife's cane, apparently wearing William's shoes."
    

    #Susan Murphy
    #voice "audio/scene82_N5_sm_1.mp3"
    sm "So they're smart enough to cover his tracks, to confuse whoever investigates. Clearly, whoever did it wanted us to think it was one of those two."
    
    #voice "audio/scene82_N5_sm_2.mp3"
    sm "Then the next day, William is murdered after we ask about his shoes and cause him to panic. Maybe he asked around and stumbled upon the real killer."
    
    #voice "audio/scene82_N5_sm_3.mp3"
    sm "So he ends up dead… in the kitchen. Who else would have been in the kitchen with William?"
    
    #voice "audio/scene82_N5_sm_4.mp3"
    sm "And the next day, poor Patty ends up dead in the bathroom, strangled by a left-handed man."
    
    #voice "audio/scene82_N5_sm_5.mp3"
    sm "Left-handed man… in the kitchen."
    
    #voice "audio/scene82_N5_sm_6.mp3"
    sm "That's it I have figured out! I know who it is!"
    
    #voice "audio/scene82_N5_sm_7.mp3"
    sm "I need to call everyone to the dining hall!"
    

    #To the Dining Hall

    scene hallway

    "Navigating to the dining hall"

    #Scene 83- The Dining Hall

    #Narrator
    #voice "audio/scene83_N1_1.mp3"
    "After calling everyone to the dining hall Susan starts explaining why everyone is in the room."
    

    #Susan Murphy
    #voice "audio/scene83_N5_sm_1.mp3"
    sm "I have figured out who the Murderer is."
    

    #Narrator
    #voice "audio/scene83_N1_2.mp3" 
    "The entire dining hall became silent soon with whispers and murmurs filling the area."
    

    #Susan Murphy
    #voice "audio/scene83_N5_sm_2.mp3"
    sm "But first, McQuaid, I have a question."
    

    #Michael McQuaid
    #voice "audio/scene83_N2_mm_1.mp3"
    mm "What, another? Surely you have everything you need, Ms. Murphy if you know who the killer is."
    

    #Susan Murphy
    #voice "audio/scene83_N5_sm_3.mp3"
    sm "Indulge me. You brought us here. You owe us that much."
    

    #Michael McQuaid
    #voice "audio/scene83_N2_mm_2.mp3"
    mm "Fine, ask your question."
    

    #Susan Murphy
    #voice "audio/scene83_N5_sm_4.mp3"
    sm "Why?"
    

    #Michael McQuaid
    #voice "audio/scene83_N2_mm_3.mp3"
    mm "Excuse me, detective?"
    

    #Susan Murphy
    #voice "audio/scene83_N5_sm_5.mp3"
    sm "Why invite us here at all? Other than blackmail, I mean. You could have asked us to your home or just sent letters, for God's sake!"
    
    #voice "audio/scene83_N5_sm_6.mp3"
    sm "So why invite us here? Hell, I'm just a detective. Why invite me?"
    

    #Michael McQuaid
    #voice "audio/scene83_N2_mm_4.mp3"
    mm "You want to know why Murphy? The great detective can't figure it out? Fine. I'll tell you why."
    
    #voice "audio/scene83_N2_mm_5.mp3"
    mm "Each of you is here for a different reason. I invited Richard and Rachel simply because that Reed Industries is a direct competitor, and I want it gone."
    
    #voice "audio/scene83_N2_mm_6.mp3"
    mm "The Whites, on the other hand, are a little bit more complicated. They're rich, yes, but they're also well-connected. Deborah knows people, knows how to get what she wants."
    
    #voice "audio/scene83_N2_mm_7.mp3"
    mm "And Patty, well, she had her own connections of a more intimate nature."
    
    #voice "audio/scene83_N2_mm_8.mp3"
    mm  "The good doctor? He's performed certain procedures at my behest that I wouldn't want to be known to the public."
    
    #voice "audio/scene83_N2_mm_9.mp3"
    mm "And then there's you. Tell me, lady Holmes, how did you first meet me?"
    

    #Susan Murphy
    #voice "audio/scene83_N5_sm_7.mp3"
    sm "You hired me. You hired me to find a corporate spy who had stolen some important documents."
    

    #Michael McQuaid
    #voice "audio/scene83_N2_mm_10.mp3"
    mm "I-"
    

    #Narrator
    #voice "audio/scene83_N1_3.mp3"
    "McQuaid gives Susan a long, hard look. After a moment, he rests his head in his hands."
    

    #Michael McQuaid
    #voice "audio/scene83_N2_mm_11.mp3"
    mm "You don't know?"
    

    #Susan Murphy
    #voice "audio/scene83_N5_sm_8.mp3"
    sm "What don't I know, McQuaid?"
    

    #Michael McQuaid
    #voice "audio/scene83_N2_mm_12.mp3"
    mm "And here I thought you were one of the great detectives. He wasn't a corporate spy!"
    
    #voice "audio/scene83_N2_mm_13.mp3"
    mm "He was a federal agent. And those documents? Some damning evidence. I thought you knew! I thought that you'd take me down any day now!"
    
    #voice "audio/scene83_N2_mm_14.mp3"
    mm "That's why I invited you along, detective. I thought you were actually good at your job. But, unfortunately, it seems I was mistaken."
    
    #voice "audio/scene83_N2_mm_15.mp3"
    mm "And I went through all the trouble of finding blackmail for you too. Now tell us, little miss detective, who's the killer?"
    

    menu killer_choice:

        "Choose the killer"

        "David Dalton":
            
            #Scene 84 - David dalton Killer

            #Susan Murphy
            #voice "audio/scene84_N5_sm_1.mp3"
            sm "David Dalton, of course. David Dalton, who was mysteriously absent for 20 minutes around thetime of Richard's murder."
            
            #voice "audio/scene84_N5_sm_2.mp3"
            sm "David Dalton, who would have been a normal sight in the kitchen for William. David Dalton, who served drinks with his left hand."
            

            #Narrator
            #voice "audio/scene84_N5_sm_1.mp3"
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            

            #David Dalton 
            #voice "audio/scene84_N4_dd_1.mp3"
            dd "Very clever, a regular Sherlock we have in our midsts. It's too bad that all of that deductive power will end up at the bottom of the ocean."
            

            #Michael McQuaid
            #voice "audio/scene84_N2_mm_1.mp3"
            mm "Dalton? What are you saying?"
            

            #David Dalton 
            #voice "audio/scene84_N4_dd_2.mp3"
            dd "I've put a bomb on the boat, 'boss.' If I can't have the satisfaction of killing you all with my bare hands, then this will have to do."
            

            #Michael McQuaid
            #voice "audio/scene84_N2_mm_2.mp3"
            mm "What? That wasn't the deal! You were supposed to get rid of them, not me!"
            

            #David Dalton
            #voice "audio/scene84_N4_dd_3.mp3" 
            dd "Did you really think you were exempt, McQuaid? You. All of you have made my life a living hell!"
            

            #Ezekeil Jones
            #voice "audio/scene84_N9_ej_1.mp3"
            ej "What the hell are you talking about? I've never even met you before!"
            

            #David Dalton 
            #voice "audio/scene84_N4_dd_4.mp3"
            dd "Oh sure, you haven't. Of course, you and your rich friends haven't been laughing behind my back while I suffered!"
            
            #voice "audio/scene84_N4_dd_5.mp3"
            dd "I was supposed to have the life that all of you have! I worked hard, and I earned it! Instead, you all just lied, cheated your way through, and then ensured that I couldn't follow!"
            
            #voice "audio/scene84_N4_dd_6.mp3"
            dd "I waited for this for years! And finally, finally, I have my chance! Did you really think I'd leave you alive, McQuaid? After everything you did to me?"
            
            #voice "audio/scene84_N4_dd_7.mp3"
            dd "And now it's ruined! Ruined by a fake detective!"
            

            #Susan Murphy Thoughts
            #voice "audio/scene84_N3_smt_1.mp3"
            sm "Damn."
            

            #Narrator
            #voice "audio/scene84_N5_sm_2.mp3"
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            

            #David Dalton
            #voice "audio/scene84_N4_dd_8.mp3" 
            dd "That's right, the woman you all trusted with your lives didn't earn her position! Just like all of you, she cheated her way to the top!"
            

            jump finale

        "Michael Mcquiad":
            
            #Scene 85 - Michael Killer

            #Susan Murphy 
            #voice "audio/scene85_N5_sm_1.mp3"
            sm "Why, it’s Michael McQuaid, of course!"
            

            #Narrator
            #voice "audio/scene85_N1_1.mp3"
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            

            #David Dalton 
            #voice "audio/scene85_N4_dd_1.mp3"
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            

            #Susan Murphy Thoughts
            #voice "audio/scene85_N3_smt_1.mp3"
            sm "Damn."
            

            #Narrator
            #voice "audio/scene85_N1_2.mp3"
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            

            #David Dalton
            #voice "audio/scene85_N4_dd_2.mp3" 
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            

            #Michael McQuaid
            #voice "audio/scene85_N2_mm_1.mp3"
            mm "Dalton? What's the meaning of this?"
            

            #David Dalton
            #voice "audio/scene85_N4_dd_3.mp3" 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            
            #voice "audio/scene85_N4_dd_4.mp3"
            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            

            jump finale

        "Ezekiel Jones":
            
            #Scene 86 - Ezekiel Killer

            #Susan Murphy
            #voice "audio/scene86_N5_sm_1.mp3" 
            sm "Why, it’s Ezekiel Jones, of course!"
            

            #Narrator
            #voice "audio/scene86_N1_1.mp3"
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            

            #David Dalton 
            #voice "audio/scene86_N4_dd_1.mp3"
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            

            #Susan Murphy Thoughts
            #voice "audio/scene86_N3_smt_1.mp3"
            sm "Damn."
            

            #Narrator
            #voice "audio/scene86_N1_2.mp3"
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            

            #David Dalton
            #voice "audio/scene86_N4_dd_2.mp3" 
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            

            #Michael McQuaid
            #voice "audio/scene86_N2_mm_1.mp3"
            mm "Dalton? What's the meaning of this?"
            

            #David Dalton
            #voice "audio/scene86_N4_dd_3.mp3" 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            
            #voice "audio/scene86_N4_dd_4.mp3"
            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            

            jump finale

        "Deborah White":
            
            #Scene 87 - Deborah Killer
            
            #Susan Murphy 
            #voice "audio/scene87_N5_sm_1.mp3"
            sm "Why, it’s Deborah White, of course!"
            

            #Narrator
            #voice "audio/scene_N1_1.mp3"
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            

            #David Dalton 
            #voice "audio/scene87_N4_dd_1.mp3"
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            

            #Susan Murphy Thoughts
            #voice "audio/scene87_N3_smt_1.mp3"
            sm "Damn."
            

            #Narrator
            #voice "audio/scene_N1_2.mp3"
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            

            #David Dalton 
            #voice "audio/scene87_N4_dd_2.mp3"
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            

            #Michael McQuaid
            #voice "audio/scene87_N2_mm_1.mp3"
            mm "Dalton? What's the meaning of this?"
            

            #David Dalton
            #voice "audio/scene87_N4_dd_3.mp3" 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            
            #voice "audio/scene87_N4_dd_4.mp3"
            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            

            jump finale

        "Rachel Reed":
            
            #Scene 88 - Rachel Reed
            
            #Susan Murphy 
            #voice "audio/scene88_N5_sm_1.mp3"
            sm "Why, it’s Rachel Reed, of course!"
            

            #Narrator
            #voice "audio/scene88_N1_1.mp3"
            "As Susan makes her damning accusation, the intercom, silent until now, squawks to life."
            

            #David Dalton 
            #voice "audio/scene88_N4_dd_1.mp3"
            dd "Far be it from me to correct the professional, but I'm afraid you're wrong, Murphy. Then again, what else could we expect from a fake detective."
            

            #Susan Murphy Thoughts
            #voice "audio/scene88_N5_sm_2.mp3"
            sm "Damn."
            

            #Narrator
            #voice "audio/scene88_N1_2.mp3"
            "At Dalton's words, the assembled crowd gasps. All except for McQuaid. The man who discovered Susan's dirty little secret."
            

            #David Dalton
            #voice "audio/scene88_N4_dd_2.mp3" 
            dd "That's right, you all put your trust in someone who had to cheat her way into becoming a detective! Of course, it doesn't matter now since soon you'll all be dead!"
            

            #Michael McQuaid
            #voice "audio/scene88_N2_mm_1.mp3"
            mm "Dalton? What's the meaning of this?"
            

            #David Dalton
            #voice "audio/scene88_N4_dd_3.mp3" 
            dd "Could you really be that stupid? Did you think I'd stick to our deal? After all, you put me through, conspiring with the rest?"
            
            #voice "audio/scene88_N4_dd_4.mp3"
            dd "Soon, you'll all be at the bottom of the ocean where you belong, and I will have my revenge!"
            

            jump finale


label finale:

    #Scene 89 - Killer cont

    scene dininghall

    #Susan Murphy 
    #voice "audio/scene89_N5_sm_1.mp3"
    sm "And there's the question we've all been asking. The motive. Every person on this boat has been laughing at you, Dalton? The first time I met you was three days ago!"
    

    #David Dalton
    #voice "audio/scene89_N4_dd_1.mp3" 
    dd " Liar! You cheated your way to the top, just like them! And now, you'll all find yourselves at the bottom of the ocean!"
    
    #voice "audio/scene89_N4_dd_2.mp3"
    dd "Finally, I will have my revenge!"
    

    #Narrator
    #voice "audio/scene89_N1_1.mp3"
    "With that, the intercom dies."
    

    #Susan Murphy
    #voice "audio/scene89_N5_sm_2.mp3" 
    sm "Ezekiel, Deborah, Rachel, had any of you ever heard of Dalton before this trip?"
    

    #Ezekiel Jones
    #voice "audio/scene89_N9_ej_1.mp3"
    ej "He might have come to my practice once or twice, years ago, but I'm not sure."
    

    #Deborah White
    #voice "audio/scene89_N12_dw_1.mp3"
    dw "Never. I would have remembered him."
    

    #Rachel Reed
    #voice "audio/scene89_N11_rar_1.mp3"
    "Not as far as I can remember. Richard might have known him, though."
    

    #Susan Murphy 
    #voice "audio/scene89_N5_sm_3.mp3"
    sm "Alright, so he's crazy. If you wanted to sink a ship, where would you put a bomb?"
    

    #Ezekiel Jones
    #zvoice "audio/scene89_N9_ej_2.mp3"
    "Either the hold or the engine room. I doubt we have the time to visit both."
    

    #Michael McQuaid
    #voice "audio/scene89_N2_mm_1.mp3"
    mm "I, er, have an elegant solution to that one. The boat's hold and engine room are the same place. Just take the stairs at the end of the hall."
    

    #Susan Murphy
    #voice "audio/scene89_N5_sm_4.mp3" 
    sm "All right. Ezekiel, follow me."
    

    #Scene 90 - The Bomb

    scene bomblocation

    #Narrator
    #voice "audio/scene90_N1_1.mp3"
    "Susan and Ezekiel sprint down the hall and practically fly down the stairs into the hold, where they discover a bomb strapped to the engine."
    

    #Susan Murphy
    #voice "audio/scene90_N5_sm_1.mp3" 
    sm "There it is!"
    

    #Narrator
    #voice "audio/scene90_N1_1.mp3"
    "Ezekiel examines the bomb closely, flinching as it ticks."
    

    #Scene 91 - The password

    scene holdingbomb

    #Ezekiel Jones
    #voice "audio/scene91_N9_ej_1.mp3"
    ej "We must be able to defuse it. See those three lights? It looks like we have three choices."
    

    #Susan Murphy 
    #voice "audio/scene91_N5_sm_1.mp3"
    sm "Come on, think! What would Dalton make the password? How are we supposed to know this?"
    

    #Ezekiel Jones
    #voice "audio/scene91_N9_ej_2.mp3"
    ej "He must have given us a hint in that long winded speech of his."
    

    #Susan Murphy 
    sm "The password must be his motive… hmm."

    menu defuse_bomb:

        "Choose Wisely"

        "Avenge":
           
            #Scene 92 - Explosion

            #Susan Murphy 
            #voice "audio/scene92_N5_sm_1.mp3"
            sm "No, wait-"
            

            #Narrator
            #voice "audio/scene92_N1_1.mp3"
            "An explosion rips through the Neptune, a roaring inferno over the water. Many on the boat are killed outright, while others…"
            

            #Narrator
            #voice "audio/scene92_N1_2.mp3"
            "Others are drowned, caught in Neptune's Net."
            

            #Narrator
            #voice "audio/scene92_N1_3.mp3"
            "With them died the knowledge of what happened on this five-day cruise and any evidence that the passengers were anything less than upstanding members of the community."
            

            scene game_over

            "Game over"

            return


        "Revenge":
            
            #Scene 93 - Accepted

            scene passwordaccepted

            #Susan Murphy 
            #voice "audio/scene93_N5_sm_1.mp3"
            sm "That's it! Now, to find Dalton. Ezekiel, you stay here. Grab him if he comes back."
            

            #Ezekiel Jones
            #voice "audio/scene93_N9_ej_1.mp3"
            ej "Right."
            

            #Scene 94 - The hallway 

            scene hallway 

            #Narrator
            #voice "audio/scene94_N1_1.mp3"
            "Susan dashes off, finding herself in the hallway."
            

            #Susan Murphy
            #voice "audio/scene94_N5_sm_1.mp3" 
            sm "Where would he be? He was on the intercom earlier. What rooms would have a microphone for the intercom."
            

            #Susan Murphy 
            #voice "audio/scene94_N5_sm_2.mp3"
            sm "The helm. He must be at the helm."
            

            #Scene 95 - the helm

            scene helm

            #Narrator
            #voice "audio/scene95_N1_1.mp3" 
            "Susan makes her way to the ship's helm, stepping cautiously inside."
            

            #David Dalton
            #voice "audio/scene95_N4_dd_1.mp3" 
            dd "You're too late, Ms. Holmes. The boat will explode, taking us to the bottom, where you all belong!"
            

            #Susan Murphy 
            #voice "audio/scene95_N5_sm_1.mp3"
            sm "I'm afraid that's incorrect, Dalton. We've already defused the bomb. Come quietly, and this can all be over."
            

            #David Dalton 
            #voice "audio/scene95_N4_dd_2.mp3"
            dd "Why should I? You all laughed at me! Even if I'm not sent to the chair, you all will make sure that I never get another job!"
            
            #voice "audio/scene95_N4_dd_3.mp3"
            dd "You've all conspired against me. Why should I trust your word now?"
            

            #Susan Murphy
            #voice "audio/scene95_N5_sm_2.mp3" 
            sm "There was never a conspiracy, Dalton. McQuaid's used you, pinned your failure on us."
            

            #David Dalton 
            #voice "audio/scene95_N4_dd_4.mp3"
            dd "No! You're lying! Just like you lied about being a detective, I can't trust anything you say! If my bomb doesn't do it, I'll kill you myself. "
            

            #Narrator
            #voice "audio/scene95_N1_1.mp3"
            "Dalton lunges for Susan, but before he can act, Susan has her gun drawn and aimed."
            

            #Susan Murphy 
            #voice "audio/scene95_N5_sm_3.mp3"
            sm "Is this worth your life, Dalton? Now come quietly. Please, I don't want to hurt you. Just come with me."
            

            #Narrator 
            #voice "audio/scene95_N1_2.mp3"
            "Dalton hesitates for a moment."
            

            #David Dalton
            #voice "audio/scene95_N4_dd_5.mp3" 
            dd "You know if you arrest me, I will reveal all your dirty little secrets. Even if I can't kill you, I'll ruin you."
            

            #Susan Murphy 
            #voice "audio/scene95_N5_sm_4.mp3"
            sm "As attempts to make me drop my guard, that one's weak. Now come with me."
            

            #Narrator 
            #voice "audio/scene95_N1_3.mp3"
            "Susan escorts her captive to the dining hall."
            

            #Scene 96 - Ending | Dining Hall

            scene dininghall

            #Susan Murphy
            #voice "audio/scene96_N5_sm_1.mp3" 
            sm "And here we have him, ladies and gentlemen. Our killer. One of you, go get Ezekiel from the hold."
            

            #Narrator
            #voice "audio/scene96_N1_1.mp3"
            "Deborah nods and leaves to get Ezekiel."
            

            #Michael McQuaid
            #voice "audio/scene96_N2_mm_1.mp3"
            mm "You little traitor! After everything I've done for you, you start killing my guests! Why I should-"
            

            #Susan Murphy 
            #voice "audio/scene96_N5_sm_2.mp3"
            sm "Hold it right there, McQuaid. I seem to remember you mentioning a deal with Dalton here. What might the terms of that deal be?"
            

            #Narrator 
            #voice "audio/scene96_N1_2.mp3"
            "Michael becomes pale."
            

            #David Dalton 
            #voice "audio/scene96_N4_dd_1.mp3"
            dd "I can tell you exactly what that deal was. Blackmail wasn't enough for you, eh McQuaid? No, you wanted them gone."
            
            #voice "audio/scene96_N4_dd_2.mp3"
            dd "So he found me with my vendetta, a perfect patsy! The deal, Murphy, was for me to kill you, and then he would protect me from the authorities."
            
            #voice "audio/scene96_N4_dd_3.mp3"
            dd "Brave enough to order a death, but not enough to do it himself."
            

            #Narrator
            #voice "audio/scene96_N1_3.mp3"
            "Ezekiel walks in with Deborah."
            

            #Ezekiel Jones
            #voice "audio/scene96_N9_ej_1.mp3"
            ej "Ah, I see you've found him. What shall we do with him?"
            

            #Susan Murphy 
            #voice "audio/scene96_N5_sm_3.mp3"
            sm "Is there anywhere on the ship that can be locked from the outside?"
            

            #Ezekiel Jones
            #voice "audio/scene96_N9_ej_2.mp3"
            ej "There were a couple of doors leading out from the hold that seemed to have locks."
            

            #Susan Murphy 
            #voice "audio/scene96_N5_sm_4.mp3"
            sm "Those'll do. Put him in one and our illustrious host in the other. Then when we get back to Honolulu, we can hand them over to the authorities."
            

            #Ezekiel Jones
            #voice "audio/scene96_N9_ej_3.mp3"
            ej "Alright. I'll keep an eye on them, just in case."
            

            #Scene 97 - THE END

            scene theend

            #Narrator
            #voice "audio/scene97_N1_1.mp3"
            "The two culprits were put in their makeshift cells while a course was charted back to the harbour. After a nerve-wracking day, they finally returned."
            
            #voice "audio/scene97_N1_2.mp3"
            "Michael McQuaid and David Dalton were handed over to the authorities. Before the trial, secrets were spilled, and lives ruined."
            
            #voice "audio/scene97_N1_3.mp3"
            "They may have escaped Neptune's Net, but the lives of those on board would never be the same again."
            

            return 


        "Change":

            #Scene 92 - Explosion

            #Susan Murphy 
            #voice "audio/scene92_N5_sm_1.mp3"
            sm "No, wait-"
            

            #Narrator
            #voice "audio/scene92_N1_1.mp3"
            "An explosion rips through the Neptune, a roaring inferno over the water. Many on the boat are killed outright, while others…"
            

            #Narrator
            #voice "audio/scene92_N1_2.mp3"
            "Others are drowned, caught in Neptune's Net."
            

            #Narrator
            #voice "audio/scene92_N1_3.mp3"
            "With them died the knowledge of what happened on this five-day cruise and any evidence that the passengers were anything less than upstanding members of the community."
            

            scene game_over

            "Game over"

            return
        









    return