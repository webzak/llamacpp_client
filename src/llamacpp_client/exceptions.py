class InvalidRequest(Exception):
    """
    Custom exception to represent a bad request with detailed error information.
    """
    def __init__(self, errors: list[dict]):
        self.errors = errors  # A list of error dictionaries, each with loc, msg, type
        super().__init__(f"Bad Request: {self.errors}")  # Call the base class constructor

    def __str__(self):
        return f"InvalidRequest: {self.errors}"

    def __repr__(self):
         return f"InvalidRequest(errors={self.errors})"