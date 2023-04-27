from UsersInfo import RedditTopUsersInfo
from graph_visualization_functions import graph_visual, graph_distribution_info

#games_subreddits
subreddit_name = 'Physics'
mc = RedditTopUsersInfo(subreddit_name, no_subreddit_posts=100, no_user_posts=4)

mc_df = mc.scrap_celebrities()

graph_visual(mc_df, no_it=250, k_val=0.9, font_siz=11)