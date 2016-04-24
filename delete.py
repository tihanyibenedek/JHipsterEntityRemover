#!/usr/bin/env python
# -*- coding: utf-8 -*-

import re
import os
import os.path
from os.path import exists
import delete_functions
import logging

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

    file_list = [name for name in os.listdir(BasePath + Changelog) if name.endswith(expansion)]

    for f in file_list:
        match_obj = re.match(regex, f)
        if match_obj:
            file_list.remove(f)

    for f in file_list:
        delete_f = BasePath+Changelog+f
        if exists(delete_f):
            os.remove(delete_f)
            if not exists(delete_f):
                print f+": Deleted!"

    # os.remove() will remove a f.
    # os.rmdir() will remove an empty directory.
    # shutil.rmtree() will delete a directory and all its contents.
    # print glob.glob("D:\Bence\Code\JHipster\BaseApp\*.xml")
    # print glob.glob("/home/adam/*.txt")

    print_ok()


def domain():
    print "Delete Domain \n"

    if delete_functions.delete_selected_item(LIST, Domain, ".java"):
        logging.info("Domain is deleted!")
    else:
        logging.info("Something went wrong!")

    print_ok()


def repository():
    print "Delete Repository \n"

    if delete_functions.delete_selected_item(LIST, Repository, ".java"):
        logging.info("Repository is deleted!")
    else:
        logging.info("Something went wrong!")

    print_ok()


def resource():
    print "Delete Resource \n"

    if delete_functions.delete_selected_item(LIST, Resource, ".java"):
        logging.info("Resource is deleted!")
    else:
        logging.info("Something went wrong!")

    print_ok()


def entities():
    print "Delete Entities \n"

    if delete_functions.delete_selected_item_with_lower(LIST, AppEntities, ""):
        logging.info("AppEntities is deleted!")
    else:
        logging.info("Something went wrong!")

    if delete_functions.delete_selected_item_with_lower(LIST, ComponentEntities, ""):
        logging.info("ComponentEntities is deleted!")
    else:
        logging.info("Something went wrong!")

    print_ok()


def nav_bar():
    print "Delete NavBar \n"

    global LIST
    global BasePath
    global NavBar

    file_name = 'navbar.html'
    file_path_name = BasePath + NavBar + file_name
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
                print line+" Deleted!"
                text_list[text_list.index(line)] = ""
            regex2 = regex_pre2+".*("+entity+").*"
            match_obj = re.match(regex2, line)
            if match_obj:
                print line+" Deleted!"
                text_list[text_list.index(line)] = ""

    file_open = open(file_path_name, 'w')

    for item in text_list:
        file_open.write("%s" % item)

    file_open.close()

    print_ok()


def resource_test():
    print "Delete ResourceTest \n"

    if delete_functions.delete_selected_item(LIST, ResourceTest, ""):
        logging.info("ResourceTest is deleted!")
    else:
        logging.info("Something went wrong!")

    print_ok()


def other_test():
    print "Delete OtherTest \n"

    if delete_functions.delete_selected_item_with_lower(LIST, OtherTest, ""):
        logging.info("OtherTest is deleted!")
    else:
        logging.info("Something went wrong!")

    print "\nDelete Gatling Test \n"

    if delete_functions.delete_selected_item(LIST, GatlingTest, "GatlingTest.scala"):
        logging.info("GatlingTest is deleted!")
    else:
        logging.info("Something went wrong!")

    print_ok()


def json():
    print "Delete Json \n"

    if delete_functions.delete_selected_item(LIST, Json, ""):
        logging.info("Json is deleted!")
    else:
        logging.info("Something went wrong!")

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
            print line + ": Deleted!"

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
                print line + ": Deleted!"

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


