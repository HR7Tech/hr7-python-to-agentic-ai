# This calculator tells how many weeks we have left, if we live until 90 years old.

def life_in_weeks(age):
    age_limit = 90
    years_left_till_90 = age_limit - age
    weeks_in_a_year = 52
    weeks_left = years_left_till_90 * weeks_in_a_year
    print(f"You have {weeks_left} weeks left.")


life_in_weeks(25)