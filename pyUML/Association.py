import pydot

from pyUML import UMLClass


class Association(pydot.Edge):
    multiplicity_labels = {"child": "set_headlabel",
                           "parent": "set_taillabel"}

    def __init__(self, child: UMLClass, parent: UMLClass, label: str = None,
                 multiplicity_child: str = None,
                 multiplicity_parent: str = None, *args, **kwargs):
        pydot.Edge.__init__(self, parent.name, child.name, *args, dir="back",
                            **kwargs)
        if label is not None:
            self.set_label(f" {label}")
        if multiplicity_child is not None:
            self.set_multiplicity("child", multiplicity_child)
        if multiplicity_parent is not None:
            self.set_multiplicity("parent", multiplicity_parent)

    def set_multiplicity(self, target, multiplicity):
        getattr(self, self.multiplicity_labels[target])(f"\n{multiplicity}")


class Implementation(Association):
    def __init__(self, child, parent, *args, **kwargs):
        Association.__init__(self, child, parent, *args,
                             arrowtail="onormal", **kwargs)


class Aggregation(Association):
    def __init__(self, child, parent, *args, **kwargs):
        Association.__init__(self, child, parent, *args,
                             arrowtail="odiamond", **kwargs)


class Composition(Aggregation):
    def __init__(self, child, parent, *args, **kwargs):
        Aggregation.__init__(self, child, parent, *args, **kwargs)
        self.set_arrowtail("diamond")
