'''
Author Notes:
I suddenly realized how poorly I implemented the input() function after checking the instructor solution. I didn't do big changes to my code so to keep the learning process documentation.
I only added some small things like, for example, the feedback in case the player gets the time 100% correct. Besides that, it was resourceful to understand a bit how to use the time module. 
'''
import time
import random

def waiting_game():
    seconds = random.randint(2,5)
    print(f'Time to achieve is {seconds} seconds')
    print('---Press Enter to Begin---')
    key_pressed = input()
    if key_pressed != None:
        start_time = time.time()
        print(f'Press Enter again after {seconds} seconds')
        key_pressed_again = input()
        if key_pressed_again != None:
            end_time = time.time()
    elapsed_time = end_time - start_time
    if elapsed_time > seconds:
        print(f'Elapsed time: {round(elapsed_time,3)} seconds. ({round(elapsed_time - seconds,3)} too slow)')
    elif elapsed_time < seconds:
        print(f'Elapsed time: {round(elapsed_time,3)} seconds. ({round(seconds - elapsed_time,3)} too fast)')
    elif elapsed_time == seconds:
        print(f'Elapsed time: {round(elapsed_time,3)} seconds. (Unbelievable!)')

# Please, uncomment the line below to execute the code with the example given
# waiting_game()
