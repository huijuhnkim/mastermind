import unittest
from Circle import Circle
import mastermind_game as m

class TestCheck(unittest.TestCase):

    # testing code validation when check button is clicked
    def test_click_check(self):
        # test setup
        secret_code = ['red', 'black', 'blue', 'purple']
        
        attempts = [
            [Circle(fillcolor='red', tag='filled'),
             Circle(fillcolor='blue', tag='filled'),
             Circle(fillcolor='yellow', tag='filled'),
             Circle(fillcolor='black', tag='filled')]
            ]
        pegs = [
            [Circle(), Circle(), Circle(), Circle()]
        ]

        red_button = Circle(-300, -120, 20, 'black', 'red', 'red')
        green_button = Circle(-240, -120, 20, 'black', 'green', 'green')
        blue_button = Circle(-180, -120, 20, 'black', 'blue', 'blue')
        yellow_button = Circle(-120, -120, 20, 'black', 'yellow', 'yellow')
        purple_button = Circle(-60, -120, 20, 'black', 'purple', 'purple')
        black_button = Circle(0, -120, 20, 'black', 'black', 'black')
        colored_buttons = [red_button, green_button, blue_button, 
            yellow_button, purple_button, black_button]
        m.click_check(attempts,[0], pegs, secret_code, colored_buttons, None)

        self.assertTrue(pegs[0][0].get_color() == 'black')
        self.assertTrue(pegs[0][1].get_color() == 'red')
        self.assertTrue(pegs[0][2].get_color() == 'red')
        self.assertTrue(pegs[0][3].get_color() == 'white')

if __name__ == "__main__":
    unittest.main(verbosity=5)
