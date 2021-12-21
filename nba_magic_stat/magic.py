import sqlite3

from nba_magic_stat import conf, logger

def connect_to_database():
    con = sqlite3.connect('basketball.sqlite')
    cur = con.cursor()
    return cur

def generate_stats():
    cur = connect_to_database()
    for row in cur.execute('SELECT * FROM Game LIMIT 5')[:5]:
        print(row)