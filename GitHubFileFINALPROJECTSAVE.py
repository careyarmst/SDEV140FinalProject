import PySimpleGUI as sg

sg.theme('Light Blue 2')

layout = [[sg.Text('Enter the two files - 1st file is the keywords, the 2nd file is the script to parse')],
          [sg.Text('File 1', size=(8, 1)), sg.Input(), sg.FileBrowse(key="-FILE_PATH1-")],
          [sg.Text('File 2', size=(8, 1)), sg.Input(), sg.FileBrowse(key="-FILE_PATH2-")],
          [sg.Submit(), sg.Cancel()]]

window = sg.Window('Parse DB script output', layout)

def text_operations():
    with open((values["-FILE_PATH1-"]), 'r') as db_keywords:
        db_keywords = [line.strip() for line in db_keywords]

    with open((values["-FILE_PATH2-"]), 'r') as db_output:
        results_out = 'outputdb.txt'
        with open(results_out, mode='w', encoding='UTF-8') as outputdb:
            for line in db_output:
                if 'SERVER_ROLE' not in line and 'DATABASE_ROLE' not in line and 'WINDOWS_USER' not in line:
                    if any(db_keyword in line for db_keyword in db_keywords):
                       print(line, file=outputdb)
        print("DONE PROCESSING")

event, values = window.read()
if event == sg.WIN_CLOSED:
   window.close()
if event == 'Submit':
   text_operations()

