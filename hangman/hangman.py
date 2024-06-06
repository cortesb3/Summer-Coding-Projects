import PySimpleGUI as sg 
from string import ascii_uppercase

class Hangman:
    def __init__(self) -> None:
        layout = [
            [
                self._build_canvas_frame(),
                self._build_letters_frame()
            ],
            [
                self._build_guessed_word_frame()
            ],
            [
                self._build_action_buttoms_frame()
            ],
        ]
        self._window = sg.Window(
            title="Hangman",
            layout=layout,
            finalize=True
        )
        self._canvas = self._window["-CANVAS-"]

    def read_event(self):
        event = self._window.read()
        event_id = event[0] if event is not None else None
        return event_id
    
    def close(self):
        self._window.close()

    def _build_canvas_frame(self):
        return sg.Frame(
            "Hangman",
            [
                [
                    sg.Graph(
                        key="-CANVAS-",
                        canvas_size=(200,400),
                        graph_bottom_left=(0,0),
                        graph_top_right=(200,400)
                    )
                ]
            ],
            font="Any 20",
        )
    
    def _build_letters_frame(self):
        # Initalizing the rows of letters to be used
        letter_groups = [
            ascii_uppercase[i : i +4 ]
            for i in range(0, len(ascii_uppercase), 4)
        ]
        # Creating the buttons
        letter_buttons = [
            [
                sg.Button(
                    button_text=f' {letter} ',
                    font="Open Sans 20",
                    border_width=0,
                    button_color=(None, sg.theme_background_color()),
                    key=f'-letter-{letter}-',
                    enable_events=True
                )
                for letter in letter_group
            ]
            for letter_group in letter_groups
        ]
        return sg.Column(
            [
                [
                    sg.Frame(
                        "Letters",
                        letter_buttons,
                        font="Any 20",
                    ),
                    sg.Sizer(),
                ]
            ]
        )
    
    def _build_guessed_word_frame(self):
        return sg.Frame(
            "",
            [
                [
                    sg.Text(
                        key="-DISPLAY-WORD-",
                        font="Open Sans 20"    
                    )
                ]
            ],
            element_justification="center"
        )
    
    def _build_action_buttons_frame(self):
        return sg.Fram(
            "",
            [
                [
                    sg.Sizer(h_pixels=90),
                    sg.Button(
                        button_text="New",
                        key="-NEW-",
                        font="Any 20"
                    ),
                    sg.Sizer(h_pixels=60),
                    sg.Button(
                        button_text="Restart",
                        key="-RESTART-",
                        font="Any 20"
                    ),
                    sg.Sizer(h_pixels=60),
                    sg.Button(
                        button_text="Quit",
                        key="-QUIT-",
                        font="Any 20"
                    ),
                    sg.Sizer(h_pixels=90)
                ]
            ],
            font="Any 20"
        )
    
    def _draw_scaffold(self):
        lines = [
            ((40, 55), (180, 55), 10),
            ((165, 60), (165, 365), 10),
            ((160, 360), (100, 360), 10),
            ((100, 365), (100, 330), 10),
            ((100, 330), (100, 310), 1),
        ]
        for *points, width in lines:
            self._canvas.DrawLine(*points, color="black", width=width)

    def _draw_hanged_man(self):
        line1 = [((40, 55), (180, 55), 10)]
        line2 = [((165, 60), (165, 365), 10)]
        line3 = [((160, 360), (100, 360), 10)]
        line4 = [((100, 365), (100, 330), 10)]
        line5 = [((100, 330), (100, 310), 1)]
        head = (100, 290)
        torso = [((100, 270), (100, 170))]
        left_arm = [
            ((100, 250), (80, 250)),
            ((80, 250), (60, 210)),
            ((60, 210), (60, 190)),
        ]
        right_arm = [
            ((100, 250), (120, 250)),
            ((120, 250), (140, 210)),
            ((140, 210), (140, 190)),
        ]
        left_leg = [
            ((100, 170), (80, 170)),
            ((80, 170), (70, 140)),
            ((70, 140), (70, 80)),
            ((70, 80), (60, 80)),
        ]
        right_leg = [
            ((100, 170), (120, 170)),
            ((120, 170), (130, 140)),
            ((130, 140), (130, 80)),
            ((130, 80), (140, 80)),
        ]
        body = [
            line1, line2, line3, line4, line5,
            torso,
            left_arm,
            right_arm,
            left_leg,
            right_leg,
        ]
        if self._wrong_guesses == 1:
            self._canvas.DrawCircle(
                head,
                20,
                line_color="red",
                line_width=2,
            )
        elif self._wrong_guesses > 1:
            for part in body[self._wrong_guesses - 2]:
                self._canvas.DrawLine(*part, color="red", width=2)

# Writing minimal event loop for hangman
if __name__ == "__main__":
    game = Hangman()
    # Event loop
    while True:
        event_id = game.read_event()
        if event_id in {sg.WIN_CLOSED}:
            break
    game.close()
