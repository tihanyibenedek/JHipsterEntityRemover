#!/usr/bin/python

import subprocess
import re
import os
import os.path
import sys
import time
import glob
from os.path import exists
import shutil

PROJECT_PATH = "";
LIST = [];
BasePath = "D:\Bence\Code\JHipster\BaseApp\\";
Changelog = "src\main\\resources\config\liquibase\changelog\\";
Domain = "src\main\java\com\ebentih\domain\\";
Repository = "src\main\java\com\ebentih\\repository\\";
Resource = "src\main\java\com\ebentih\web\\rest\\";
AppEntities = "src\main\webapp\scripts\\app\entities\\";
ComponentEntities = "src\main\webapp\scripts\components\entities\\";
NavBar = "src\main\webapp\scripts\components\\navbar\\";
ResourceTest = "src\\test\java\com\ebentih\web\\rest\\";
Json = ".jhipster\\";
References = "src\main\\resources\config\liquibase\\";
Index = "src\main\webapp\\";

def help():
	print '''
==========================
	HELP
==========================
	
	- Torli egyesevel a letrehozott file-okat, valamint a bizonyos bejegyzeseket a file-okbol.
	- Amiket töröl: 
		- input; - changelog; - domain; - repository; - resource; - entities; - navBar; - resourceTest; - json; - references; - index;
	- Egyesvel kell megadni neki a letrehozott etity-k neveit, es ha minden megvan, tolri az osszeset
	- BasePath: "D:\Bence\Code\JHipster\BaseApp\\" - Bekéri az eléri utat de alapból ezt használja
	- 
	
'''

def printOK():
	print '\t\033[32m[OK]\033[32m\033[39m\n'

def input():
	global PROJECT_PATH;
	global LIST;
	val = 1;
	param = "";
	list = [];
	
	while val:
		pPath = raw_input("\nAdd meg az eleresi utat: ")
		if (os.path.exists(pPath)):
			val = 0;
		else:
			print "Wrong file_path, try agai:"
			
	PROJECT_PATH = pPath;
			
	val = 1;			
	
	while val:
		param = "";
		param = raw_input("\nVan torlendo tabla? (y/n): ")
		if (param is "y"):
			tables = raw_input("\nAdd meg a table nevet (nagykezdobetuvel): ")
			list.extend ([tables]);
			tables = "";
		elif (param is "n"):
			val = 0;
			LIST = list;
		else:
			print "\nWrong parameter!"

	
def changelog():
	print "Delete Changelog \n"
	
	global BasePath;
	global Changelog;
	
	expansion = ".xml";
	regex = ".*(initial_schema).*";
	
	# subprocess.Popen(r'explorer /select,BasePath');
	fileList = [name for name in os.listdir(BasePath+Changelog) if name.endswith(expansion)];
	
	for file in fileList:	
		matchObj = re.match(regex, file);
		if matchObj:
			fileList.remove(file);
			
	for file in fileList:
		deleteF = BasePath+Changelog+file;
		if (exists(deleteF)):
			os.remove(deleteF);
			if (exists(deleteF) == False):
				print file+": Torolve!";

	# os.remove() will remove a file.
	# os.rmdir() will remove an empty directory.
	# shutil.rmtree() will delete a directory and all its contents.
	# print glob.glob("D:\Bence\Code\JHipster\BaseApp\*.xml");
	# print glob.glob("/home/adam/*.txt")
	
	printOK()

	
def domain():
	print "Delete Domain \n"
	
	global LIST;
	global BasePath;
	global Domain;
	
	expansion = ".java";
	
	fileList = [name for name in os.listdir(BasePath+Domain) if name.endswith(expansion)];
	
	for entity in LIST:
		for file in fileList:
			matchObj = re.match(entity, file);
			if matchObj:
				deleteF = BasePath+Domain+file;
				if (exists(deleteF)):
					os.remove(deleteF);
					if (exists(deleteF) == False):
						print file+": Torolve!";
		
	printOK()
	

def repository():
	print "Delete Repository \n"
	
	global LIST;
	global BasePath;
	global Repository;
	
	expansion = ".java";
	
	fileList = [name for name in os.listdir(BasePath+Repository) if name.endswith(expansion)];
	
	for entity in LIST:
	    for file in fileList:
			matchObj = re.match(entity, file);
			if matchObj:
				deleteF = BasePath+Repository+file;
				if (exists(deleteF)):
					os.remove(deleteF);
					if (exists(deleteF) == False):
						print file+": Torolve!";
					
	printOK()
	
	
def resource():
	print "Delete Resource \n"
	
	global LIST;
	global BasePath;
	global Resource;
	
	expansion = ".java";
	
	fileList = [name for name in os.listdir(BasePath+Resource) if name.endswith(expansion)];
	
	for entity in LIST:
		for file in fileList:
			matchObj = re.match(entity, file)
			if matchObj:
				deleteF = BasePath + Resource + file
				if exists(deleteF):
					os.remove(deleteF)
					if exists(deleteF) == False:
						print file + ': Torolve!'
		
	printOK()
	
	
