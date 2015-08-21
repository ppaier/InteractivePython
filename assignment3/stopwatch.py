# template for "Stopwatch: The Game"

import simpleguitk as simplegui

# define global variables
tenth_seconds = 0
num_tries  = 0
num_success = 0
is_stopped = True

# define helper function format that converts time
# in tenths of seconds into formatted string A:BC.D
def format(t):
    m  = int(t/(600))
    s  = int((t - 600 * m) / 10)
    s1 = int(s/10)
    s2 = int(s - 10 * s1) 
    ts = t - 600*m - 10*s 
    return str(m) + ":" + str(s1) + str(s2) + ":" + str(ts)
    
# define event handlers for buttons; "Start", "Stop", "Reset"
def start_button_handler():
    global is_stopped
    timer.start()
    is_stopped = False
    
def stop_button_handler():
    global is_stopped, num_tries, num_success
    if is_stopped==False:
        timer.stop()
        num_tries = num_tries + 1
        if tenth_seconds % 10 == 0:
            num_success = num_success + 1
    is_stopped = True

def reset_button_handler():
    global tenth_seconds, num_tries, num_success, is_stopped
    timer.stop()
    tenth_seconds = 0
    num_tries = 0
    num_success = 0
    is_stopped = True
    
    
# define event handler for timer with 0.1 sec interval
def timer_handler():
    global tenth_seconds
    tenth_seconds = tenth_seconds + 1

# define draw handler
def draw_handler(canvas):
    canvas.draw_text(str(num_success)+ "/" + str(num_tries), [230, 30], 24, "Black")
    canvas.draw_text(format(tenth_seconds), [80, 150], 50, "Black")
    
# create frame
frame = simplegui.create_frame("Home", 300, 300)

# register event handlers
timer = simplegui.create_timer(100, timer_handler)
frame.set_draw_handler(draw_handler)
frame.set_canvas_background("White")
frame.add_button("Start", start_button_handler)
frame.add_button("Stop", stop_button_handler)
frame.add_button("Reset", reset_button_handler)

# start frame
frame.start()

# Please remember to review the grading rubric
