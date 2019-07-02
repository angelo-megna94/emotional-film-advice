from Settings import consumerSecret, consumerKey, accessSecret, accessToken
import tweepy
from tweepy import OAuthHandler
import csv

auth = OAuthHandler(consumerKey, consumerSecret)  # oggetto autenticatore
auth.set_access_token(accessToken, accessSecret)  # token d'accesso
api = tweepy.API(auth)

num_tweets = int(input("Quanti tweets vuoi prelevare? "))
username = input("Inserisci lo username dell'utente (es. Leonardo Di Caprio = @LeoDiCaprio): ").replace("@", "")
print("*** DOWNLOAD E SALVATAGGIO DEI TWEETS DI " + username + " ***\n")
# Con items(n) decidiamo quanti tweet (n) prendere
for status in tweepy.Cursor(api.user_timeline, screen_name=username, tweet_mode="extended", lang="en",
                            include_rts=False).items(num_tweets):
    # print("Tweet:\n",status.full_text)
    print("...")
    #with open('tweet_estratti_' + username + '2.csv', 'a+', encoding='utf8') as file:
        #writer = csv.writer(file)
        #for line in status.iter_lines():
        #writer.writerow(status.full_text.decode('utf-8').split(','))
        # file.write(status.full_text)
        # file.write("\n")
    with open('tweet_estratti_' + username + '.csv', 'a+') as file:
        writer = csv.writer(file)
        writer.writerow([status.full_text])

