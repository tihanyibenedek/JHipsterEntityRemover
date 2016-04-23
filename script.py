#!/usr/bin/env python
# -*- coding: utf-8 -*-

# import subprocess
# import re
# import _mysql
# import os
# import os.path
# import sys
# import time
import random
# import datetime
# import glob
# from os.path import exists
# import shutil
# import MySQLdb as mdb
import mysql.connector
from datetime import date, datetime, timedelta

Cars = [
    # ('Citroen', 'LRG - 342', 210, 1200000, date(2010, 06, 14)),
    ('Citroen', 'LRG - 342', 210, 1200000),
    ('Volvo', 'JLB - 619', 230, 2300000),
    ('Opel', 'JXF - 600', 180, 1700000),
    ('Skoda', 'HNL - 317', 130, 1100000),
    ('Lada', 'KKD - 006', 90, 500000),
    ('Mitsubisi', 'NNL - 003', 230, 1500000),
    ('Honda', 'HIW - 288', 115, 2100000),
    ('Jaguar', 'HRB - 834', 280, 12400000),
    ('Vokswagen', 'VSZ - 422', 250, 5500000),
    ('Suzuki', 'JZG - 853', 120, 900000),
    ]

Telephones = [
    ('Samsunk', '06 20 7767 840', 120000),
    ('Sony', '06 30 5090 644', 95000),
    ('Motorola', '06 20 7716 253', 64000),
    ('HTC', '06 70 0142 784', 87000),
    ('Alcatel', '06 70 9156 593', 21000),
    ('iPhone', '06 20 4943 920', 230000),
    ('Nokia', '06 30 3899 822', 4000),
    ('Windows', '06 30 8502 922', 37000),
    ('BlackBerry', '06 70 8361 015', 170000),
    ('LG', '06 20 3957 744', 74000),
    ]

WorkPlaces = [
    ('Ericsson', 'Törökvész út 11b, Budapest, 1025', '(1) 493 440'),
    ('Telecom', 'Lövölde tér 2a, Budapest, 1071', '(1) 625 499'),
    ('MOL', 'Szőlővirág utca 8, Budapest, 1108', '(35) 240 599'),
    ('Swietelsky', 'Zöldmező utca 1, Szigetszentmiklós, 2310', '(89) 324 492'),
    ('Morgan Stanley', 'Erdősor utca 2-4, Várgesztes, 2824', '(94) 524 158'),
    ('Strabag zrt', 'Bajcsy-Zsilinszky utca 1, Kunpeszér, 6096', '(25) 436 927'),
    ('MacDonald', 'Tóth László sétány, Kecskemét, 6000', '(72) 559 870'),
    ('Magyar Posta', 'Zádor utca 13, Kunhegyes, 5340', '(93) 408 850'),
    ('Henkel Magyarország', 'Közép utca 6, Nyíregyháza, 4400', '(79) 604 884'),
    ('MAV zrt', 'Petőfi utca 3, Kupa, 3813', '(82) 792 702'),
    ]

Persons = [
    ('Hajba Dádiv', 'male', date(1979, 03, 18), 'david@mail.com', 'Tündér utca 1-5, Budapest, 1125', 'widowed'),
    ('Tihanyi Bence', 'male', date(1950, 01, 11), 'bence@mail.com', 'Felső Svábhegyi út 2, Budapest, 1125', 'married'),
    ('Kiss Péter', 'male', date(1980, 04, 05), 'peter@mail.com', 'Törökugrató utca 11-13, Budapest, 1118', 'single'),
    ('Toth Sándor', 'male', date(1952, 11, 29), 'sandor@mail.com', 'Citera utca 5, Budapest, 1116', 'divorced'),
    ('Bíró Tamás', 'male', date(1976, 9, 25), 'tamas@mail.com', 'Temetődűlő út 1-5, Budapest, 1211', 'single'),
    ('Németh Anikó', 'female', date(1986, 12, 28), 'aniko@mail.com', 'Köztársaság tér 14, Budapest, 1204', 'widowed'),
    ('Béres Orsolya', 'male', date(1989, 8, 16), 'orsolya@mail.com', 'Hitel Márton utca 53, Budapest, 1205', 'cohabiting'),
    ('Baál Gábor', 'male', date(1976, 03, 07), 'gabor@mail.com', 'Hungária út 23, Budapest, 1192', 'civil union'),
    ('Kiss Anna', 'female', date(1988, 11, 27), 'anna@mail.com', 'Károlyi Sándor út 3-17, Budapest, 1151', 'divorced'),
    ('Varga Ildikó', 'female', date(1987, 02, 20), 'ildiko@mail.com', 'Bródy Sándor utca 24, Dunakeszi, 2120', 'single'),
    ]

def printOK():
    print '\t\033[32m[OK]\033[32m\033[39m\n'

