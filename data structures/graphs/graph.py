
import bisect


class Graph():
    
    number_of_nodes = 0
    adjacent_list = {}
    
    def add_verterx(self, node):
        self.adjacent_list[node] = []
        self.number_of_nodes += 1

    def add_edge(self,node1, node2) -> bool:
        n1 =self.adjacent_list.get(node1)
        n2 = self.adjacent_list.get(node2)

        add_condition = n1 is not None and n2 is not None
        if(add_condition):
            # Using bellow to keep list sorted.
            # n1.append(node2)
            # n1.append(node1)


            # https://stackoverflow.com/questions/47608315/python-how-to-append-integer-in-list-and-to-sort
            bisect.insort(n1, node2)
            bisect.insort(n2, node1)

        return add_condition
        

    def show_connections(self):
        for k,v in self.adjacent_list.items():
            print(k,"->",', '.join(v))




myGraph = Graph()
myGraph.add_verterx('0')
myGraph.add_verterx('1')
myGraph.add_verterx('2')
myGraph.add_verterx('3')
myGraph.add_verterx('4')
myGraph.add_verterx('5')
myGraph.add_verterx('6')
myGraph.add_edge('3', '1') 
myGraph.add_edge('3', '4') 
myGraph.add_edge('4', '2') 
myGraph.add_edge('4', '5') 
myGraph.add_edge('1', '2') 
myGraph.add_edge('1', '0') 
myGraph.add_edge('0', '2') 
myGraph.add_edge('6', '5')

myGraph.show_connections()
