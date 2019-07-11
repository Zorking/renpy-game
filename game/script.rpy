# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define gm = Character("", color="#0020C2")
default some_flag = False


# убрать главное меню
# label main_menu:
#     return

label start:
    $ some_flag = not some_flag
    show screen keymap_screen
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg return_home
    with fade


    # show shark normal at left - показывает персонажа with dissolve - эффект
    #This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.



    # These display lines of dialogue.

    gm "Наконец-то я дома."

    scene bg computer_turns_on
    with fade

    gm "Продолжим игру..."

    scene bg choose_gender
    with fade

    gm "Создание персонажа! Моя любимая часть. За кого я хочу играть?"

    #Как сделать выбор пола? Сейчас пол установлен на женский.

    gm "Я люблю отыгрывать себя в разных мирах."

    scene bg choose_name
    with fade

    gm "Мое имя.."

    #Появляется консоль ввода букв.

    gm "Очень оригинально конечно, но я люблю свое имя."

    scene bg room_for_girl

    define g = Character("Элина?", color="#0020C2")

    show gg girl home at left
    with dissolve

    g "На этом пока можно закончить, хочу прилечь."

    # This ends the game.

    return
