#Fill in a letter template given below with name and date 
# letter = ''' Dear <|Name|>, You are selected! <|Date|>'''

letter = '''
Dear <|NAME|>,
Greetings from Root Solutions. I am happy to tell you about your selection.
You are selected!
Have a great day ahead!
Thanks and regards,
Root.
Date: <|DATE|>
'''
name = input("Enter your name:\n")
date = input("Enter Date:\n")
letter = letter.replace("<|NAME|>",name)
letter = letter.replace("<|DATE|>",date)
print(letter)