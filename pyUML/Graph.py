import pydot

from pyUML.Association import Aggregation, Association, Composition,\
    Implementation


class Graph(pydot.Dot):
    def __init__(self, *args, **kwargs):
        pydot.Dot.__init__(self, *args, graph_type="digraph", **kwargs)

    def write_raw(self, *args, **kwargs):
        super().write_raw(self, *args, **kwargs)

    def add_association(self, child, parent, *args, **kwargs):
        self.add_edge(Association(child, parent, *args, **kwargs))

    def add_implementation(self, child, parent, *args, **kwargs):
        self.add_edge(Implementation(child, parent, *args, **kwargs))

    def add_classes(self, *uml_classes):
        for uml_class in uml_classes:
            self.add_class(uml_class)

    def add_class(self, uml_class):
        self.add_node(uml_class)

    def add_composition(self, child, parent, *args, **kwargs):
        self.add_edge(Composition(child, parent, *args, **kwargs))

    def add_aggregation(self, child, parent, *args, **kwargs):
        self.add_edge(Aggregation(child, parent, *args, **kwargs))
