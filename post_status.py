import config.twitter_connection as twitter
import config.mysql_connection as mysql

# Get tweets where reply status = FALSE .
tweets = mysql.getTweetsWithFalseState()

if tweets != 'FALSE':
    for tweet in tweets:

        # Get rand place ready for reply.
        text = mysql.getRandPlace()

        # Reply to the tweet and update reply status to true .
        twitter.api.PostUpdate('@' + tweet[0] + ' ' + text.decode('utf-8'),
                               media=None,
                               media_additional_owners=None,
                               media_category=None,
                               in_reply_to_status_id=tweet[2],
                               auto_populate_reply_metadata=False,
                               exclude_reply_user_ids=None,
                               latitude=None,
                               longitude=None,
                               place_id=None,
                               display_coordinates=False,
                               trim_user=False,
                               verify_status_length=True,
                               attachment_url=None)

        mysql.UpdateTweetStateToTrue(tweet[2])
