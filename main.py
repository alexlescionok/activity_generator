#### This app will generate a random activity from the provided list

'''
PREREQUISITES:
- googlesearch installed: 
-- https://pypi.org/project/googlesearch-python/ // https://www.geeksforgeeks.org/performing-google-search-using-python-code/

'''

#########################################################################


import random
from googlesearch import search
from app_lists.activities import activities_list
from app_lists.suggestion_phrases import phrases_list
from app_lists.names import names_list


################ MAJOR VERSION UPDATE - leave the command line to create more of a game experience
### explore PyGame


################ VERSION 3.2 - same version as 3.1 but as Class and adding experimental generator ##################
'''
 Current limitations:
 - google search sometines times out
 - google search sometimes gives the same result multiple times

'''

version = "3.2"
file_with_names = "app_lists/names.py"

class ActivityGenerator():

    # Welcome user(s)
    def welcome_users(self):
        print("\nACTIVITY_GENERATOR_##########################################_ACTIVITY_GENERATOR")
        print(f"VERSION-{version}")

    ##### Grab name(s)
    def name_grabber(self):
        names = input("\nPlease enter your names: ")
        return names

    # #### check if user exists
    def check_user_exists(self, names):
        if names in names_list:
            print(f"Welcome back {names}!")
        else:
            print(f"Welcome to activity generator {names} :)")
            ActivityGenerator.add_user_to_list(self, names)

        ActivityGenerator.activity_generator(self, names)

    ###### add names to python list instead of text file
    def add_user_to_list(self, names): #  may adapt this to make more dynamic by adding another argument before names (to be used as the text file)
        with open(file_with_names, "r") as read_file:
            replacement = ""
            for line in read_file:
                line = line.strip()
                if "'" in line:
                    changes = line.replace("]", f", '{names}']")
                else:
                    changes  = line.replace("]", f"'{names}']")
                replacement = replacement + changes
            
        with open(file_with_names, "w") as write_file:
            write_file.write(replacement)

    ### Generate activity
    def activity_generator(self, names):
        play = True
        while play:
            suggested_activity = random.choice(activities_list)
            suggested_activities = []
            user_response = ""
            print("\nHow about...")
            while user_response != "y" or "n":
                user_response = input(f"{suggested_activity}? (y/n/q) ")
                if user_response == "q":
                    print("\nExited activity generator.")
                    break
                elif user_response == "y":
                    print("Heck yeah, let's do it!")
                    print("\n##########################################")
                    print(f"\n{names}, you have chosen \033[3;36;32m'{suggested_activity.lower()}'\033[0;0m\n") #don't entirely understand how to not use a background colour, using 32m as the background digit seems to do the trick though?

                    # list google results for activity
                    ActivityGenerator.google_suggestion(self, suggested_activity)

                    # print rejected activities (if any)
                    if len(suggested_activities) > 0:
                        print("\n##########################################")
                        print("\nThese are the activities you said 'no' to:")
                        for rejected_activity in suggested_activities:
                            print(f"- {rejected_activity.lower()}")
                    
                    # ask the user if they would like to play again
                    play_again = input("\nPlease enter 'a' if you would like to play again! Otherwise, enter 'q' if you wish to leave. ")
                    if play_again == "a":
                        play = True
                    elif play_again == "q":
                        play = False
                        print(f"See you next time {names}!")
                    else:
                        # play = False
                        print("I only accept 'a' and 'q' :)")
                        play_again = input("\nPlease enter 'a' if you would like to play again! Otherwise, enter 'q' if you wish to leave. ")

                    break

                elif user_response == "n":
                    alternative_activity_phrase = random.choice(phrases_list)
                    print(f"Let's try something else! {alternative_activity_phrase}")
                    suggested_activities.append(suggested_activity)
                    suggested_activity = random.choice(activities_list)
                else:
                    print("I only accept 'y' or 'n' as a response, please try again :)")

    ### Generate google suggestions
    def google_suggestion(self, suggested_activity):
        query = suggested_activity
        print("Here are some (hopefully) useful links for this activity: ")
        for result in search(query, num_results=3):
            print(result)


##### Launch activity generator #####

#### ORIGINAL
original = ActivityGenerator() # instantiating object 'original', could instantiate 'experimental' and call other methods

try:
    original.welcome_users()
    original.check_user_exists(original.name_grabber()) #launches all subsequent functions as and when required
except KeyboardInterrupt:
    print("\nLeaving acitvity generator, see you next time!")
except: # comment out when troubleshooting
    print("\nSomething went wrong.")



################# VERSION 3.1 - store user's names in case they play the game again - IMPROVED USING PYTHON LISTS
### will call name_grabber in welcome_users; name_grabber will call add_user_to_list, or we can combine name_grabber and add_user_to_list

# version = "3.1"
# file_with_names = "app_lists/names.py"

# # Welcome user(s)
# def welcome_users():
#     print("\nACTIVITY_GENERATOR_##########################################_ACTIVITY_GENERATOR")
#     print(f"VERSION-{version}")

# ##### Grab name(s)
# def name_grabber():
#     names = input("\nPlease enter your names: ")
#     return names

