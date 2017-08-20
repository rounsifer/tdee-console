'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
This program will be able to calculate both the BMR and the TDEE of the user.
@author Ronald Rounsifer
@version 0.0.1
@date 08-19-2017
'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
The main method that will execute the program.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def main():
	collectData()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Collect the user input
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def collectData():
	calculation = False # False == BMR / True = TDEE
	gender = False # False == Male / True = Female
	age = 0
	height = 0
	weight = 0
	activity_level = 0

	calculation = calculationToBoolean(input("Type of calculation: "))
	gender = genderToBoolean(input("Gender: "))
	age = getAge()
	height = getHeight()
	weight = getWeight()
	if calculation == True:
		activity_level = getActivityLevel()
		info = [calculation, gender, age, height, weight, activity_level]
	else:
		info = [calculation, gender, age, height, weight]


	calculate(info)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Directs the program to the correct algorithm to run.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def calculate(info):
	if info[0] == False:
		return bmr(info)
	else:
		return tdee(info)

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Calculates the BMR of the user.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def bmr(info):
	gender = info[1]
	age = info[2]
	height = info[3]
	weight = info[4]

	if len(info) == 6:
		if gender == False:
			return 655 + (9.6 * weight) + (1.8 * height) - (4.7 * age)
		else:
			return 66 + (13.7 * weight) + (5 * height) - (6.8 * age)

	if len(info) == 5:
		if gender == False:
			print("\n-------------------------------------------------------------------")
			print(str(int(655 + (9.6 * weight) + (1.8 * height) - (4.7 * age))) + " k/cal per day")
			print("-------------------------------------------------------------------\n")
		else:
			print("\n-------------------------------------------------------------------")
			print(str(int(66 + (13.7 * weight) + (5 * height) - (6.8 * age))) + " k/cal per day")
			print("-------------------------------------------------------------------\n")


"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Calculates the TDEE of the user.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def tdee(info):
	gender = info[1]
	age = info[2]
	height = info[3]
	weight = info[4]
	activity_level = info[5]
	activity_multiplier = 0.0
	basal = bmr(info)
	tdee = 0.0

	if activity_level == 0:
		activity_multiplier = 1.2
	if activity_level == 1:
		activity_multiplier = 1.375
	if activity_level == 2:
		activity_multiplier = 1.55
	if activity_level == 3:
		activity_multiplier = 1.725
	if activity_level == 4:
		activity_multiplier = 5

	tdee = basal * activity_multiplier

	print("\n-------------------------------------------------------------------")
	print(str(int(tdee)) + " k/cal per day")
	print("-------------------------------------------------------------------\n")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets the activity level of the user.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def getActivityLevel():
	activityLevelDescriptions()
	level = input("\nActivity Level: ")
	level_ok = isNumber(level) and level in ['0','1','2','3','4']
	if level_ok:
		level = int(level)
		return level
	else:
		getActivityLevel()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Called when prompting the user for their activity level.
Simply displays the choices for the user.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def activityLevelDescriptions():
	print("To calculate your TDEE you must select from one of the 5 activity level choices below:")
	print("\n0 - Sedentary (Little or no exercise)")
	print("\n1 - Lightly Active (Light exercise 1-3/week)")
	print("\n2 - Moderately Active (Moderate exercise 3-5/week)")
	print("\n3 - Very Active (Heavy exercise 6-7/week)")
	print("\n4 - Extremely Active (Very heavy exercise 2x/day)")

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets the weight of the user.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def getWeight():
	weight = input("Weight: ")
	weight_ok = isNumber(weight)
	if weight_ok:
		weight = int(weight)
		return weight
	else:
		getWeight()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Gets the height from the user
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def getHeight():
	height = input("Height: ")
	height_ok = isNumber(height)
	if height_ok:
		height = int(height)
		return height
	else:
		getHeight()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Handles the logic behind acquiring the age from the user.
Makes use of the checkAge() function
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def getAge():
	age = input("Age: ")
	age_ok = isNumber(age)
	if age_ok:
		age = int(age)
		return age
	else:
		getAge()

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Checks if the age inputted is an actual number
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def isNumber(age):
	if age.isdigit():
		return True
	else:
		return False

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Converts a string to a boolean and is used to determine
the gender of the user based on their input.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def genderToBoolean(str):
	female = ("girl", "f", "fe", "fem", "fema", "femal", "female")
	return str.lower() in female

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Converts a string to a boolean and is used to determine
the calculation that the user wants performed.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
def calculationToBoolean(str):
	tdee = ("1", "t", "td", "tde", "tdee")
	return str.lower() in tdee

"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
Executes the main method if this program is run.
"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
if __name__ == "__main__":
	main()