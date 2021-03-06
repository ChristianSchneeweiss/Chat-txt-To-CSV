import pandas as pd

from model.Message import Message


def is_new_message_line(line: str) -> bool:
    return line.startswith("[")


def extract_messages_lines(fp) -> [str]:
    messages = []
    line = fp.readline()
    message = ""
    while line:
        if not is_new_message_line(line):
            if not line == "\n":
                message += ". " + line
        else:
            if message:
                messages.append(message)
            message = line
        message = message.strip()
        line = fp.readline()
    messages.append(message)
    return messages


def parse_messages(fp):
    messages = extract_messages_lines(fp)
    messages = [Message(message) for message in messages]
    return messages


class WhatsappConverter:
    def __init__(self, filepath: str):
        self.filepath = filepath
        self.data = None
    
    def start_conversion(self):
        with open(self.filepath) as reader:
            messages = parse_messages(reader)
            messages = list(filter(lambda message: message.body, messages))
            messages = list(map(lambda message: message.to_tuple(), messages))
            df = pd.DataFrame.from_records(data=messages, columns=["Writer", "Body", "Datetime"])
            self.data = df
    
    def save_to_csv(self, filename: str):
        assert isinstance(self.data, pd.DataFrame)
        self.data.to_csv(filename, index=False)
