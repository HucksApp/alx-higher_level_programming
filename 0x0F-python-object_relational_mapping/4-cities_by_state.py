#!/usr/bin/python3
"""Defines a Mysqldb query function"""
from MySQLdb import connect
from sys import argv


def dbQuery(query: str) -> None:
    """Query the Mysql database"""
    db = connect(host="localhost", user=argv[1],
                 passwd=argv[2], db=argv[3], port=3306)
    cursor = db.cursor()
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()


if __name__ == "__main__":
    query = "SELECT cities.id, cities.name, states.name FROM \
                cities INNER JOIN states ON states.id=cities.state_id"
    dbQuery(query)
