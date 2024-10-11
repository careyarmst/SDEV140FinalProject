# Program Title: SQL Script output parser
# Author: Carey Armstrong IDE: Pycharm Professional Edition
# Date: 2024-10-11 Version: 12.0
# Purpose: This program is designed to get two files from the user - one is the database keywords
# and the other is the SQL script output to parse. After getting the two files, the program
# processes the file and picks out the lines in the output file that contain the keywords.
# Finally, the script sends the output of the found lines both to the screen in a window and also
# to a text file.
# Pseudocode: (1) Ask the user to specify the keyword file (2) Ask the user for the script output file
# (3) Validate that the files exit and are text files, if not exit the program (4) Find the lines in the SQL database
# output file that match the keywords (5) produce the results in a text file (6) produce the results in a window.

# Import the pysimplegui module and the os module and set the overall theme for pysimplegui
import PySimpleGUI as sg
import os
sg.theme('Material 1')

# Display the window to get the files to process
def getdatawin():
    layout = [[sg.Text('Enter the two files - 1st file is the keywords, the 2nd file is the script to parse')],
              [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse(key="-FILE_PATH1-")],
              [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse(key="-FILE_PATH2-")],
              [sg.Button('Submit'), sg.Button('Get Output Results in Window'), sg.Button('Exit')]]
    return sg.Window('Parse DB script output', layout, finalize=True)

# Process the two files; values[0] and values[1] are the pysimplegui dictionary entries for the
# file paths entered in the getdatawin() function.

def text_operations():
# Try/except block if the file entered is empty
    try:
        with open(values[0], 'r') as db_keywords:
            if not values[0].endswith(".txt"):
    # Reject the file if not a .txt file and exit
                print(f"Rejecting {values[0]}: not a .txt file")
                exit(1)
            db_keywords = [line.strip() for line in db_keywords]
    except FileNotFoundError:
        print("No file entered")
        exit(1)
# Try/except block if the file entered is empty
    try:
        with open(values[1], 'r') as db_output:

# Reject the file if it's not a text file and exit
            if not values[1].endswith(".txt"):
                print(f"Rejecting {values[1]}: not a .txt file")
                exit(1)
        # Specify the text output file.
            results_out = 'outputdb.txt'
            with open(results_out, mode='w', encoding='UTF-8') as outputdb:
                for line in db_output:
            # Remove lines that you don't want - these lines don't add value for the user in the output
                    if 'SERVER_ROLE' not in line and 'DATABASE_ROLE' not in line and '0x' not in line:
                        if any(db_keyword in line for db_keyword in db_keywords):
                            print(line, file=outputdb)
        # Print message to user that the file is done processing
                print("DONE PROCESSING")
    except FileNotFoundError:
        print("No file entered")
        exit(1)
# Open the output file to use in the window
def getresults():
    with open('outputdb.txt', 'r') as retresult:
        return retresult.read()
# Produce the window with the output results if the user clicks "Get Output Results"
def trywinout():
    outputwin = getresults()
    return sg.easy_print(outputwin, size=(300, 600), text_color='white', background_color='dark blue')

#  First statement opens the 1st window, the event loop processes the functions of the
#  submit button to parse the data and display the output window.
window1, window2 = getdatawin(), None
while True:
    window, event, values = sg.read_all_windows()
    if event == sg.WIN_CLOSED or event == 'Exit':
        window.close()
        if window == window2:  # if closing win 2, mark as closed
            window2 = None
        elif window == window1:  # if closing win 1, exit program
            break
    elif event == 'Submit':
        text_operations()
    elif event == 'Get Output Results in Window' and not window2:
        window2 = trywinout()
window.close()
