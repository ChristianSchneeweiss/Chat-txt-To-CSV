import sys
import pandas as pd
from model.Message import Message


def is_line_new_message(line: str) -> bool:
    return line.startswith("[")


def main():
    filepath = sys.argv[1]
    with open(filepath) as fp:
        messages = parse_messages(fp)
        messages = list(map(lambda message: message.to_series(), messages))
        df = pd.DataFrame(messages)
        print(df.head())
        df.to_csv(path_or_buf="messages.csv", index=False)


def parse_messages(fp):
    messages = extract_messages_lines(fp)
    messages = [Message(message) for message in messages]
    return messages


def extract_messages_lines(fp) -> [str]:
    messages = []
    line = fp.readline()
    message = ""
    while line:
        if not is_line_new_message(line):
            message += ". " + line
        else:
            messages.append(message)
            message = line
        message = message.strip()
        line = fp.readline()
    return messages


if __name__ == '__main__':
    if len(sys.argv) > 1:
        main()
