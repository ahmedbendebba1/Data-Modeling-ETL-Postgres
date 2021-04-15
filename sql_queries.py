create_table = "CREATE TABLE IF NOT EXISTS "
drop_table = "DROP TABLE IF EXISTS "

create_songplays = create_table + "songplays(\
    songplay_id SERIAL PRIMARY KEY,\
    start_time varchar,\
    user_id int ,\
    level varchar,\
    song_id varchar ,\
    artist_id varchar ,\
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
    start_time varchar PRIMARY KEY, \
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


song_table_insert = "INSERT INTO songs (song_id, title, artist_id, year,\
    duration) VALUES (%s, %s, %s, %s, %s)"
artist_table_insert = "INSERT INTO artists (artist_id, name, location, latitude,\
    longitude) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (artist_id) DO NOTHING;"
time_table_insert = "INSERT INTO time (start_time, hour, day, week,\
    month, year, weekday) VALUES (%s, %s, %s, %s, %s, %s, %s) ON CONFLICT\
    (start_time) DO NOTHING"
user_table_insert = "INSERT INTO users (user_id, first_name, last_name, gender,\
    level) VALUES (%s, %s, %s, %s, %s) ON CONFLICT (user_id) DO NOTHING;"
songplay_table_insert = "INSERT INTO songplays (start_time, user_id, level, song_id,\
    artist_id, session_id, location, user_agent) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)\
    ON CONFLICT DO NOTHING;"

song_select = ("SELECT songs.song_id, artists.artist_id FROM songs \
JOIN artists ON songs.artist_id = artists.artist_id \
WHERE songs.title = %s AND artists.name = %s AND songs.duration = %s")




