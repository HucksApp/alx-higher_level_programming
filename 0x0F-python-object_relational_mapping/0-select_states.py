#!/usr/bin/python3
"""  lists all states from the database hbtn_0e_0_usa """
from MySQLdb import connect
from sys import argv


def connectDb(query: str) -> None:
    """ lists all states from the database hbtn_0e_0_usa """
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
    query = "SELECT * FROM states"
    connectDb(query)
