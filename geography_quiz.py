import random


europe_capitals = {
    "slovenia": "ljubljana",
    "croatia": "zagreb",
    "bosnia & herzegovina": "sarajevo",
    "serbia": "belgrade",
    "north macedonia": "skopje",
    "greece": "athens",
    "russia": "moscow",
    "austria": "vienna",
    "hungary": "budapest",
    "italy": "rome",
    "france": "paris",
    "sweden": "stockholm",
    "finland": "helsinki",
    "germany": "berlin",
    "spain": "madrid",
    "poland": "warsaw",
    "portugal": "lisbon",
    "slovakia": "bratislava",
    "czech republic": "prague",
    "netherlands": "amsterdam",
    "belgium": "brussels",
}


asia_capitals = {
    "china": "beijing",
    "india": "new delhi",
    "iraq": "baghdad",
    "iran": "tehran",
    "malaysia": "kuala lumpur",
    "vietnam": "hanoi",
    "thailand": "bangkok",
    "taiwan": "taipei",
    "saudi arabia": "riyadh",
    "south korea": "seoul",
    "united arab emirates": "abu dhabi",
    "nepal": "kathmandu",
    "north korea": "pyongyang",
    "japan": "tokyo",
    "qatar": "doha",
    "syria": "damascus",
    "philippines": "manila",
    "pakistan": "islamabad",
    "oman": "muscat",
    "singapore": "singapore",
    "afghanistan": "kabul",
}


america_capitals = {
    "usa": "washington d.c.",
    "canada": "ottawa",
    "cuba": "havana",
    "jamaica": "kingston",
    "mexico": "mexico city",
    "dominican republic": "santo domingo",
    "peru": "lima",
    "chile": "santiago",
    "bolivia": "la paz",
    "brazil": "brasilia",
    "colombia": "bogota",
    "venezuela": "caracas",
    "ecuador": "quito",
    "uruguay": "montevideo",
    "paraguay": "asuncion",
    "argentina": "buenos aires",
}


def game_intro():
    print("""
    Hello and welcome to Geography quiz!
    Choose between three continents (Europe, Asia or America) to test your knowledge about capital's cities.
    You will answer on 10 questions.
    Type 'quit' during quiz if you want to end the quiz.
    """)
    while True:
        choose_continent = input("Enter a continent (europe, asia or america) to start a quiz: ")
        if choose_continent.lower().strip() == "europe":
            check_capital(europe_capitals)
        elif choose_continent.lower().strip() == "asia":
            check_capital(asia_capitals)
        elif choose_continent.lower().strip() == "america":
            check_capital(america_capitals)
        else:
            print("Select right continent!")
            continue


def check_capital(capital_city):

    correct_answer = 0

    i = 1
    while i <= 10:

        pick_random_country = random.choice(list(capital_city.keys()))
        print(f"Game: What is a capital city of {pick_random_country.title()}?")

        answer = input("User: ")

        if answer.lower().strip() == "quit":
            break
        else:
            if answer.lower().strip() == capital_city[pick_random_country]:
                print("That is correct!")
                correct_answer += 1
            else:
                print("Your answer is not correct!")

            capital_city.pop(pick_random_country)
            i += 1

    print_scores(correct_answer)
    play_again()


def print_scores(true_answer):

    print("-" * 50)
    print(f"You guessed {true_answer} out of 10 questions which is {(true_answer/10) * 100}%.")
    print("-" * 50)


def play_again():

    print("\nEnter 'Yes' to play again.")
    prompt = input("Would you like to play again? ")

    if prompt.lower().strip() == "yes":
        game_intro()
    else:
        exit()


game_intro()