#!/usr/bin/python3
# list states from db hbtn_0e_0_usa

import MySQLdb as Db
import sys


if __name__ == "__main__":
    db = Db.connect(host="localhost",
                    port=3306,
                    user=sys.argv[1],
                    passwd=sys.argv[1],
                    db=sys.argv[3])
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id ASC")
    rows = c.fetchall()
    for row in rows:
        print(row)
    c.close()
    db.close()
