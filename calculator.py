from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
import math as m

# root widget
class ProvaBoxLayout(BoxLayout):
    def __init__(self):
        super(ProvaBoxLayout, self).__init__()
        self.screen_string = "0"
        self.calc_string = "0"

    def screen_update(self):
        """This function updates what appears on screen."""
        self.ids.screen.text = self.screen_string

    def add_to_string(self, s_val, c_val):
        """This function adds s_val to the showable string, and c_val to the evaluable string, then calls a screen update."""
        if self.screen_string == "0":
            self.screen_string = s_val
            self.calc_string = c_val
        elif self.screen_string == "ERROR!":
            pass
        else:
            self.screen_string += s_val
            self.calc_string += c_val
        self.screen_update()

    def clear_strings(self):
        """This function resets the two strings, then calls a screen update."""
        self.screen_string = "0"
        self.calc_string = "0"
        self.screen_update()

    def calculate(self):
        """This function calculates the result, then calls a screen update."""
        try:
            result = eval(self.calc_string)
        except:
            result = "ERROR"
        self.screen_string = str(result)
        self.screen_update()

# app class
class CalculatorApp(App):
    def build(self):
        return ProvaBoxLayout()

if __name__ == "__main__":
    CalculatorApp().run()
