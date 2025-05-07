import pygame as pg

# png billeder
bgImg = pg.image.load("pngs/background.png").convert()
askAudience = pg.transform.scale(pg.image.load("pngs/askaudience.png"), (85, 52)).convert()
askHost = pg.transform.scale(pg.image.load("pngs/askhost.png"), (85, 52)).convert()
fiftyFifty = pg.transform.scale(pg.image.load("pngs/5050.png"), (85, 52)).convert()
callFriend = pg.transform.scale(pg.image.load("pngs/call.png"), (85, 52)).convert()
levelIndicator = pg.image.load("pngs/level_indicator.png").convert_alpha()

    # svarmuligheder og tilhørende positioner
correctAnwser = pg.image.load("pngs/correct.png").convert_alpha()
correctAnwser.set_alpha(100)
selectedAnwser = pg.image.load("pngs/selected.png").convert_alpha()
selectedAnwser.set_alpha(100)
hoverAnwser = pg.image.load("pngs/selected.png").convert_alpha()
hoverAnwser.set_alpha(35)
disabledAnwser = pg.image.load("pngs/unavailable.png").convert_alpha()
disabledAnwser.set_alpha(80)
destA, destB, destC, destD = (93, 592), (460, 592), (93, 642), (460, 642)
destinations = [destA, destB, destC, destD]

    # lifelines og tilhørende positioner
usedLL = pg.transform.scale(pg.image.load("pngs/LLused.png"), (85, 52)).convert_alpha()
usedLL.set_alpha(80)
hoverLL = pg.transform.scale(pg.image.load("pngs/LLselected.png"), (85, 52)).convert_alpha()
hoverLL.set_alpha(50)
destAskAudience, destAskHost, dest5050, destCallFriend = (30, 125), (30, 190), (30, 255), (30, 320)
destinationsLL = [destAskAudience, destAskHost, dest5050, destCallFriend]

    # lyd toggle
soundOn = pg.transform.scale(pg.image.load("pngs/sound on.png"), (int(83*0.75), int(74*0.75))).convert()
soundOff = pg.transform.scale(pg.image.load("pngs/sound off.png"), (int(83*0.75), int(74*0.75))).convert()
soundOnHover = pg.transform.scale(pg.image.load("pngs/sound on hover.png"), (int(83*0.75), int(74*0.75))).convert_alpha()
soundOnHover.set_alpha(80)
soundOffHover = pg.transform.scale(pg.image.load("pngs/sound off hover.png"), (int(83*0.75), int(74*0.75))).convert_alpha()
soundOffHover.set_alpha(80)

    # popup relateret
popUp = pg.transform.scale(pg.image.load("pngs/pop up image.png"), (int(590*0.75), int(414*0.75))).convert_alpha()
closeContinue = pg.transform.scale(pg.image.load("pngs/closePopUp.png"), (250, 45)).convert_alpha()

# skrifttyper
FONT0 = pg.font.Font("ARIAL.TTF", size=16)
FONT1 = pg.font.Font("ARIAL.TTF", size=20)

# text til milesten
levels=[FONT1.render("1   $ 100", True, "orange"),
        FONT1.render("2   $ 200", True, "orange"),
        FONT1.render("3   $ 300", True, "orange"),
        FONT1.render("4   $ 500", True, "orange"),
        FONT1.render("5   $ 1.000", True, "white"),
        FONT1.render("6   $ 2.000", True, "orange"),
        FONT1.render("7   $ 4.000", True, "orange"),
        FONT1.render("8   $ 8.000", True, "orange"),
        FONT1.render("9   $ 16.000", True, "orange"),
        FONT1.render("10  $ 32.000", True, "white"),
        FONT1.render("11  $ 64.000", True, "orange"),
        FONT1.render("12  $ 125.000", True, "orange"),
        FONT1.render("13  $ 250.000", True, "orange"),
        FONT1.render("14  $ 500.000", True, "orange"),
        FONT1.render("15  $ 1.000.000", True, "white")]