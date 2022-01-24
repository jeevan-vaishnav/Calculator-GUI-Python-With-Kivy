from time import perf_counter
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window


# Set the app size
Window.size = (500, 700)

# Load the exernal kv file
Builder.load_file('calckv.kv')


class MyLayout(Widget):

    # clear function to use clear the text input box
    def clear(self):
        self.ids.cal_input.text = "0"

    # create a function to remove text box from last character
    def remove(self):
        prior = self.ids.cal_input.text
        # remove the last item in the text box
        prior = prior[:-1]
        # output back to the text box
        self.ids.cal_input.text = prior
    # create button function

    def button_press(self, button):
        # create variable that containe whatever in container

        prior = self.ids.cal_input.text
        if "Error" in prior:
            prior = ""
            # if determine if 0 is setting there
        if prior == "0":
            self.ids.cal_input.text = ""
            self.ids.cal_input.text = f"{button}"
        else:
            self.ids.cal_input.text = f"{prior}{button}"

    # Create function to make text box positive or negiative no

    def pos_neg(self):
        prior = self.ids.cal_input.text

        # Text to see if there 's a - sign or + sign
        if "-" in prior:
            self.ids.cal_input.text = f'{prior.replace("-","")}'
        else:
            self.ids.cal_input.text = f'-{prior}'
    # create decimal function

    def dot(self):
        prior = self.ids.cal_input.text

        # Split out text box by+
        num_list = prior.split("+")

        if "+" in prior and "." not in num_list[-1]:
            # Add a decimal to the end of the text
            prior = f"{prior}."
            self.ids.cal_input.text = prior
        elif "." in prior:
            pass
        else:
            # Add a decimal to the end of the text
            prior = f"{prior}."
            self.ids.cal_input.text = prior
    # lets create addition function

    def math_sign(self, sign):
        # create variable that container whateve in container
        prior = self.ids.cal_input.text
        # slap a puls sign to the text
        self.ids.cal_input.text = f"{prior}{sign}"

    # def divided(self):
    #     # create variable that container whateve in container
    #     prior = self.ids.cal_input.text
    #     # slap a puls sign to the text
    #     self.ids.cal_input.text = f"{prior}/"

    # def multiply(self):
    #     # create variable that container whateve in container
    #     prior = self.ids.cal_input.text
    #     # slap a puls sign to the text
    #     self.ids.cal_input.text = f"{prior}*"

    # def substr(self):
    #     # create variable that container whateve in container
    #     prior = self.ids.cal_input.text
    #     # slap a puls sign to the text
    #     self.ids.cal_input.text = f"{prior}-"

    # create equsl to function

    def eqauls(self):
        prior = self.ids.cal_input.text
        # the evel the math from the text box
        try:
            answer = eval(prior)
            self.ids.cal_input.text = str(answer)
        except:
            self.ids.cal_input.text = "Error"

           # Addition
          # if "+" in prior:
          #     num_li = prior.split("+")
          #     answer = 0.0
          #     # loop thru our list
          #     for number in num_li:
          #         answer = answer + float(number)
          #     # print the asnwer in the txt box
          #     self.ids.cal_input.text = str(answer)


class CalculatorApp(App):
    def build(self):

        return MyLayout()


if __name__ == "__main__":
    CalculatorApp().run()
