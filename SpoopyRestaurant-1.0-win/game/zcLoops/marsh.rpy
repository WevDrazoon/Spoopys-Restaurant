label Muck1:
    $ Muck_current = True

    s "Next customer please!"
    show rest second
    m "..."
    m "Hi…"
    s "Oh welcome! You seem a little down is something wrong ma’am?"
    m "Meh, had a hard day today..."
    m "Another slippery human tripped over my mud trail again."
    s "Those pesky humans! They never learn respect, sorry that happened seems like it really affected you."
    m "Not really, I’m just usually very monotonous so this is my normal tone, my apologies."

    menu:
        "No need to apologize":
            s "No need to be sorry! It’ll pass, but it’s alright to be sad in the moment!"
            m "Aww shucks..."
            m "Thanks for being so considerate! "
            $ stars += 1
            jump Muck2
        "Smile through it!":
            s "No need to be sorry! Smiles work for me; you should try it!"
            m "Meh, I guess so.."
            m "Thanks for the advice..."
            jump Muck2


label Muck2:
    m "Will definitely take note of that for future Muck. I wish I can just control my emotions…"
    menu:
        "All you need is... this quote I will give":
            s "One quote I always like to remember when I feel like I am not in control is the one from Forest Gump."
            s "Hmmm how does it go again? My ghoulish brain, that does not exist, is not working right today."
            s "OH! “Life is like a box of chocolates; you never know what you’re gonna get"
            m "Haha that was a good one, that definitely puts me at ease. Maybe eating something sweet would help as well..."

            $ stars += 1
            jump Muck3
        "Just control.":
            s "Just control what you can and ditch the rest!"
            m "I guess so, but I would need some time to adjust to that."
            jump Muck3


label Muck3:
    m "AH! I forgot I have to order! Sorry I’m making so many mistakes."
    m "Ah! Sorry for apologizing so much too. Argh!"
    menu:
        "Plan ahead!":
            s "Hehehe, here is an idea for next time, try to come up with a plan to avoid making mistakes, it can help put you at ease."
            m "Sure… maybe that can work, thanks."
            jump Muck4
        "It's ok to make mistakes":
            s "Hehehe it’s alright to make mistakes from time to time, we all do and we learn from them for our future selves."
            s "I’m sure future Muck will really appreciate past Muck!"
            m "That’s really sweet, thank you for this Mr. Spoopy! "
            m "This was the perfect cherry on top of this sundae of a day!"
            $ stars += 1
            jump Muck4


label Muck4:
    s "Miss Muck, may I guess what you would like to order, for some ghoulish fun?"
    m "Of course, go right ahead!"
    jump main_cooking_loop
