
import numpy as np

def linear_model(
		floor_number, 
		year_construction, 
		square_meters, 
		rooms_number, 
		baths_number
		):

	intercept = 8.351244
	floor_coef = 0
	year_coef = 0
	rooms_coef = -0.067523
	baths_coef = 0.060102

	y = intercept + floor_coef * floor_number + year_coef * year_construction + rooms_coef * rooms_number + baths_coef * baths_number

	price = square_meters * np.exp(y)

	return np.round(price, 2)