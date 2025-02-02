import random
from art import logo


cards=['11','1','2','3','4','5','6','7','8','9','10','10','10','10']

def sum_list(list1):
    sum1=0
    for item in list1:
        sum1 = sum1 + int(item)
    return int(sum1)

def add_in_list(list1):
    x = random.randint(0, 12)
    element = cards[x]
    list1.append(element)

    while sum_list(list1) > 21 and "11" in list1:
        list1[list1.index("11")] = "1"  # Convert Ace from 11 to 1


def evaluate(sum1,sum2):
    if sum1>21:
        print("You crossed 21 ,you lost")
    elif sum2>21:
        print("computer crossed 21 ,You winnnnn")
    elif sum1==sum2:
        print("Match draw")
    elif sum1>sum2:
        print("You winnnnnn")
    else:
        print("you lost")


def blackjack():
    choice = input("Do you want to play game of Blackjack? type 'y' or 'n' ").lower()
    print(logo)
    if choice=="y":
        player_list = []
        comp_list = []
        add_in_list(player_list)
        add_in_list(player_list)
        add_in_list(comp_list)
        add_in_list(comp_list)
        comp_curr_sum = int(sum_list(comp_list))
        while comp_curr_sum<16:
            add_in_list(comp_list)
            comp_curr_sum = int(sum_list(comp_list))
        keep_going=True
        while keep_going:
            curr_sum = int(sum_list(player_list))
            print(f"Your cards :{player_list},current sum: {curr_sum}")
            print(f"First card of computer is {comp_list[0]}")
            more_card=input("Type 'y' to get another card ,type 'n' to pass\n")
            if more_card=="y":
                add_in_list(player_list)
            else:
                keep_going=False
        sum1=int(sum_list(player_list))
        sum2=int(sum_list(comp_list))
        print(f"Your cards :{player_list},your total: {sum1}")
        print(f"computer's cards :{comp_list},computer's total: {sum2}")
        evaluate(sum1,sum2)
        blackjack()
    else:
        return

blackjack()
