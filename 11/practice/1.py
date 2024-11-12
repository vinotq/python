import sys
import io, os

input = io.BytesIO(os.read(0, os.fstat(0).st_size)).readline

n, m = map(int, input().split())
edges = []
adj = {i:[] for i in range(n)}
for _ in range(m):
    u, v, w = map(int, input().split())
    edges.append((w, u - 1, v - 1))
    adj[u].append((v, w))
    adj[v].append((u, w))

def primas(w1, u1, v1):
    keys = {i:float("inf") for i in range(n)}
    mst = [0] * n

    for _ in range(n):
        u = min(range(n), key=lambda x: (mst[x], keys[x]))
        mst[u] = 1

        for v, w in adj[u]:
            if not mst[v] and keys[v] > w:
                keys[v] = w
                mst[v] = u

    return sum(keys.values())




ans = [0] * m
for i, (w, u, v) in enumerate(edges):
    ans[i] = str(primas(u, v, w))

sys.stdout.write("\n".join(ans) + "\n")
