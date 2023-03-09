import pandas as pd
import matplotlib.pyplot as plt

# read in the data from the file
df = pd.read_csv("romplus.txt", delimiter="\t")

# remove duplicates based on the DATE column
#df.drop_duplicates(subset="DATE", inplace=True)

# convert the DATE column to a datetime data type
df["DATE"] = pd.to_datetime(df["DATE"])

# calculate the time difference between earthquakes in seconds
df["TIME_DIFF"] = df["DATE"].diff().dt.total_seconds()

# convert time difference to frequency in Hz
df["FREQUENCY"] = 1 / df["TIME_DIFF"]

# plot the frequency over time
fig, ax1 = plt.subplots()

ax1.plot(df["DATE"], df["FREQUENCY"], color="blue")
ax1.set_xlabel("Date")
ax1.set_ylabel("Frequency (Hz)", color="blue")
ax1.tick_params(axis="y", labelcolor="blue")

# add a second y-axis for magnitude
ax2 = ax1.twinx()

ax2.plot(df["DATE"], df["MAG"], color="red")
ax2.set_ylabel("Magnitude", color="red")
ax2.tick_params(axis="y", labelcolor="red")

plt.show()
