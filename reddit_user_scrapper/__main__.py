from .users_info import RedditTopUsersInfo

from .graph_visualization_functions import graph_visual


SUB_NAME = "Gaming"
rtui = RedditTopUsersInfo(SUB_NAME, subreddit_posts_count=100, user_posts_count=1)
rtui_df = rtui.scrap_celebrities()

graph_visual(rtui_df, no_it=250, k_val=0.95, labels_bool=False)
