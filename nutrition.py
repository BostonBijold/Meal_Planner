class Food:
    def __init__(self, name, protein, fat, carbs, calories):
        self.name = name
        self.protein = protein
        self.fat = fat
        self.carbs = carbs
        self.calories = calories
        self.set_fraction(1.0)

    def set_fraction(self, fraction):
        self.fraction = fraction
        self.protein_calories = 4 * fraction * self.protein
        self.carbs_calories = 4 * fraction * self.carbs
        self.fat_calories = 9 * fraction * self.fat
        self.calories = fraction * self.calories

    def __str__(self):
        return "[%0.4f] %s (P=%s,C=%s,F=%s,E=%s)" % (
        self.fraction, self.name, self.protein, self.carbs, self.fat, self.calories)


class MealPlan:
    def __init__(self):
        self.foods = []
        self.total_calories = 0.0
        self.total_protein_calories = 0.0
        self.total_carbs_calories = 0.0
        self.total_fat_calories = 0.0

    def add_food(self, food):
        self.foods.append(food)
        self.total_protein_calories += food.protein_calories
        self.total_carbs_calories += food.carbs_calories
        self.total_fat_calories += food.fat_calories
        self.total_calories += food.calories

        # returns the current percent value (in range [0.0, 1.0]) of the given nutrient in the current meal plan
        # , by calories.
    def percent_nutrient(self, nutrient):
        if self.total_calories > 0.0:
            return getattr(self, "total_%s_calories" % nutrient) / self.total_calories
        else:
            return 0.0

        #  returns the total percent (in range [0.0, 1.0]) of the given nutrient if the given food were added.
        #  The food item is not added to the the meal plan by the method; the method is just for speculation only.
    def calories_with_food(self, food):
        return self.total_calories + food.calories

        #  returns the total calories the meal plan would have, if the given food were added.
        #  The food item is not added to the meal plan by this method; the method is just for speculation only.
    def percent_nutrient_with_food(self, food, nutrient):
        if self.total_calories + food.calories > 0.0:
            return (getattr(self, "total_%s_calories" % nutrient) + getattr(food, "%s_calories" % nutrient)) / (
                        self.total_calories + food.calories)
        else:
            return 0.0

    def fraction_to_fit_calories_limit(self, food, calorie_limit):                  # Check later!!!!
        # Returns the fraction (0.0-1.0) of the food required to get
        # the calorie limit.
        if food.calories == 0:
            return 1.0
        fraction = (calorie_limit - self.total_calories) / food.calories
        if fraction >= 1.0:
            return 1.0
        elif fraction <= 0.0:
            return 0.0
        else:
            return fraction


    def fraction_to_fit_nutrient_goal(self, food, nutrient, goal):
        # Returns the fraction (0.0-1.0) of the food required to get
        # the nutrient goal.
        denom = getattr(food, '%s_calories' % nutrient) - goal * food.calories
        if denom == 0:
            return 1.0
        fraction = (goal * self.total_calories - getattr(self, 'total_%s_calories' % nutrient)) / denom
        if fraction >= 1.0:
            return 1.0
        elif fraction <= 0.0:
            return 0.0
        else:
            return fraction

    def meets_calorie_limit(self, calorie_limit, threshold):

        difference = calorie_limit - self.total_calories
        return -threshold <= difference and difference <= threshold


    def meets_nutrient_goal(self, nutrient, goal, threshold):
        # Returns True if the total calorie contribution (by percent) of the
        # given nutrient ('protein', 'carbs' or 'fat') for the current
        # meal plan is within the specified threshold of the given goal.
        difference = goal - self.percent_nutrient(nutrient)
        return -threshold <= difference and difference <= threshold



    def __str__(self):
        #  returns a string listing the foods selected for the meal plan along with summary information about calorie
        #  content.
        s = ""
        if len(self.foods) == 0: return "Empty Plan"
        item = 1
        for food in self.foods:
            s += "%d: %s\n" % (item, food)
            item += 1

        s += "Total Calories: %s\n" % self.total_calories
        s += "\tProtein: %s\n" % self.percent_nutrient("protein")
        s += "\tCarbs: %s\n" % self.percent_nutrient("carbs")
        s += "\tFat: %s" % self.percent_nutrient("fat")

        return s
