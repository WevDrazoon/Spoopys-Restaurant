label Ked1:
    $ Kedrick_current = True

    s "Next customer please"
    show rest third
    k "Yooo!"
    k "How’s it going ghost bro?"
    s "Hey Kedrick! How are you and the fellas?"
    k "Not bad, but we’re like starrrrrving."
    k "We’ve been out all-day doing stuff."
    menu:
        "Y'all are always hungry":
            s "You guys are always hungry! No matter what kinda “stuff” you do haha."
            k "True true, this time I was tussling with the boys. "
            jump Ked2
        "What kinda stuff?":
            s "What kinda stuff?"
            k "Some tussling with the dudes of course! All in good fun though, no worries."
            $ stars += 1
            jump Ked2



label Ked2:
    s "Haha, that must have been fun!"
    k "How are you not always hungry Spoops?"
    k "You’re always around food!"
    menu:
        "I like making the food":
            s "I’m not around food because I like to eat it, I’m around food because I like making it for people!"
            k "Aww, well I’ll be over any time I’m hungry which is always haha!"
            $ stars += 1
            jump Ked3
        "I don't eat":
            s "Simple, I don’t eat."
            k "HOW? Oh wait… you’re a ghost, right. "
            jump Ked3


label Ked3:
    s "Yep yep that’s right"
    k "Sometimes I wish I didn’t have to eat. I’d get so much done!"

    menu:
        "Have you tried being a ghost?":
            s "Have you tried being a ghost?"
            k "No, not really. I’d have to give up my flesh and bones though, so I think I’ll pass."
            jump Ked4

        "But eating is nice!":
            s "True, but eating is so nice. There are so many tasty things to eat! Why pass that up?"
            k "Maaaan, you are so right!"
            $ stars += 1
            jump Ked4

label Ked4:
    s "Kedrick, may I guess what you would actually like to order, for some ghoulish fun?"
    k "Heck yeah bro!"
    jump main_cooking_loop
