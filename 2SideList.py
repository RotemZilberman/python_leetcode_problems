class Solution:
    def dfs(self, V, adj, visited, color, node):
        visited[node] = True
        for i in adj[node]:
            if not visited[i]:
                color[i] = not color[node]
                if not self.dfs(V, adj, visited, color, i):
                    return False
            elif color[i] == color[node]:
                return False
        return True
    def isBipartite(self, V, adj):
        #running bfs on each node
        visited = [False] * V
        color = [False] * V
        for i in range(V):
            if not visited[i]:
                if not self.dfs(V, adj, visited, color, i):
                    return 0
        return 1

