# Ultimate Werewolf Deluxe Edition (Hunting party pack) role randomizer [Web UI version]
# Made by 6-Isa-9

# Script works for players 5 - 40 (more no. of players = slightly slower output)
# NOTE: This script was mainly made for the Ultimate Werewolf Deluxe Edition (Hunting party pack).

# Q. How to add custom roles or other roles? 
# A. To the 'roles' list in the main function, add the role in the format ["Name", Strength, "Type"]

# Q. What is strength?
# A. It is the +ve or -ve value in the bottom right of the werewolf card

# Q. What are the supported types?
# A. As of now the only supported types are (more supported types coming soon... maybe):
#       "W" - Werewolf
#       "T" - Town
#       "V" - Vampire
#       "S" - Solo
#    If vampires dont exist in your current pack, you may replace the role with a 3rd team from your own pack.
#    Keep in mind that vampires represent a 3rd team independent from the town and werewolves.
#    Also even if the 3rd team are not vampires, still add the "V" to their type.

# NOTE: The role list included in this program does not include the "Mason" roles cause... they are lame =)
# To include Masons, add 3 entries of ["Mason", +2, "T"] in the bottom of the roles list (Make sure to add , after each entry).


from flask import Flask, render_template
from forms import Randomizer
import random

app = Flask(__name__)
app.config['SECRET_KEY'] = 'h#@hbJHB$@uygAHB!3137_yu_@_bl@(k_n!G@_JKH@#nlNAUBKJ~/AS,.69<>ASDfl..911,aSFOJ'

@app.route("/", methods=['GET', 'POST'])
def main():
    form = Randomizer()

    # Define the roles and their strength values
    final_roles = []
    total_strength = 0
    roles = [
        # Special Wolves
        ["Alpha Wolf", -9, "W"],
        ["Lone Wolf", -5, "W"],
        ["Wolf Cub", -8, "W"],
        ["Minion", -6, "W"],
        ["Sorceress", -3, "W"],
        # Normal Wolves
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        ["Werewolf", -6, "W"],
        # Vampires
        ["Vampire", -7, "V"],
        ["Vampire", -7, "V"],
        ["Vampire", -7, "V"],
        ["Vampire", -7, "V"],
        ["Vampire", -7, "V"],
        ["Vampire", -7, "V"],
        ["Vampire", -7, "V"],
        ["Vampire", -7, "V"],
        # NPCs
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        ["Villager", +1, "T"],
        # Solo
        ["Cult Leader", +1, "S"],
        ["Hoodlum", 0, "S"],
        ["Tanner", -2, "S"],
        # Special people
        ["Huntress", +3, "T"],
        ["Lycan", +1, "T"],
        ["Doppleganger", -2, "T"],
        ["Bodyguard", +3, "T"],
        ["Hunter", +3, "T"],
        ["Seer", +7, "T"],
        ["Mad Bomber", -2, "T"],
        ["Tough Guy", +3, "T"],
        ["Trouble Maker", -3, "T"],
        ["Village Idiot", +2, "T"],
        ["Drunk", +4, "T"],
        ["Apprentice Seer", +4, "T"],
        ["Prince", +3, "T"],
        ["Diseased", +3, "T"],
        ["Mystic Seer", +9, "T"],
        ["Witch", +4, "T"],
        ["Cursed", -3, "T"],
        ["Old Hag", +1, "T"],
        ["Mayor", +2, "T"],
        ["Spellcaster", +1, "T"],
        ["Revealer", +4, "T"],
        ["P.I.", +3, "T"],
        ["Mentalist", +6, "T"],
        ["Priest", +3, "T"],
        ["Pacifist", -1, "T"],
        ["Aura Seer", +3, "T"],
        ["Cupid", -3, "T"],
        ["Ghost", +2, "T"]
    ]

    if form.validate_on_submit():
        max_card_input = form.players.data
        solo_input = form.solo.data
        triplet_input = form.vampires.data
        npc_input = form.npc.data


        filtered_roles = []


        for role in roles:
            # Check solo roles condition
            if solo_input == False and role[2] == "S":
                continue
            # Check three teams condition
            if triplet_input == False and role[2] == "V":
                continue
            # Check normal villager condition
            if npc_input == False and role[0] == "Villager" and role[1] == 1:
                continue
            # If role passed all filters, add to filtered_roles
            filtered_roles.append(role)


        if len(filtered_roles) > max_card_input:
            found = False
            while found != True:
                # Shuffling cards and picking random cards
                user_selected_roles = shuffler(max_card_input, filtered_roles)
                # Checking if currently selected random cards are balanced
                balanced, current_total_strength = balancer(user_selected_roles)

                # Found a perfect match
                if balanced and ratio(user_selected_roles, solo_input, triplet_input):

                    # Sorting the final selected roles in order
                    order = {"W": 0, "V": 1, "S": 2, "T": 3}
                    final_roles = sorted(user_selected_roles, key = lambda x: order[x[2]])
                    # Re-calculating total strength
                    total_strength = current_total_strength

                    found = True
                
                # No match found: continue loop
                else:
                    continue
        else:
            print("Error! The max players specified exceed the filtered list of roles.")


    return render_template("main.html",
                           form = form,
                           total_strength = total_strength,
                           final_roles = final_roles,
                           prev_players = form.players.data,
                           prev_solo = form.solo.data,
                           prev_vampires = form.vampires.data,
                           prev_npc = form.npc.data)



# Function to randomly pick a given number of cards
def shuffler(max_cards, roles_list):
    temp_roles = roles_list.copy()
    final_roles = []

    # Looping to get all unique cards = max cards
    for i in range(0, max_cards):
        selected_role = random.choice(temp_roles)
        final_roles.append(selected_role)
        temp_roles.pop(temp_roles.index(selected_role))

    return final_roles

# Function to balance out the strengths of the roles (-2 to 2)
def balancer(selected_roles_list):
    total_strength = 0

    for role in selected_roles_list:
        total_strength += role[1]

    if total_strength >= -2 and total_strength <= 2:
        return True, total_strength
    else:
        return False, total_strength

# Function to check for correct role ratio
def ratio(selected_roles_list, solo_input, triplet_input):
    w = 0   # Werewolves
    t = 0   # Town
    s = 0   # Solo
    v = 0   # Vampires
    
    # Counting roles
    for role in selected_roles_list:
        if role[2] == "W":
            w += 1
        if role[2] == "T":
            t += 1
        if role[2] == "S" and solo_input == True:
            s += 1
        if role[2] == "V" and triplet_input == True:
            v += 1

    # If pass all conditions return True, else False
    if not (len(selected_roles_list) * 0.15 <= w <= len(selected_roles_list) * 0.3):
        return False
    
    if triplet_input == True and not (len(selected_roles_list) * 0.1 <= v <= len(selected_roles_list) * 0.2):
        return False
    
    if solo_input == True and s < 1:
        return False
    
    return True



if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
