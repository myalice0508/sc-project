"""
File: weather_master.py
Name:Irene Chen 陳筱涵
-----------------------
This program should implement a console program
that asks weather data from user to compute the
average, highest, lowest, cold days among the inputs.
Output format should match what is shown in the sample
run in the Assignment 2 Handout.

"""
EXIT = -100


def main():
	"""
	pre-condition: user can type the temperature
	post-condition: show the highest, lowest, average and the cold day in the scope
					which is the user typing.
	"""
	print('stanCode "weather Master 4.0"')

	temperature = int(input('Next Temperature: (or -100 to quit)?'))

	if temperature == EXIT:
		print('No temperatures were entered.')
	else:
		maximum = temperature
		minimum = temperature
		summary = temperature
		day = 1
		average = float(temperature)
		if temperature < 16:
			cold_day = 1
		else:
			cold_day = 0

		while True:
			temperature = int(input('Next Temperature: (or -100 to quit)?'))

			if temperature == EXIT:
				break
			if temperature > maximum:
				maximum = temperature
				# Higher number replace the old maximum
			elif temperature < minimum:
				minimum = temperature
				# lower number replace the old minimum
			if temperature < 16:
				cold_day += 1
			if temperature != -100:
				summary += temperature
				day += 1
				average = summary/day
		print('Highest temperature : ' + str(maximum))
		print('Lowest temperature : ' + str(minimum))
		print('Average: ' + str(average))
		print(str(cold_day) + ' cold days')



###### DO NOT EDIT CODE BELOW THIS LINE ######


if __name__ == "__main__":
	main()
