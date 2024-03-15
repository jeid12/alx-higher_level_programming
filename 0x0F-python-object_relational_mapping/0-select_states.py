#!/usr/bin/python3
"""
Script that lists all states from the database hbtn_0e_0_usa.
"""

import sys
import MySQLdb

if __name__ == "__main__":
    # Check if correct number of arguments is provided
    if len(sys.argv) != 4:
        print("Usage: {} username password database".format(sys.argv[0]))
        sys.exit(1)

    # Extract MySQL connection information from command-line arguments
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    try:
        # Connect to MySQL database
        db = MySQLdb.connect(host="localhost",
                             port=3306,
                             user=username,
                             passwd=password,
                             db=database)

        # Create a cursor object using cursor() method
        cursor = db.cursor()

        # Execute SQL query to select all states
        cursor.execute("SELECT * FROM states ORDER BY id ASC")

        # Fetch all rows
        rows = cursor.fetchall()

        # Display results
        for row in rows:
            print(row)

    except MySQLdb.Error as e:
        print("MySQLdb Error:", e)

    finally:
        # Close database connection
        if 'db' in locals() or 'db' in globals():
            db.close()

