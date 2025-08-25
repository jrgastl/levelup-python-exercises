'''
Author Notes:
This time I wrote the challenge briefing before the code, which I understand is a good practice.
Besides that, the challenge video was slightly confusing on what exactly should be done. What the instructor said was slightly different from what was on the screen.
In the end, I created a second function to do what was written on the screen, that is, play a sound and write a message, but still did a general function according
to what he was saying, that is at a certain time print a string ('Howdy') on the screen. I enjoyed the exploration on how to play sounds in python.
It was a funny challenge.

Briefing:
Python function which sets an alarm that plays a sound and prints a message at a specified time.
Three inputs: event time, function and any number of arguments.
Sound file, printing a message at a specified time.
A call might look like this schedule_function(time.time()+1,print,'Howdy'): -> example given doesn't play the sound, but I added it anyway
'''
import time
import os

def alarm(sound_file,message):
    os.system('start' + sound_file)
    return print(message)

def schedule_function(set_time,user_function,*args):
    if set_time <= time.time():
        print('Desire time is in the past')
    else:
        print(f'{(user_function.__name__)}() scheduled  for {time.asctime(time.localtime(set_time))}')
        while set_time >= time.time():
            if set_time <= time.time():
                return user_function(*args)


# Please, uncomment the line below to execute the code with the example given
# schedule_function((time.time()+2),alarm,'./sounds/Ring08.wav','Good morning!')