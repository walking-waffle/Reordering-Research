import sys
import random
import networkx as nx
import matplotlib.pyplot as plt


def genGraph(graph_type: str, weight: bool, params: list):

    try:
        # Connected-Watts-Strogatz
        if graph_type == "ws":
            if len(params) != 3:
                raise ValueError

            n = int(params[0])
            k = int(params[1])
            p = float(params[2])

            g = nx.connected_watts_strogatz_graph(n, k, p, tries=100)

        # Powerlaw Cluster
        elif graph_type == "plc":
            if len(params) != 3:
                raise ValueError

            n = int(params[0])
            m = int(params[1])
            p = float(params[2])

            g = nx.powerlaw_cluster_graph(n, m, p)

        # Barabasi-Albert
        elif graph_type == "ba":
            if len(params) != 2:
                raise ValueError

            n = int(params[0])
            m = int(params[1])

            g = nx.barabasi_albert_graph(n, m)

        else:
            print("Unknown graph type:", graph_type)
            sys.exit(1)

    except ValueError:
        print("Parameter error!")
        sys.exit(1)

    print("isConnected:", nx.is_connected(g))
    print("isDirected:", nx.is_directed(g))

    # ===== 加權重 =====
    if weight:
        for u, v in g.edges():
            g[u][v]["weight"] = random.randint(1, 100)

    # ===== 轉有向圖 =====
    g = g.to_directed()

    # ===== 檔名 =====
    filename = f"{graph_type}.el"

    # ===== 寫檔 =====
    if weight:
        nx.write_edgelist(g, filename, data=["weight"])
    else:
        nx.write_edgelist(g, filename, data=False)

    print("V:", g.number_of_nodes())
    print("E:", g.number_of_edges())
    print("finish")

    # ===== 顯示圖 =====
    if g.number_of_nodes() <= 1000:
        nx.draw(g, node_size=30)
        plt.show()
    else:
        print("Too Large")


def main():
    if len(sys.argv) < 3:
        print("Usage:")
        print("  ws  [-w] n k p")
        print("  plc [-w] n m p")
        print("  ba  [-w] n m")
        sys.exit(1)

    graph_type = sys.argv[1]

    # ===== 是否加權 =====
    weight = False

    if sys.argv[2] == "-w":
        weight = True
        params = sys.argv[3:]
    else:
        params = sys.argv[2:]

    genGraph(graph_type, weight, params)


if __name__ == "__main__":
    main()
