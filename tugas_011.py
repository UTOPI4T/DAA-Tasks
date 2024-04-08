# Contoh
graph = {"a": ["b","c"],
         "b": ["a","d"],
         "c": ["a","d"],
         "d": ["e"],
         "e": ["d"]
         }
print(graph)

#______________________________________________________________________________________________
# Latihan graph STUVWXZ
graph = {"S": ["X"],
         "T": ["U","W"],
         "U": ["V"],
         "V": ["X"],
         "W": ["X","Z"],
         "X": [],
         "Z": []
         }
print(graph)

#______________________________________________________________________________________________
# Latihan graph LMNOPR
graph = {"l": ["r","p"],
         "m": ["o","n"],
         "n": ["p"],
         "o": ["p","r"],
         "p":[],
         "r":[]
         }

print(graph)

#______________________________________________________________________________________________
# Menampilkan Simpul STUVWXZ
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def getVertices(self):
          return list(self.gdict.keys())

graph_ma = {"S": ["X"],
            "T": ["U","W"],
            "U": ["V"],
            "V": ["X"],
            "W": ["X","Z"],
            "X": [],
            "Z": []
            }
g = Graph(graph_ma)

print(g.getVertices())

#______________________________________________________________________________________________
# Menampilkan Simpul LMNOPR
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def getVertices(self):
          return list(self.gdict.keys())

graph_ma = {"l": ["r","p"],
            "m": ["o","n"],
            "n": ["p"],
            "o": ["p","r"],
            "p":[],
            "r":[]
            }
g = Graph(graph_ma)

print(g.getVertices())

#______________________________________________________________________________________________
# Menampilkan Sudut STUVWXZ
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def edges(self):
          return self.findedges()

      def findedges(self):
          edgename = []
          for vrtx in self.gdict:
              for nxtvrtx in self.gdict[vrtx]:
                  if {nxtvrtx, vrtx} not in edgename:
                     edgename.append({vrtx, nxtvrtx})
          return edgename

graph_ma = {"S": ["X"],
            "T": ["U","W"],
            "U": ["V"],
            "V": ["X"],
            "W": ["X","Z"],
            "X": [],
            "Z": []
            }

g = Graph(graph_ma)
print(g.edges())

#______________________________________________________________________________________________

# Menampilkan Sudut LMNOPR
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def edges(self):
          return self.findedges()

      def findedges(self):
          edgename = []
          for vrtx in self.gdict:
              for nxtvrtx in self.gdict[vrtx]:
                  if {nxtvrtx, vrtx} not in edgename:
                     edgename.append({vrtx, nxtvrtx})
          return edgename

graph_ma = {"l": ["r","p"],
            "m": ["o","n"],
            "n": ["p"],
            "o": ["p","r"],
            "p":[],
            "r":[]
            }

g = Graph(graph_ma)
print(g.edges())
#______________________________________________________________________________________________
# Menambahkan Simpul STUVWXZ
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def getVertices(self):
          return list(self.gdict.keys())

      def addVertex(self, vrtx):
          if vrtx not in self.gdict:
              self.gdict[vrtx] = []

graph_ma =  {"S": ["X"],
             "T": ["U","W"],
             "U": ["V"],
             "V": ["X"],
             "W": ["X","Z"],
             "X": [],
             "Z": []
             }
g = Graph(graph_ma)
g.addVertex("hihi")
print(g.getVertices())

#______________________________________________________________________________________________
# Menambahkan Simpul LMNOPR
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def getVertices(self):
          return list(self.gdict.keys())

      def addVertex(self, vrtx):
          if vrtx not in self.gdict:
              self.gdict[vrtx] = []

graph_ma =  {"l": ["r","p"],
             "m": ["o","n"],
             "n": ["p"],
             "o": ["p","r"],
             "p":[],
             "r":[]
             }
g = Graph(graph_ma)
g.addVertex("hihi")
print(g.getVertices())


#______________________________________________________________________________________________
# Menambahkan Sudut STUVWXZ
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def edges(self):
          return self.findedges()

      def AddEdge(self, edge):
          edge = set(edge)
          (vrtx1, vrtx2) = tuple(edge)
          if vrtx1 in self.gdict:
              self.gdict[vrtx1].append(vrtx2)
          else:
              self.gdict[vrtx1] = [vrtx2]

      def findedges(self):
          edgename = []
          for vrtx in self.gdict:
              for nxtvrtx in self.gdict[vrtx]:
                  if {nxtvrtx, vrtx} not in edgename:
                     edgename.append({vrtx, nxtvrtx})
          return edgename

graph_ma = {"S": ["X"],
            "T": ["U","W"],
            "U": ["V"],
            "V": ["X"],
            "W": ["X","Z"],
            "X": [],
            "Z": []
            }

g = Graph(graph_ma)
g.AddEdge({'a','e'})
print(g.edges())

#______________________________________________________________________________________________
# Menambahkan Sudut LMNOPR
class Graph:
      def __init__(self, gdict=None):
          if gdict is None:
             gdict = {}
          self.gdict = gdict

      def edges(self):
          return self.findedges()

      def AddEdge(self, edge):
          edge = set(edge)
          (vrtx1, vrtx2) = tuple(edge)
          if vrtx1 in self.gdict:
              self.gdict[vrtx1].append(vrtx2)
          else:
              self.gdict[vrtx1] = [vrtx2]

      def findedges(self):
          edgename = []
          for vrtx in self.gdict:
              for nxtvrtx in self.gdict[vrtx]:
                  if {nxtvrtx, vrtx} not in edgename:
                     edgename.append({vrtx, nxtvrtx})
          return edgename

graph_ma = {"l": ["r","p"],
            "m": ["o","n"],
            "n": ["p"],
            "o": ["p","r"],
            "p":[],
            "r":[]
            }

g = Graph(graph_ma)
g.AddEdge({'a','e'})
print(g.edges())
