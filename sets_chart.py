import pandas as pd
import matplotlib.pyplot as plt
#%matplotlib inline

# Read sets data as `sets`
sets=pd.read_csv('datasets/sets.csv.gz')

# Create a summary of average number of parts by year: `parts_by_year`
parts_by_year = (sets.groupby("year").mean())["num_parts"]

# Plot trends in average number of parts by year

parts_by_year.plot()  #need to figgure out how to draw this from visual studio code.


# themes_by_year: Number of themes shipped by year
# -- YOUR CODE HERE --

themes_by_year=(sets.groupby("year")[['theme_id']].nunique())
#print(themes_by_year.head())

# Get the number of unique themes released in 1999
themes_in_1999 = themes_by_year.loc[1999,'theme_id']

# Print the number of unique themes released in 1999
print(themes_in_1999)