def insertCar(cnx):
    print "Car insert\n"

    person_id = cursor.execute("SELECT id FROM baseapp.person")
    person_id = cursor.fetchall()
    person_id = list(person_id)

    add_car = ("INSERT INTO car "
       "(type, reg_number, max_speed, price, person_id) "
       "VALUES (%s, %s, %s, %s, %s)")

    for x in range(0, 10):
        rndPerson = random.randrange(0, len(person_id))
        rndPerson = person_id[rndPerson]
        person_id.remove(rndPerson)
        rndPerson = rndPerson[0]

        carList = Cars[x]
        carList = list(carList)
        carList.extend([rndPerson])

        cursor.execute(add_car, carList)

    printOK()

def insertTelephone(cnx):
    print "Telephone insert\n"

    person_id = cursor.execute("SELECT id FROM baseapp.person")
    person_id = cursor.fetchall()
    person_id = list(person_id)

    add_telephone = ("INSERT INTO telephone "
       "(type, number, price, person_id) "
       "VALUES (%s, %s, %s, %s)")

    for x in range(0, 10):
        rndPerson = random.randrange(0, len(person_id))
        rndPerson = person_id[rndPerson]
        person_id.remove(rndPerson)
        rndPerson = rndPerson[0]

        telephoneList = Telephones[x]
        telephoneList = list(telephoneList)
        telephoneList.extend([rndPerson])

        cursor.execute(add_telephone, telephoneList)

    printOK()

def insertWorkPlace(cnx):
    print "WrokPlace insert\n"

    add_workPlace = ("INSERT INTO work_place "
       "(name, address, phone) "
       "VALUES (%s, %s, %s)")

    for x in range(0, 10):
        cursor.execute(add_workPlace, WorkPlaces[x])

    printOK()

def insertPersonWorkPlace(cnx):
    print "PersonWorkPlace insert\n"

    # person_ids = cursor.execute("SELECT persons_id FROM baseapp.work_place_person")
    # person_ids = cursor.fetchall()
    # person_ids = list(person_ids)

    # print person_ids

    workPlaces = cursor.execute("SELECT id FROM baseapp.work_place")
    workPlaces = cursor.fetchall()
    workPlaces = list(workPlaces)

    personNum = cursor.execute("SELECT id FROM baseapp.person")
    personNum = cursor.fetchall()
    personList = list(personNum)

    personNum = len(personList)
    # print personNum

    add_personWorkPlace = ("INSERT INTO work_place_person "
       "(persons_id, work_places_id) "
       "VALUES (%s, %s)")

    x = 0
    while x < (personNum):
        # print "hello"
        rndWork = random.randrange(0, len(workPlaces))
        rndWork = workPlaces[rndWork]
        workPlaces.remove(rndWork)
        rndWork = rndWork[0]
        person = personList[x]
        person = person[0]
        # print person
        param = [person, rndWork]
        # print param
        cursor.execute(add_personWorkPlace, param)
        x = x + 1

    printOK()	

def insertPerson(cnx):
    print "Person insert\n"

    car_id = cursor.execute("SELECT id FROM baseapp.car")
    car_id = cursor.fetchall()
    car_id = list(car_id)
    # print car_id
    telephone_id = cursor.execute('SELECT id FROM baseapp.telephone')
    telephone_id = cursor.fetchall()
    telephone_id = list(telephone_id)
    # print telephone_id

    add_person = ("INSERT INTO person "
       "(name, gender, birth_date, e_mail, address, state) "
       "VALUES (%s, %s, %s, %s, %s, %s)")

    for x in range(0, 10):
        # rndCar = random.randrange(0, len(car_id))
        # rndCar = car_id[rndCar]
        # car_id.remove(rndCar)
        # rndCar = rndCar[0]
        # rndTelephone = random.randrange(0, len(telephone_id))
        # rndTelephone = telephone_id[rndTelephone]
        # telephone_id.remove(rndTelephone)
        # rndTelephone = rndTelephone[0]

        personList = Persons[x]
        personList = list(personList)
        # personList.extend([rndCar, rndTelephone])

        cursor.execute(add_person, personList)

    printOK()

if __name__ == "__main__":

    print "Base App inserter\n"

    config = {
        'user': 'root',
        'password': 'root',
        'host': '127.0.0.1',
        'database': 'baseapp',
        'raise_on_warnings': True,
    }

    cnx = mysql.connector.connect(**config)
    cnx.autocommit = True
    cursor = cnx.cursor(buffered=True)

    # insertPerson(cnx)
    
    # insertCar(cnx)

    # insertTelephone(cnx)

    # insertWorkPlace(cnx)

    insertPersonWorkPlace(cnx)

    cnx.commit()
    cursor.close()
    cnx.close()
