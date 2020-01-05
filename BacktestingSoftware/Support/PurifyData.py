import sqlite3
import csv
import datetime
import random
# Create a database if not exists and get a connection to it
connection = sqlite3.connect('C:\\Users\\JGISI\\OneDrive\\Desktop\\BackTestData.db')

# Get a cursor to execute sql statements
cursor = connection.cursor()


def with_Next(iterable):
    """Yield (current, next_item) tuples for each item in iterable."""
    iterator = iter(iterable)
    current = next(iterator)
    for next_item in iterator:
        yield current, next_item
        current = next_item


with open('C:\\Users\\treeb\\OneDrive\\Documents\\AmazonDriveDownload\\FXData_201901\\GBP_USD_2006-01-01_2019-02-02\\GBP_USD_2006-01-01_2019-02-02.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')
    i=0
    for row, rowNext in with_Next(csv_reader):
        #print(f'\t{row[0]} {row[1]} {row[2]} {row[3]} {row[4]} {row[5]}')
        time = row[2]

        if len(time) == 1: time = '00000' + time
        if len(time) == 2: time = '0000' + time
        if len(time) == 3: time = '000' + time
        if len(time) == 4: time = '00' + time
        if len(time) == 5: time = '0' + time


        time = time[:2] + ':' + time[2:4] + ':' + time[-2:]
        date = row[1]
        date = date[:4] + '-' + date[4:6] + '-' + date[-2:]
        d = date + ' ' + time
        dCurrent = datetime.datetime.strptime(d, '%Y-%m-%d %H:%M:%S')


        timeNext = rowNext[2]
        if len(timeNext) == 1: timeNext = '00000' + timeNext
        if len(timeNext) == 2: timeNext = '0000' + timeNext
        if len(timeNext) == 3: timeNext = '000' + timeNext
        if len(timeNext) == 4: timeNext = '00' + timeNext
        if len(timeNext) == 5: timeNext = '0' + timeNext


        timeNext = timeNext[:2] + ':' + timeNext[2:4] + ':' + timeNext[-2:]
        dateNext = rowNext[1]
        dateNext = dateNext[:4] + '-' + dateNext[4:6] + '-' + dateNext[-2:]
        dNext = dateNext + ' ' + timeNext
        dNext = datetime.datetime.strptime(dNext, '%Y-%m-%d %H:%M:%S')

        open = row[3]
        high = row[4]
        low = row[5]
        close = row[6]
        volume = row[7]

        sql = "INSERT INTO GBP_USD(DATETIME, OPEN, HIGH, LOW, CLOSE, VOLUME, GENERATED ) " \
              "VALUES ( '" + str(dCurrent) + "', " + str(open) + ", " + str(high) + ", " + str(low) + ", " + str(
            close) + ", " + str(volume) + ", 0 )"
        print(sql)

        cursor.execute(sql)

        #print('"'+str(dCurrent) + '" ' + str(open) +' ' + str(high) +' ' + str(low) +' ' + str(close) +' ' + str(volume) + ' False')
        if datetime.timedelta(minutes=1) < dNext-dCurrent < datetime.timedelta(hours=2):
            c = (dNext - dCurrent)
            c = int(c.total_seconds()/60)
            fillin = dCurrent
            for x in range(1,c):
                fillin = fillin + datetime.timedelta(minutes=1)
                o = round(random.uniform(float(row[3]),float(rowNext[3])), 5)
                h = round(random.uniform(float(row[4]),float(rowNext[4])), 5)
                l = round(random.uniform(float(row[5]),float(rowNext[5])), 5)
                c = round(random.uniform(float(row[6]),float(rowNext[6])), 5)
                v = random.randint(min(int(row[7]),int(rowNext[7])),max(int(row[7]),int(rowNext[7])))
                #print('"' + str(fillin) + '" ' + str(o) + ' ' + str(h) + ' ' + str(l) + ' ' + str(c) + ' ' + str(v) + ' 1')
                sql = "INSERT INTO GBP_USD(DATETIME, OPEN, HIGH, LOW, CLOSE, VOLUME, GENERATED ) " \
                      "VALUES ( '" + str(fillin) + "', " + str(o) + ", " + str(h) + ", " + str(l) + ", " + str(
                    c) + ", " + str(v) + ", 1 )"
                print(sql)
                cursor.execute(sql)





connection.commit()
connection.close()


