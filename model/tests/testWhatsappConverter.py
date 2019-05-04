import unittest
from datetime import datetime

import pandas as pd

from model.WhatsappConverter import WhatsappConverter


class MyTestCase(unittest.TestCase):
    def test_init(self):
        converter = WhatsappConverter("test-chats.txt")
        self.assertEqual(converter.filepath, "test-chats.txt")
    
    def test_start_conversion(self):
        converter = WhatsappConverter("test-chats.txt")
        converter.start_conversion()
        
        # [20.10.17, 12: 23:53] Adam: Test1, Test2
        # [20.10.17, 13: 39:12] Eva: Test1 back Test3
        # [20.10.17, 13: 45:55] Adam: Hello testing
        # [20.10.17, 14: 11:20] Eva: Hello Adam
        # [20.10.17, 14: 44:16] Adam: Hello Eva
        #
        # Hello Hello
        # [21.10.17, 14: 43:14] Adam: How is it going?
        # [21.10.17, 14: 55:21] Eva: Good good
        #
        # And you?
        
        correct_data = [
            ("Adam", "Test1; Test2", datetime.strptime("20.10.17, 12:23:53", "%d.%m.%y, %H:%M:%S")),
            ("Eva", "Test1 back Test3", datetime.strptime("20.10.17, 13:39:12", "%d.%m.%y, %H:%M:%S")),
            ("Adam", "Hello testing", datetime.strptime("20.10.17, 13:45:55", "%d.%m.%y, %H:%M:%S")),
            ("Eva", "Hello Adam", datetime.strptime("20.10.17, 14:11:20", "%d.%m.%y, %H:%M:%S")),
            ("Adam", "Hello Eva. Hello Hello", datetime.strptime("20.10.17, 14:44:16", "%d.%m.%y, %H:%M:%S")),
            ("Adam", "How is it going?", datetime.strptime("21.10.17, 14:43:14", "%d.%m.%y, %H:%M:%S")),
            ("Eva", "Good good. And you?", datetime.strptime("21.10.17, 14:55:21", "%d.%m.%y, %H:%M:%S")),
        ]
        correct_data = pd.DataFrame.from_records(correct_data, columns=["Writer", "Body", "Datetime"])
        self.assertEqual(converter.data.equals(correct_data), True)


if __name__ == '__main__':
    unittest.main()
