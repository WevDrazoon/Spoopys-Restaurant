#label cooking_zombie:

    #"Alright... that was um... vague... Time to choose an item to make I suppose"

    #menu:
        #"Good option":
        #    $ zombie_good_food == True
        #    call screen raw_beef

        #    show brain bloody:
        #        xalign 0.4 yalign 0.8
        #    pause 1.0
        #    show brain cooked:
        #        xalign 0.4 yalign 0.8
        #    pause 1.0

        #    "Okay, we put the [beef] in the [pan]."
        #    "Time to prep it for the estimed costomer"

        #    hide brain cooked
        #    call screen prep_beef

        #    show brain cooked:
        #        xalign 0.8 yalign 0.8
        #    $ stars += 1
        #    jump zombie_order

        #"Bad option1":
        #    "Nopr nope"
        #    call screen qte_blend

        #"Bad option2":
        #    "Nopr nope2"
        #    call screen clicker
        #    jump blender_zombie1
