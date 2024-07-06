import pandas as pd
import tkinter as tk
from tkinter import ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv(r"C:\Users\HP\Desktop\kartik\Dataset .csv")

# Determine the top three most common cuisines
top_cuisines = data['Cuisines'].str.split(', ').explode().value_counts().head(3)

# Calculate the percentage of restaurants that serve each of the top cuisines
total_restaurants = len(data)
cuisine_percentages = (top_cuisines / total_restaurants) * 100

# Identify the city with the highest number of restaurants
city_counts = data['City'].value_counts()
top_city = city_counts.idxmax()
top_city_count = city_counts.max()

# Calculate the average rating for restaurants in each city
average_ratings = data.groupby('City')['Aggregate rating'].mean()

# Determine the city with the highest average rating
top_avg_rating_city = average_ratings.idxmax()
highest_avg_rating = average_ratings.max()

# Create the main window
root = tk.Tk()
root.title("Restaurant Data Analysis")

# Create a frame for the top cuisines
frame = ttk.Frame(root, padding="10")
frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

# Create labels for the top cuisines and their percentages
for i, (cuisine, count) in enumerate(top_cuisines.items()):
    ttk.Label(frame, text=f"{cuisine}: {count} restaurants ({cuisine_percentages[cuisine]:.2f}%)").grid(row=i, column=0, sticky=tk.W)

# Add padding around all components
for child in frame.winfo_children():
    child.grid_configure(padx=5, pady=5)

# Create a label for the city with the highest number of restaurants
ttk.Label(frame, text=f"City with the highest number of restaurants: {top_city} ({top_city_count} restaurants)").grid(row=4, column=0, sticky=tk.W)

# Create a label for the city with the highest average rating
ttk.Label(frame, text=f"City with the highest average rating: {top_avg_rating_city} (Average Rating: {highest_avg_rating:.2f})").grid(row=5, column=0, sticky=tk.W)

# Create a figure for the graph
fig, ax = plt.subplots(2, 1, figsize=(8, 10))

# Plot the top cuisines and their percentages
ax[0].bar(top_cuisines.index, cuisine_percentages)
ax[0].set_xlabel('Cuisines')
ax[0].set_ylabel('Percentage of Restaurants')
ax[0].set_title('Top 3 Cuisines and Their Percentages')

# Plot the average ratings for the top 10 cities by number of restaurants
top_cities = city_counts.head(10)
top_cities_ratings = average_ratings[top_cities.index]
ax[1].bar(top_cities_ratings.index, top_cities_ratings)
ax[1].set_xlabel('Cities')
ax[1].set_ylabel('Average Rating')
ax[1].set_title('Average Ratings for Top 10 Cities by Number of Restaurants')

# Embed the plot in the tkinter window
canvas = FigureCanvasTkAgg(fig, master=root)
canvas.draw()
canvas.get_tk_widget().grid(row=6, column=0, padx=10, pady=10)

# Start the main event loop
root.mainloop()
