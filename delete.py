#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import subprocess
import re
import os
import os.path
# import sys
# import time
# import glob
from os.path import exists
import shutil

PROJECT_PATH = ""
LIST = []
BasePath = "D:\Bence\Code\JHipster\BaseApp\\"
Changelog = "src\main\\resources\config\liquibase\changelog\\"
Domain = "src\main\java\com\ebentih\domain\\"
Repository = "src\main\java\com\ebentih\\repository\\"
Resource = "src\main\java\com\ebentih\web\\rest\\"
AppEntities = "src\main\webapp\scripts\\app\entities\\"
ComponentEntities = "src\main\webapp\scripts\components\entities\\"
NavBar = "src\main\webapp\scripts\components\\navbar\\"
ResourceTest = "src\\test\java\com\ebentih\web\\rest\\"
OtherTest = "src\\test\javascript\spec\\app\entities\\"
GatlingTest = "src\\test\gatling\simulations\\"
Json = ".jhipster\\"
References = "src\main\\resources\config\liquibase\\"
Index = "src\main\webapp\\"


def help_function():
    print """
==========================
HELP
==========================

- Torli egyesevel a letrehozott file-okat, valamint a bizonyos bejegyzeseket a file-okbol.
- Amiket töröl:
- input; - changelog; - domain; - repository; - resource; - entities; - navBar; - resourceTest; - json; - references; -
index;
- Egyesvel kell megadni neki a letrehozott etity-k neveit, es ha minden megvan, tolri az osszeset
- BasePath: "D:\Bence\Code\JHipster\BaseApp\\" - Bekéri az eléri utat de alapból ezt használja
-
"""


def print_ok():
    print "\t\033[32m[OK]\033[32m\033[39m\n"


def input_func():
    global PROJECT_PATH
    global LIST
    val = 1
    array = []

    while val:
        p_path = raw_input("\nAdd meg az eleresi utat: ")
        if os.path.exists(p_path):
            val = 0
        else:
            print "Wrong file_path, try agai:"

    PROJECT_PATH = p_path

    val = 1
    ref = 1

    while val:
        param = raw_input("\nVan torlendo tabla? (y/n): ")
        if param is "y":
            while ref:
                tables = raw_input("\nAdd meg a table nevet: ")
                list_e = list(tables)
                if list_e[0].isupper():
                    ref = 0
                else:
                    print "Nagybetuvel kell kezdodnie!!"
            array.extend([tables])
            ref = 1
            tables = ""
        elif param is "n":
            val = 0
            LIST = array
        else:
            print "\nWrong parameter!"


def changelog():
    print "Delete Changelog \n"

    global BasePath
    global Changelog

    expansion = ".xml"
    regex = ".*(initial_schema).*"

    # subprocess.Popen(r'explorer /select,BasePath')
    file_list = [name for name in os.listdir(BasePath+Changelog) if name.endswith(expansion)]

    for f in file_list:
        match_obj = re.match(regex, f)
        if match_obj:
            file_list.remove(f)

    for f in file_list:
        delete_f = BasePath+Changelog+f
        if exists(delete_f):
            os.remove(delete_f)
            if not exists(delete_f):
                print f+": Torolve!"

    # os.remove() will remove a f.
    # os.rmdir() will remove an empty directory.
    # shutil.rmtree() will delete a directory and all its contents.
    # print glob.glob("D:\Bence\Code\JHipster\BaseApp\*.xml")
    # print glob.glob("/home/adam/*.txt")

    print_ok()


def domain():
    print "Delete Domain \n"

    global LIST
    global BasePath
    global Domain

    expansion = ".java"

    file_list = [name for name in os.listdir(BasePath+Domain) if name.endswith(expansion)]

    for entity in LIST:
        for file_l in file_list:
            match_obj = re.match(entity, file_l)
            if match_obj:
                delete_f = BasePath+Domain+file_l
                if exists(delete_f):
                    os.remove(delete_f)
                    if not exists(delete_f):
                        print file_l+": Torolve!"

    print_ok()


def repository():
    print "Delete Repository \n"

    global LIST
    global BasePath
    global Repository

    expansion = ".java"

    file_list = [name for name in os.listdir(BasePath+Repository) if name.endswith(expansion)]

    for entity in LIST:
        for f in file_list:
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath+Repository+f
                if exists(felete_f):
                    os.remove(felete_f)
                    if not exists(felete_f):
                        print f+": Torolve!"

    print_ok()


def resource():
    print "Delete Resource \n"

    global LIST
    global BasePath
    global Resource

    expansion = ".java"

    file_list = [name for name in os.listdir(BasePath+Resource) if name.endswith(expansion)]

    for entity in LIST:
        for f in file_list:
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath + Resource + f
                if exists(felete_f):
                    os.remove(felete_f)
                    if not exists(felete_f):
                        print f + ': Torolve!'

    print_ok()


def entities():
    print "Delete Entities \n"

    global LIST
    global BasePath
    global AppEntities
    global ComponentEntities

    file_list = [name for name in os.listdir(BasePath+AppEntities) if name.endswith("")]

    # print upper.upper()
    # print lower.lower()

    for entity in LIST:
        for f in file_list:
            list_e = list(entity)
            list_e[0] = list_e[0].lower()
            entity = "".join(list_e)
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath + AppEntities + f
                if exists(felete_f):
                    shutil.rmtree(felete_f)
                    if not exists(felete_f):
                        print f + ': AppEntities Torolve!'

    file_list = [name for name in os.listdir(BasePath+ComponentEntities) if name.endswith("")]

    for entity in LIST:
        for f in file_list:
            list_e = list(entity)
            list_e[0] = list_e[0].lower()
            entity = "".join(list_e)
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath + ComponentEntities + f
                if exists(felete_f):
                    shutil.rmtree(felete_f)
                    if not exists(felete_f):
                        print f + ': ComponentEntities Torolve!'

    print_ok()


