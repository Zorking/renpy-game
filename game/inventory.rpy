init python:
    class myDisplay(renpy.Displayable):
        def __init__(self, **kwargs):
            renpy.Displayable.__init__(self, **kwargs)

        def render(self, width, height, st, at):
                render = renpy.Render(1280, 150)
                canvas = render.canvas()

                # canvas.polygon("#003366", (461, 199, 300, 400), width=0)
                canvas.rect("#000", (0, 0, 1280, 150))
                for x in range(10):
                    canvas.rect("#fff", (10 + x * 160, 2, 140, 140))
                # color, (left offset, right offset, width, height)
                # canvas.line("#000", (80, 10), (80, 80))
                # canvas.line("#000", (150, 45), (80, 80))
                # canvas.line("#000", (150, 300), (80, 799))
                # canvas.line("#000", (400, 45), (80, 500))

                return render

screen inventory_menu:
    add myDisplay()
    # zorder 5
    # imagemap:
    #     xpos 0
    #     ypos 0
    #     xsize 1200 #width of ground/hover image.
    #     ysize 150 #height of ground/hover image.
    #
    #     ground "images/bottom_panel.png"
        # hover "images/bottom_panel_hover.png"
        #Menu Name
        # add "images/button_wide.png" xpos 130 ypos 0
        # text title xalign 0.5 yalign 0.5 xpos 130+70 ypos 0+18 size 12

    #     #Categories
    #     for i in range(0,len(categories)):
    #         #hotspot (300+(33*i), 0, 33, 34) clicked SetVariable("category_choice",categories[i]), Return(categories[i])
    #         #add "interface/topbar/buttons/" +interface_color+ "/" +str(categories[i])+ ".png" xpos 300+(33*i) ypos 0
    #
    #         # Use imagebutton instead of hotspot to make use of imagehover() tint function
    #         imagebutton:
    #             xpos 300+(33*i)
    #             ypos 0
    #             idle "interface/topbar/buttons/" +interface_color+ "/" +str(categories[i])+ ".png"
    #             hover image_hover("interface/topbar/buttons/" +interface_color+ "/" +str(categories[i])+ ".png")
    #             action [SetVariable("category_choice",categories[i]), Return(categories[i])]
    #
    #     if func_btn:
    #         imagebutton:
    #             xpos 300+(33*(len(categories)+1))
    #             ypos 0
    #             idle "interface/topbar/buttons/"+interface_color+"/"+func_btn_ico+".png"
    #             hover image_hover("interface/topbar/buttons/"+interface_color+"/"+func_btn_ico+".png")
    #             action Return("func")
    #
    #     #Items
    #     for i in range(current_page*items_shown, (current_page*items_shown)+items_shown):
    #         if i < len(menu_items):
    #             $ col = i % 5
    #             $ row = i % 1
    #             hotspot ( 140+(90*(i-(current_page*items_shown))), 34, 83, 85) clicked Return(menu_items[i])
    #             use icon_menu_item(menu_items[i], 135+(90*(i-(current_page*items_shown))), 34 )
    #
    # #Left Button
    # imagebutton:
    #     xpos UI_xpos_offset +80
    #     ypos UI_ypos_offset +50
    #     idle "interface/general/"+interface_color+"/button_arrow_left.png"
    #     if not current_page <= 0:
    #         hover "interface/general/"+interface_color+"/button_arrow_left_hover.png"
    #         action Return("dec")
    #
    # #Right Button
    # imagebutton:
    #     xpos UI_xpos_offset +80 +880
    #     ypos UI_ypos_offset +50
    #     idle "interface/general/"+interface_color+"/button_arrow_right.png"
    #     if current_page < math.ceil((len(menu_items)-1)/items_shown):
    #         hover "interface/general/"+interface_color+"/button_arrow_right_hover.png"
    #         action Return("inc")
