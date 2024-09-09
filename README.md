# Ultimate-Werewolf-Role-Randomizer
![Ultimate Werewolf Deluxe Edition](https://cf.geekdo-images.com/dncdxD1g4dxMh9e8oKlzbg__opengraph/img/fyS4S6BZX_krWoxUwRBgjvECKZU=/0x0:1000x525/fit-in/1200x630/filters:strip_icc()/pic1878492.png)
This is a simple role randomizer tool made specifically for the 'Ultimate Werewolf Deluxe Edition (Hunting Party Expansion)' pack. But it can be modified to make it compatible with other versions of werewolf.
<br/><br/>
Check it out: https://randomwolf.vercel.app

## Requirements
- Python 3.8+

## Installation & Usage

### Setting up the server
1. While in the main directory type the following to install all the required python libraries:
   ```
   pip install -r requirements.txt
   ```
2. To host the server locally, scroll all the way down in 'app.py' and change
   ```
   if __name__ == '__main__':
    app.run(debug=False, host='0.0.0.0')
   ```
   to this
   ```
   if __name__ == '__main__':
    app.run(debug=True)
   ```
4. Run the Flask app:
   ```
   flask run --debug
   ``` 
5. Launching the server may take a while but once launched it should be good to go.

### Usage
1. Select the number of players (5 - 40) excluding the moderator.
2. Enable or disable any of the options based on preference.
3. Generate!

## FAQs
Q. How to add custom roles or other roles?<br/>
A. To the 'roles' list in the main function, add the role in the format ["Name", Strength, "Type"].

Q. What is strength?<br/>
A. It is the +ve or -ve value in the bottom right of the werewolf card.

Q. What are the supported types?<br/>
A. As of now the only supported types are (more supported types coming soon... maybe):<br/>
&emsp;&emsp;"W" - Werewolf<br/>
&emsp;&emsp;"T" - Town<br/>
&emsp;&emsp;"V" - Vampire<br/>
&emsp;&emsp;"S" - Solo<br/>
&emsp;If vampires dont exist in your current pack, you may replace the role with a 3rd team from your own pack.<br/>
&emsp;Keep in mind that vampires represent a 3rd team independent from the town and werewolves.<br/>
&emsp;Also even if the 3rd team are not vampires, still add the "V" to their type.

## NOTE:
- This tool is 95% accurate. If you end getting the 5% of inaccuracy, randomize the roles again, or hand pick the roles.
- When randomizing roles for players > 35 it's better to enable all the options.
- The role list included in this program does not include the "Mason" roles cause... they are lame =)<br/>
  To include Masons, add 3 entries of ["Mason", +2, "T"] in the bottom of the roles list (Make sure to add , after each entry).
  
