import sys
from model.Message import Message


def is_line_new_message(line: str) -> bool:
    return line.startswith("[")


def main():
    filepath = sys.argv[1]
    with open(filepath) as fp:
        messages = extract_messages_lines(fp)
        messages = [Message(message) for message in messages]
        for message in messages:
            print(message)


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
