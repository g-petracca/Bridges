import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
app = Viewer(G)
app.mainloop()