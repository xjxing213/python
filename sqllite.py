import sqlite3
def convert(value):
    if value.startswith('~'):
        return value.strip('~')
    if not value:
        value = '0'
    return float(value)

conn = sqlite3.connect('food.db')
curs = conn.cursor()

##curs.execute('''
##CREATE TABLE food2 (
##id TEXT PRIMARY KEY,
##desc TEXT,
##water FLOAT,
##kcal FLOAT,
##protein FLOAT,
##fat FLOAT,
##ash FLOAT,
##carbs FLOAT,
##fiber FLOAT,
##sugar FLOAT
##)
##''')

query = 'INSERT INTO food VALUES (2,"t",1.0,1.0,1.0,1.0,1.0,1.0,1.0,1.0)'
##field_count = 10
##for line in open('ABBREV.txt','w+'):
##    fields = line.split('^')
##    vals = [convert(f) for f in fields[:field_count]]
##    curs.execute(query, vals)
print(curs.execute(query))
conn.commit()
conn.close()
