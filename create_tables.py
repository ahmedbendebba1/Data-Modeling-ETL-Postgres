import psycopg2
from sql_queries import * 

#Set connexion and cursor. Database should be already created (see Readme.md)
conn = psycopg2.connect(database ="sparkifydb", user="postgres", \
      password="postgres", host="localhost")
cursor = conn.cursor()

#Set autocommit transactions
conn.set_session(autocommit=True)

#Drop old version of tables if existed
cursor.execute(drop_songplays)
cursor.execute(drop_users)
cursor.execute(drop_songs)
cursor.execute(drop_artists)
cursor.execute(drop_time)

#Create new version of tables if not existed
cursor.execute(create_users)
cursor.execute(create_artists)
cursor.execute(create_songs)
cursor.execute(create_time)
cursor.execute(create_songplays)