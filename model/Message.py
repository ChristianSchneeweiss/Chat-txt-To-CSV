from datetime import datetime
import pandas as pd


class Message:
    body: str
    writer: str
    date_time: datetime
    
    def __init__(self, message_line: str):
        try:
            date_time, writer_message = message_line.split("]")
            date_time = date_time.replace("[", "")
            writer_message = writer_message.split(":")
            self.writer = writer_message[0].strip()
            self.body = "".join(writer_message[1:]).strip()
            self.date_time = datetime.strptime(date_time, "%d.%m.%y, %H:%M:%S")
        except:
            self.writer = str()
            self.body = str()
            self.date_time = None
    
    def __str__(self) -> str:
        return f"{self.writer}: {self.body} at {self.date_time}"
    
    def to_tuple(self) -> []:
        self.replace_commas()
        return tuple([self.writer, self.body, self.date_time])
    
    def replace_commas(self):
        self.writer.replace(",", ";")
        self.body.replace(",", ";")
