
def createSQLiteTable(theDBObject, theSQLiteDatabaseName,theDeleteIfExists):
    con = None
    try:
        con = lite.connect(theSQLiteDatabaseName)
        cur = con.cursor()
        if (theDeleteIfExists):
            cur.execute("DROP TABLE IF EXISTS " + theDBObject.getTableName())
        sqlCmd = "CREATE TABLE " + theDBObject.getTableName() + "("
        i = 0
        colNames = theDBObject.getColumns()
        for col in colNames:
            if (i !=0 ):
                sqlCmd = sqlCmd + "," + col + " TEXT"
            else:
                sqlCmd = sqlCmd + col + " TEXT"
        sqlCmd = sqlCmd + ")"
        cur.execute(sqlCmd)
        print("Table " + theDBObject.getTableName() + " Created")
        con.commit()
    except lite.Error, e:
        if con:
            con.rollback()
            print "Error %s:" % e.args[0]
            sys.exit(1)
    finally:
        if con:
            con.close()
