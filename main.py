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

    #### Welcome user(s)
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
    def add_user_to_list(self, names):
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

    #### Generate activity
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
                    print(f"\n{names}, you have chosen \033[3;36;32m'{suggested_activity.lower()}'\033[0;0m\n") #### don't entirely understand how to not use a background colour, using 32m as the background digit seems to do the trick though?

                    #### list google results for activity
                    ActivityGenerator.google_suggestion(self, suggested_activity)

                    #### print rejected activities (if any)
                    if len(suggested_activities) > 0:
                        print("\n##########################################")
                        print("\nThese are the activities you said 'no' to:")
                        for rejected_activity in suggested_activities:
                            print(f"- {rejected_activity.lower()}")
                    
                    #### ask the user if they would like to play again
                    play_again = input("\nPlease enter 'a' if you would like to play again! Otherwise, enter 'q' if you wish to leave. ")
                    if play_again == "a":
                        play = True
                    elif play_again == "q":
                        play = False
                        print(f"See you next time {names}!")
                    else:
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

    #### Generate google suggestions
    def google_suggestion(self, suggested_activity):
        query = suggested_activity
        print("Here are some (hopefully) useful links for this activity: ")
        for result in search(query, num_results=3):
            print(result)


##### Launch activity generator #####

original = ActivityGenerator()

try:
    original.welcome_users()
    original.check_user_exists(original.name_grabber()) #### launches all subsequent methods as and when required
except KeyboardInterrupt:
    print("\nLeaving acitvity generator, see you next time!")
except: #### COMMENT OUT WHEN TROUBLESHOOTING
    print("\nSomething went wrong.")