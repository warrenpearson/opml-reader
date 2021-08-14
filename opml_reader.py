import sys
import xml.etree.ElementTree as eTree


class OpmlReader:
    def __init__(self):
        self.elements = []

    def run(self, input_file):

        mytree = eTree.parse(input_file)
        root = mytree.getroot()
        # print(myroot)
        body = root.find("body")
        parent = body.findall("outline")[0]

        self.add_element(parent, "")
        for el in self.elements:
            print(el)

    def add_element(self, node, parent_id):
        element = f"{parent_id}· {node.attrib['text']}"
        self.elements.append(element)

        children = node.findall("outline")

        parent_id += "\t"

        for x in children:
            self.add_element(x, parent_id)


if __name__ == "__main__":
    OpmlReader().run(sys.argv[1])
