import pandas as pd
import praw
from prawcore.exceptions import Forbidden
import json

CREDENTIALS = "UserCredentials.json"
with open(CREDENTIALS, "r") as j:
    cred = j.read()
cred = json.loads(cred)

reddit = praw.Reddit(
    client_id=cred["client_id"],
    client_secret=cred["client_secret"],
    password=cred["password"],
    user_agent=cred["user_agent"],
    username=cred["username"],
)


class RedditTopUsersInfo:
    def __init__(self, subreddit_name, subreddit_posts_count=100, user_posts_count=10):
        self.subreddit_name = subreddit_name
        self.user_posts_count = user_posts_count
        self.subreddit_posts_count = subreddit_posts_count
        self.top_posts_info_df : pd.DataFrame
        self.freq_authors : pd.DataFrame

    def get_top_posts_info(self):
        """
        Retrieve info based on top subreddit posts.
        :return: pandas dataframe with 4 columns: 'id', 'author', 'score', 'subreddit'
        """
        subreddit = reddit.subreddit(self.subreddit_name)
        post_info = [
            (subm.id, str(subm.author), int(subm.score), subm.subreddit)
            for subm in subreddit.top(limit=self.subreddit_posts_count)
        ]
        df = pd.DataFrame(post_info, columns=["id", "author", "score", "subreddit"])
        print(df)
        return df

    def get_top_users_info(self, info=True):
        self.top_posts_info_df = self.get_top_posts_info()
        self.freq_authors = self.top_posts_info_df.loc[
            self.top_posts_info_df["author"].ne("None"), "author"
        ].unique()

        if info:
            print(f"Length of freq_authors = {len(self.freq_authors)}")
            print(self.freq_authors)

        return self.freq_authors

    def get_users_post(self, username, number=5):
        user = reddit.redditor(username)
        user_comments_info = []

        for comment in user.comments.new(limit=number):
            user_comments_info.append(
                (
                    str(comment.id),
                    str(username),
                    int(comment.score),
                    str(comment.subreddit.display_name),
                )
            )

        user_posts_df = pd.DataFrame(
            user_comments_info, columns=["id", "user_name", "score", "subreddit_name"]
        )
        return user_posts_df[["id", "score", "user_name", "subreddit_name"]]

    def scrap_celebrities(self):
        usernames : list = self.get_top_users_info()
        celebrities = list()

        for author in usernames:
            try:
                users_post = self.get_users_post(author, self.user_posts_count)
                print(users_post)
                celebrities.append(users_post)
            except Forbidden:
                print(f"{author} account deleted or banned")

        df = pd.concat(celebrities)
        print(df.info())
        print(df)
        return df
