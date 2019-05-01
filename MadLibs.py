"""
This program generates passages that are generated in mad-lib format which is a story that is given with a blank spot for a word to be added to.
Author: Daniel Eyny
"""

# The template for the story

STORY = "This morning %s woke up feeling %s. 'It is going to be a %s day!' Outside, a bunch of %ss were protesting to keep %s in stores. They began to %s to the rhythm of the %s, which made all the %ss very %s. Concerned, %s texted %s, who flew %s to %s and dropped %s in a puddle of frozen %s. %s woke up in the year %s, in a world where %ss ruled the world."

print "Mad Libs Has Started... Enjoy!"

name= raw_input(" Enter your name or any name of your choice: ")
adj1= raw_input("Enter your first adjective: ")
adj2= raw_input("Enter your second adjective: ")
adj3= raw_input("Enter your third adjective: ")
verb= raw_input("Enter a verb: ")
noun1= raw_input("Enter your first noun: ")
noun2= raw_input("Enter your second noun: ")
animal= raw_input("Enter an Animal: ")
food= raw_input("Enter a Food: ")
fruit= raw_input("Enter a Fruit: ")
superhero= raw_input("Enter a Superhero: ")
country= raw_input("Enter a country: ")
dessert= raw_input("Enter a dessert: ")
year= raw_input("Enter year: ")

print STORY % (name, adj1, adj2, animal, food, verb, noun1, fruit, adj3, name, superhero, name, country, name, dessert, name, year, noun2)
