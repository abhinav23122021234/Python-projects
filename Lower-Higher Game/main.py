is_right=True
from art import logo,vs
from game_data import data
import random
account_A=random.choice(data)
account_B=random.choice(data)
while account_A==account_B:
    account_B=random.choice(data)

def format_line(account):
    account_name=account["name"]
    account_description=account["description"]
    account_origin=account["country"]
    return f"{account_name}, {account_description} from {account_origin}"
print(len(data))
score=0
while is_right:
    print(logo)
    user1=format_line(account_A)
    user2=format_line(account_B)
    if score!=0:
        print(f"you're right : Current score {score}")

    print(f"Compare A: {user1}")
    print(vs)
    print(f"Against B: {user2}")
    choice=input(f"Who has more followers ? Type 'A' or 'B' ").lower()
    if choice=='a' and account_A["follower_count"]>account_B["follower_count"]:
        score+=1
        account_A = account_B
        account_B = random.choice(data)
    elif choice=='b' and account_A["follower_count"]<account_B["follower_count"]:
        score+=1
        account_A=account_B
        account_B = random.choice(data)
    else:
        print(f"You're wrong : Final score {score}")
        is_right=False
