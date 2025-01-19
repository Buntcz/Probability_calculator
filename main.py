import copy
import random
from collections import Counter

class Hat:
    def __init__(self,**kwargs):
        self.contents = []
        for color,count in kwargs.items():
            self.contents.extend([color] * count)
    def draw(self,n):
        if n > len(self.contents) - 1:
            n = len(self.contents)
        drawn_balls = []
        i = len(self.contents) - 1
        while n > 0:
            popped_ball = self.contents.pop(random.randint(0,i))
            drawn_balls.append(popped_ball)
            n -= 1
            i -= 1
        return drawn_balls

def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
    if not isinstance(hat,Hat):
        return "hat ust be an instace of the Hat class object."
    count = 0
    for _ in range(num_experiments):
        experiment_hat = copy.deepcopy(hat)
        balls_drawn = experiment_hat.draw(num_balls_drawn)
        success = True
        for color,req_count in expected_balls.items():
            if balls_drawn.count(color) < req_count:
                success = False
                break
        if success:
            count+=1
        
    return count / num_experiments
    
        

hat = Hat(black=6, red=4, green=3)
probability = experiment(hat=hat,
                  expected_balls={'red':2,'green':1},
                  num_balls_drawn=5,
                  num_experiments=2000)
print(probability)
