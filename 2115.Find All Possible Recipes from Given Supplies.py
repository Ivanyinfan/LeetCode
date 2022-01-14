#
# @lc app=leetcode id=2115 lang=python3
#
# [2115] Find All Possible Recipes from Given Supplies
#
from typing import List
from collections import deque
# @lc code=start
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        # string -> List
        # list[0] the in-degree
        # list[1] the children
        # list[2] is recipe
        graph = dict()
        for recipe in recipes:
            graph[recipe] = [0, list(), True]
        for i, ingredient_i in enumerate(ingredients):
            for ingredient in ingredient_i:
                if ingredient not in graph:
                    graph[ingredient]=[0, list(), False]
                graph[ingredient][1].append(recipes[i])
                graph[recipes[i]][0]+=1
        queue = deque(supplies)
        result = list()
        while queue:
            name = queue.popleft()
            node = graph.pop(name, None)
            if node == None: continue
            if node[2]:
                result.append(name)
            children = node[1]
            for child in children:
                node = graph.get(child, None)
                if node == None: continue
                node[0]-=1
                if node[0]==0:
                    queue.append(child)
        return result

# @lc code=end
from utils import test
if __name__ == "__main__":
    sol = Solution()
    test(sol.findAllRecipes(recipes = ["bread"], ingredients = [["yeast","flour"]], supplies = ["yeast","flour","corn"]),["bread"])
    test(sol.findAllRecipes(recipes = ["bread","sandwich"], ingredients = [["yeast","flour"],["bread","meat"]], supplies = ["yeast","flour","meat"]),["bread","sandwich"])
    test(sol.findAllRecipes(recipes = ["bread","sandwich","burger"], ingredients = [["yeast","flour"],["bread","meat"],["sandwich","meat","bread"]], supplies = ["yeast","flour","meat"]), ["bread","sandwich","burger"])
    test(sol.findAllRecipes(recipes = ["bread"], ingredients = [["meat"]], supplies = ["meat"]), ["bread"])
    test(sol.findAllRecipes(recipes = ["bread", "meat"], ingredients = [["meat"],["bread"]], supplies = ["meat"]), ["bread","meat"], ordered=False)
    test(sol.findAllRecipes(recipes = ["bread"], ingredients = [["read"]], supplies = ["meat"]), [], ordered=False)

    