# # #### check if user exists
# def check_user_exists(names):
#     if names in names_list:
#         print(f"Welcome back {names}!")
#     else:
#         print(f"Welcome to activity generator {names} :)")
#         add_user_to_list(names)
    
#     activity_generator(names) 

# ###### add names to python list instead of text file
# def add_user_to_list(names): #  may adapt this to make more dynamic by adding another argument before names (to be used as the text file)
#     with open(file_with_names, "r") as read_file:
#         replacement = ""
#         for line in read_file:
#             line = line.strip()
#             if "'" in line:
#                 changes = line.replace("]", f", '{names}']")
#             else:
#                 changes  = line.replace("]", f"'{names}']")
#             replacement = replacement + changes
        
#     with open(file_with_names, "w") as write_file:
#         write_file.write(replacement)


# ### Generate activity
# def activity_generator(names):
#     suggested_activity = random.choice(activities_list)
#     suggested_activities = []
#     user_response = ""
#     print("\nHow about...")
#     while user_response != "y" or "n":
#         user_response = input(f"{suggested_activity}? (y/n/q) ")
#         if user_response == "q":
#             print("\nExited activity generator.")
#             break
#         elif user_response == "y":
#             print("Heck yeah, let's do it!")
#             print("\n##########################################")
#             print(f"\n{names}, you have chosen \033[3;36;32m'{suggested_activity.lower()}'\033[0;0m\n") #don't entirely understand how to not use a background colour, using 32m as the background digit seems to do the trick though?

#             # list google results for activity
#             google_suggestion(suggested_activity)

#             # print rejected activities (if any)
#             if len(suggested_activities) > 0:
#                 print("\n##########################################")
#                 print("\nThese are the activities you said 'no' to:")
#                 for rejected_activity in suggested_activities:
#                     print(f"- {rejected_activity.lower()}")
#             break
#         elif user_response == "n":
#             alternative_activity_phrase = random.choice(phrases_list)
#             print(f"Let's try something else! {alternative_activity_phrase}")
#             suggested_activities.append(suggested_activity)
#             suggested_activity = random.choice(activities_list)
#         else:
#             print("I only accept 'y' or 'n' as a response, please try again :)")

# ### Generate google suggestions
# def google_suggestion(suggested_activity):
#     query = suggested_activity
#     print("Here are some (hopefully) useful links for this activity: ")
#     for result in search(query, num_results=3):
#         print(result)

# ##### Launch activity generator #####
# try:
#     welcome_users()
#     check_user_exists(name_grabber()) #launches all subsequent functions as and when required
# except KeyboardInterrupt:
#     print("\nLeaving acitvity generator, see you next time!")
# except:
#     print("\nSomething went wrong.")


################# VERSION 3.0 - store user's names in case they play the game again
### will call name_grabber in welcome_users; name_grabber will call add_user_to_list, or we can combine name_grabber and add_user_to_list

# file_with_names = "app_lists/names.txt"

# # Welcome user(s)
# def welcome_users():
#     print("\nACTIVITY_GENERATOR_##########################################_ACTIVITY_GENERATOR")

# # Grab name(s)
# def name_grabber():
#     names = input("\nPlease enter your names: ")
#     return names

### Check if user exists in text file - OLD NOT NEEDED, KEEP UNTIL ADD USER TO LIST FUNCTION STARTS TO WORK
# check_user_exists("and") #works, but also assumes name exists if part of a longer string, e.g. alex2 or alex and lexi
# def check_user_exists(names):
#     with open(file_with_names, "r") as names_file:
#         names_file.seek(0)
#         data = names_file.read()
#         if names in data:
#             print(f"\nWelcome back {names}!")
#         else:
#             # call add_user_to_list function 
#             print(f"Welcome to activity generator {names}!")
#             add_user_to_list(names)
    
#     activity_generator(names) 


### Add user to text file
#### FOR TEXT FILE, EACH NAME ON NEW LINE
# def add_user_to_list(names): #  may adapt this to make more dynamic by adding another argument before names (to be used as the text file)
#     with open(file_with_names, "a+") as names_file: # open names.txt - may adapt this to make more dynamic
#         names_file.seek(0) # Move read cursor to the start of file.
#         data = names_file.read() # Read all data in the file and save it as variable
#         if len(data) > 0: # Check if there is any data in the file
#             names_file.write("\n") # if so, add a new line
#         names_file.write(names) # Append names


# ### Generate activity
# def activity_generator(names):
#     suggested_activity = random.choice(activities_list)
#     suggested_activities = []
#     user_response = ""
#     print("\nHow about...")
#     while user_response != "y" or "n":
#         user_response = input(f"{suggested_activity}? (y/n/q) ")
#         if user_response == "q":
#             print("\nExited activity generator.")
#             break
#         elif user_response == "y":
#             print("Heck yeah, let's do it!")
#             print("\n##########################################")
#             print(f"\n{names}, you have chosen \033[3;36;32m'{suggested_activity.lower()}'\033[0;0m\n") #don't entirely understand how to not use a background colour, using 32m as the background digit seems to do the trick though?

