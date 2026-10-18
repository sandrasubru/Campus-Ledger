import sqlite3

def init_db():
    print('Connecting to SQLite Database...')
    conn = sqlite3.connect('campus_ledger.db')
    c = conn.cursor()
    
    # Drop to cleanly recreate schema (Keep events for persistence)
    c.execute('DROP TABLE IF EXISTS students')
    c.execute('DROP TABLE IF EXISTS admins')
    # c.execute('DROP TABLE IF EXISTS events')
    
    c.execute('''CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        wallet_address TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS admins (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        username TEXT UNIQUE NOT NULL,
        password TEXT NOT NULL,
        club_name TEXT NOT NULL,
        wallet_address TEXT NOT NULL
    )''')
    c.execute('''CREATE TABLE IF NOT EXISTS events (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        club_name TEXT NOT NULL,
        event_name TEXT NOT NULL,
        date TEXT NOT NULL,
        start_time TEXT NOT NULL,
        end_time TEXT NOT NULL,
        cost INTEGER NOT NULL,
        wallet_address TEXT NOT NULL
    )''')
    
    # Store the exact accounts requested
    c.execute("INSERT INTO students (username, password, wallet_address) VALUES ('rushdha', 'rushdha123', '0x2dF228A9E4F3D60ad292402C38BDb17d40a4Edd4')")
    c.execute("INSERT INTO admins (username, password, club_name, wallet_address) VALUES ('tinkerhub', 'tinkerhub123', 'TINKERHUB', '0xdB49dca421e1d95B25819Ab633040A03FB0674Ad')")
    c.execute("INSERT INTO admins (username, password, club_name, wallet_address) VALUES ('asthra', 'asthra123', 'ASTHRA', '0x0ef04cB9A52995dC4e6beec5d40d45D41FCdd6f6')")
    c.execute("INSERT INTO admins (username, password, club_name, wallet_address) VALUES ('orso', 'orso123', 'ORSO', '0x6E62AA14E0D7E81E641cb0F92777737A3D8E6481')")
    
    conn.commit()
    conn.close()
    print('Database initialized successfully with the requested accounts containing wallet addresses!')

if __name__ == '__main__':
    init_db()
