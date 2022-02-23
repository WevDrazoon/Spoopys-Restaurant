label Toe1:
    $ Toe_current = True

    s "Alright, it's a new day filled with customers!"
    s "Ever since the grand opening of my new restaurant, business has been doing well."
    s "Being a fresh ghost and a college graduate, people do not take my restaurant too seriously."
    s "However, I'm hoping for a brighter ghoulish future to come!"


    s "Next customer please!"
    show rest first
    t "Hello hello, I’m Leonartoe and you must be Mr. Spoopy, am I right?"
    s "Yep you got me, how are you doing today?"
    t "Good! But my foot is hecka sore."

    menu:
        "How come?":
            t "Oh! I just had a hand drawing contest between me and my friend Handry."
            t "I came out victorious, but not without the casualty of my poor foot."
            $ stars += 1
            jump Toe2

        "Don’t worry!":
            s "I’m sure the pain will wear off soon! Don’t worry!"
            t "Ah, yeah, I’m sure it will."
            jump Toe2


label Toe2:
    s "Maybe something can help soothe the pain, like some advice or food?"
    t "Perhaps, what do you advise?"

    menu:
        "Stop doing things that make you sore":
            s "Just stop doing the stuff that makes you sore! You’ll feel way better!"
            t "But that means I can’t draw…"
            s "Aww shucks."
            jump Toe3

        "Treat yourself kindly":
            s "Well, you will sometimes get sore, but what’s important is that you treat yourself kindly when you are."
            s "Don’t push yourself more than you have to!"
            t "Thanks! You always give great advice Spoopy! Maybe something cold can help the aches haha."
            $ stars += 1
            jump Toe3


label Toe3:
    t "Spoopy, have you ever had a passion?"
    menu:
        "Customer Service!":
            s "My passion is getting to know customers like you!"
            t "Oh wow! That’s so cool, but I’m sure that drains you after long days."
            $ stars += 1
            jump Toe4

        "...Cooking?":
            t "As expected from you haha!"
            jump Toe4
label Toe4:

    s "Of course haha."
    s "Leonartoe, may I guess what you would actually like to order, for some ghoulish fun?"
    t "Ah! I forgot to order since we were talking haha!"
    t "Go ahead give me your best guess."
    jump main_cooking_loop
