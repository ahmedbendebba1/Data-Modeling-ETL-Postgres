import os
import glob
import psycopg2
import pandas as pd
import numpy as np
from sql_queries import *


def get_files(filepath):
    """get a list of all song JSON files in data/song_data"""
    all_files = []
    for root, dirs, files in os.walk(filepath):
        files = glob.glob(os.path.join(root,'*.json'))
        for f in files :
            all_files.append(os.path.abspath(f))
    
    return all_files

#Set connexion and cursor
conn = psycopg2.connect(
    "host=127.0.0.1 dbname=sparkifydb user=postgres password=postgres"
    )
cur = conn.cursor()

#Set automcommit
conn.set_session(autocommit=True)

song_paths = get_files('data/song_data')

#ETL artists table
for song_path in song_paths:
    #Extract data
    artist_df = pd.read_json(song_path, lines=True)
    artist_data = artist_df[[
        'artist_id','artist_name','artist_location','artist_latitude','artist_longitude'
        ]]\
        .values[0]\
        .tolist()
        #Load data
    cur.execute(artist_table_insert, artist_data)

#ETL songs table
for song_path in song_paths:
    #Extract data
    song_df = pd.read_json(song_path, lines=True)
    song_data = song_df[['song_id','title','artist_id','year','duration']]\
        .values[0]\
        .tolist()
    #Load data
    cur.execute(song_table_insert, song_data)

log_paths = get_files('data/log_data')

#ETL time table
for log_path in log_paths:
    #Extract data
    log_df = pd.read_json(log_path, lines=True)

    #Transform data
    ts_df = log_df[log_df.page == "NextSong"]['ts']
    log_df['ts'] = pd.to_datetime(ts_df, unit='ms')
    t = log_df.copy()

    time_data = (t.ts, t.ts.dt.hour , t.ts.dt.day , t.ts.dt.dayofweek ,\
        t.ts.dt.month , t.ts.dt.year , t.ts.dt.weekday\
        )
    column_labels = ['start_time', 'hour', 'day', 'week', 'month', 'year', 'weekday']

    time_df = pd.DataFrame(columns=column_labels)

    for index, column_label in enumerate(column_labels):
        time_df[column_label] = time_data[index]

    time_df.dropna(subset=['start_time'],inplace=True)

    #Load data
    for i, row in time_df.iterrows():
        cur.execute(time_table_insert, list(row))

#ETL user table
for log_path in log_paths:
    #Extract data
    log_df = pd.read_json(log_path, lines=True)
    user_df = log_df[['userId', 'firstName', 'lastName', 'gender', 'level']].copy()
    user_df['userId'] = user_df['userId'].replace('',np.nan)
    user_df.dropna(subset=['userId'],inplace=True)
    #Load data
    for i, row in user_df.iterrows():
        cur.execute(user_table_insert, row)

#ETL songplays table
for log_path in log_paths:
    #Extract data
    log_df = pd.read_json(log_path, lines=True)
    ts_df = log_df['ts']
    log_df['ts'] = pd.to_datetime(ts_df, unit='ms')

    log_df['userId'] = log_df['userId'].replace('',np.nan)
    log_df.dropna(subset=['userId'],inplace=True)
    
    for index, row in log_df.iterrows():
        # get songid and artistid from song and artist tables
        cur.execute(song_select, (row.song, row.artist, row.length))
        results = cur.fetchone()
        
        if results:
            songid, artistid = results
        else:
            songid, artistid = None, None

        # insert songplay record
        songplay_data = (row.ts, row.userId, row.level, songid, artistid,\
            row.sessionId, row.location, row.userAgent\
            )
        cur.execute(songplay_table_insert, songplay_data)

conn.close()





    










