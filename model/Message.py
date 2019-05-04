from datetime import datetime
import pandas as pd


class Message:
    def __init__(self, message_line: str):
        if not message_line:
            self.writer = "none"
            self.body = "no message"
            self.date_time = None
            return
        try:
            date_time, writer_message = message_line.split("]")
            date_time = date_time.replace("[", "")
            writer_message = writer_message.split(":")
            self.writer = writer_message[0].strip()
            self.body = "".join(writer_message[1:]).strip()
            self.date_time = datetime.strptime(date_time, "%d.%m.%y, %H:%M:%S")
        except:
            self.writer = "none"
            self.body = "no message"
            self.date_time = None
    
    def __str__(self) -> str:
        return f"{self.writer}: {self.body} at {self.date_time}"
    
    def to_series(self) -> pd.Series:
        return pd.Series([self.writer, self.body, self.date_time], index=["Writer", "Body", "Datetime"])
