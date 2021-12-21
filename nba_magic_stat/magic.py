import sqlite3

import pandas

from nba_magic_stat import conf, logger

def connect_to_database():
    #con = sqlite3.connect('basketball.sqlite')
    con = sqlite3.connect('file:data/basketball.sqlite?mode=rw', uri=True)
    #cur = con.cursor()
    return con

def generate_stats():
    con = connect_to_database()
    req = """
    SELECT 
        name
    FROM 
        sqlite_schema
    WHERE 
        type ='table' AND 
        name NOT LIKE 'sqlite_%';
    """
    req = 'SELECT * FROM Game ORDER BY GAME_DATE DESC LIMIT 5'
    #req = "SELECT * FROM sqlite_schema"
    # logger.debug(f"Running query {req}")
    # for row in cur.execute(req):
    #     print(row)

    res = pandas.read_sql_query(req, con)
    pandas.set_option("display.max_columns", None)
    print(res)
    # query