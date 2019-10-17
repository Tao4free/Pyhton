# -*- coding:utf-8 -*-
# 参考になったリンク
# https://pypi.org/project/mysql-connector-python/
# https://dev.mysql.com/doc/connector-python/en/connector-python-examples.html
# https://dev.mysql.com/doc/connector-python/en/connector-python-example-connecting.html
# https://dev.mysql.com/doc/refman/5.7/en/insert-on-duplicate.html

import os, sys
import mysql.connector


config = {
  'user': 'xxx',
  'password': 'xxx',
  'host': 'localhost',
  'database': "xxx",
  'raise_on_warnings': True
}


if __name__ == "__main__":
    cnx = mysql.connector.connect(**config)
    cursor = cnx.cursor()

    addRec = ("INSERT INTO yourtable"
              "(time, label)"
              "VALUES (%s, %s) ON DUPLICATE KEY UPDATE label=%s")
    rec = ("20191017113220", 1, 3)

    # Insert new employee
    cursor.execute(addRec, rec)

    # Make sure data is committed to the database
    cnx.commit()

    cursor.close()
    cnx.close()
