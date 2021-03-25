import mysql.connector
import datetime
import os
from decouple import config

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

mydb = mysql.connector.connect(
    host=config('DB_HOST'),
    user=config('DB_USERNAME'),
    passwd=config('DB_PASSWORD'),
    database=config('DB_DATABASE')
)

mycursor = mydb.cursor()

mycursor.execute('SET NAMES utf8mb4')
mycursor.execute("SET CHARACTER SET utf8mb4")
mycursor.execute("SET character_set_connection=utf8mb4")


# check tweet if exist or not ^_^
def check(id):
    mycursor.execute("select * from tweets where tweet_id = " + id + " LIMIT 1")
    myresult = mycursor.fetchall()
    if not myresult:
        return 'FALSE'
    else:
        return 'TRUE'


# store tweet ^_*
def store(tweet):
    if check(tweet.id_str) == 'FALSE':
        mycursor = mydb.cursor()
        sql = "INSERT INTO tweets (name, screen_name, text, tweet_id, state, created_at) VALUES (%s, %s, %s, %s, %s, %s)"
        val = (tweet.user.name, tweet.user.screen_name, tweet.text.replace('@waynArwh ', ''), tweet.id_str, 'false',
               datetime.datetime.now())
        mycursor.execute(sql, val)
        mydb.commit()
        return 'Tweet number : ' + tweet.id_str + ' Saved'
    else:
        return 'Tweet number : ' + tweet.id_str + ' already saved'


# get tweets with false state *_*
def getTweetsWithFalseState():
    mycursor.execute("select screen_name, text, tweet_id from tweets where state = 'false'")
    myresult = mycursor.fetchall()
    if not myresult:
        return 'FALSE'
    else:
        return myresult


# get random place *_^
def getRandPlace():
    mycursor.execute("select text from places ORDER BY RAND() LIMIT 1;")
    myresult = mycursor.fetchall()
    if not myresult:
        return 'FALSE'
    else:
        return myresult[0][0]


# update state of tweet -_-
def UpdateTweetStateToTrue(id):
    sql = "UPDATE tweets SET state = 'true' WHERE tweet_id = " + id
    mycursor.execute(sql)
    mydb.commit()
