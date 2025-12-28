def canonicalize(components, edges):
   components = sorted({c["type"] for c in components})
   edges = sorted(set(edges))
   return {"components": components, "edges": edges}

