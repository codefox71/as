def on_up_repeated():
    mySprite.y += -1
controller.up.on_event(ControllerButtonEvent.REPEATED, on_up_repeated)

def on_right_repeated():
    mySprite.x += 1
controller.right.on_event(ControllerButtonEvent.REPEATED, on_right_repeated)

def game_tick():
    global mySprite
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

def on_down_repeated():
    mySprite.y += 1
controller.down.on_event(ControllerButtonEvent.REPEATED, on_down_repeated)

def on_left_repeated():
    mySprite.x += -1
controller.left.on_event(ControllerButtonEvent.REPEATED, on_left_repeated)

mySprite: Sprite = None
scene.set_background_image(assets.image("""
    core-level
"""))
game_tick()