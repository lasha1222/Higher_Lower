import random
from art import logo, vs
from data import data

def get_random_account():
    return random.choice(data)

def format_data(account):
    name = account['name']
    description = account['description']
    country = account['country']

    return f"{name}, a {description}, from {country}"

def check_answer(answer, a_followers_count, b_followers_count):
    if a_followers_count > b_followers_count:
        return answer == "a"
    else:
        return answer == "b"

def game():
    print(logo)

    scores = 0
    should_continue = True

    a_account = get_random_account()
    b_account = get_random_account()

    while should_continue:
        a_account = b_account
        b_account = get_random_account()

        while a_account == b_account:
            b_account = get_random_account()

        print(f"Compare A: {format_data(a_account)}")
        print(vs)
        print(f"Against B: {format_data(b_account)}")

        guess = input("Who has more followers: Type A or B: ").lower()
        a_followers_count = a_account['follower_count']
        b_followers_count = b_account['follower_count']
        is_correct = check_answer(guess, a_followers_count, b_followers_count)

        print(logo)
        if is_correct:
            scores += 1
            print(f"You are right! Current score {scores}")
        else:
            should_continue = False
            print(f"Wrong answer! Final score {scores}")

game()