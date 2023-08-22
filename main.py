def on_up_repeated():
    global mySprite
    mySprite.y += -1
    mySprite = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f e e e e f f . . . . 
                    . . . f e e e f f e e e f . . . 
                    . . f f f f f 2 2 f f f f f . . 
                    . . f f e 2 e 2 2 e 2 e f f . . 
                    . . f e 2 f 2 f f 2 f 2 e f . . 
                    . . f f f 2 2 e e 2 2 f f f . . 
                    . f f e f 2 f e e f 2 f e f f . 
                    . f e e f f e e e e f e e e f . 
                    . . f e e e e e e e e e e f . . 
                    . . . f e e e e e e e e f . . . 
                    . . e 4 f f f f f f f f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 4 4 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.player)
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def on_right_repeated():
    global mySprite
    mySprite.x += 1
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . . . f f f f f f . . . . 
                    . . . . f f e e e e f 2 f . . . 
                    . . . f f e e e e f 2 2 2 f . . 
                    . . . f e e e f f e e e e f . . 
                    . . . f f f f e e 2 2 2 2 e f . 
                    . . . f e 2 2 2 f f f f e 2 f . 
                    . . f f f f f f f e e e f f f . 
                    . . f f e 4 4 e b f 4 4 e e f . 
                    . . f e e 4 d 4 1 f d d e f . . 
                    . . . f e e e 4 d d d d f . . . 
                    . . . . 4 d d e 4 4 4 e f . . . 
                    . . . . e d d e 2 2 2 2 f . . . 
                    . . . . f e e f 4 4 5 5 f f . . 
                    . . . . f f f f f f f f f f . . 
                    . . . . . f f . . . f f f . . .
        """),
        SpriteKind.player)
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def on_down_repeated():
    global mySprite
    mySprite.y += 1
    mySprite = sprites.create(img("""
            . . . . . . f f f f . . . . . . 
                    . . . . f f f 2 2 f f f . . . . 
                    . . . f f f 2 2 2 2 f f f . . . 
                    . . f f f e e e e e e f f f . . 
                    . . f f e 2 2 2 2 2 2 e e f . . 
                    . . f e 2 f f f f f f 2 e f . . 
                    . . f f f f e e e e f f f f . . 
                    . f f e f b f 4 4 f b f e f f . 
                    . f e e 4 1 f d d f 1 4 e e f . 
                    . . f e e d d d d d d e e f . . 
                    . . . f e e 4 4 4 4 e e f . . . 
                    . . e 4 f 2 2 2 2 2 2 f 4 e . . 
                    . . 4 d f 2 2 2 2 2 2 f d 4 . . 
                    . . 4 4 f 4 4 5 5 4 4 f 4 4 . . 
                    . . . . . f f f f f f . . . . . 
                    . . . . . f f . . f f . . . . .
        """),
        SpriteKind.player)
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_left_repeated():
    global mySprite
    mySprite.x += -1
    mySprite = sprites.create(img("""
            . . . . . . . . . . . . . . . . 
                    . . . . f f f f f f . . . . . . 
                    . . . f 2 f e e e e f f . . . . 
                    . . f 2 2 2 f e e e e f f . . . 
                    . . f e e e e f f e e e f . . . 
                    . f e 2 2 2 2 e e f f f f . . . 
                    . f 2 e f f f f 2 2 2 e f . . . 
                    . f f f e e e f f f f f f f . . 
                    . f e e 4 4 f b e 4 4 e f f . . 
                    . . f e d d f 1 4 d 4 e e f . . 
                    . . . f d d d e e e e e f . . . 
                    . . . f e 4 e d d 4 f . . . . . 
                    . . . f 2 2 e d d e f . . . . . 
                    . . f f 5 5 f e e f f f . . . . 
                    . . f f f f f f f f f f . . . . 
                    . . . f f f . . . f f . . . . .
        """),
        SpriteKind.player)
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

mySprite: Sprite = None
scene.set_background_image(assets.image("""
    core-level
"""))