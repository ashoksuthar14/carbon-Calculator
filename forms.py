from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField, FloatField
from wtforms.validators import DataRequired, Optional

class CarbonFootprintForm(FlaskForm):
    # Basic Info
    name = StringField('Name', validators=[DataRequired()])
    age = IntegerField('Age', validators=[DataRequired()])
    location = StringField('Location/Area', validators=[DataRequired()])
    
    # Household Energy
    household_members = IntegerField('Household Members', validators=[DataRequired()])
    monthly_electricity = FloatField('Monthly Electricity Bill (₹)', validators=[DataRequired()])
    renewable_energy = SelectField('Renewable Energy Sources',
                                 choices=[('no', 'No'), ('yes', 'Yes')])
    cooking_fuel = SelectField('Cooking Fuel',
                             choices=[('lpg', 'LPG'), ('electricity', 'Electricity'),
                                    ('induction', 'Induction'), ('biomass', 'Firewood/Biomass'),
                                    ('others', 'Others')])
    
    # Transportation
    transport_mode = SelectField('Primary Transportation',
                               choices=[('car', 'Car'), ('bike', 'Bike'),
                                      ('bus', 'Public Bus'), ('metro', 'Metro/Train'),
                                      ('bicycle', 'Bicycle'), ('walking', 'Walking'),
                                      ('wfh', 'Work from Home')])
    vehicle_fuel = SelectField('Vehicle Fuel Type',
                             choices=[('none', "I don't use a personal vehicle"),
                                    ('petrol', 'Petrol'), ('diesel', 'Diesel'),
                                    ('cng', 'CNG'), ('electric', 'Electric')])
    daily_travel = FloatField('Daily Travel Distance (km)', validators=[Optional()])
    domestic_flights = IntegerField('Domestic Flights per Year', default=0)
    international_flights = IntegerField('International Flights per Year', default=0)
    
    # Food & Diet
    diet_type = SelectField('Diet Type',
                          choices=[('vegetarian', 'Vegetarian'),
                                 ('non-vegetarian', 'Non-Vegetarian'),
                                 ('vegan', 'Vegan'),
                                 ('eggetarian', 'Eggetarian')])
    red_meat = SelectField('Red Meat Consumption',
                         choices=[('never', 'Never'),
                                ('occasional', 'Occasionally'),
                                ('weekly', '1-2 times/week'),
                                ('frequent', 'More than 3 times/week')])
    dairy = SelectField('Dairy Consumption',
                      choices=[('daily', 'Daily'),
                             ('occasional', 'Occasionally'),
                             ('rarely', 'Rarely'),
                             ('never', 'Never')])
    food_waste = SelectField('Food Waste Frequency',
                          choices=[('often', 'Often'),
                                 ('sometimes', 'Sometimes'),
                                 ('rarely', 'Rarely'),
                                 ('never', 'Never')])
    
    # Waste & Recycling
    waste_segregation = SelectField('Do you segregate your waste (dry/wet)?',
                                  choices=[('yes', 'Yes'), ('no', 'No')])
    recycling = SelectField('What do you recycle?',
                          choices=[('all', 'All (Plastic, Paper, Metal, E-waste)'),
                                 ('some', 'Some Items'),
                                 ('none', 'None')])
    weekly_waste = SelectField('Weekly household waste generation',
                             choices=[('low', 'Less than 5 kg'),
                                    ('medium', '5-10 kg'),
                                    ('high', '10-20 kg'),
                                    ('very_high', 'More than 20 kg')])
    
    # Shopping & Lifestyle
    yearly_clothes = SelectField('Yearly clothing purchases',
                               choices=[('minimal', 'Less than 10 items'),
                                      ('moderate', '10-20 items'),
                                      ('frequent', '20-50 items'),
                                      ('excessive', 'More than 50 items')])
    electronics = SelectField('Yearly electronics purchases',
                           choices=[('none', '0'),
                                  ('low', '1'),
                                  ('medium', '2-3'),
                                  ('high', 'More than 3')])
    online_shopping = SelectField('Online shopping frequency',
                               choices=[('rarely', 'Rarely'),
                                      ('monthly', '1-2 times/month'),
                                      ('weekly', 'Weekly'),
                                      ('daily', 'Daily')])
    
    # Living Environment & Green Practices
    ac_usage = SelectField('Air conditioner usage',
                         choices=[('no', 'No AC'),
                                ('seasonal', '1-3 months'),
                                ('moderate', '4-6 months'),
                                ('heavy', 'More than 6 months')])
    home_type = SelectField('Home type',
                          choices=[('apartment1', 'Apartment (1 BHK)'),
                                 ('apartment2', 'Apartment (2-3 BHK)'),
                                 ('house', 'Independent House'),
                                 ('villa', 'Villa/Large Bungalow')])
    water_usage = SelectField('Monthly water usage',
                           choices=[('low', 'Less than 5000 Litres'),
                                  ('medium', '5000-10000 Litres'),
                                  ('high', 'More than 10000 Litres'),
                                  ('unknown', 'Not sure')])
    green_programs = SelectField('Participation in green programs',
                               choices=[('none', 'None'),
                                      ('tree', 'Tree planting'),
                                      ('credits', 'Green energy credits'),
                                      ('multiple', 'Multiple programs')])
    pets = SelectField('Do you have pets?',
                     choices=[('none', 'No'),
                            ('dog', 'Yes - Dog'),
                            ('cat', 'Yes - Cat'),
                            ('multiple', 'Yes - Multiple pets')])
