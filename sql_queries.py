create_table = "CREATE TABLE IF NOT EXISTS "
drop_table = "DROP TABLE IF EXISTS "

create_songplays = create_table + "songplays(\
    songplay_id SERIAL PRIMARY KEY,\
    start_time timestamp REFERENCES time(start_time),\
    user_id int REFERENCES users(user_id),\
    level varchar,\
    song_id varchar REFERENCES songs(song_id),\
    artist_id varchar REFERENCES artists(artist_id),\
    session_id int,\
    location varchar,\
    user_agent varchar\
    );"

create_users = create_table + "users(\
    user_id int PRIMARY KEY, \
    first_name varchar, \
    last_name varchar, \
    gender char, \
    level varchar\
    );"

create_songs = create_table + "songs(\
    song_id varchar PRIMARY KEY, \
    title varchar, \
    artist_id varchar, \
    year int, \
    duration float\
    );"

create_artists = create_table + "artists(\
    artist_id varchar PRIMARY KEY, \
    name varchar, \
    location varchar, \
    latitude float, \
    longitude float\
    );"

create_time = create_table + "time(\
    start_time timestamp PRIMARY KEY, \
    hour int, \
    day int, \
    week int, \
    month int, \
    year int, \
    weekday int\
    );"

drop_songplays = drop_table + "songplays;"
drop_users = drop_table + "users;"
drop_songs = drop_table + "songs;"
drop_artists = drop_table + "artists;"
drop_time = drop_table + "time;"




