#!/usr/bin/python3
# list states from db hbtn_0e_0_usa

import MySQLdb as Db
import sys


if __name__ == "__main__":
    args = sys.argv[1:]
    db = Db.connect(host="localhost",
                    port=3306,
                    user=args[0],
                    passwd=args[1],
                    db=args[2])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
