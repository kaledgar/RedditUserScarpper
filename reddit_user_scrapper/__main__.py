import argparse
import sys

from .constants import DEFAULT_SUBREDDIT_NAME
from .graph_visualization_functions import graph_distribution_info, visualize_network
from .users_info import RedditTopUsersInfo


def parse_cli_arguments():
    parser = argparse.ArgumentParser(
        prog="python3 -m reddit_user_scrapper",
        description="I scrap",
        epilog="That's all folks!",
    )
    parser.add_argument("-s", "--subreddit", default=DEFAULT_SUBREDDIT_NAME)
    parser.add_argument("-p", "--posts-count", default=100)
    parser.add_argument("-u", "--user-posts-count", default=10)
    return parser.parse_args()


if __name__ == "__main__":
    args = parse_cli_arguments()
    print(args)

    rtui = RedditTopUsersInfo(
        args.subreddit,
        args.posts_count,
        args.user_posts_count,
    )
    rtui_df = rtui.scrap_celebrities()

    visualize_network(rtui_df, no_it=250, k_val=0.95, labels_bool=False)
    graph_distribution_info(rtui_df)
