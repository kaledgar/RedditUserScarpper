from .graph_visualization_functions import visualize_network
from .users_info import RedditTopUsersInfo

SUB_NAME = "Gaming"
rtui = RedditTopUsersInfo(SUB_NAME, subreddit_posts_count=1000, user_posts_count=10)
rtui_df = rtui.scrap_celebrities()

visualize_network(rtui_df, no_it=250, k_val=0.95, labels_bool=False)
