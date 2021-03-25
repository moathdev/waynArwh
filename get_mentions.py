import config.twitter_connection as twitter
import config.mysql_connection as mysql


# store tweets into our tweets table :)
for tweet in twitter.api.GetMentions():
    print(mysql.store(tweet))
