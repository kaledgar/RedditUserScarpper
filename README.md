# RedditUserScarpper
Python program to request Top Authors on a given subreddit and plot connections between different communities.

![Graph with 360 nodes and 371 edges_visual](https://github.com/kkinastowski66/RedditUserScarpper/assets/101144906/ce8c75fa-f03b-4c9f-a98a-22ce60d1ecc0)


## RedditTopUsersInfo.py
This is a Python script that uses the PRAW (Python Reddit API Wrapper - https://praw.readthedocs.io/en/stable/index.html) library to gather information about top users on a specific subreddit. It returns a pandas dataframe with information based on top subreddit posts.

## Dependencies:
- json: A module for working with JSON data.
- logging: A module for logging messages during program execution.
- pandas: A library for data manipulation and analysis.
- praw: A Python wrapper for the Reddit API.
- prawcore.exceptions.Forbidden: An exception raised when access to a resource is forbidden.
- .constants: A module containing constant values for the application.

## Python virtual environment

To spawn a Python virtual environment shell run:

```sh
python3 -m venv .venv
source .venv/bin/activate
```

Then, to install the dependencies in the virtual environment run:

```sh
pip install --requirement requirements.txt
```

## Usage
To use this script, simply import the RedditTopUsersInfo class from UsersInfo.py and create an instance of the class with the desired subreddit name and number of posts to scrape. Then, call the appropriate method to get the desired information.

```python 
from UsersInfo import RedditTopUsersInfo

# create instance
rtui = RedditTopUsersInfo(subreddit_name='python', no_subreddit_posts=100, no_user_posts=10)

# get top posts info
rtui.get_top_posts_info()

# get top users info
rtui.get_top_users_info()

# get user's post info
rtui.get_users_post(username='example_user', number=10)

# scrap celebrities' post info
rtui.scrap_celebrities()
```

## Output
The output of get_top_posts_info() is a pandas dataframe with 4 columns:

- id: id of a post (str)
- author: username (str)
- score: number of upvotes (int)
- subreddit: name of the subreddit that the submission was posted on (str)


The output of 'get_top_users_info()' is a numpy array with unique usernames of the authors who have made the top posts.

The output of 'get_users_post()' is a pandas dataframe with 4 columns:

 - id: id of a comment or post (str)
 - score: number of upvotes (int)
 - user_name: username of the author (str)
 - subreddit_name: name of the subreddit that the comment or post was submitted to (str)
 
The output of scrap_celebrities() is a pandas dataframe with the same columns as get_users_post(), but it contains the information for the top users on the specified subreddit. If an account has been deleted or banned, a message will be printed to the console and the information for that account will not be included in the final dataframe.
