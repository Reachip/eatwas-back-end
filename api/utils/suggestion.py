import random
import asyncio
import logging

from bdd.models.goal import Goal
from bdd.models.sex import Sex
from utils.ciqual import CiqualTable
from utils.greenpeace_sheet import GreenPeaceSheet


class Suggestion:
    def __init__(self, user_token):
        self.user_token = user_token
        self.ciqual = CiqualTable()
        self.green_peace_sheet = GreenPeaceSheet()
        self.dishes = self.ciqual.get_mixed_dishes
        self.fruit = self.green_peace_sheet.fruit_according_to_month()
        self.basal_metabolism = self._get_basal_metabolism(
            user_token["sex"],
            user_token["weight"],
            user_token["size"],
            user_token["age"],
            user_token["sportFrequency"],
        )

        self.calories_to_consume_per_meal = self._get_calories_to_consume_per_meal()

    def _get_basal_metabolism(self, sex, weight, size, age, sport_frequency):
        if sex == Sex.MAN.value:
            return (
                (13.7516 * weight) + (500.33 * size) - (6.7550 * age) + 66.473
            ) * sport_frequency

        if sex == Sex.WOMAN.value:
            return (
                (9.5634 * weight) + (184.96 * size) - (4.6756 * age) + 655.0955
            ) * sport_frequency

    def _get_calories_to_consume_per_meal(self):
        if self.user_token["goal"] == Goal.SLIM.value:
            return (self.basal_metabolism + (10 / 100) * self.basal_metabolism) / 3

        if self.user_token["goal"] == Goal.SWELL.value:
            return (self.basal_metabolism - (10 / 100) * self.basal_metabolism) / 3

        if self.user_token["goal"] == Goal.STABILIZE.value:
            return self.basal_metabolism / 3


    def suggest(self):
        logging.debug("TRAITEMENT DE LA SUGGESTION")

        if self.user_token["goal"] == Goal.SLIM.value:
            return random.choice(self.dishes), random.choice(self.fruit)

        if self.user_token["goal"] == Goal.SWELL.value:
            return random.choice(self.dishes), random.choice(self.fruit)

        if self.user_token["goal"] == Goal.STABILIZE.value:
            return random.choice(self.dishes), random.choice(self.fruit)
