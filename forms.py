from flask_wtf import FlaskForm
from wtforms import BooleanField, IntegerField
from wtforms.validators import DataRequired

class Randomizer(FlaskForm):
    players = IntegerField("Enter the total number of players (excl. Mod)")
    solo = BooleanField("Enable solo characters?")
    vampires = BooleanField("Enable vampire team?")
    npc = BooleanField("Enable normal villager roles?")