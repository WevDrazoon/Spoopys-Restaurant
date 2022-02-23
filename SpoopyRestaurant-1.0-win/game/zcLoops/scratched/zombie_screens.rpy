#screen qte_bell:
    #3vbox xalign 0.5 yalign 0.5:
        #imagebutton:
        #    idle "brain bloody.png"
            #hover "brain cooked.png"
        #    action Jump("qte_one_success")

    #timer 3.0 action Jump("qte_one_fail")

#screen qte_blend:
#    vbox xalign 0.5 yalign 0.5:
    #    imagebutton:
#            idle "brain bloody.png"
#            hover "brain cooked.png"
#            action Jump("blending animation")
#
#screen clicker:
#    vbox xalign 0.5 yalign 0.5:
#        imagebutton:
#            idle "brain bloody.png"
#            hover "brain cooked.png"
#            action Jump("blender_zombie1")

#screen clicker1:
#    vbox xalign 0.5 yalign 0.5:
#        imagebutton:
#            idle "brain bloody.png"
#            hover "brain cooked.png"
#            action Jump("")

#screen clicker2:
#    vbox xalign 0.5 yalign 0.5:
#        imagebutton:
#            idle "brain bloody.png"
#            hover "brain cooked.png"
#            action Jump("zombie_order")


#screen raw_beef():
    #draggroup:

        #drag:
            #33#drag_name "Raw Beef"
            #child "brain bloody.png"
            #dragged beef_wiggle
            #droppable False
            #xalign 0.1 yalign 0.8

        #drag:
            #drag_name "Skillet"
            #child "pan_flat.png"
            #draggable False
            #xalign 0.4 yalign 0.8

#screen prep_beef():
    #draggroup:

        #drag:
            #drag_name "Cooked Beef"
            ##child "brain cooked.png"
            #d#ragged beef_ready
            #droppable False
            #xalign 0.4 yalign 0.8

        #drag:
            #drag_name "Skillet"
            #child "plate_flaat.png"
            #draggable False
            #xalign 0.8 yalign 0.8
