import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression




def linear_model(
		floor_number, 
		year_construction, 
		square_meters, 
		rooms_number, 
		baths_number
		):
	return 0.5 * floor_number + 0.5 * year_construction + 0.5 * square_meters + 0.5 * rooms_number + 0.5 * baths_number