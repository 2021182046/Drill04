from pico2d import *

open_canvas()
run_character = load_image('robot_run.png')
idle_character = load_image('robot_idle.png')
tuk_ground = load_image('TUK_GROUND.png')

def handle_events():
    global running, dir, dir_y, idle

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_RIGHT:
                running = True
                idle = False
                dir += 1
            elif event.key == SDLK_LEFT:
                running = True
                idle = False
                dir -= 1
            elif event.key == SDLK_UP:
                running = True
                idle = False
                dir_y += 1
            elif event.key == SDLK_DOWN:
                running = True
                idle = False
                dir_y -= 1
            elif event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_RIGHT:
                running = False
                idle = True
                dir -= 1
            elif event.key == SDLK_LEFT:
                running = False
                idle = True
                dir += 1
            elif event.key == SDLK_UP:
                running = False
                idle = True
                dir_y -= 1
            elif event.key == SDLK_DOWN:
                running = False
                idle = True
                dir_y += 1

idle = True
running = False
x = 800 // 2
y = 600 // 2
frame = 0
frame_idle = 0
dir = 0
dir_y = 0

while running:
    clear_canvas()
    tuk_ground.draw(800//2, 600//2)
    run_character.clip_draw(frame*63, 0, 60, 70, x, y)
    update_canvas()
    handle_events()
    frame = (frame+1) % 8
    x += dir * 5
    y += dir_y * 5
    delay(0.05)

while idle:
    clear_canvas()
    tuk_ground.draw(800//2, 600//2)
    idle_character.clip_draw(frame_idle*46, 0, 50, 50, x, y)
    update_canvas()
    handle_events()
    frame_idle = (frame_idle+1) % 10
    delay(0.05)


close_canvas()
