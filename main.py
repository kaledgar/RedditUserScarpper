from UsersInfo import RedditTopUsersInfo
from graph_visualization_functions import graph_visual, graph_distribution_info


sub_name = 'Gaming'
rtui = RedditTopUsersInfo(sub_name, no_subreddit_posts=100, no_user_posts=1)
rtui_df = rtui.scrap_celebrities()

graph_visual(rtui_df, no_it=250, k_val=0.95, labels_bool = False)