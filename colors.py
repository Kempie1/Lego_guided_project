import pandas as pd

# Read colors data
colors=pd.read_csv('datasets/colors.csv.gz')

# Print the first few rows

#print(colors.head())

# How many distinct colors are available?
# -- YOUR CODE FOR TASK 3 --
num_colors= colors.shape[0]

# Print num_colors

#print("There are a total of")
#print(num_colors)
#print("colors")


# colors_summary: Distribution of colors based on transparency
# -- YOUR CODE FOR TASK 4 --
colors_summary=colors.groupby("is_trans").count()
#print(colors_summary)


