import unittest
from unittest.mock import patch, mock_open
from xml.etree.ElementTree import Element, tostring
from xml_file_processor import FileProcessor


class TestFileProcessor(unittest.TestCase):
    def setUp(self):
        self.processor = FileProcessor()

    @patch('builtins.open', new_callable=mock_open, read_data='<root></root>')
    def test_read_file(self, mock_open_file):
        root = self.processor.read_file("dummy.xml")
        self.assertIsNotNone(root)

    @patch('xml.etree.ElementTree.ElementTree.write')
    @patch('builtins.open', new_callable=mock_open)
    def test_add_record(self, mock_open_file, mock_write):
        record = Element("record", {"id": "1"})
        self.processor.add_record("dummy.xml", record)


    @patch('xml.etree.ElementTree.ElementTree.write')
    @patch('builtins.open', new_callable=mock_open)
    def test_delete_record(self, mock_open_file, mock_write):
        record = Element("record", {"id": "1"})
        self.processor.delete_record("dummy.xml", "1")

    @patch('xml.etree.ElementTree.ElementTree.write')
    @patch('builtins.open', new_callable=mock_open)
    def test_update_record(self, mock_open_file, mock_write):
        old_record = Element("record", {"id": "1"})
        new_record = Element("record", {"id": "2"})
        self.processor.update_record("dummy.xml", "1", new_record)


    @patch('builtins.print')
    @patch('builtins.open', new_callable=mock_open, read_data='<root><record id="1"></record></root>')
    def test_display_records(self, mock_open_file, mock_print):
        self.processor.display_records("dummy.xml")
        mock_print.assert_called_once()


if __name__ == '__main__':
    unittest.main()