import json


class GardenManager:

    def __init__(self):
        self.pathToJson = "./Json/gardens.json"

    def getGarden(self, targetID):
        with open(self.pathToJson, "r") as f:
            gardenList = json.load(f)


