#!/usr/bin/env python3

import sys
import xml.etree.ElementTree as eTree
from pathlib import Path


class OpmlReader:
    FORMAT_DELIMITERS = {"txt": "\t", "csv": ","}
    FORMATTING = {"txt": "·", "csv": ""}

    def __init__(self, format_type):
        self.elements = []
        self.format_type = format_type

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
        element = f"{parent_id}{self.get_formatting()} {node.attrib['text']}"
        self.elements.append(element)

        children = node.findall("outline")

        parent_id += self.FORMAT_DELIMITERS[self.format_type]

        for x in children:
            self.add_element(x, parent_id)

    def get_formatting(self):
        return self.FORMATTING[self.format_type]

    def write_output(self, input_file, buf):
        output_file = input_file.split(".", 2)[0] + "." + self.format_type
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
    input_file = sys.argv[1]
    format_type = "txt"
    if len(sys.argv) > 2:
        format_type = sys.argv[2]
    OpmlReader(format_type).run(input_file)
