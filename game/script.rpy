﻿# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.
init -1 python:
    import renpy.store as store
    import renpy.exports as renpy # we need this so Ren'Py properly handles rollback with classes
    from operator import attrgetter # we need this for sorting items

    inv_page = 0 # initial page of teh inventory screen
    item = None
    class Player(renpy.store.object):
        def __init__(self, name, max_hp=0, max_mp=0, element=None):
            self.name=name
            self.max_hp=max_hp
            self.hp=max_hp
            self.max_mp=max_mp
            self.mp=max_mp
            self.element=element
    player = Player("Derp", 100, 50)

    class Item(store.object):
        def __init__(self, name, player=None, hp=0, mp=0, element="", image="", cost=0):
            self.name = name
            self.player=player # which character can use this item?
            self.hp = hp # does this item restore hp?
            self.mp = mp # does this item restore mp?
            self.element=element # does this item change elemental damage?
            self.image=image # image file to use for this item
            self.cost=cost # how much does it cost in shops?
        def use(self): #here we define what should happen when we use the item
            if self.hp>0: #healing item
                player.hp = player.hp+self.hp
                if player.hp > player.max_hp: # can't heal beyond max HP
                    player.hp = player.max_hp
                inventory.drop(self) # consumable item - drop after use
            elif self.mp>0: #mp restore item
                player.mp = player.mp+self.mp
                if player.mp > player.max_mp: # can't increase MP beyond max MP
                    player.mp = player.max_mp
                inventory.drop(self) # consumable item - drop after use
            else:
                player.element=self.element #item to change elemental damage; we don't drop it, since it's not a consumable item

    class Inventory(store.object):
        def __init__(self, money=10):
            self.money = money
            self.items = []
        def add(self, item): # a simple method that adds an item; we could also add conditions here (like check if there is space in the inventory)
            self.items.append(item)
        def drop(self, item):
            self.items.remove(item)
        def buy(self, item):
            if self.money >= item.cost:
                self.items.append(item)
                self.money -= item.cost

    def item_use():
        item.use()

    #Tooltips:
    style.tips_top = Style(style.default)
    #style.title.font="gui/arial.ttf"
    style.tips_top.size=14
    style.tips_top.color="fff"
    style.tips_top.outlines=[(3, "6b7eef", 0,0)]
    style.tips_top.kerning = 5

    style.tips_bottom = Style(style.tips_top)
    style.tips_top.size=20
    style.tips_bottom.outlines=[(0, "6b7eef", 1, 1), (0, "6b7eef", 2, 2)]
    style.tips_bottom.kerning = 2

    style.button.background=Frame("gui/frame.png",25,25)
    style.button.yminimum=52
    style.button.xminimum=52
    style.button_text.color="000"


    showitems = True #turn True to debug the inventory
    # def display_items_overlay():
        # if showitems:
            # inventory_show = "Money:" + str(inventory.money) + " HP: " + str(player.hp) + " bullets: " + str(player.mp) + " element: " + str(player.element) + "\nInventory: "
            # for i in range(0, len(inventory.items)):
                # item_name = inventory.items[i].name
                # if i > 0:
                    # inventory_show += ", "
                # inventory_show += item_name

            # ui.frame()
            # ui.text(inventory_show, color="#000")
    # config.overlay_functions.append(display_items_overlay)


screen my_keys2():
    textbutton "Cont..." action Return()

screen inventory_button:
    textbutton "Show Inventory" action [ Show("inventory_screen"), Hide("inventory_button")] align (.95,.04)

