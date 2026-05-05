class GardenError(Exception):
    def __init__(self, message: str = "Unknown garden error") -> None:
        self.message = message
        super().__init__(self.message)

class PlantError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)

class WaterError(GardenError):
    def __init__(self, message: str = "Unknown garden error") -> None:
        super().__init__(message)
        

def