try:
    from sqlite3 import dbapi2 as sqlite3
except ImportError:
    print "Support for Sqlite 3 needed. Quitting."
    sys.exit(-2)

def db_init():
    db = self.__get_db()
    try:
        with open('schema.sql') as fd:
            db.cursor().executescript(fd.read())
            db.commit()
    except Exception, e:
        print "Failed to open DB: %s" % e
        sys.exit(-2)
            
def db_get():
    try:
        sqlite_db = sqlite3.connect('swedbank.db')
        sqlite_db.row_factory = sqlite3.Row
    except Exception, e:
        print "Failed to connect to DB (is the database initialized?): %s" % e
        sys.exit(-2)
    return sqlite_db

def db_insert(label, value):
    try:
        db = db_get()
        db.execute('insert into sys_stat (label, value) values(?, ?)', 
                   (label, value))
        db.commit()
    except:
        return None