screen inventory_screen:
    add "gui/inventory.png" # the background
    modal True #prevent clicking on other stuff when inventory is shown
    #use battle_frame(char=player, position=(.97,.20)) # we show characters stats (mp, hp) on the inv. screen
    #use battle_frame(char=dog, position=(.97,.50))
    hbox align (.95,.04) spacing 20:
        textbutton "Close Inventory" action [ Hide("inventory_screen"), Show("inventory_button"), Return(None)]
    $ x = 515 # coordinates of the top left item position
    $ y = 25
    $ i = 0
    $ sorted_items = sorted(inventory.items, key=attrgetter('element'), reverse=True) # we sort the items, so non-consumable items that change elemental damage (guns) are listed first
    $ next_inv_page = inv_page + 1
    if next_inv_page > int(len(inventory.items)/9):
        $ next_inv_page = 0
    for item in sorted_items:
        if i+1 <= (inv_page+1)*9 and i+1>inv_page*9:
            $ x += 190
            if i%3==0:
                $ y += 170
                $ x = 515
            $ pic = item.image
            $ my_tooltip = "tooltip_inventory_" + pic.replace("gui/inv_", "").replace(".png", "") # we use tooltips to describe what the item does.
            imagebutton idle pic hover pic xpos x ypos y action [Hide("gui_tooltip"), Show("inventory_button"), SetVariable("item", item), Hide("inventory_screen"), item_use] hovered [ Play ("sound", "sfx/click.wav"), Show("gui_tooltip", my_picture=my_tooltip, my_tt_ypos=693) ] unhovered [Hide("gui_tooltip")] at inv_eff
            if player.element and (player.element==item.element): #indicate the selected gun
                add "gui/selected.png" xpos x ypos y anchor(.5,.5)
        $ i += 1
        if len(inventory.items)>9:
            textbutton _("Next Page") action [SetVariable('inv_page', next_inv_page), Show("inventory_screen")] xpos .475 ypos .83

screen gui_tooltip (my_picture="", my_tt_xpos=58, my_tt_ypos=687):
    add my_picture xpos my_tt_xpos ypos my_tt_ypos

init -1:
    transform inv_eff: # too lazy to make another version of each item, we just use ATL to make hovered items super bright
        zoom 0.5 xanchor 0.5 yanchor 0.5
        on idle:
            linear 0.2 alpha 1.0
        on hover:
            linear 0.2 alpha 2.5

    image information = Text("INFORMATION", style="tips_top")
    #Tooltips-inventory:
    image tooltip_inventory_chocolate=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("Generic chocolate to heal\n40 points of health.", style="tips_bottom"))
    image tooltip_inventory_banana=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("A healthy banana full of potassium! You can also use it as ammo for your guns! O.O Recharges 20 bullets.", style="tips_bottom"))
    image tooltip_inventory_gun=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An gun that looks like something a cop would\ncarry around. Most effective on humans.", style="tips_bottom"))
    image tooltip_inventory_laser=LiveComposite((665, 73), (3,0), ImageReference("information"), (3,30), Text("An energy gun that shoots photon beams.\nMost effective on aliens.", style="tips_bottom"))

    image sidewalk = "Sidewalk.jpg"


define gm = Character("qwerty", color="#0020C2")
define shark = Character("shark", color="#0020C2")
default some_flag = False


# убрать главное меню
label main_menu:
    return

screen input_q:

    window:

        style "nvl_window"

        text "Твое имя" xalign 0.5 yalign 0.4
        input id "input" xalign 0.5 yalign 0.5

    use quick_menu

label start:
    python:
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


    $ some_flag = not some_flag
    show screen keymap_screen
    show screen inventory_button

    scene bg return_home

    show screen my_keys2()
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

        "Boy":
            $ input_gender = "boy"

        "Girl":
            $ input_gender = "girl"

    gm "Я люблю отыгрывать себя в разных мирах."

    scene bg choose_name
    $ inputed_name = renpy.call_screen("input_q", prompt="Мое имя..")

    #Появляется консоль ввода букв.

    gm "Пол [input_gender] и имя [inputed_name] Очень оригинально конечно, но я люблю свое имя."

    scene bg room_for_girl

    define g = Character("Элина?", color="#0020C2")

    show gg girl home at left
    with dissolve

    g "На этом пока можно закончить, хочу прилечь."

    # This ends the game.

    return
