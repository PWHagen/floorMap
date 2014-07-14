__author__ = 'Patrick'
import json
import urllib.request


url = 'http://niweb-notes.natinst.com/operations/niphone.nsf/LastNameWeb?readviewentries&outputformat=JSON&OpenView&Start=1&Count=500&Expand=1#1'
f = urllib.request.urlopen(url)
charset = f.info().get_param('charset', 'utf8')
print(charset)
data = f.read()
decoded = json.loads(data.decode(charset))
print(json.dumps(data.decode(charset), indent=4))
viewEntries = decoded['viewentry']
view = viewEntries[15]['entrydata']
info = view[0]['text']
print(info['0'])