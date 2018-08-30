import json
import pprint
import re


bayanRegex = re.compile(r'(\w){,20}')
districtRegex = re.compile(r'\d\w\w')
bayanList = open('bayan-list.de', 'r')

bayans = []

for b in bayanList:
#	bd = bayanRegex.search(b)
#	for a in b:
#		print(a + '####')
	bayan = {}
	db = districtRegex.search(b)
	bd = bayanRegex.search(b)
	if bd:
		bayan['name'] = bd.group()
	if db:
		bayan['district'] = db.group()
	bayans.append(bayan)

pprint.pprint(bayans)

bayanList.close()
json_file = open('file.json', 'w')
json.dump(bayans, json_file)
json_file.close()