def nav_bar():
    print "Delete NavBar \n"

    global LIST
    global BasePath
    global NavBar

    file_name = 'navbar.html'
    file_path_name = BasePath+NavBar+file_name
    regex_pre = ".*(ui-sref-active).*"
    regex_pre2 = ".*(<span >).*"

    file_open = open(file_path_name, 'r')
    text_list = file_open.readlines()
    file_open.close()

    for entity in LIST:
        for line in text_list:
            list_e = list(entity)
            list_e[0] = list_e[0].lower()
            entity = "".join(list_e)
            regex = regex_pre+".*("+entity+").*"
            match_obj = re.match(regex, line)
            if match_obj:
                print line+" Torolve!"
                text_list[text_list.index(line)] = ""
            regex2 = regex_pre2+".*("+entity+").*"
            match_obj = re.match(regex2, line)
            if match_obj:
                print line+" Torolve!"
                text_list[text_list.index(line)] = ""

    file_open = open(file_path_name, 'w')

    for item in text_list:
        file_open.write("%s" % item)

    file_open.close()

    print_ok()


def resource_test():
    print "Delete ResourceTest \n"

    global LIST
    global BasePath
    global ResourceTest

    file_list = [name for name in os.listdir(BasePath+ResourceTest) if name.endswith("")]

    for entity in LIST:
        for f in file_list:
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath + ResourceTest + f
                if exists(felete_f):
                    os.remove(felete_f)
                    if not exists(felete_f):
                        print f+": Torolve!"

    print_ok()


def other_test():
    print "Delete OtherTest \n"

    global LIST
    global BasePath
    global OtherTest

    file_list = [name for name in os.listdir(BasePath+OtherTest) if name.endswith("")]

    for entity in LIST:
        for f in file_list:
            list_e = list(entity)
            list_e[0] = list_e[0].lower()
            entity = "".join(list_e)
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath + OtherTest + f
                if exists(felete_f):
                    shutil.rmtree(felete_f)
                    if not exists(felete_f):
                        print f + ': Test Torolve!'

    print "\nDelete Gatling Test \n"

    global GatlingTest

    expansion = "GatlingTest.scala"

    file_list = [name for name in os.listdir(BasePath+GatlingTest) if name.endswith(expansion)]

    for entity in LIST:
        for f in file_list:
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath + GatlingTest + f
                if exists(felete_f):
                    os.remove(felete_f)
                    if not exists(felete_f):
                        print f + ': Gatling Test Torolve!'

    print_ok()


def json():
    print "Delete Json \n"

    global LIST
    global BasePath
    global Json

    file_list = [name for name in os.listdir(BasePath+Json) if name.endswith("")]

    for entity in LIST:
        for f in file_list:
            match_obj = re.match(entity, f)
            if match_obj:
                felete_f = BasePath + Json + f
                if exists(felete_f):
                    os.remove(felete_f)
                    if not exists(felete_f):
                        print f+": Torolve!"

    print_ok()


def references():
    print "Delete References \n"

    global LIST
    global BasePath
    global References

    file_name = 'master.xml'
    regex = ".*(added_entity).*"
    file_path_name = BasePath+References+file_name

    file_open = open(file_path_name, 'r')
    text_list = file_open.readlines()

    for line in text_list:
        match_obj = re.match(regex, line)
        if match_obj:
            text_list[text_list.index(line)] = ""
            print line + ": Torolve!"

    file_open.close()

    file_open = open(file_path_name, 'w')

    for item in text_list:
        file_open.write("%s" % item)

    file_open.close()

    print_ok()


def index():
    print "Delete Index \n"

    global LIST
    global BasePath
    global Index

    file_name = 'index.html'
    regex_pre = ".*(scripts/(app|components)/entities/"
    regex_post = ").*"
    file_path_name = BasePath+Index+file_name

    file_open = open(file_path_name, 'r')
    text_list = file_open.readlines()
    file_open.close()

    for entity in LIST:
        for line in text_list:
            list_e = list(entity)
            list_e[0] = list_e[0].lower()
            entity = "".join(list_e)
            regex = regex_pre+entity+regex_post
            match_obj = re.match(regex, line)
            if match_obj:
                text_list[text_list.index(line)] = ""
                print line + ": Torolve!"

    file_open = open(file_path_name, 'w')

    for item in text_list:
        file_open.write("%s" % item)

    file_open.close()

    print_ok()


if __name__ == "__main__":
    print "\nJHipster, entity remover!\n"

    input_func()

    changelog()

    domain()

    repository()

    resource()

    entities()

    nav_bar()

    resource_test()

    other_test()

    json()

    references()

    index()

    # try:
    #     if len(sys.argv) >=2:
    #         if sys.argv[1] == '--help' or sys.argv[1] == '-h':
    #             help()
    #         elif sys.argv[1] == '':
    #             print "run"
    #         else:
    #             help()
    #     else:
    #         help()
    #
    # except Exception, e:
    #     print "Exception"


