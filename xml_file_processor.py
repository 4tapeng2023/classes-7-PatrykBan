import xml.etree.ElementTree as ET


class FileProcessor:
    def read_file(self, filename):
        try:
            tree = ET.parse(filename)
            root = tree.getroot()
            return root
        except ET.ParseError as e:
            print(f"Error reading file {filename}: {e}")
            return None

    def add_record(self, filename, record):
        root = self.read_file(filename)
        if root is not None:
            root.append(record)
            self._write_to_file(filename, root)

    def delete_record(self, filename, record_id):
        root = self.read_file(filename)
        if root is not None:
            for record in root.findall(".//record[@id='" + str(record_id) + "']"):
                root.remove(record)
            self._write_to_file(filename, root)

    def update_record(self, filename, record_id, new_record):
        root = self.read_file(filename)
        if root is not None:
            for record in root.findall(".//record[@id='" + str(record_id) + "']"):
                root.remove(record)
            root.append(new_record)
            self._write_to_file(filename, root)

    def display_records(self, filename):
        root = self.read_file(filename)
        if root is not None:
            for record in root.findall(".//record"):
                print(record.attrib)

    def _write_to_file(self, filename, root):
        tree = ET.ElementTree(root)
        tree.write(filename)