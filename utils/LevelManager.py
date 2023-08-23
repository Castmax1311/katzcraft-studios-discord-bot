# Code by EnderKatze

import json
import math


class LevelManager:

    def __init__(self, guildID, pathToDatafile):
        self.guildID = guildID
        self.pathToDatafile = pathToDatafile

    def addExp(self, targetID, amount):
        """
        Adds the given amount of exp to the user in the guild defined in the constructor

        :param targetID: The ID of the user to add exp to
        :param amount: The amount of exp to add (Can be negative)
        """

        with open(self.pathToDatafile, "r") as f:
            expList = json.load(f)

        if str(self.guildID) not in expList:
            expList[str(self.guildID)] = {}

        if str(targetID) not in expList[str(self.guildID)]:
            expList[str(self.guildID)][str(targetID)] = 0

        expList[str(self.guildID)][str(targetID)] = self.getExp(targetID) + amount

        with open(self.pathToDatafile, "w") as f:
            json.dump(expList, f, indent=4)

    def getExp(self, targetID):
        """
        Returns the exp of a user in the guild defined in the constructor

        :param targetID: The user whose exp you want
        :return: The current exp of the user in the guild
        """
        with open(self.pathToDatafile, "r") as f:
            expList = json.load(f)
        try:
            exp = expList[str(self.guildID)][str(targetID)]
            return exp
        except:
            return 0

    def getExpToLevelup(self, targetID):
        """
        Returns the amount of exp a user needs to level up in the guild defined in the constructor

        :param targetID: The user to get the needed exp
        :return: The amount of exp the user needs to level up
        """
        level = self.getLevel(targetID)-1

        nextXp = math.pow((level+1)/0.1, 2)

        toNextLevel = nextXp - self.getExp(targetID)
        toNextLevel = round(toNextLevel, 2)

        return toNextLevel

    def getLevel(self, targetID):
        """
        Gets the level of a user in the guild defined in the constructor

        :param targetID: The user whose level you want
        :return: The current level of the user in the guild
        """
        level = int(0.1 * math.sqrt(self.getExp(targetID)))

        return (level+1)
