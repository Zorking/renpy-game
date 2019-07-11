# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define s = Character("Shark", color="#0020C2")
default some_flag = False


# The game starts here.


label start:
    $ some_flag = not some_flag
    show screen keymap_screen
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg street
    with fade


    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show shark normal at left
    with dissolve


    # These display lines of dialogue.

    s "You've created a new Ren'Py game."

    s "Once you add a story, pictures, and music, you can release it to the world!"

    # This ends the game.

    return
