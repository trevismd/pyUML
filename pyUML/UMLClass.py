from typing import Union

import pydot


class UMLClass(pydot.Node):
    def __init__(self, name, attributes=None, methods=None, caption=None,
                 **kwargs):
        pydot.Node.__init__(self, name, shape="record", **kwargs)
        self.name = name
        self.caption = caption if caption is not None else name
        self._attributes = {"public": {},
                            "private": {}}
        if attributes is not None:
            self.add_attributes(attributes)

        self._methods = {"public": [],
                         "private": []}

        if methods is not None:
            self.add_methods(methods)
        self.update_content()

    def add_attribute(self, name: str, dtype: str = None, public: bool = True):
        target = self._attributes["public" if public else "private"]
        target[name] = dtype

    def add_method(self, name: str, public: bool = True):
        target = self._methods["public" if public else "private"]
        target.append(name)

    def update_content(self):
        header = "{" + self.caption

        attributes = self._render_attributes() + self._render_attributes(False)
        methods = self._render_methods() + self._render_methods(False)

        self.set_label(f"{header}|{attributes}|{methods}" + "}")

    def _render_attributes(self, public: bool = True):
        source, sep = self._get_source_sep("_attributes", public)

        return "".join([f"{sep} {name} : {dtype}\\l"
                        for name, dtype
                        in source.items()])

    def _render_methods(self, public: bool = True):
        source, sep = self._get_source_sep("_methods", public)

        return "".join([f"{sep} {method}\\l" for method in source])

    def _get_source_sep(self, kind, public):
        public_private, sep = {
            True: ("public", "+"),
            False: ("private", "-")}[public]

        source = getattr(self, kind)[public_private]
        return source, sep

    def add_attributes(self, attributes):
        if attributes.keys() == {"private", "public"}:
            for public_private, pp_attributes in attributes.items():
                for attribute, dtype in pp_attributes.items():
                    self.add_attribute(attribute, dtype,
                                       public_private == "public")
        else:
            for attribute, dtype in attributes.items():
                self.add_attribute(attribute, dtype)

    def add_methods(self, methods: Union[list, dict]):
        if isinstance(methods, list):
            for method in methods:
                self.add_method(method)

        elif methods.keys() == {"private", "public"}:
            for public_private, pp_method in methods.items():
                for method in pp_method:
                    self.add_method(method, public_private == "public")
        else:
            raise ValueError("Wrong format for methods, which should either be"
                             "a list of strings or a dictionary with private "
                             "and public keys with string-list values")


class UMLClassWithPublicIntID(UMLClass):
    def __init__(self, name, attributes=None, methods=None, id_dtype="int"):
        UMLClass.__init__(self, name, attributes=attributes, methods=methods)
        self._attributes["public"] = {"id": id_dtype,
                                      **self._attributes["public"]}
        self.update_content()
