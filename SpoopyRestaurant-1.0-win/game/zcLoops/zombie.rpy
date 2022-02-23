
label Zombie_Interaction1:
    "First Interaction"

    menu:
        "Good option":
            "Huh, it worked"
            $ stars += 1
            jump Zombie_Interaction2
        "Bad option":
            "Nopr nope"
            jump Zombie_Interaction2


label Zombie_Interaction2:
    "Second Interaction"
    menu:
        "Good option":
            "Huh, it worked"
            $ stars += 1
            jump Zombie_Interaction3
        "Bad option":
            "Nopr nope"
            jump Zombie_Interaction3


label Zombie_Interaction3:
    "Third Interaction"
    menu:
        "Good option":
            "Huh, it worked"
            $ stars += 1
            jump cooking_zombie
        "Bad option":
            "Nopr nope"
            jump cooking_zombie



label main_cooking_loop:

    menu:
        "Make a Smart Smoothie":
            if  Toe_current == True:
                $ Toe_happy = True
                $ stars += 1

            s "A Smart Smoothie huh.. let's see if I guessed correctly!"
            s "Let's see... to make this item I gotta.... Right! I gotta make sure to press the blender and wait a bit till it's ready!"
            call screen blend

        "Make a Gory Gonut":
            if  Muck_current == True:
                $ Muck_happy = True
                $ stars += 1
            s "A Gory Gonut huh... quite the sweet treat! Let's see if I guessed correctly"
            s "Now... to make a Gory Gonut. If I remember correctly, i just gotta press and squeeze in the jelly a few times before it's all puffed up!"

            call screen clicker01


        "Make a Brain Burger":
            if Kedrick_current == True:
                $ Kedrick_happy = True
                $ stars += 1

            if Hammy_current == True:
                $ Hammy_happy = True
                $ stars += 1

            "Ah the classical Brain Burger, let's see... Gotta drag it on the pan, watch it cook to drag it back on the plate!"
            call screen raw_brain

            show brain:
                xalign 0.05 yalign 0.6
            play sound "flames.mp3"
            pause 2.0
            stop sound
            hide brain
            show burger:
                xalign 0.05 yalign 0.6
            pause 1.0
            "Ah the sweet sweet smell of brain burger. Let's set this beauty on a plate. "

            hide burger
            call screen prep_brain

            show burger:
                xalign 0.6 yalign 0.6

            s "Well what am I waiting for! Let's ring the bell by the plates to call the customer back."
            hide burger
            call screen bell





label clicker_2:
    call screen clicker02

label clicker_3:
    call screen clicker03

label clicker_4:
    show doughnut:
        xalign 0.6 yalign 0.6
    stop sound 
    s "Well what am I waiting for! Let's ring the bell by the plates to call the customer back."
    hide doughnut
    call screen bell

label blending_ani:

    show brain:
        xalign 0.05 yalign 0.3
    pause 2.0
    stop sound
    hide brain
    show smoothie:
        xalign 0.05 yalign 0.3
    "And just like that... one super Smart Smoothie!"
    hide smoothie
    show smoothie:
        xalign 0.6 yalign 0.46
    s "Well what am I waiting for! Let's ring the bell by the plates to hand the meal to the customer."
    hide smoothie
    call screen bell

label orders:
    if Toe_current == True:
        jump toe_ending
    else:
        pass

    if Muck_current == True:
        jump muck_ending
    else:
        pass

    if Kedrick_current == True:
        jump ked_ending
    else:
        pass

    if Hammy_current == True:
        jump ham_ending

label toe_ending:
    if Toe_happy == True:
        t "Wow, a Smart Smoothie! Do you read minds Spoopy?"
        show rest
        $ Toe_current = False
        jump Muck1
    else:
        t "Not quite what I wanted, but thanks anyways! Off I go again!"
        show rest
        $ Toe_current = False
        jump Muck1

label muck_ending:
    if Muck_happy == True:
        m "YES! That is exactly what I wanted and needed."
        m "This was the highlight of my day and truly washed away all of my sadness!"
        m "You are the best, I’ll make sure to come and visit again, thank you for everything!"
        show rest
        $ Muck_current = False
        jump Ked1
    else:
        m "Oh…, not quite but thanks anyways! "
        show rest
        $ Muck_current = False
        jump Ked1

label ked_ending:
    if Kedrick_happy == True:
        k "Awe thanks dude! This place is pretty snazzy, we’ll be sure to swing back around if we’re still hungry for seconds. "
        show rest
        $ Kedrick_current = False
        jump Ham1
    else:
        k "Man…not quite right, but heck if I’m gonna let food go to waste."
        show rest
        $ Kedrick_current = False
        jump Ham1

label ham_ending:
    if Hammy_happy == True:
        h "Oh yes this is right, wow you are a genius. Enjoy your meal too! AH! Never mind that last part!"
        show rest
        $ Hammy_current = False
        jump final_ratings
    else:
        h "This um this… I’m sorry, I must be remembering my order wrong, so sorry… I must be on my way now, toodles!"
        show rest
        $ Hammy_current = False
        jump final_ratings
