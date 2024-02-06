import turtle
import pandas

screen= turtle.Screen()
screen.title("U.S States Game")
image="blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)
turtle.penup()

guessed_States=0
data=pandas.read_csv("50_states.csv")
all_states= data.state.to_list()
states=[]
while len(states)<len((all_states)):
    answer_state = screen.textinput(title=f"{guessed_States}/50 Guess the state",prompt="What's another state's name?")
    answer_state= answer_state.title()


    if answer_state=="Exit":
          missing_states=[state for state in all_states if state not in states]
          new_data=pandas.DataFrame(missing_states)
          new_data.to_csv("states_to_learn.csv")                   
          break

    '''if answer_state=="Exit":
          missing_states=[]
          for state in all_states:
                if state not in states:
                      missing_states.append(state)
          new_data=pandas.DataFrame(missing_states)
          new_data.to_csv("states_to_learn.csv")                   
          break'''
    
    if answer_state in states:
          pass
    elif answer_state in all_states:
            ecem=turtle.Turtle()
            ecem.hideturtle()
            ecem.penup()
            state_data = data[data["state"] == answer_state]
            x_cor = int(state_data["x"])
            y_cor = int(state_data["y"])            
            ecem.goto([x_cor, y_cor])
            ecem.write(answer_state, align="left", font=("Arial", 8, "normal"))
            states.append(answer_state)
            guessed_States+=1
    if guessed_States==50:
          ecem.goto(0,0)
          ecem.color("green")
          ecem.write("Congrutations!! You guessed all the states!",font=("Arial", 30, "normal"))


