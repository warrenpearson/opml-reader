#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as eTree
from pathlib import Path


class OpmlReader:
    def __init__(self):
        self.elements = []

    def run(self, input_file):

        if not input_file.endswith(".opml"):
            print("This script only handles opml files")
            return

        buf = ""
        mytree = eTree.parse(input_file)
        root = mytree.getroot()

        body = root.find("body")
        parent = body.findall("outline")[0]

        self.add_element(parent, "")

        for el in self.elements:
            buf += el + "\n"

        print(buf)
        self.write_output(input_file, buf)

    def add_element(self, node, parent_id):
        element = f"{parent_id}· {node.attrib['text']}"
        self.elements.append(element)

        children = node.findall("outline")

        parent_id += "\t"

        for x in children:
            self.add_element(x, parent_id)

    def write_output(self, input_file, buf):
        output_file = input_file.split(".", 2)[0] + ".txt"
        if self.output_file_exists(output_file):
            print(f"Not overwriting {output_file}")
            return

        print(f"Writing {output_file}")
        with open(output_file, "w") as outf:
            outf.write(buf)

    def output_file_exists(self, output_file):
        path = Path(output_file)
        if path.is_file():
            return True

        return False


if __name__ == "__main__":
    OpmlReader().run(sys.argv[1])
