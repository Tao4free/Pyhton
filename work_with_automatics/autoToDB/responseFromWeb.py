# -*- coding:utf-8 -*-

# 参考になったリンク
# https://medium.com/@onejohi/building-a-simple-rest-api-with-python-and-flask-b404371dc699

import mysql.connector
from flask import Flask, jsonify
import socket
import fcntl
import struct

# Input the host IP address
ipAddres = 'xxx.xxx.xxx.xxx'

# Connect the SQL
config = {
  "user": "xxx",
  "password": "xxx",
  "host": "localhost",
  "database": "xxx",
  "raise_on_warnings": True
}

cnx = mysql.connector.connect(**config)
cursor = cnx.cursor()

# Start web framework
app = Flask(__name__)

# Split string with '_'
def getTimeLabel(filename):
    bodyname = filename.split('.')[0]
    time = bodyname.split('_')[0]
    label = bodyname.split('_')[1]
    return time, label

# Method to query records according to time span
def getFromSQL(timefrom, timeto):
    query = ("SELECT time, label FROM yourTable "
             "WHERE time BETWEEN %s AND %s")

    # Define variable to pass to query
    rec = (timefrom, timeto)

    # Excute the query
    cursor.execute(query, rec)

# GET method for REST
@app.route('/get/<string:timespan>', methods=['GET'])
def getMovie(timespan):
    timefrom, timeto = getTimeLabel(timespan)
    getFromSQL(timefrom, timeto)
    movieInfo = {}
    for cur in cursor:
        time = cur[0]
        label = cur[1]#, label = getTimeLabel(cur[0])
        get = {time:{"label":label, "url":"xxx" % (time, label)}}
        movieInfo.update(get)
    return jsonify(movieInfo)

if __name__ == '__main__':
    app.run()

    # Shutdown connection with MySQl
    cursor.close()
    cnx.close()
