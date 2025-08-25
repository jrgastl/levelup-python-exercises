# Level Up: Python - Coding Challenges

## Status
Completed! [Professional Certificate][url_finished]

## Welcome!

The idea of this repository is to demonstrate Python skills acquired while doing the ["OpenEDG Python Institute: Programming with Python Professional Certificate"][url_certificate].  
It contains a collection of Python coding challenges that are part of the Level Up: Python course in [LinkedIn Learning][url_course] by Barron Stone.  
Each script is self-contained and demonstrates a specific concept or programming technique.  

## Overview

Below is the general structure with a small description and summary of skills.  

| Challenge | Description | Brief summary of skills learned |
|-|-|-|
| 1 | Get prime factors of a number | For loops, list methods |
| 2 | Check if a word is palindrome | String methods |
| 3 | Sort words in a phrase | Regular expressions, join() method |
| 4 | Find all the positions of an element in a list | Recursion |
| 5 | Game to guess how many seconds have passed | Time module, input() function |
| 6 | Save and load dictionaries to a file | Reading and writing files, JSON module |
| 7 | Schedule another function | OS module, multiple arguments function |
| 8 | Send an e-mail with subject and message | smtplib module, MIMEText |
| 9 | Probabilities of each outcome of a set of dices | Random module, get() method |
|10 | Count the words of a text file and rank top 20 words | Expression patterns, list comprehensions |
|11 | Generate Diceware pass phrases | Reinforcing join() method, reading files and regular expressions |
|12 | Merge CSV files | csv module, DictWriter() method |
|13 | Solve a Sudoku | Backtracking, itertools |
|14 | Build a ZIP archive | zipfile module, pathlib module |
|15 | Download sequential files | urllib module, more regular expressions  |

## Folder structure  

With exception of the Challenge 8, to run the codes, please uncomment the last line (or lines) of each file and then execute the python command in bash.  

```bash
python "challenge_name.py"
```  

For Challenge 8, please follow instructions in the file.  

```plaintext
levelup-python-challenges/
├── hello.py                        # Simple hello world script
├── get_prime_factors.py            # Challenge 1
├── is_palindrome.py                # Challenge 2
├── sort_words.py                   # Challenge 3
├── index_all.py                    # Challenge 4
├── waiting_game.py                 # Challenge 5
├── save_a_dictionary.py            # Challenge 6
├── dictionaries/
    └── PythonDictionary.txt        # Output of Challenge 6
├── schedule_a_function.py          # Challenge 7 
├── sounds/
    └── Ring08.wav                  # Sound used in Challenge 7
├── send_an_email.py                # Challenge 8
├── simulate_dice.py                # Challenge 9
├── count_unique_words.py           # Challenge 10
├── texts/
    └── pg100.txt                   # Text used in Challenge 10
    └── diceware.wordlist.asc       # Ascii file used in Challenge 11
    └── el_diceware_numbered.txt    # Alternative txt file used in Challenge 11
├── generate_a_password.py          # Challenge 11
├── merge_csv_files.py              # Challenge 12
├── csv/
    └── class1.csv                  # CSV file created for Challenge 12
    └── class2.csv                  # CSV file created for Challenge 12
    └── all_students.csv            # Output of Challenge 12
├── solve_a_sudoku.py               # Challenge 13
├── build_a_zip_archive.py          # Challenge 14
├── zip/
    └── pics
        └── 480-360-sample.jpg      # JPG file used in Challenge 14
        └── logo.png                # PNG file used in Challenge 14
        └── python-logo-only.svg    # SVG file used in Challenge 14
    └── texts
        └── APPNOTE.TXT             # TXT file used in Challenge 14
├── download_sequential_files.py    # Challenge 15
├── downloads/                      # Folder to store the files from Challenge 15
├── README.md                       # This file
└── .gitignore                      # Ignored files
```

This repository used to contain files with the instructor code for reference. To avoid any copyright problems, I removed the files. The solutions can be found in the respective Linkedin Learning course.

[url_course]:https://www.linkedin.com/learning/level-up-python
[url_certificate]:https://www.linkedin.com/learning/paths/openedg-python-institute-programming-with-python-professional-certificate
[url_finished]:https://www.linkedin.com/learning/certificates/d18785f9637401e309fa7d9b3520fdeb5119905cb733f30a6a1e71c39e92bbbe?trk=share_certificate

Author: Ricardo Gastl
