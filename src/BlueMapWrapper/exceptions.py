class NoMatches(Exception):
    def __init__(self, message:str="No matches found"):
        super().__init__(message)

class MultipleMatches(Exception):
    def __init__(self, key: str, message:str="Multiple matches found"):
        self.message = f"{key}: {message}"
        super().__init__(self.message)