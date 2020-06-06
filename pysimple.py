#import the package
import PySimpleGUI as sg 
#Choose the theme    
sg.theme('BluePurple') 

#define the layout
layout = [[sg.Text('Your typed characters appear here:'), 
           sg.Text(size=(15,1), key='-OUTPUT-')], 
          [sg.Input(key='-IN-')], 
          [sg.Button('Display'), sg.Button('Exit')]] 
  
window = sg.Window('Introduction', layout) 

#looping the event and the value
while True: 
    event, values = window.read() 
    print(event, values) 
      
    if event in  (None, 'Exit'): 
        break
      
    if event == 'Display': 
        # Update the "output" text element 
        # to be the value of "input" element 
        window['-OUTPUT-'].update(values['-IN-']) 

#closure
window.close() 
