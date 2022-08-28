# # Project 1
# # madlibs
# # string concatenation
youtuber = "DigitalSridhar"

print("subscribe to" + youtuber)
print(f"subscribe to {youtuber}")  # cleanest way for string concatenation
print("subscribe to {}".format(youtuber))

adj = input("Adjective: ")
verb1 = input ("Verb: ")
verb2 = input ("Verb: ")
famous_person = input ("Famous person: ")
madlib =f"Computer programming is so {adj}! It makes me so excited all the time because \
          I love to  {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"
print (madlib)
madlib =f"Computer programming is so {adj}! It makes me so excited all the time because \
I love to  {verb1}. Stay hydrated and {verb2} like you are {famous_person}!"          
print (madlib)