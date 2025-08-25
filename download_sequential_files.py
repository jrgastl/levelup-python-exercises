'''
Author Notes:
My approach for this challenge was to cover as much cases as possible, although I still missed the case where a file could be missing in the server and
the case where the directory is non existent. The instructors solution follows a slightly different approach. It doesn't try to find all the numbers that could iterate. 
But it includes indeed the case where a file is missing and it creates the directory if it is non existent. I also prefer more the instructor approach to breakdown the url,
with the os module.

Briefing:
Write a function to download and save a sequence of files.
Input: URL for first item, output directory path

Example:
>>> download_files('http://699340.youcanlearnit.net/image001.jpg','./images' )

Successfully downloaded
http://699340.youcanlearnit.net/image001.jpg

Successfully downloaded
http://699340.youcanlearnit.net/image002.jpg

...

Successfully downloaded
http://699340.youcanlearnit.net/image050.jpg

Could not retrive
http://699340.youcanlearnit.net/image051.jpg

Documentation:
https://realpython.com/python-download-file-from-url/
https://docs.python.org/3/library/re.html#frie09
https://docs.python.org/3/howto/regex.html#regex-howto
https://docs.python.org/3/library/re.html
'''
from urllib.error import URLError
from urllib.request import urlopen,urlretrieve
from urllib.parse import urlparse,urlunparse
from pathlib import Path
import re

def check_url(url):
    try:
        with urlopen(url) as u:
            return True
    except URLError:
        return False
    
def download_and_message(url, output_path): #Download the file and print the message
    url_path = urlparse(url).path
    path = Path(output_path) / url_path.lstrip('/')
    urlretrieve(url,path)
    print(f'Successfully downloaded\n{url}')

def increment_url_path(url_path, start, end):
    number = int(url_path[start:end]) + 1 #Get the value of the string
    str_number = str(number).zfill(end - start) #Return the value to the string format with the proper number of zeros
    url_path = url_path[:start] + str_number + url_path[end:] #Reassemble the url path with the new number
    return url_path

def set_url_path_to_1(url_path, start, end):
    str_number = '1'.zfill(end - start) #Return the value to the string format with the proper number of zeros
    url_path = url_path[:start] + str_number + url_path[end:] #Reassemble the url path with the new number
    return url_path

def download_files(url,output_path):
    
    #Finding valid iterator:

    url_scheme, url_netloc, url_path, url_params, url_query, url_fragment  = urlparse(url) # Although I don't use these variables in the example, I tried to be more general and cover as much cases as possible
    url_path_positions = re.finditer(r'[0-9]+', url_path) #Parse the part of the url that has the file path (in the example "/image001.jpg") and get all the numbers positions
    positions_span = [number.span() for number in url_path_positions] #Separate the position for numbers
    for span in positions_span: #Go through every potential valid iterator and try to download the second image
        start, end = span
        next_path = increment_url_path(url_path,start,end)
        second_url = urlunparse([url_scheme, url_netloc, next_path, url_params, url_query, url_fragment]) #Reassemble the url
        if check_url(second_url): #Check if it is possible to download the second image
            if int(url_path[start:end]) != 1: #If number is different than one, resets it to 1
                url_path = set_url_path_to_1(url_path,start,end)
                url = urlunparse([url_scheme, url_netloc, url_path, url_params, url_query, url_fragment])
                next_path = increment_url_path(url_path,start,end)
                second_url = urlunparse([url_scheme, url_netloc, next_path, url_params, url_query, url_fragment])
         # Start download of first files with valid iterators:
            download_and_message(url,output_path)
            download_and_message(second_url,output_path)
            # Continue the download
            while True:
                next_path = increment_url_path(next_path,start,end)
                next_url = urlunparse([url_scheme, url_netloc, next_path, url_params, url_query, url_fragment])
                if check_url(next_url):
                    download_and_message(next_url,output_path)
                else:
                    break
            print(f'Could not retrieve!\n{next_url}')
            break
    else:
        print(f'Failed to download from {url}')

# Please, uncomment the line below to execute the code with the example given
# download_files('http://699340.youcanlearnit.net/image001.jpg','./downloads')