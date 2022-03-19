from pyUML import Graph


def print_and_save(graph: Graph, name, program="dot", format_="png", verbose=False):
    if verbose:
        print("=DOT rendering=\n", graph.to_string())
    graph.write_raw(f"{name}.dot")
    graph.write(f"{name}.{format_}", program, format_)
