# Pandas Dataframe with Computed column

import pandas as pd

data = {
    "A": [1, 2, 2, 1],
    "B": [3.1, 4.2, 1.5, 6.3],
    "C": [800, 150, 400, 210]
}

# Create the DataFrame using the data dictionary
data_frame = pd.DataFrame(data)

# Add computed columns: A times C and B times C
data_frame["A_times_C"] = data_frame["A"] * data_frame["C"]
data_frame["B_times_C"] = data_frame["B"] * data_frame["C"]

print(data_frame)