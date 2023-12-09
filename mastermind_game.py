from datetime import datetime
import turtle as t
from random import randint
from Circle import Circle
from functools import partial


def log_error(error_type, message):
    """ Error logging functionality. 
        Args:
            error_type: exception object.
            message: str type of message.
    """
    timestamp = datetime.today()
    with open('mastermind_errors.err', 'a') as outfile:
        outfile.write(f"{timestamp}:::{error_type}:::{message}\n")

def register_shapes():
    """ Registering shapes for later usage. 
    """
    t.register_shape('file_error.gif')
    t.register_shape('checkbutton.gif')
    t.register_shape('xbutton.gif')
    t.register_shape('quit.gif')
    t.register_shape('leaderboard_error.gif')
    t.register_shape('quitmsg.gif')
    t.register_shape('lose.gif')
    t.register_shape('winner.gif')

def stamp_shapes(x=0, y=0, shape=None):
    """ Stamp shapes, default position is center. 
        Args:
            x, y : coordinates in screen.
            shape : desired shape that is already registered. 
    """
    t.goto(x, y)
    t.shape(shape)
    t.stamp()

def generate_code():
    """ Returns a list of 4 strings indicating colors of secret code. 
    """
    secret_code = []
    colors = ['red', 'green', 'blue', 'yellow', 'purple', 'black']
    
    # Randomly pop from 4 elements from colors and append it to secret_code
    i = 0
    while i < 4:
        secret_code.append(colors.pop(randint(0, 5 - i)))
        i += 1

    return secret_code

def draw_rectangle(x, y, width, height, pencolor='black'):
    """ Simple rectangle drawing functionality for 
        drawing different sections in game screen.
    """
    
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.pencolor(pencolor)
    t.goto(x + width, y)
    t.goto(x + width, y - height)
    t.goto(x, y - height)
    t.goto(x, y)
    t.penup()

def reset_color_buttons(color_button_list):
    """ Resetting color buttons to its original color. 
    """
    for button in color_button_list:
        button.set_color(button.get_tag())
        button.draw()

def click_quit():
    """ on-click event when quit button is clicked.
    """
    stamp_shapes(0, 0, 'quitmsg.gif')
    t.ontimer(t.bye, 1200)

def player_wins(name, score):
    """ Updates leaderboard and display winner.gif visuals. 
    """
    # update leaderboard
    update_leaderboard('leaderboard.txt', name, score)
    
    # display visuals
    stamp_shapes(0, 0, 'winner.gif')
    t.ontimer(t.bye, 2000)

def click_reset(attempts, attempt_count, color_button_list):
    """ on-click event when player clickes reset button. 
    """
    # set color of all guesses in attempt to white
    for guess in attempts[attempt_count[0]]:
        guess.set_tag('unfilled')
        guess.set_color('white')
        guess.draw()

    # reset guess board
    reset_color_buttons(color_button_list)

def click_check(attempts, attempt_count, pegs, secret_code, 
                color_buttons_list, name):  
    """ checks attempt when check button is clicked.
        Args:
            Attempts: Nested list of ten 4 Circle objects indicating guesses.
            Attempt_count: a list containing 1 integer indicating current 
                           attempt count (for passing by reference)
            pegs: Nested list of ten 4 Circle objects indicating pegs.
            secret_code : list of 4 string type indicating colors of code.
            color_buttons_list: list of Circle objects which are buttons.
            name: string type of player's name.  
    """
    # Flag for incomplete attempt
    if attempts[attempt_count[0]][-1].get_tag() != 'filled':
        return None
    
    # match attempt with code
    for i, guess in enumerate(attempts[attempt_count[0]]):
        for j, code in enumerate(secret_code):
            if guess.get_color() == code and i == j:
                pegs[attempt_count[0]][i].set_color('black')
            
            elif guess.get_color() == code and i != j:
                pegs[attempt_count[0]][i].set_color('red')

    # selection sort
    sorted = 0
    for i, peg in enumerate(pegs[attempt_count[0]]):
        if pegs[attempt_count[0]][i].get_color() == 'black':
            if sorted == len(pegs[attempt_count[0]]) - 1:
                break
            temp = pegs[attempt_count[0]][0 + sorted].get_color()
            pegs[attempt_count[0]][0 + sorted].set_color('black')
            pegs[attempt_count[0]][i].set_color(temp)
            sorted += 1

    for i, peg in enumerate(pegs[attempt_count[0]]):
        if pegs[attempt_count[0]][i].get_color() == 'red':
            if sorted == len(pegs[attempt_count[0]]) - 1:
                break
            temp = pegs[attempt_count[0]][0 + sorted].get_color()
            pegs[attempt_count[0]][0 + sorted].set_color('red')
            pegs[attempt_count[0]][i].set_color(temp)
            sorted += 1

    for peg in pegs[attempt_count[0]]:
        peg.draw()

    # check if every peg is black. if so, record score and display win.
    if pegs[attempt_count[0]][0].get_color() == 'black' and \
    pegs[attempt_count[0]][1].get_color() == 'black' and \
    pegs[attempt_count[0]][2].get_color() == 'black' and \
    pegs[attempt_count[0]][3].get_color() == 'black':
        attempt_count[0] += 1
        player_wins(name, attempt_count[0])

    # if not, increment attempt_count and reset color_buttons
    else:
        reset_color_buttons(color_buttons_list)
        attempt_count[0] += 1
        if attempt_count[0] > 9:
            stamp_shapes(0, 0, 'quitmsg.gif')
            t.ontimer(t.bye, 1200)

