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
    scene apartment 
    #Susan's Apartment from door with mail slot (background)
    # Narrator voice
    voice "audio/narrator/n01.mp3"
    "Coming home from her latest case, Susan Murphy, private eye, opens the door to her apartment."

    # Scene 2 - inside Susan’s front door, mail on the floor 

    #scene Bg
    scene inside apartment
    #Inside Susan Apartment Mail on floor

    # Narrator voice
    voice "audio/narrator/n02.mp3"
    "Stepping inside, glancing down, she sees the expected bills and magazines slipped through the mail slot onto the floor."

    # Narrator voice

    "Among the pile is an ornate envelope, with an equally ornate invitation inside."

    # Scene 3 - Envelope 

    #Scene Bg - an image of the envelope and invitation with text on them
    scene envelope inside #The invitation 

    #voice of mcquaid
    #do we need this as text or would a graphic be enough?

    "Dear Susan Murphy, you have been cordially invited as a distinguished guest to ring in 1952 in style aboard the USS Neptune. We will be departing at 6:00 P.M. December 30th from Honolulu Harbour, and returning to the same location on January 3rd. I hope to see you there! - Michael McQuaid"

    # Susan thought voice 

    sm "McQuaid, McQuaid, where have I heard that name before? Oh right, I did a case for him. Well, I could use a vacation after today…Sure, why the heck not!"

    # Scene 4 - Yatch
    #Scene Bg - an image of the yacht on the water
    scene yatchonwater

    #Narrator Voice

    "A couple of weeks later, Susan readies to board the Neptune, admiring the lavish yacht."

    # Scene 5 - Susan Cabin
    #scene bg - Inside Susan Cabin
    #scene susan cabin

    #Narrator voice

    "As Susan sorts through her luggage, there is a knock at the door."

    #dalton Voice

    dd "There will be a dinner for all the guests in the dining hall in 30 minutes."

    #play sound susan cabin - Susan Voice
    sm "Okay, thanks for the information."

    #play sound susan cabin thought
    #thoughts screen maybe ( displaying that susan is thinking)
    sm " Okay, time for me to get dolled up for dinner. I hope the food is going to be good."


    #choice scene
    #The player is given the ability to navigate the boat and makes their way to the dining room.

    #Scene Navigation 





    #Scene Bg - Navigation Option screen


    #Scene 6 

    #scene dining room 

    #Narrator Voice

    "Susan enters the dining room and sees a well-dressed crowd sitting around the room at different tables."
    
    #play sound/music with fade in here not voice
    #Michael speaking as the player enters the room

    mm "Ah, and here’s our final guest arriving! Welcome, Susan. Please, take a seat. Now that we’re all here, the party can start!"

    mm "I know some of you are already acquainted with each other, but to help break the ice, why don’t we have a few introductions?"

    mm "First, we have Mr. Richard Reed, the CEO of Reed Industries, and his wife, Mrs. Rachel Reed."

    mm "Next, we have the illustrious Dr. Ezekiel Jones. The man’s service to our country and his patients' lives speaks for itself."

    mm "Then, We have the White sisters, Deborah and Patricia. True yin and yang if I’ve ever seen one."

    mm"Of course, the brilliant Susan Murphy, one of the great detectives of our time."
    
    mm "And finally, our talented captain, Lloyd Lewis! He’ll be navigating the boat for the next five days, so don’t expect to see much of him away from the helm"

    
    #Narrator voice of LLoyd Lewis
    ll "That’s my cue. Back to the helm, I go. Have a good meal, folks"

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

    #Susan Murphy Voice
    sm "A pleasure to make your acquaintance. Well, Zeke, I think I’ll go mingle a bit. See you around."

    #Narrator Voice
    "Susan gets up and wanders the dining room. She comes to a table with three elegantly dressed women where Richard had been sitting"

    #Scene switch tables

    #Patricia White Voice
    pw "Susan gets up and wanders the dining room. She comes to a table with three elegantly dressed women where Richard had been sitting."

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

    #Narator / Rachel
    #rar is for rachel for narator just remove rar
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

    #Scene 8 
    #scene hallway

    #narrator voice
    "Susan leaves the room in search of Rachel. She is now in the Hallway."    

    #Susan Murphy
    sm "She said she was feeling sick. I should probably go and check the washroom."

    #Scene 9
    #Navigating to the washroom

    #scene navigatingtowashroom

    #Narator Voice
    "Susan enters the washroom but finds no one."

    #Susan Murphy Voice
    sm "Drat, she’s not here. Where else would she be… their cabin!"

    #The player navigates to the Reed’s cabin, the door is slightly ajar

    #Scene 10
    #scene reedscabin

    #narrator Voice
    "As Susan opens the door, she is met with a horrific sight. Richard Reed, former CEO of Reed Industries, has been beaten bloody, and unmoving."

    #Susan Murphy Voice
    sm "Oh Shit. Is that Richard? Oh my God, I need to tell everyone about this."

    #Goes back to the dining room

    #scene diningroom

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




    return
