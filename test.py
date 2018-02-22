# encoding = "utf-8"

import twitterAPIKey


# import re
#
# a = ["123", "weq12", "wwq123wqe", "123qw", "123weq123", "wer我", "123", "我wq12"]
# temp = []
#
# for i in a:
#     if re.match("^[a-z0-9]+$", i):
#         temp.append(i)
# print(temp)



api = twitterAPIKey.linkToTwitter()
list = api.friends_ids(screen_name="MyTopicTest")
print(len(list))
