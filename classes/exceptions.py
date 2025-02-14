
class NotAnPositiveNumberError(Exception):
    def __init__(self):
        super().__init__("PARSED VALUE ISN'T AN INTEGER")


class EmptyStringError(Exception):
    def __init__(self):
        super().__init__("PARSED STRING IS EMPTY")
