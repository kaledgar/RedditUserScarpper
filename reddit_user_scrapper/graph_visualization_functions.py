import matplotlib.pyplot as plt
import networkx as nx
import numpy as np
from matplotlib.pyplot import figure


def scrap_df_to_nx(scrap_df):
    return nx.from_pandas_edgelist(
        scrap_df, source="user_name", target="subreddit_name"
    )


def graph_visual(
    scrap_df,
    no_it=50,
    k_val=0.2,
    name="Reddit connections",
    labels_bool=True,
    font_siz=15,
):
    plt.figure(figsize=(30, 30))
    g = scrap_df_to_nx(scrap_df)
    gc = g.subgraph(sorted(nx.connected_components(g), key=len, reverse=True)[0])
    layout = nx.spring_layout(gc, k=k_val, iterations=no_it, scale=10)
    nx.draw(
        gc,
        layout,
        node_color="lime",
        node_size=190,
        with_labels=labels_bool,
        font_size=font_siz,
        alpha=0.5,
    )
    plt.title(name)
    plt.savefig(f"{g}_visual.png")
    plt.show()
    plt.close()


def graph_distribution_info(scrap_df, name="Reddit connections degree info"):
    G = scrap_df_to_nx(scrap_df)
    degree_sequence = sorted((d for n, d in G.degree()), reverse=True)
    dmax = max(degree_sequence)
    davg = np.mean(degree_sequence)
    dvar = np.var(degree_sequence)

    centrality = nx.betweenness_centrality(G)
    cent_list = [
        (x, round(centrality[x], 3))
        for x in sorted(centrality, key=centrality.get, reverse=True)[:10]
    ]

    print(f"Max Degree of a {name} = {dmax}")
    print(f"Average Degree of a {name} = {davg}")
    print(f"Variance of a Degree destribution = {dvar}")
    print(f"Top Celebrities:")
    print(cent_list)

    fig = plt.figure("Degree of a random graph", figsize=(8, 8))
    # Create a gridspec for adding subplots of different sizes
    axgrid = fig.add_gridspec(5, 4)

    ax0 = fig.add_subplot(axgrid[0:3, :])
    Gcc = G.subgraph(sorted(nx.connected_components(G), key=len, reverse=True)[0])
    pos = nx.spring_layout(Gcc, seed=33)
    nx.draw_networkx_nodes(Gcc, pos, ax=ax0, node_size=5)
    nx.draw_networkx_edges(Gcc, pos, ax=ax0, alpha=0.1)
    ax0.set_title(f"Connected components of {name}")
    ax0.set_axis_off()

    ax1 = fig.add_subplot(axgrid[3:, :2])
    ax1.plot(degree_sequence, "b-", marker="o")
    ax1.set_title("Degree Rank Plot")
    ax1.set_ylabel("Degree")
    ax1.set_xlabel("Rank")

    ax2 = fig.add_subplot(axgrid[3:, 2:])
    ax2.bar(*np.unique(degree_sequence, return_counts=True))
    ax2.set_title("Degree histogram")
    ax2.set_xlabel("Degree")
    ax2.set_ylabel("# of Nodes")

    fig.tight_layout()
    plt.savefig(f"{G}_visual_info.png")
    plt.show()
    plt.close()
