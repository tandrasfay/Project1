# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

import os.path
import ConfigParser
import gspread
home = os.path.expanduser("~")
configfile = os.path.join(home, 'stat157.cfg')
config = ConfigParser.SafeConfigParser()
config.read(configfile)
username = config.get('google', 'username')
password = config.get('google', 'password')
print username
docid = config.get('questionnaire', 'docid')
client = gspread.login(username, password)
spreadsheet = client.open_by_key(docid)
worksheet = spreadsheet.get_worksheet(0)
print docid
fieldnames = ['What is your learning style?','In which of these topics would you feel confident being a technical lead for other students?']
print fieldnames
filtered_data = []
for row in worksheet.get_all_records():
    filtered_data.append({k:v for k,v in row.iteritems() if k in fieldnames})
print "Number of rows: {}".format(len(filtered_data))
#for row in (filtered_data):
 #   print row
questionnaire = filtered_data
from pandas import DataFrame, read_csv
from xml.etree import ElementTree
import pandas as pd
questdf = DataFrame(questionnaire)


questdf['Visual'] = questdf['What is your learning style?']
questdf['Aural'] = questdf['What is your learning style?']
questdf['Read/Write'] = questdf['What is your learning style?']
questdf['Kinesthetic'] = questdf['What is your learning style?']
Visual = questdf['Visual']
for i in range(len(Visual)):
    Visual[i] = Visual[i].rpartition("Visual:" or "Visual-")[2]
    Visual[i] = Visual[i].partition("\n")[0]
    if len(Visual[i]) >0:
        Visual[i] = Visual[i].rsplit()[-1]
    if Visual[i].isdigit():
        Visual[i] = Visual[i]
    else:
        Visual[i] = "NA"

Aural = questdf['Aural']
for i in range(len(Aural)):
    Aural[i] = Aural[i].rpartition("Aural:"or"Aural-")[2]
    Aural[i] = Aural[i].partition("\n")[0]
    if len(Aural[i]) >0:
        Aural[i] = Aural[i].rsplit()[-1]
    if Aural[i].isdigit():
        Aural[i] = Aural[i]
    else:
        Aural[i] = "NA"



ReadWrite = questdf['Read/Write']
for i in range(len(ReadWrite)):
    ReadWrite[i] = ReadWrite[i].rpartition("Read/Write:"or"Read/Write-")[2]
    ReadWrite[i] = ReadWrite[i].partition("\n")[0]
    if len(ReadWrite[i]) >0:
        ReadWrite[i] = ReadWrite[i].rsplit()[-1]
    if ReadWrite[i].isdigit():
        ReadWrite[i] = ReadWrite[i]
    else:
        ReadWrite[i] = "NA"

Kinesthetic = questdf['Kinesthetic']
for i in range(len(Kinesthetic)):
    Kinesthetic[i] = Kinesthetic[i].rpartition("Kinesthetic:"or"Kinesthetic-")[2]
    Kinesthetic[i] = Kinesthetic[i].partition("\n")[0]
    if len(Kinesthetic[i]) >0:
        Kinesthetic[i] = Kinesthetic[i].rsplit()[-1]
    if Kinesthetic[i].isdigit():
        Kinesthetic[i] = Kinesthetic[i]
    else:
        Kinesthetic[i] = "NA"
questdf['Visual'] = Visual  ### Now assigning these back to the dataframe
questdf['Aural'] = Aural
questdf['Read/Write'] = ReadWrite
questdf['Kinesthetic'] = Kinesthetic
del questdf["What is your learning style?"]


questdf["TechLead"] = questdf["In which of these topics would you feel confident being a technical lead for other students?"]
del questdf["In which of these topics would you feel confident being a technical lead for other students?"]

questdf['Visual'] = Visual  ### Now assigning these back to the dataframe
questdf['Aural'] = Aural
questdf['Read/Write'] = ReadWrite
questdf['Kinesthetic'] = Kinesthetic




# <codecell>

questdf["Python"] = questdf["TechLead"]
Python = questdf["Python"]
for i in range(len(Python)):
    Python[i] = 'IPython Notebook or Python' in Python[i]

# <codecell>

questdf["Python"] = Python
questdf["github"] = github

# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


# <codecell>