#             # list google results for activity
#             google_suggestion(suggested_activity)

#             # print rejected activities (if any)
#             if len(suggested_activities) > 0:
#                 print("\n##########################################")
#                 print("\nThese are the activities you said 'no' to:")
#                 for rejected_activity in suggested_activities:
#                     print(f"- {rejected_activity.lower()}")
#             break
#         elif user_response == "n":
#             alternative_activity_phrase = random.choice(phrases_list)
#             print(f"Let's try something else! {alternative_activity_phrase}")
#             suggested_activities.append(suggested_activity)
#             suggested_activity = random.choice(activities_list)
#         else:
#             print("I only accept 'y' or 'n' as a response, please try again :)")

# ### Generate google suggestions
# def google_suggestion(suggested_activity):
#     query = suggested_activity
#     print("Here are some (hopefully) useful links for this activity: ")
#     for result in search(query, num_results=3):
#         print(result)

# welcome_users()
# check_user_exists(name_grabber()) #launches all subsequent functions as and when required


############### VERSION 2 - app split into multiple functions, 1 welcomes user(s), 2 grabs user name(s), 3 generates activity

# # Welcome user(s)
# def welcome_users():
#     print("\nACTIVITY_GENERATOR_##########################################_ACTIVITY_GENERATOR")
#     print("\nWelcome to activity generator!")

# # Grab name(s)
# def name_grabber():
#     names = input("Please enter your names: ")
#     print(f"\nHello {names}!")
#     return names

# def activity_generator(names):
#     suggested_activity = random.choice(activities_list)
#     suggested_activities = []
#     user_response = ""
#     print("\nHow about...")
#     while user_response != "y" or "n":
#         user_response = input(f"{suggested_activity}? (y/n/q) ")
#         if user_response == "q":
#             print("\nExited activity generator.")
#             break
#         elif user_response == "y":
#             print("Heck yeah, let's do it!")
#             print("\n##########################################")
#             print(f"\n{names}, you have chosen \033[3;36;32m'{suggested_activity.lower()}'\033[0;0m\n") #don't entirely understand how to not use a background colour, using 32m as the background digit seems to do the trick though?

#             # list google results for activity
#             query = suggested_activity
#             print("Here are some (hopefully) useful links for this activity: ")
#             for result in search(query, num_results=3):
#                 print(result)

#             # print rejected activities (if any)
#             if len(suggested_activities) > 0:
#                 print("\n##########################################")
#                 print("\nThese are the activities you said 'no' to:")
#                 for rejected_activity in suggested_activities:
#                     print(f"- {rejected_activity.lower()}")
#             break
#         elif user_response == "n":
#             alternative_activity_phrase = random.choice(phrases_list)
#             print(f"Let's try something else! {alternative_activity_phrase}")
#             suggested_activities.append(suggested_activity)
#             suggested_activity = random.choice(activities_list)
#         else:
#             print("I only accept 'y' or 'n' as a response, please try again :)")

# welcome_users()
# activity_generator(name_grabber()) # no need to call name_grabber() by by itself (if you do, then the function runs twice)


############# VERSION 1 - single function handling everything
# def activity_generator(names):
#     suggested_activity = random.choice(activities_list)
#     suggested_activities = []
#     user_response = ""
#     print("\nACTIVITY_GENERATOR_##########################################_ACTIVITY_GENERATOR")
#     print("\nWelcome to activity generator!")
#     names = input("Please enter your names: ")
#     print(f"\nHello {names}!")
#     print("\nHow about...")
#     while user_response != "y" or "n":
#         user_response = input(f"{suggested_activity}? (y/n/q) ")
#         if user_response == "q":
#             print("\nExited activity generator.")
#             break
#         elif user_response == "y":
#             print("Heck yeah, let's do it!")
#             print("\n##########################################")
#             print(f"\n{names}, you have chosen \033[3;36;32m'{suggested_activity.lower()}'\033[0;0m\n") #don't entirely understand how to not use a background colour, using 32m as the background digit seems to do the trick though?

#             # list google results for activity
#             query = suggested_activity
#             print("Here are some (hopefully) useful links for this activity: ")
#             for result in search(query, num_results=3):
#                 print(result)

#             # print rejected activities (if any)
#             if len(suggested_activities) > 0:
#                 print("\n##########################################")
#                 print("\nThese are the activities you said 'no' to:")
#                 for rejected_activity in suggested_activities:
#                     print(f"- {rejected_activity.lower()}")
#             break
#         elif user_response == "n":
#             alternative_activity_phrase = random.choice(phrases_list)
#             print(f"Let's try something else! {alternative_activity_phrase}")
#             suggested_activities.append(suggested_activity)
#             suggested_activity = random.choice(activities_list)
#         else:
#             print("I only accept 'y' or 'n' as a response, please try again :)")

# names = ""
# activity_generator(names)


# VERSION ?? - make work with Docker

# VERSION ?? - add dictionary for something? # integrate a dictionary to practise retrieving values
# dict = {"key1" : "value1", "key2" : "value2"}
# print(dict.get("key1"))