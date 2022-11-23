import sqlite3

con = sqlite3.connect("./cineManage.db")
cur = con.cursor()

cur.executescript("""
            DROP TABLE IF EXISTS studio;
            DROP TABLE IF EXISTS seat;
            DROP TABLE IF EXISTS screening;
            DROP TABLE IF EXISTS film;
            DROP TABLE IF EXISTS ticket;
            DROP TABLE IF EXISTS user;
            
            CREATE TABLE ticket(
                SeatID TEXT NOT NULL,
                StudioID INT NOT NULL,
                ScreeningID INT NOT NULL,
                OrderDatetime TEXT NOT NULL,
                PRIMARY KEY (SeatID, StudioID, ScreeningID)
            );
            
            CREATE TABLE user(
                UserID INT NOT NULL PRIMARY KEY,
                Password TEXT NOT NULL,
                Role TEXT NOT NULL
            );

            CREATE TABLE studio (
                StudioID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT, 
                Name TEXT NOT NULL UNIQUE, 
                Capacity INTEGER NOT NULL);
            
            CREATE TABLE screening(
                ScreeningID INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
                StudioID INT NOT NULL,
                FilmTitle TEXT NOT NULL,
                StartTime TEXT NOT NULL,
                EndTime TEXT NOT NULL
            );

            CREATE TABLE film(
                FilmID INTEGER PRIMARY KEY AUTOINCREMENT,
                Title TEXT NOT NULL UNIQUE,
                Duration INTEGER,
                Description TEXT,
                Poster TEXT
            );

            CREATE TABLE seat(
                SeatID TEXT NOT NULL,
                StudioID INT NOT NULL,
                ScreeningReserved TEXT,
                FOREIGN KEY (StudioID) REFERENCES studio (StudioID) ON UPDATE CASCADE ON DELETE CASCADE,
                PRIMARY KEY (SeatID, StudioID)
            );
            """)