def click_colored_buttons(button, attempts, attempt_count):
    """ Pass color of clicked button to attempt. 
        Args:
            button: clicked Circle object
            Attempts: Nested list of ten 4 Circle objects indicating guesses.
            Attempt_count: a list containing 1 integer indicating current 
                           attempt count (for passing by reference)
    """
    made_guess = False
    
    for guess in attempts[attempt_count[0]]:
        if attempts[attempt_count[0]][-1].get_tag() == 'filled' or \
          made_guess is True or guess.get_color() == button.get_color():
            return None
    
        if guess.get_tag() == 'filled':
            continue

        guess.set_color(button.get_color())
        guess.set_tag('filled')
        guess.draw()
        button.set_color('white')
        button.draw()
        made_guess = True

def pass_click(x, y, buttons_list, attempts, attempt_count, 
               pegs, secret_code, name):
    """ 
    Handles on-click event.

    Args:
        x, y: float type of clicked coordinates.

        buttons_list:
            0: quit button
            1: reset button
            2: check button
            3 - 8: color buttons in the order of 
                   red, green, blue, yellow, purple, black

        attempts: Nested list of Circle objects indicating attempts.
            attempts[0][0]: first circle of attempt 1.
            ...
            attempts[9][3]: last circle of attempt 10.
    """
    
    # passing click for quit button:
    if buttons_list[0].is_clicked(x, y) == True:
        click_quit()

    # passing click for reset buttons
    if buttons_list[1].is_clicked(x, y) == True:
        click_reset(attempts, attempt_count, buttons_list[3:])

    # passing click for check buttons
    if buttons_list[2].is_clicked(x, y) == True:
        click_check(attempts, attempt_count, pegs, secret_code, 
                    buttons_list[3:], name)

    # passing click for color buttons
    for button in buttons_list[3:]:
        if button.is_clicked(x, y) == True:
            click_colored_buttons(button, attempts, attempt_count)

def initialize_leaderboard(filename):
    t.teleport(150, 200)
    t.write("BEST SCORES", font=("Helvetica", 18, "normal"))
    with open(filename, 'r') as infile: 
        for i, each in enumerate(infile):
            t.teleport(150, 150 - (i * 30))
            t.write(each, font=("Helvetica", 15, "normal"))

def update_leaderboard(filename, player_name, score):
    """ iterate through data in filename and update if there is a new best 
    score. 
    """
    # put in data from filename to leaderboard
    leaderboard = []
    with open(filename, 'r') as infile:
        # separate text line to list
        for index, line in enumerate(infile):
            leaderboard.append(line.split(":"))
            leaderboard[index][1] = leaderboard[index][1].strip()

    # insertion sort
    new_leaderboard = [[player_name, score]]
    for index, player in enumerate(leaderboard):
        if score < int(player[1]):
            new_leaderboard.append(player)
        elif score >= int(player[1]):
            temp = player
            new_leaderboard.append(new_leaderboard[-1])
            new_leaderboard[index] = temp

    with open(filename, 'w') as outfile:
        for i, each in enumerate(new_leaderboard):
            if i == 3:
                break
            outfile.write(f"{each[0]}:{each[1]}\n")

