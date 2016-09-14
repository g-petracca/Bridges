import networkx as nx
from networkx_viewer import Viewer
G = nx.DiGraph()
G.add_edge('diag_uart_log','diag_uart_log')
G.edge['diag_uart_log']['diag_uart_log']['write-read'] = '[open open][setattr getattr][write read][add_name search][remove_name search][write read]'
G.edge['diag_uart_log']['diag_uart_log']['fill'] = 'red'
app = Viewer(G)
app.mainloop()