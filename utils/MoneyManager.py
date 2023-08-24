# Code by EnderKatze

import json
import math


class MoneyManager:

    def __init__(self):
        self.pathToDatafile = "./Json/money.json"

    def addMoney(self, targetID, amount):
        """
        Adds the given amount of exp to the user in the guild defined in the constructor

        :param targetID: The ID of the user to add money to
        :param amount: The amount of money to add (Can be negative)
        """

        with open(self.pathToDatafile, "r") as f:
            moneyList = json.load(f)

        if str(targetID) not in moneyList:
            moneyList[str(targetID)] = 0

        moneyList[str(targetID)] = self.getMoney(targetID) + amount

        with open(self.pathToDatafile, "w") as f:
            json.dump(moneyList, f, indent=4)

    def getMoney(self, targetID):
        """
        Returns the exp of a user in the guild defined in the constructor

        :param targetID: The user whose exp you want
        :return: The current exp of the user in the guild
        """
        with open(self.pathToDatafile, "r") as f:
            moneyList = json.load(f)
        try:
            money = moneyList[str(targetID)]
            return money
        except:
            startBalance = 100
            return startBalance
