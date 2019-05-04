import unittest
from datetime import datetime

from model.Message import Message


class MyTestCase(unittest.TestCase):
    def test_init_with_correct_data(self):
        message = Message(
            "[21.10.17, 16:19:29] Christian: Ähm i büd ma ei i hob gsogt i wü kan tequila mea, oba ds büd i ma wsl nua ei😂🙈")
        self.assertEqual(message.body,
                         "Ähm i büd ma ei i hob gsogt i wü kan tequila mea, oba ds büd i ma wsl nua ei😂🙈")
        self.assertEqual(message.date_time, datetime(2017, 10, 21, 16, 19, 29))
        self.assertEqual(message.writer, "Christian")
    
    def test_init_with_empty_body(self):
        message = Message("[21.10.17, 16:19:29] Christian:")
        self.assertEqual(message.body, "")
        self.assertEqual(message.date_time, datetime(2017, 10, 21, 16, 19, 29))
        self.assertEqual(message.writer, "Christian")
    
    def test_init_with_empty_writer(self):
        message = Message(
            "[21.10.17, 16:19:29] : Ähm i büd ma ei i hob gsogt i wü kan tequila mea, oba ds büd i ma wsl nua ei😂🙈")
        self.assertEqual(message.body,
                         "Ähm i büd ma ei i hob gsogt i wü kan tequila mea, oba ds büd i ma wsl nua ei😂🙈")
        self.assertEqual(message.date_time, datetime(2017, 10, 21, 16, 19, 29))
        self.assertEqual(message.writer, "")
    
    def test_init_with_empty_message_line(self):
        message = Message("")
        self.assertEqual(message.body, "")
        self.assertEqual(message.date_time, None)
        self.assertEqual(message.writer, "")
    
    def test_to_tuple_with_correct_data(self):
        message = Message("[21.10.17, 16:19:29] Christian: Hello Testing")
        self.assertEqual(message.to_tuple(), tuple(["Christian", "Hello Testing", datetime(2017, 10, 21, 16, 19, 29)]))
    
    def test_to_tuple_with_empty_body(self):
        message = Message("[21.10.17, 16:19:29] Christian:")
        self.assertEqual(message.to_tuple(), tuple(["Christian", "", datetime(2017, 10, 21, 16, 19, 29)]))
    
    def test_replacing_commas_with_commas(self):
        message = Message("[21.10.17, 16:19:29] Christian: Hello, Testing")
        message.replace_commas()
        self.assertEqual(message.body, "Hello; Testing")
    
    def test_replacing_commas_without_commas(self):
        message = Message("[21.10.17, 16:19:29] Christian: Hello Testing")
        message.replace_commas()
        self.assertEqual(message.body, "Hello Testing")


if __name__ == '__main__':
    unittest.main()
