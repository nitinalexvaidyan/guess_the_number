import random

def guess_the_number(high_num):
    low_num = 1
    feedback = ""
    while feedback != "c":
        if low_num == high_num:
            guess_num = low_num
            break
        guess_num = random.randint(low_num, high_num)
        feedback = input(f"The guessed number is {guess_num}. If the guessed number is correct enter 'C', if higher 'H' and if lower 'L' ").lower()
        if feedback == "l":
            low_num = guess_num + 1
        if feedback == "h":
            high_num = guess_num - 1
            
    print(f"Yay! Found the number !!! ... It is {guess_num}")
            

high_num = int(input("Please input the highest number in which the guess to be made between 1 and that number?"))
guess_the_number(high_num)