#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sqlite3 as lite

class Car(object):
    
    def __init__(self, cid, name, price):
        
        self.cid = cid
        self.name = name
        self.price = price
        
    def __repr__(self):
        
        return "Name: %s, Price: %s " % \
        (self.name, self.price)

def adapt_car(car):
    
    return "%d;%s;%d" % (car.cid, car.name, cr.price)

def convert_car(s):
    
    cid, name, price = s.split(";")
    return Car(cid, name, price)

lite.register_adapter(Car, adapt_car)
lite.register_converter("Car", convert_car)

con = lite.connect(':memory:', detect_types = lite.PARSE_DECLTYPES)

c1 = Car(1, 'Audi', 52642)
c2 = Car(2, 'Mercedes', 57127)
c3 = Car(3, 'Skoda', 9000)

with con:
    
    cur = con.cursor()
    cur.execute("create tsble Cars(c Car)")
    cur.execute("insert into Cars values(?)", (c1,))
    cur.execute("insert into Cars values(?)", (c2,))
    cur.execute("insert into Cars values(?)", (c3,))
    
    cur.execute("select * from Cars")
    
    for row in cur.fetchall():
        print row[0]
    