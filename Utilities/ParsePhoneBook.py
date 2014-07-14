__author__ = 'Patrick'
import json
import urllib.request
import re
from Utilities.Employee import *


url = 'http://niweb-notes.natinst.com/operations/niphone.nsf/FirstNameWeb?readviewentries&outputformat=JSON&OpenView&Start=20.480&Count=1000&Expand=20#20'
f = urllib.request.urlopen(url)
charset = f.info().get_param('charset', 'utf8')
print(charset)
data = f.read()
data = data.decode(charset)
data = re.sub('(?!\\\\r)[\\\\].', '', data)
decoded = json.loads(data)
print(json.dumps(data, indent=4))
viewEntries = decoded['viewentry']
view = viewEntries[20]['entrydata']
info = view[0]['text']
print(info['0'])
print()
employee_dict = dict()
for i in range(0, 26):
    print (i)
    url = 'http://niweb-notes.natinst.com/operations/niphone.nsf/' \
          'FirstNameWeb?readviewentries&outputformat=JSON&OpenView&Start=1&Count=1000&Expand=' + str(i+1) + '#20'
    f = urllib.request.urlopen(url)
    charset = f.info().get_param('charset', 'utf8')
    data = f.read()
    data = data.decode(charset)
    data = re.sub('(?!\\\\r)[\\\\].', '', data)
    decoded = json.loads(data)
    viewEntries = decoded['viewentry']
    view = viewEntries[i+1]['entrydata']
    info = view[0]['text']
    print(info.keys())

