
import pygame as pg



class ResourceManager:


    def __init__(self):

        # resources
        self.resources = {
            "wood": 100,
            "stone": 30,
            "food":100
        }

        #costs
        self.costs = {
            "Towncenter": {"wood": 10, "stone":5, "food":10},
            "House": {"wood": 5, "stone": 3 , "food":5},
            "castle": {"wood": 20, "stone": 15, "food":10},
            "moulin": {"wood": 8, "stone":5, "food":3},
            "Horse": {"wood": 0, "stone": 0, "food": -14},
            "Chicken": {"wood": 0, "stone": 0, "food": -4},
            "Goat": {"wood": 0, "stone": 0, "food": -6},
            "Sheep": {"wood": 0, "stone": 0, "food": -9},


        }

    def apply_cost_to_resource(self, building):
        for resource, cost in self.costs[building].items():
            self.resources[resource] -= cost

    def is_affordable(self, building):
        print("there's enough resources")
        for resource, cost in self.costs[building].items():
            if cost > self.resources[resource]:
                print("there's no enough resources")
            if self.resources[resource] <= 0:
                self.resources[resource] += 80