def entities():
	print "Delete Entities \n"
	
	global LIST;
	global BasePath;
	global AppEntities;
	global ComponentEntities;
	
	fileList = [name for name in os.listdir(BasePath+AppEntities) if name.endswith("")];
	
	# print upper.upper()
	# print lower.lower()
	
	for entity in LIST:
		for file in fileList:
			listE = list(entity);
			listE[0] = listE[0].lower();
			entity = "".join(listE);
			matchObj = re.match(entity, file);
			if matchObj:
			    deleteF = BasePath + AppEntities + file;
			    if exists(deleteF):
					shutil.rmtree(deleteF);
					if exists(deleteF) == False:
						print file + ': AppEntities Torolve!'
						
	fileList = [name for name in os.listdir(BasePath+ComponentEntities) if name.endswith("")];
	
	for entity in LIST:
		for file in fileList:
			listE = list(entity);
			listE[0] = listE[0].lower();
			entity = "".join(listE);
			matchObj = re.match(entity, file);
			if matchObj:
			    deleteF = BasePath + ComponentEntities + file;
			    if exists(deleteF):
					shutil.rmtree(deleteF);
					if exists(deleteF) == False:
						print file + ': ComponentEntities Torolve!'
	
	printOK()

def navBar():
	print "Delete NavBar \n"
	
	global LIST;
	global BasePath;
	global NavBar;
	
	fileName = 'navbar.html';
	filePathName = BasePath+NavBar+fileName;
	regexPRE = ".*(ui-sref-active).*";
	regexPRE2 = ".*(<span >).*";
	
	fileOpen = open(filePathName, 'r');
	textList = fileOpen.readlines();
	fileOpen.close();
	
	for entity in LIST:
		for line in textList:
			listE = list(entity);
			listE[0] = listE[0].lower();
			entity = "".join(listE);
			regex = regexPRE+".*("+entity+").*";
			matchObj = re.match(regex, line);
			if matchObj:
				print line+" Torolve!";
				textList[textList.index(line)] = "";
			regex2 = regexPRE2+".*("+entity+").*";
			matchObj = re.match(regex2, line);
			if matchObj:
				print line+" Torolve!";
				textList[textList.index(line)] = "";
				
	fileOpen = open(filePathName, 'w');
	
	for item in textList:
		fileOpen.write("%s" % item);
	
	fileOpen.close();
	
	printOK()
	
	
def resourceTest():
	print "Delete ResourceTest \n"
	
	global LIST;
	global BasePath;
	global ResourceTest;
	
	fileList = [name for name in os.listdir(BasePath+ResourceTest) if name.endswith("")];
	
	for entity in LIST:
		for file in fileList:
			matchObj = re.match(entity, file)
			if matchObj:
				deleteF = BasePath + ResourceTest + file
				if (exists(deleteF)):
					os.remove(deleteF);
					if (exists(deleteF) == False):
						print file+": Torolve!";

	
	printOK()
	
	
def json():
	print "Delete Json \n"
	
	global LIST;
	global BasePath;
	global Json;
	
	fileList = [name for name in os.listdir(BasePath+Json) if name.endswith("")];
	
	for entity in LIST:
		for file in fileList:
			matchObj = re.match(entity, file)
			if matchObj:
				deleteF = BasePath + Json + file
				if (exists(deleteF)):
					os.remove(deleteF);
					if (exists(deleteF) == False):
						print file+": Torolve!";
	
	printOK()
	
	
def references():
	print "Delete References \n"
	
	global LIST;
	global BasePath;
	global References;
	
	fileName = 'master.xml';
	regex = ".*(added_entity).*";
	filePathName = BasePath+References+fileName;
	
	fileOpen = open(filePathName, 'r');
	textList = fileOpen.readlines();
	
	for line in textList:
		matchObj = re.match(regex, line);
		if matchObj:
			textList[textList.index(line)] = "";
			print line + ": Torolve!";
	
	fileOpen.close();

	fileOpen = open(filePathName, 'w');
	
	for item in textList:
		fileOpen.write("%s" % item);
	
	fileOpen.close();
	
	printOK()
	
	
def index():
	print "Delete Index \n"
	
	global LIST;
	global BasePath;
	global Index;
	
	fileName = 'index.html';
	regexPRE = ".*(scripts/(app|components)/entities/";
	regexPOST = ").*";
	filePathName = BasePath+Index+fileName;
	
	
	fileOpen = open(filePathName, 'r');
	textList = fileOpen.readlines();
	fileOpen.close();
	
	for entity in LIST:
		for line in textList:
			listE = list(entity);
			listE[0] = listE[0].lower();
			entity = "".join(listE);
			regex = regexPRE+entity+regexPOST;
			matchObj = re.match(regex, line);
			if matchObj:
				textList[textList.index(line)] = "";
				print line + ": Torolve!";

	fileOpen = open(filePathName, 'w');
	
	for item in textList:
		fileOpen.write("%s" % item);
	
	fileOpen.close();
	
	printOK()
	
	
if __name__=="__main__":
	print "\nJHipster, entity remover!\n"
	
	input();
		
	changelog();
	
	domain();

	repository()

	resource()

	entities()
	
	navBar()

	resourceTest()

	json()

	references()

	index()
	
	# try:	
		# if len(sys.argv) >=2:
			# if sys.argv[1] == '--help' or sys.argv[1] == '-h':
				# help()
			# elif sys.argv[1] == '':
				# print "run"
			# else:
				# help()
		# else:
			# help()		
			
	# except  Exception, e:
		# print "Exception"



