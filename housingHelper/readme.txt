http://findmyfbid.com/success/1650616371871158

https://developers.facebook.com/docs/graph-api/reference/v2.8/group/members/

https://developers.facebook.com/tools/explorer/211505512667724?method=GET&path=7030462319%2Ffeed%3Ffields%3Dmessage%2Ccreated_time%2Clikes.limit(0).summary(true)%26limit%3D100&version=v2.8


7030462319/feed?fields=message,created_time,likes.limit(0).summary(true)&limit=100

http://stackoverflow.com/questions/39314152/fb-graph-api-get-group-wall-posts-with-time-posted-and-number-of-likes

group-id/feed?fields=message,created_time,likes.limit(0).summary(true)&limit=100

https://developers.facebook.com/docs/graph-api/advanced/rate-limiting

https://developers.facebook.com/docs/graph-api/making-multiple-requests

https://developers.facebook.com/docs/graph-api/using-graph-apihttps://developers.facebook.com/docs/graph-api/using-graph-api

#debuf the access token
https://developers.facebook.com/tools/debug/access_token/

GET graph.facebook.com
  /photos?ids={user-id-a},{user-id-b}
Is equivalent to the following individual API requests:

GET graph.facebook.com
  /{user-id-a}/photos

GET graph.facebook.com
  /{user-id-b}/photos



#THIS IS NEEDED FOR A LONG LIVED ACCESS TOKEN (2months).  You will need a short-lived one in order to make a long lived one
https://developers.facebook.com/docs/facebook-login/access-tokens/expiration-and-extension

The current access token was generated on August 27th.  and will expire Thursday, October 26, 2017 3:28:13 (use the debug access token link to see that...You will get epoch time back).  I went here
https://developers.facebook.com/tools/explorer/211505512667724?method=GET&path=oauth%2Faccess_token%3Fgrant_type%3Dfb_exchange_token%26client_id%3D211505512667724%26client_secret%3Dacd17831eb4c87cc740d83ab304643df%26fb_exchange_token%3DEAADAXPbzWkwBAGJhK6BiORkTo0K8kjcZAAmMeADie0dPARwTcSSZBuBZCZCuGz8rTCsUS8oLgiAjzGuEiTn4Tf5Wd7czvd07I3SZBJbnkB8jWNhkvJybM6XJB7g5hTs2aezvcQrrZCWgQVUIV41DJZB6rkgISv15ZArT9htdIQDH1NAdHAiZAr4JaIQCK8diZCXp0lzcUvrQBBrQZDZD&version=v2.10

##app id and app-secret are in the config.cfg file.  Go generate a short-lived access token from the fackebook web app tester
and use the endpoint here:
GET /oauth/access_token?
    grant_type=fb_exchange_token&
    client_id={app-id}&
    client_secret={app-secret}&
    fb_exchange_token={short-lived-token}

also see https://stackoverflow.com/questions/12168452/long-lasting-fb-access-token-for-server-to-pull-fb-page-info?rq=1



Your app can make 200 calls per hour per user in aggregate. As an example, if your app has 100 users, this means that your app can make 20,000 calls. This isn't a per-user limit, so one user could make 19,000 of those calls and another could make 1,000. This limit is calculated based on the number of calls made in the previous hour.


#TO DO::
use a python spell corrector or equiv


######VIRTUALENV at  ~/VEnvironments/housingHelper/