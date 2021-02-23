import sys
import pefile
import xmltodict
import pprint
import json
import xml.etree.ElementTree as ET
import os 
from os.path import isfile, join


dirname = sys.argv[1]
if os.path.isfile(dirname):
	arquivos = []
	arquivos.append(dirname)
else:
	arquivos = [a for a in os.listdir(dirname) if isfile(join(dirname, a))]
	os.chdir(dirname)

for i in arquivos:
	pe = pefile.PE(i)
	Executaveis = []

	for section in pe.sections:
		if section.IMAGE_SCN_MEM_EXECUTE:
			Executaveis.append(section.Name.decode('utf-8'))
	print("As seções executaveis do programa " + i + " são: ")
	for a in Executaveis:
		print("	" + a)

