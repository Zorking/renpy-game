# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


define gm = Character("qwerty", color="#0020C2")
define shark = Character("shark", color="#0020C2")
default some_flag = False

# убрать главное меню
label main_menu:
    return


label start:
    $ has_laser = False
    python:
        # тут все для инвентаря
        player = Player("Derp", 100, 50)
        player.hp = 50
        player.mp = 10
        chocolate = Item("Chocolate", hp=40, image="gui/inv_chocolate.png")
        banana = Item("Banana", mp=20, image="gui/inv_banana.png")
        gun = Item("Gun", element="bullets", image="gui/inv_gun.png", cost=7)
        laser = Item("Laser Gun", element="laser", image="gui/inv_laser.png")
        inventory = Inventory()
        #add items to the initial inventory:
        inventory.add(chocolate)
        inventory.add(chocolate)
        inventory.add(banana)
        inventory.add(laser)


    show screen keymap_screen
    show screen inventory_button

    scene bg return_home
    
    # show screen lock_keys()

    gm "Нужно что-то найти!"

    if not has_laser:
        with fade
        show screen item_search
        $ renpy.pause()
    
    return

label main_scene:
    gm "Наконец-то я дома."

    scene bg computer_turns_on
    # with fade

    gm "Продолжим игру..."

    scene bg choose_gender
    # with fade

    gm "Создание персонажа! Моя любимая часть. За кого я хочу играть?"

    #Как сделать выбор пола? Сейчас пол установлен на женский.

    menu:

        gm "Are you a boy or a girl"



screen item_search:
    # показать лазерган на экране и по нажатию делать всякое
    modal False
    imagebutton:
        xpos 20 ypos 200
        idle "gui/inv_laser.png"
        hover "gui/inv_laser.png"
        action [SetVariable("has_laser", True), Hide("item_search"), Jump("out")] 

        "Boy":
            $ input_gender = "boy"

        "Girl":
            $ input_gender = "girl"

    gm "Я люблю отыгрывать себя в разных мирах."

    scene bg choose_name
    $ inputed_name = renpy.call_screen("input_center", prompt="Мое имя..")

    #Появляется консоль ввода букв.

    gm "Пол [input_gender] и имя [inputed_name] Очень оригинально конечно, но я люблю свое имя."

    scene bg room_for_girl

    define g = Character("Элина?", color="#0020C2")

    show gg girl home at left
    with dissolve

    g "На этом пока можно закончить, хочу прилечь."

    # This ends the game.