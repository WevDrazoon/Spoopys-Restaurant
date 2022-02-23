#screen myFirstScreen():

    #imagemap:
        #ground "gamimg.jpg"
        #hotspot(162, 1, 144, 214) action Jump("after_attack")
        #hotspot(23, 55, 129, 113) action Show("mySecondScreen"), hide(myFirstScreen)

#screen mySecondScreen():
    #text "Hey there owo"
#screen cookin():


screen bell:
    vbox xalign 0.785 yalign 0.55:
        imagebutton:
            idle "bell_from_hell.png"
            hover "bell_from_hell.png"
            action [Play("sound", "Bell.mp3"), Jump("orders")]


    #timer 3.0 action Jump("qte_one_fail")

screen blend:
    vbox xalign 0.05 yalign 0.3:
        imagebutton:
            idle "brain.png"
            hover "brain.png"
            action [Play("sound", "blender.mp3"), Jump("blending_ani")]

screen clicker01:
    vbox xalign 0.04 yalign 0.6:
        imagebutton:
            idle "brain.png"
            hover "doughnut.png"
            action [Play("sound", "squish.mp3"), Jump("clicker_2")]

screen clicker02:
    vbox xalign 0.3 yalign 0.6:
        imagebutton:
            idle "brain.png"
            hover "doughnut.png"
            action [Play("sound", "squish.mp3"),Jump("clicker_3")]

screen clicker03:
    vbox xalign 0.6 yalign 0.6:
        imagebutton:
            idle "brain.png"
            hover "doughnut.png"
            action [Play("sound", "squish.mp3"), Jump("clicker_4")]


screen raw_brain():
    draggroup:

        drag:
            drag_name "Raw Beef"
            child "brain.png"
            dragged beef_wiggle
            droppable False
            xalign 0.8 yalign 0.6

        drag:
            drag_name "Skillet"
            child "pan_colored.png"
            draggable False
            xalign 0.05 yalign 0.6

screen prep_brain():
    draggroup:

        drag:
            drag_name "Cooked Beef"
            child "burger.png"
            dragged beef_ready
            droppable False
            xalign 0.05 yalign 0.6

        drag:
            drag_name "Skillet"
            child "plate_colored.png"
            draggable False
            xalign 0.6 yalign 0.6
