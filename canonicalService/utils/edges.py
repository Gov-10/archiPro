DEFAULT_FLOWS = [
    ("frontend", "api"),
    ("api", "queue"),
    ("api", "cache"),
    ("api", "database"),
    ("queue", "worker"),
    ("worker", "database"),
]
def infer_edges(components):
    names = {c["name"] for c in components}
    edges = []
    for src, dst in DEFAULT_FLOWS:
        if src in names and dst in names:
            edges.append(f"{src}->{dst}")
    return edges

