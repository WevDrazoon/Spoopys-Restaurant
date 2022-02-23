label Ham1:
    $ Hammy_current = True

    s "Next customer please!"
    show rest forth
    hy "AH!"
    hy "Oh hello!"
    s "Oops, did I scare you by accident?"
    s "You know being a ghost I tend to do that… a lot."
    hy "Oh not at all, I am a bit- I’m just a tad socially anxious so I just got startled."
    s "Oh, I see don’t worry about being anxious around me, I’m just here to get you your food as soon as possible hehe."
    hy "Oh right about that, what is the easiest thing to order?"
    hy "Darn it I should have prepared..."

    menu:
        "Easiest would be... Not ordering":
            s "I mean if it really irks you, maybe not ordering anything can work?"
            hy "But I would have just caused you unnecessary trouble coming here… oh no."
            jump Ham2

        "Don't worry about it":
            s "Don’t worry about it, just order what you really wish to have!"
            hy "Ohh I guess your right, should have thought, and tried that haha."
            $ stars += 1
            jump Ham2



label Ham2:
    s "No no though, its alright please don’t worry."
    s "Just breathe in and out, act natural, and order what you’d like!"
    hy "Right! But I wouldn’t want to cause you much trouble so maybe just one Smart Smoothie, for Ha- Hammy?"
    menu:

        "Haha, sounds a bit odd":
            s "Oh ok… that was slightly odd haha."
            h "Oops, sorry I tend to do that."
            h "Argh, actually maybe I may want to try something else... I don’t know anymore!"
            h "Come on Hammy decide already!"
            jump Ham3

        "Coming right up Hammy!":
            s "Aww what a cute ghoulish name!"
            s "Alright, one order for Hammy coming up!"
            s "But, if you want something else instead, please say so, preparing food or a drink are equally easy so no trouble!"
            h "Oh, well I appreciate the sincerity, but it’ll take me a couple minutes to build some more courage haha."
            s "Take your time Hammy, I don’t wanna stress you out."
            h "Ah... Thank you..."
            h "..."
            s "..."
            h "..."
            h "Ok... I think I would want to try something meaty?"
            s "Alright! Perfect. You did it!"
            $ stars += 1
            jump Ham3


label Ham3:
    s "Let’s change topics for a bit to ease some stress."
    h "Oh... ok! How are you feeling today, and do you like the weather we have today?"
    menu:
        "Good, Weather is Good":
            s "I’ve been doing alright, and the weather is just splendid today, thanks for asking actually."
            h "Oh, hehe that’s really good to hear actually. Gosh I feel great now thanks for that!"
            $ stars += 1
            jump Ham4
        "Fine":
            s "Fine I guess."
            h "Oh sorry for asking then, but it helped me a bit, so I guess that’s good."
            jump Ham4

label Ham4:
    s "Hammy, may I guess what you would actually like to order, for some ghoulish fun?"
    h "Oh sure that can be a fun guessing game, shoot!"
    jump main_cooking_loop
