import tkinter as tk

LARGE_FONT_STYLE = ("Arial", 40, "bold")
SMALL_FONT_STYLE = ("Arial", 16)
LIGHT_GRAY = "#F5F5F5"
LABEL_COLOR = "#25265E"
DIGIT_FONT_STYLE = ("Arial", 24, "bold")

LIGHT_BLUE = "#CCEDFF"
OFF_WHITE = "#F8F8F5"
DEFAULT_FONT_STYLE = ("Arial", 20)
WHITE = "#ffffff"


class Calculator:
    def __init__(self):
        self.window = tk.Tk()
        self.window.geometry("475x667")
        self.window.title("Calculator")
        self.window.resizable(width=0, height=0)

        self.total_expression = ""
        self.current_expression = ""
        self.display_frame = self.create_display_frame()

        self.total_label, self.label = self.create_display_labels()

        self.digits = {
            7: (2, 1), 8: (2, 2), 9: (2, 3),
            4: (3, 1), 5: (3, 2), 6: (3, 3),
            1: (4, 1), 2: (4, 2), 3: (4, 3),
            0: (5, 2), ".": (5, 3),
        }

        self.operations = {"/": "\u00F7", "*": "\u00D7", "-": "-", "+": "+"}
        self.buttons_frame = self.create_buttons_frame()

        self.buttons_frame.rowconfigure(0, weight=1)
        for x in range(1, 5):
            self.buttons_frame.rowconfigure(x, weight=1)
            self.buttons_frame.columnconfigure(x, weight=1)

        self.create_digit_buttons()
        self.create_operator_buttons()
        self.create_special_buttons()
        self.bind_keys()

    def create_special_buttons(self):
        self.create_clear_button()
        self.create_cleare_button()
        self.create_backspace_button()
        self.create_equals_button()
        self.create_sqrt_button()
        self.create_square_button()
        self.create_percentage_button()
        self.create_overx_button()
        self.create_plus_or_minus_button()

    def bind_keys(self):
        self.window.bind("<Return>", lambda event: self.evaluate())
        for key in self.digits:
            self.window.bind(str(key), lambda event, digit=key: self.add_to_expression(digit))

        for key in self.operations:
            self.window.bind(key, lambda event, operator=key: self.append_operator(operator))

    def create_display_labels(self):
        total_label = tk.Label(self.display_frame, text=self.total_expression, anchor=tk.E, bg=LIGHT_GRAY,
                               fg=LABEL_COLOR, padx=24, font=SMALL_FONT_STYLE)
        total_label.pack(expand=True, fill="both")

        label = tk.Label(self.display_frame, text=self.current_expression, anchor=tk.E, bg=LIGHT_GRAY,
                         fg=LABEL_COLOR, padx=24, font=LARGE_FONT_STYLE)
        label.pack(expand=True, fill="both")

        return total_label, label

    def create_display_frame(self):
        frame = tk.Frame(self.window, height=221, bg=LIGHT_GRAY)
        frame.pack(expand=True, fill="both")
        return frame

    def add_to_expression(self, value):
        self.current_expression += str(value)
        self.update_label()

    def create_digit_buttons(self):
        for digit, grid_value in self.digits.items():
            button = tk.Button(self.buttons_frame, text=str(digit), bg=WHITE, fg=LABEL_COLOR, font=DIGIT_FONT_STYLE,
                               borderwidth=0, command=lambda x=digit: self.add_to_expression(x))
            button.grid(row=grid_value[0], column=grid_value[1], sticky=tk.NSEW)

    def append_operator(self, operator):
        self.current_expression += operator
        self.total_expression += self.current_expression
        self.current_expression = " "
        self.update_total_label()
        self.update_label()

    def clear(self):
        self.current_expression = " "
        self.total_expression = " "
        self.update_total_label()
        self.update_label()

    def cleare(self):
        self.current_expression = " "
        self.update_total_label()
        self.update_label()

    def backspace(self):
        self.current_expression = self.current_expression[:-1]
        self.update_total_label()
        self.update_label()

    def create_operator_buttons(self):
        i = 1
        for opr, symbol in self.operations.items():
            button = tk.Button(self.buttons_frame, text=symbol, bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                               borderwidth=0, command=lambda x=opr: self.append_operator(x))
            button.grid(row=i, column=4, sticky=tk.NSEW)
            i += 1

    def percentage_button(self):
        per = str(eval(f"{self.current_expression}*0.01"))
        self.current_expression = str(eval(f"({self.total_expression}+1)*{per}"))
        self.update_label()

    def create_percentage_button(self):
        button = tk.Button(self.buttons_frame, text="\u0025", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.percentage_button)
        button.grid(row=0, column=1, sticky=tk.NSEW)

    def plus_or_minus_button(self):
        self.current_expression = str(eval(f"{self.current_expression} * -1"))
        self.update_label()

    def create_plus_or_minus_button(self):
        button = tk.Button(self.buttons_frame, text="\u00B1", bg=WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.plus_or_minus_button)
        button.grid(row=5, column=1, sticky=tk.NSEW)

    def create_cleare_button(self):
        button = tk.Button(self.buttons_frame, text="CE", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.cleare)  # Need to create a command
        button.grid(row=0, column=2, sticky=tk.NSEW)

    def create_clear_button(self):
        button = tk.Button(self.buttons_frame, text="C", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.clear)
        button.grid(row=0, column=3, sticky=tk.NSEW)

    def create_backspace_button(self):
        button = tk.Button(self.buttons_frame, text="\u2906", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.backspace)
        button.grid(row=0, column=4, sticky=tk.NSEW)

    def square(self):
        self.current_expression = str(eval(f"{self.current_expression}**2"))
        self.update_label()

    def create_square_button(self):
        button = tk.Button(self.buttons_frame, text="x\u00b2", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.square)
        button.grid(row=1, column=2, sticky=tk.NSEW)

    def sqrt(self):
        self.current_expression = str(eval(f"{self.current_expression}**0.5"))
        self.update_label()

    def create_sqrt_button(self):
        button = tk.Button(self.buttons_frame, text="\u221ax", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.sqrt)
        button.grid(row=1, column=3, sticky=tk.NSEW)

    def overx(self):
        self.total_expression += "1 \u00F7 " + self.current_expression
        self.current_expression = str(eval(f"1/{self.current_expression}"))
        self.update_total_label()
        self.update_label()

    def create_overx_button(self):
        button = tk.Button(self.buttons_frame, text="\u00b9\u2044\u2093", bg=OFF_WHITE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.overx)
        button.grid(row=1, column=1, sticky=tk.NSEW)

    def evaluate(self):
        self.total_expression += self.current_expression
        self.update_total_label()
        try:

            self.current_expression = str(eval(self.total_expression))

            self.total_expression = " "
        except Exception as e:
            self.current_expression = "Math Error"
        finally:
            self.update_label()

    def create_equals_button(self):
        button = tk.Button(self.buttons_frame, text="=", bg=LIGHT_BLUE, fg=LABEL_COLOR, font=DEFAULT_FONT_STYLE,
                           borderwidth=0, command=self.evaluate)
        button.grid(row=5, column=4, sticky=tk.NSEW)

    def create_buttons_frame(self):
        frame = tk.Frame(self.window)
        frame.pack(expand=True, fill="both")
        return frame

    def update_total_label(self):
        expression = self.total_expression
        for operator, symbol in self.operations.items():
            expression = expression.replace(operator, f' {symbol}')
        self.total_label.config(text=expression)

    def update_label(self):
        self.label.config(text=self.current_expression[:11])

    def run(self):
        self.window.mainloop()


if __name__ == "__main__":
    calc = Calculator()
    calc.run()