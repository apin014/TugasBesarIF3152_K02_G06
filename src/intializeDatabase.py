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
            
            CREATE TABLE studio(
                StudioID INT NOT NULL PRIMARY KEY,
                Name TEXT NOT NULL UNIQUE,
                Capacity INTEGER NOT NULL
            );
            
            CREATE TABLE seat(
                SeatID TEXT NOT NULL,
                StudioID INT NOT NULL,
                Row INTEGER NOT NULL,
                Column INTEGER NOT NULL,
                FOREIGN KEY (StudioID) REFERENCES studio (StudioID) ON UPDATE CASCADE ON DELETE CASCADE,
                PRIMARY KEY (SeatID, StudioID)
            );
            
            CREATE TABLE film(
                FilmID INT PRIMARY KEY,
                Title TEXT NOT NULL UNIQUE,
                Duration INTEGER,
                Description TEXT
            );
            
            CREATE TABLE screening(
                ScreeningID INT NOT NULL PRIMARY KEY,
                StudioID INT NOT NULL,
                FilmTitle TEXT NOT NULL,
                StartTime TEXT NOT NULL,
                EndTime TEXT NOT NULL,
                FOREIGN KEY (StudioID) REFERENCES studio (StudioID) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (FilmTitle) REFERENCES film (Title) ON UPDATE CASCADE ON DELETE CASCADE
            );
            
            CREATE TABLE ticket(
                SeatID TEXT NOT NULL,
                ScreeningID INT NOT NULL,
                OrderDatetime TEXT NOT NULL,
                FOREIGN KEY (SeatID) REFERENCES seat (SeatID) ON UPDATE CASCADE ON DELETE CASCADE,
                FOREIGN KEY (ScreeningID) REFERENCES screening (ScreeningID) ON UPDATE CASCADE ON DELETE CASCADE,
                PRIMARY KEY (SeatID, ScreeningID)
            );
            
            CREATE TABLE user(
                UserID INT NOT NULL PRIMARY KEY,
                Password TEXT NOT NULL,
                Role TEXT NOT NULL
            )
            """)