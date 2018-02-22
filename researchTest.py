# encoding: utf-8

import twitterAPIKey
import stop_words
import re
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.decomposition import LatentDirichletAllocation
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer
# import mglearn
# from sklearn.pipeline import make_pipeline
# from sklearn.linear_model import LogisticRegression
stop = stop_words.stop_words


###################################################
# Link to Twitter
try:
    api = twitterAPIKey.linkToTwitter()
except RuntimeError:
    print('Fail to access to Twitter!\n')
else:
    print("Access to Twitter successfully!\n")


###################################################
# Get tweets from users' following list
class TimeLineContent:

    def __init__(self, id):
        self.id = id
        self.name = api.get_user(id=self.id).name

    def get_timeline(self, count):
        print("\nGetting " + self.name + "'s tweets...")
        try:
            timelines = api.user_timeline(id=self.id, count=count)
        except:
            print("Failed to get " + self.name + "'s tweets!")
        else:
            print("Got " + self.name + "'s tweets successfully!")
            return timelines

    def output_timeline(self, count=500):
        timelines = self.get_timeline(count)
        timeline_new = ""
        try:
            for timeline in timelines:
                timeline_new += timeline.text.replace('\n', ' ')
        except:
            pass
        else:
            return timeline_new


###################################################
# delete not English words
def englishlize(textList):
    temp = []
    for i in textList:
        temp2 = []
        for n in i.split(" "):
            if re.match("^[@#]*[A-Za-z0-9]+$", n):
                temp2.append(n)
        temp.append(" ".join(temp2))
    return temp


###################################################
# Get favorite contents
def favorites(account_id):
    favorites_list = []
    for i in api.favorites(id=account_id):
        vect = CountVectorizer(max_features=150, stop_words=stop)
        i = englishlize(i.text.replace('\n', ' ').split(' '))
        vect.fit_transform(i)
        favorites_list.append(" ".join(vect.get_feature_names()))
    print(favorites_list)
    return favorites_list


###################################################
# LDA model
def lda_clustering(new_timeline, n):
    print('\nStart to do clustering . . .')
    #################
    # Bag of Words
    # Delete stop words
    # Delete non-english words
    vect = CountVectorizer(max_features=50000, min_df=.1, stop_words=stop)
    temp = englishlize(new_timeline)
    X = vect.fit_transform(temp)
    #################
    # LDA
    lda = LatentDirichletAllocation(n_topics=n, learning_method='batch', max_iter=25, random_state=0)
    lda.fit_transform(X)
    feature_names = np.array(vect.get_feature_names())

    topic_list = []
    index = 0
    for topic_idx, topic in enumerate(lda.components_):
        # message = "Topic #%d: " % topic_idx
        message = ""
        message += " ".join([feature_names[i] for i in topic.argsort()[:-20 - 1:-1]])
        topic_list.append(message)
        print('\n', "#Topic", index, ":", message)
        index += 1
    print('\nFinishing clustering . . .')
    return topic_list


###################################################
# cosine similarity
def cos_similarity(key_word_list, profile):
    train_set = [key_word_list]
    train_set.append(" ".join([x for x in profile]))
    tfidf_vectorizer = TfidfVectorizer()
    tfidf_matrix_train = tfidf_vectorizer.fit_transform(train_set)
    similarity_list = cosine_similarity(tfidf_matrix_train[0:1], tfidf_matrix_train)
    return similarity_list


###################################################
# main
# twitter_name = input("アカウントを入力してください：")
twitter_name = "MyTopicTest"
new_timeline = []
followingList = api.friends_ids(screen_name=twitter_name)
print(len(followingList), "in following list.")
followingCount = 0

for i in followingList:
    followingCount += 1
    try:
        temp = TimeLineContent(i)
    except:
        print('\nFailed to get information from user id:', i)
        continue
    else:
        new_timeline.append(str(temp.output_timeline(200)))
    print("(", followingCount, "/", len(followingList), ") Done")
    # if followingCount == 3:
    #     break

topic_list = lda_clustering(new_timeline, 10)

print('\nFavorites:')
favorites_list = favorites(twitter_name)
print()

topic_index = 0
for i in topic_list:
    print('\nTopic #', topic_index, '***************')
    print("Cosine similarity is", cos_similarity(i, favorites_list)[0][1])
    topic_index += 1


# a = api.get_user(id='PokemonGoApp')
# print('\nPokemonGpApp: ' + a.description)





