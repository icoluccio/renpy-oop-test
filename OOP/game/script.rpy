# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Eileen")





# The game starts here.

label start:
    python:
        class LuckPerCharacter:
            luck = {}
            def get(self, character):
              return self.luck[character]
            def give(self, character, howMuch = 1):
              if character in self.luck:
                self.luck[character] += howMuch
              else:
                self.luck[character] = howMuch

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy

    # These display lines of dialogue.
    $ luckPerCharacter = LuckPerCharacter()
    $ luckPerCharacter.give(e, 122)
    $ luck = luckPerCharacter.get(e)
    $ renpy.say(e, str(luck))
    if luck > 2:
        e "Really lucky"
    else:
        e "Not really lucky"

    # This ends the game.

    return
