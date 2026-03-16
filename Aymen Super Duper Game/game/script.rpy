define N = Character("Narrator")
default player = "Aymen"
define P = Character("[player]")
default studied = False
default worked = False
image bg room = "images/BG.png"

label start:
    scene bg room

    N "You signed up for Hack Club Resolution,\nBut exams and procrastination got in the way."
    N "Now you only have 1.5 hours left to ship something."

    $ player = renpy.input("What is your name? (default is Aymen)", length=32)
    $ player = player.strip() if player is not None else ""
    $ player = player.capitalize()
    if player == "":
        $ player = "Aymen"

    N "[player], nice name."

    N "1:30:00 Left"
    P "I should really start working..."

    menu:
            "What should I do?"
            "Start studying":
                jump studying1
            "Start working on the game":
                jump working1
            "Play Clash Royale":
                jump bad_ending


label studying1:

    $ studied = True

    N "For some divine reason you get the idea to start studying."
    N "Now you probably won't fail your exams."
    N "+5 INT"
    N "1:15:00 Left"

    menu:
            "Now what?"
            "Start working on the game":
                jump working1
            "Play Clash Royale":
                jump secret_ending


label working1:

    $ worked = True

    N "You start working on the game."
    N "The basic mechanics are coming together."
    N "1:00:00 Left"

    menu:
            "Next step"
            "Keep working":
                jump working2
            "Play Clash Royale":
                jump bad_ending


label working2:

    N "You keep coding."
    N "Menus, enemies, and UI are starting to work."
    N "0:30:00 Left"

    menu:
            "Final decision"
            "Finish the game":
                jump ending_check
            "Play Clash Royale":
                jump bad_ending


label ending_check:

    if studied:
        jump best_ending
    else:
        jump good_ending


label best_ending:

    N "Because you studied earlier, your mind is clear."
    N "You code efficiently and finish the game just before the deadline."
    N "BEST ENDING: Game Completed AND Exams Saved"
    return


label good_ending:

    N "You finish the game just before the deadline."
    N "But your exams tomorrow might be rough. (You're cooked, lil bro.)"
    N "GOOD ENDING: Game Completed"
    return


label bad_ending:

    N "You start playing Clash Royale."
    N "One match becomes ten."
    N "You look at the clock..."
    N "Time is up."
    N "BAD ENDING: Procrastination Wins"
    return


label secret_ending:

    N "You start playing Clash Royale."
    N "One match becomes ten."
    N "You look at the clock..."
    N "Time is up."
    N "But thanks to your extra intelligence, you get a great idea."
    N "You email the organizer asking for an extension."
    N "Somehow... they actually say yes."
    N "You now have time for both exams and your game."
    N "SECRET ENDING: EXTENSION OBTAINED"
    return