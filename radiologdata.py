#!/usr/bin/python

import socket
from syslogmp import parse

#<--cwilson edit-->#

import mysql.connector

mydb = mysql.connector.connect(
        host = "127.0.0.1",     #server host ip
        user = "root",          #host username
        password = "",          #host password
        database = "radio",     #name of mysql database
        )

mycursor = mydb.cursor()

#<--end of cwilson edit-->#

LISTEN_IP = "0.0.0.0"           #leave default
LISTEN_PORT = 514               #port for log transfer

sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
sock.bind((LISTEN_IP, LISTEN_PORT))

while True:
    data, addr = sock.recvfrom(1024)
    syslogData = parse(data)
    logString = str(syslogData.message)
    ch = 'x86_64}'
    shortLogString = logString.split(ch, 1)
    
    if len(shortLogString) > 0:
        shortLogString = shortLogString[1]
    
    shortLogString = shortLogString[:-3]

    varlist = shortLogString.split(",")
    
    for var in varlist:
        time = varlist[0]
        site_num = varlist[1]
        action = varlist[2]
        source_type = varlist[3]
        source_id = varlist[4]
        target_type = varlist[5]
        target_id = varlist[6]
        channel_num = varlist[7]
        call_type = varlist[8]
        
    print(str(syslogData.message) + "\n")
    print("Edited Data: " + shortLogString + "\n")
    print("Variable List: ") 
    print(varlist)
    print("\n")
    print("Individual Variables: " + "\n")
    print("Time: " + time + "\n")
    print('Site Number: ' + site_num + "\n")
    print('Action: ' + action + "\n")
    print('Source Type: ' + source_type + "\n")
    print('Source ID: ' + source_id + "\n")
    print('Target Type: ' + target_type + "\n")
    print('Target ID: ' + target_id + "\n")
    print('Channel Number: ' + channel_num + "\n")
    print('Call Type: ' + call_type + "\n")
    print("----------------------------------------------------------------------------------------------" + "\n")
    
    #<--cwilson edit-->

    sql = """INSERT INTO RadioLogTable (time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"""
    
    val = (time, site_num, action, source_type, source_id, target_type, target_id, channel_num, call_type)
    
    mycursor.execute(sql, val)
    
    mydb.commit()

    print(mycursor.rowcount, "record inserted.")
    #<--end of cwilson edit-->
