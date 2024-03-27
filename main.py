import turtle  # Importing the turtle module for graphics
import pandas  # Importing pandas for data manipulation

# Creating a turtle screen
screen = turtle.Screen()
screen.title("Africa Countries Game")

# Adding the image of Africa map as a shape
image = "africaMap.gif"
screen.addshape(image)
turtle.shape(image)

# Setting up game variables
game_is_on = True
num_of_guesses = 0

# Loading data of African countries from CSV file
data = pandas.read_csv("african_countries.csv")
all_countries = data.Country.to_list()  # Extracting country names from the DataFrame

# Main game loop
while game_is_on:

    # Prompting the user to input a country name
    user_answer = turtle.textinput(title=f"({num_of_guesses}/50) Guess The Country", prompt="Enter a county name"
                                   ).title()

    # Checking if the user wants to exit the game
    if user_answer == "Exit":
        break

    # Checking if the guessed country is in the list of all countries
    if user_answer in all_countries:
        # Creating a turtle to mark the guessed country on the map
        t = turtle.Turtle()
        t.penup()
        t.hideturtle()

        # Getting data of the guessed country
        country_data = data[data.Country == user_answer]

        # Moving the turtle to the coordinates of the guessed country and marking its name
        t.goto(int(country_data.x), int(country_data.y))
        t.write(f"📍{country_data.Country.item()}", font=('Arial', 8, 'bold'))

        # Incrementing the number of correct guesses
        num_of_guesses += 1
    # Ending the game if the number of guesses reaches 50
    elif num_of_guesses == 50:
        game_is_on = False

# Allowing the screen to stay open until closed by the user
screen.mainloop()
