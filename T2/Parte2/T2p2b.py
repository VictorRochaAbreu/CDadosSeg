import sys
import pefile
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
import os 
from os.path import isfile, join

filename = sys.argv[1]
filename1 = sys.argv[2]

secs = {}



pe = pefile.PE(filename)
sectionname = []
for section in pe.sections:
	sectionname.append(section.Name.decode('utf-8'))
secs[filename] = set(sectionname)

pe = pefile.PE(filename1)
sectionname = []
for section in pe.sections:
	sectionname.append(section.Name.decode('utf-8'))
secs[filename1] = set(sectionname)


print("----------------------")
print("--                  --")
print("--  SESSÕES COMUNS  --")
print("--     DOS  EXE     --")
print("--                  --")
print("----------------------")


sets = tuple([secs[p] for p in secs])
comuns = set.intersection(*sets)

for a in comuns:
		print(f'\t - {a}')

print("----------------------")
print("--                  --")
print("--  SESSÕES UNICAS  --")
print("--     DOS  EXE     --")
print("--                  --")
print("----------------------")

unic = {}
for a in secs:
	unic[a] = secs[a] - comuns

for a in unic:
	if (len(unic[a]) != 0 ):
		print(a)
		for b in unic[a]:
			print(f'\t - {b}')
