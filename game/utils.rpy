
screen lock_keys():
    # залочит клики, нужно будет нажимать на кнопку на экране
    textbutton "Cont..." action Return()

screen input_center:
    # инпут для имени персонажа, потом можно будет сделать кастомное что-то
    window:
        style "nvl_window"
        text "Твое имя" xalign 0.5 yalign 0.4
        input id "input" xalign 0.5 yalign 0.5
    use quick_menu


label out:
    menu:
        gm "Взять лазерган?"
        "Да!":
            $ inventory.add(laser)
            gm "Я нашел ЛАЗЕРГАН!"
        "Нет":
            pass
    jump main_scene


screen item_search:
    # показать лазерган на экране и по нажатию делать всякое
    modal False
    imagebutton:
        xpos 20 ypos 200
        idle "gui/inv_laser.png"
        hover "gui/inv_laser.png"
        action [SetVariable("has_laser", True), Hide("item_search"), Jump("out")] 
