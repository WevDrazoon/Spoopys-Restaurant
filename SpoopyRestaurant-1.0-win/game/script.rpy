# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Spoopy")
define t = Character("Leonartoe", who_color="#81a493")
define m = Character("Muck", who_color="#72a4ae")
define h = Character("Hammy", who_color="#f8ad9a")
define k = Character("Kedrick", who_color="#a8649c")
define hy = Character("??????", who_color="#f8ad9a")

#python code :D
init python:
    def beef_wiggle(drags, drop):
        if not drop:
            return

        store.beef = drags[0].drag_name
        store.pan = drop.drag_name

        return True
init python:
    def beef_ready(drags, drop):
        if not drop:
            return

        store.beafeat = drags[0].drag_name
        store.plate = drop.drag_name

        return True


default Hammy_happy = False
default Toe_happy = False
default Kedrick_happy = False
default Muck_happy = False

default Hammy_current = False
default Toe_current = False
default Kedrick_current = False
default Muck_current = False

#order of order = Leonartoe, Muck, Kedrick and Hammy

init:
    $ _game_menu_screen = None
    $ stars_max = 20
    $ stars = stars_max


layeredimage rest:
    always:
        "background_most_behind"


    group chara:

        attribute first:
            "foot"
        attribute second:
            "marsh_seem"
        attribute third:
            "kedrick"
        attribute forth:
            "hammy"

    group background:
        attribute front default:
            "background_front"

    group blend:
        attribute blender default:
            "blender_colored"
    group bell:
        attribute bellhell default:
            "bell_form_hell"
    group pip:
        attribute piping default:
            "piping_colored"
    group plate:
        attribute plate default:
            "plate_colored"

    group bowl:
        attribute brainbowl default:
            "brain_bowl_colored"

    group pan:
        attribute panc default:
            "pan_colored"



# The game starts here.
label start:
    $ stars -= 20
    play music "Spoopy_Theme_2_1.mp3"
    show rest

        #intro to your job, who you are, who to expect
    jump Toe1


label final_ratings:
    play music "Spoopy_opening.mp3"
    if stars >= 9:
        jump good_ending
    else:
        jump bad_ending


label good_ending:
    scene background_behind with fade
    s "Perfect, service for today is done! It almost feels as if I have achived some sort of {b}good ending{/b}."
    s "Another successful day at Spoopy's Restaurant, with great customers and more locals to come going forward!"

    return


label bad_ending:
     #maybeeeeeee add fadeout??????
    scene background_behind with fade
    s "Service is done for today! Not my best work, it even feels like I've stumbled in a {b}bad ending{/b} or something"
    s "But hey there always room for improvement here at Spoopy's Restaurant!"

    return
