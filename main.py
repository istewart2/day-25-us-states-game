import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

data = pandas.read_csv("./50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50 States Guessed",
                                    prompt="Enter another state: ")

    answer_title_case = answer_state.title()

    if answer_title_case == "Exit":
        missing_states = [state for state in all_states if state not in guessed_states]
        missing_states_dataframe = pandas.DataFrame(missing_states)
        missing_states_dataframe.to_csv("missing_states.csv")
        break

    duplicate_answer = answer_title_case in guessed_states
    if duplicate_answer:
        continue

    state_row = data[data.state == answer_title_case]

    if not state_row.empty:
        guessed_states.append(state_row.state.item())
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        t.setposition(int(state_row.x), int(state_row.y))
        t.write(answer_title_case, font=("Arial", 12, "bold"))