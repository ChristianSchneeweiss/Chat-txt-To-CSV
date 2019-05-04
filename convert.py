import sys
import pandas as pd

from model.WhatsappConverter import WhatsappConverter
from model.Message import Message


def main():
    filepath = sys.argv[1]
    converter = WhatsappConverter(filepath)
    converter.start_conversion()
    converter.save_to_csv("messages.csv")


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
