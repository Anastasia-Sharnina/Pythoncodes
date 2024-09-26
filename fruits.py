# using random module the random smoothies can be made ^^

import random
# let's add some more fruits!

fruits_list = ["Apple", "Orange", "Banana", "Watermelon", "Grapes"] #list

print(f'Fruits: {fruits_list}')

smoothie_inside = random.sample(fruits_list, 3) # let's make smoothies with 3 random ingredients (using randeom.sample()) 

print("Here's a random smoothie for our dear customer!")
print(f'Smoothie mix: {smoothie_inside}')