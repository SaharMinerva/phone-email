# Phone Number and Email Address Extractor
#! python3
# phoneAndEmail.py - Finds phone numbers and email addresses on the clipboard.
import re
import pyperclip
phoneRegex = re.compile(r'''(
(\d{3} | \(\d{3}\))? #area code
(\s|-|\.)?  #seperator
(\d{3}) #first 3 digits
(\s|-|\.) #separator
(\d{4})  # last 4 digits
(\s*(ext|x|ext.)\s*(\d{2,5}))?  # extension
)''',re.VERBOSE)
# Create Email regex
emailRegex = re.compile(r"""
[\w\d]+
@
[\w]
(\.[\w]{2,4})
""",re.VERBOSE |re.IGNORECASE)
# Find matches in clipboard text.
text = str(pyperclip.paste())
matches = []
for groups in phoneRegex.findall(text):
    phoneNum = '-'.join([groups[1],groups[3],groups[5]])
    if groups[8] !='':
        phoneNum += ' x' + groups[8]
    matches.append(phoneNum)
for groups in emailRegex.findall(text):
    matches.append(groups[0])

# Copy results to the clipboard.
"""
If no phone numbers or email addresses were found, the program should inform the user
"""
if len(matches) > 0:
    pyperclip.copy('\n'.join(matches))
    print('Copied to clipboard: ')
    print('\n'.join(matches))
else:
    print('No phone numbers or email addresses found.')