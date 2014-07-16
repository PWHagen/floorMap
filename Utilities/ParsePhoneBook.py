__author__ = 'Patrick'
import json
import urllib.request
import re
from Utilities.Employee import *


employee_dict = dict()

for i in range(0, 26):  # Iterate over URLs for each letter (26 in the alphabet)
    #-----Use Count = 1000 so that the page does not get clipped which causes missing data in JSON--------#
    url = 'http://niweb-notes.natinst.com/operations/niphone.nsf/' \
          'FirstNameWeb?readviewentries&outputformat=JSON&OpenView&Start=1&Count=1000&Expand=' + str(i+1) + '#' + str(i+1)
    #-----Use Count = 1000 so that the page does not get clipped which causes missing data in JSON--------#

    page = urllib.request.urlopen(url)
    charset = page.info().get_param('charset', 'utf8')  # Determine the character set of the JSON
    data = page.read()
    data = data.decode(charset) # Decode the bytes to JSON string
    data = re.sub('(?!\\\\r)[\\\\].', '', data)  # JSON has bad escape characters fixed with this substitution
    decoded = json.loads(data)
    viewEntries = decoded['viewentry']  # All data broken down by letter
    view = viewEntries[i+1]['entrydata']  # Gives first person in a letter group
    x = i + 1
    while str(i+1) + '.' in viewEntries[x]['@position']:
        view = viewEntries[x]['entrydata']
        employee = Employee()
        employee.set_name(view[0]['text']['0'])  # Name JSON Field
        employee.set_phone_number(view[1]['text']['0'])  # Phone Number JSON Field
        employee.set_department(view[5]['text']['0'])  # Department JSON Field
        employee.set_cube(view[7]['text']['0'])  # Cube JSON Field
        employee_dict[employee.get_name()] = employee  # Eventually I will make this an entry to the DB

        x += 1  # Increment through array of names

name = input('Enter a name you would like to look up \n')
person = employee_dict[name]
print(person.get_name())
print(person.get_phone_number())
print(person.get_department())
print(person.get_cube())
