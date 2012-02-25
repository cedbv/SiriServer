#!/usr/bin/python
# -*- coding: utf-8 -*-

import cPickle
import sqlite3
from uuid import uuid4

# SQLite
db_type = "sqlite"
__database__ = "database.sqlite3"

# MySQL
"""
db_type = "mysql"
__host__ = "localhost"
__username__ = "root"
__password__ = ""
__database__ = "siriserver"
"""

if db_type == "mysql":
    try:
        import MySQLdb
    except:
        print "You must install MySQLdb to use MySQL with SiriServer."
        exit()

def setup():
    conn = getConnection()
    c = conn.cursor()
    if db_type == "mysql":
        try:
            c.execute("create table assistants (assistantId VARCHAR(255) PRIMARY KEY, assistant TEXT)")
        except MySQLdb.Error, e:
            if e[0] != 1050:
                print e
                exit()
    else:
        c.execute("create table if not exists assistants(assistantId text primary key, assistant assi)")
    conn.commit()
    c.close()
    conn.close()

def getConnection():
    if db_type == "mysql":
        return MySQLdb.connect(__host__, __username__, __password__, __database__, use_unicode=True)
    else:
        return sqlite3.connect(__database__, detect_types=sqlite3.PARSE_DECLTYPES)

class Assistant(object):
    def __init__(self, assistantId=str.upper(str(uuid4()))):
        self.assistantId = assistantId
        self.censorspeech = None
        self.timeZoneId = None
        self.language = None
        self.region = None
        self.firstName = u""
        self.nickName = u""

def adaptAssistant(assistant):
    return cPickle.dumps(assistant)

def convertAssistant(fromDB):
    return cPickle.loads(fromDB)

if db_type == "sqlite":
    sqlite3.register_adapter(Assistant, adaptAssistant)
    sqlite3.register_converter("assi", convertAssistant)
