# DROP TABLES

songplay_table_drop = "DROP TABLE IF EXISTS SONGPLAYS;"
user_table_drop = "DROP TABLE IF EXISTS USERS;"
song_table_drop = "DROP TABLE IF EXISTS SONGS;"
artist_table_drop = "DROP TABLE IF EXISTS ARTISTS;"
time_table_drop = "DROP TABLE IF EXISTS TIME;"

# CREATE TABLES

songplay_table_create = ("""
CREATE TABLE IF NOT EXISTS SONGPLAYS (
    SONGPLAY_ID SERIAL PRIMARY KEY,
    START_TIME TIMESTAMP NOT NULL,
    USER_ID INTEGER NOT NULL,
    LEVEL VARCHAR NOT NULL,
    SONG_ID VARCHAR,
    ARTIST_ID VARCHAR,
    SESSION_ID INTEGER NOT NULL,
    LOCATION VARCHAR,
    USER_AGENT VARCHAR
);
""")

user_table_create = ("""
CREATE TABLE IF NOT EXISTS USERS (
    USER_ID INTEGER PRIMARY KEY,
    FIRST_NAME VARCHAR NOT NULL,
    LAST_NAME VARCHAR NOT NULL,
    GENDER VARCHAR,
    LEVEL VARCHAR NOT NULL
);
""")

song_table_create = ("""
CREATE TABLE IF NOT EXISTS SONGS (
    SONG_ID VARCHAR PRIMARY KEY,
    TITLE VARCHAR NOT NULL,
    ARTIST_ID VARCHAR NOT NULL,
    YEAR INTEGER NOT NULL,
    DURATION FLOAT NOT NULL
);
""")

artist_table_create = ("""
CREATE TABLE IF NOT EXISTS ARTISTS (
    ARTIST_ID VARCHAR PRIMARY KEY,
    NAME VARCHAR NOT NULL,
    LOCATION VARCHAR,
    LATITUDE FLOAT,
    LONGITUDE FLOAT
);
""")

time_table_create = ("""
CREATE TABLE IF NOT EXISTS TIME (
    START_TIME TIMESTAMP PRIMARY KEY,
    HOUR INTEGER NOT NULL,
    DAY INT NOT NULL,
    WEEK INTEGER NOT NULL,
    MONTH INTEGER NOT NULL,
    YEAR INTEGER NOT NULL,
    WEEKDAY INTEGER NOT NULL
);
""")

# INSERT RECORDS

songplay_table_insert = ("""
    INSERT INTO SONGPLAYS (START_TIME, USER_ID, LEVEL, SONG_ID, ARTIST_ID, SESSION_ID, LOCATION, USER_AGENT)
    VALUES(to_timestamp(%s), %s, %s, %s, %s, %s, %s, %s);
""")

user_table_insert = ("""
    INSERT INTO USERS (USER_ID, FIRST_NAME, LAST_NAME, GENDER, LEVEL)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (USER_ID)
    DO UPDATE
    SET LEVEL = EXCLUDED.LEVEL;
""")

song_table_insert = ("""
    INSERT INTO SONGS (SONG_ID, TITLE, ARTIST_ID, YEAR, DURATION)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (SONG_ID)
    DO NOTHING;
""")

artist_table_insert = ("""
    INSERT INTO ARTISTS (ARTIST_ID, NAME, LOCATION, LATITUDE, LONGITUDE)
    VALUES(%s, %s, %s, %s, %s)
    ON CONFLICT (ARTIST_ID)
    DO NOTHING;
""")

time_table_insert = ("""
    INSERT INTO TIME (START_TIME, HOUR, DAY, WEEK, MONTH, YEAR, WEEKDAY)
    VALUES(to_timestamp(%s), %s, %s, %s, %s, %s, %s)
    ON CONFLICT (START_TIME)
    DO NOTHING;
""")

# FIND SONGS

song_select = ("""
    SELECT SONGS.SONG_ID, ARTISTS.ARTIST_ID FROM SONGS
    JOIN ARTISTS ON SONGS.ARTIST_ID = ARTISTS.ARTIST_ID
    WHERE SONGS.TITLE = %s AND ARTISTS.NAME = %s AND SONGS.DURATION = %s;
""")

# QUERY LISTS

create_table_queries = [songplay_table_create, user_table_create, song_table_create, artist_table_create, time_table_create]
drop_table_queries = [songplay_table_drop, user_table_drop, song_table_drop, artist_table_drop, time_table_drop]
