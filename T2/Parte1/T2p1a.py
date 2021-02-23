import sys

import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
import os 
from os.path import isfile, join


dirname = sys.argv[1]
arquivos = [a for a in os.listdir(dirname) if isfile(join(dirname, a))]
os.chdir(dirname)
perm = {}

for i in arquivos:
	tree = ET.parse(i)
	root = tree.getroot()
	permissoes = []
	print(i)
	for android in root.iter('uses-permission'):
		permissao = android.attrib["{http://schemas.android.com/apk/res/android}name"].split(".")[-1]
		permissoes.append(permissao)
	perm[i] = set(permissoes)

print("----------------------")
print("--                  --")
print("--    PERMISSÕES    --")
print("--     POR  APK     --")
print("--                  --")
print("----------------------")
for a in perm:
		print("{}: {}\n".format(a,perm[a]))



print("----------------------")
print("--                  --")
print("--    PERMISSÕES    --")
print("--      UNICAS      --")
print("--     POR  APK     --")
print("--                  --")
print("----------------------")

unic = {}
for a in perm:
	sets = tuple([perm[p] for p in perm if p != a])
	uniao = set.union(*sets)
	unic[a] = perm[a] - uniao

for a in unic:
	if (len(unic[a]) != 0 ):
		print(a)
		for b in unic[a]:
			print(f'\t - {b}')


print("----------------------")
print("--                  --")
print("--    PERMISSÕES    --")
print("--      COMUNS      --")
print("--     DAS  APK     --")
print("--                  --")
print("----------------------")


sets = tuple([perm[p] for p in perm])
comuns = set.intersection(*sets)

for a in comuns:
		print(f'\t - {a}')