def main():
    """ Driver Function"""
    # Register .gifs as shapes
    try:
        register_shapes()    
    # raise FileNotFoundError if .gif file does not exist
    except:
        log_error(str(FileNotFoundError), "File Not Found")
        stamp_shapes(0, 0, 'file_error.gif')
        t.ontimer(t.bye, 6000)
        raise FileNotFoundError

    # Initialize gameboard
    screen = t.Screen()
    screen.screensize(720, 480)
    t.ht()
    t.speed(0)

    # Get player name
    player_name = t.textinput("YOUR NAME", "Enter Your name: ")

    # Get secret code
    secret_code = generate_code()

    # Initialize leaderboard
    draw_rectangle(120, 240, 240, 320)
    try: 
        initialize_leaderboard('leaderboard.txt')
        
    except FileNotFoundError:        
        # display visual error message
        stamp_shapes(240, 80, 'leaderboard_error.gif')
        
        # create new leaderboard.txt file
        with open('leaderboard.txt', 'w') as infile:
            pass

        # log error message
        log_error(FileNotFoundError, "Leaderboard.txt Not Found")


    # Initialize attempt board
    draw_rectangle(-360, 240, 480, 320)
    attempts = []
    pegs = []
    for _ in range(10):
        attempts.append([])
        pegs.append([])

    for row in range(5):
        for col in range(4):
            attempts[row].append(Circle(-320 + 40 * col, 200 - 40 * row))
            attempts[row][col].draw()
        for i in range(2):
            for j in range(2):
                pegs[row].append(Circle(-160 + (10 * j), 
                                        210 - (10 * i) - (40 * row), 5))
                pegs[row][-1].draw()

    for row in range(5):
        for col in range(4):
            attempts[5 + row].append(Circle(-120 + 40 * col, 200 - 40 * row))
            attempts[5 + row][col].draw()
        for i in range(2):
            for j in range(2):
                pegs[row + 5].append(Circle(40 + (10 * j), 
                                            210 - (10 * i) - (40 * row), 5))
                pegs[row+ 5][-1].draw()

    # Initialize guess board
    draw_rectangle(-360, -80, 720, 80)
    red_button = Circle(-300, -120, 20, 'black', 'red', 'red')
    red_button.draw()
    green_button = Circle(-240, -120, 20, 'black', 'green', 'green')
    green_button.draw()
    blue_button = Circle(-180, -120, 20, 'black', 'blue', 'blue')
    blue_button.draw()
    yellow_button = Circle(-120, -120, 20, 'black', 'yellow', 'yellow')
    yellow_button.draw()
    purple_button = Circle(-60, -120, 20, 'black', 'purple', 'purple')
    purple_button.draw()
    black_button = Circle(0, -120, 20, 'black', 'black', 'black')
    black_button.draw()
    check_button = Circle(120, -120, 30, tag='check button')
    stamp_shapes(check_button.get_x(), check_button.get_y(), "checkbutton.gif")
    reset_button = Circle(180, -120, 30, tag='reset button')
    stamp_shapes(reset_button.get_x(),reset_button.get_y(), "xbutton.gif")
    quit_button = Circle(300, -120, 30, tag='quit button')
    stamp_shapes(quit_button.get_x(), quit_button.get_y(), "quit.gif")

    buttons = [
        quit_button, reset_button, check_button, 
        red_button, green_button, blue_button,
        yellow_button, purple_button, black_button
        ]
    
    # set attempt_count as list to pass by reference
    attempt_count = [0]

    # onclick event handler
    screen.onclick(partial(pass_click, buttons_list=buttons, 
                        attempts=attempts, attempt_count=attempt_count,
                        pegs=pegs, secret_code=secret_code, name=player_name))
    t.mainloop()

if __name__ == "__main__":
    main()

"""

Milestone 8: Write design.txt: Write your design description. Do your final 
testing and any extra optional work (e.g. skinning your game). Wrap up any 
other outstanding task.

Release: Before 11:59pm, December 08th: Make a "staging area" with all the 
code and assets you need to run your game. Run the game ONE final time to make
sure it works and you haven't left anything out. Ensure the staging area has 
your design.txt document too (that's part of your grade). Double-triple check 
you have everything required for launch and - Ship It!
"""