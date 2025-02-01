stone = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random
your_choice=input("Enter your choice : stone,paper or scissors\n")
your_choice.lower()
comp_choice_avail=["stone","paper","scissors"]
random= random.randint(0,2)
comp_choice=comp_choice_avail[random]
if(your_choice=="stone"):
    if(comp_choice=="scissors"):
        print("your choice\n"+ stone +"\n")
        print("computer choice\n"+ scissors +"\n")
        print("you won")
    elif(comp_choice=="stone"):
        print("your choice\n" + stone + "\n")
        print("computer choice\n" + stone + "\n")
        print("draw")
    elif(comp_choice=="paper"):
        print("your choice\n" + stone + "\n")
        print("computer choice\n" + paper + "\n")
        print("you lost")
elif(your_choice == "paper"):
    if (comp_choice == "scissors"):
        print("your choice\n" + paper + "\n")
        print("computer choice\n" + scissors + "\n")
        print("you lost")
    elif (comp_choice == "stone"):
        print("your choice\n" +paper + "\n")
        print("computer choice\n" + stone + "\n")
        print("you won")
    elif (comp_choice == "paper"):
        print("your choice\n" + paper + "\n")
        print("computer choice\n" + paper + "\n")
        print("draw")
elif(your_choice=="scissors"):
    if(comp_choice=="scissors"):
        print("your choice\n"+ stone +"\n")
        print("computer choice\n"+ scissors +"\n")
        print("draw")
    elif(comp_choice=="stone"):
        print("your choice\n" + stone + "\n")
        print("computer choice\n" + stone + "\n")
        print("you lost")
    elif(comp_choice=="paper"):
        print("your choice\n" + stone + "\n")
        print("computer choice\n" + paper + "\n")
        print("you won")
