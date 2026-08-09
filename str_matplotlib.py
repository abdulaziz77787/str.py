import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# Update this path to where your file is stored:
df = pd.read_csv(r'C:\archive\tmdb_movies_data.csv')

print(df.head())
#df.info()

#x=np.random.randn(500)
#print(plt.hist(x,5));
#print(plt.show());



x = np.array([1, 2, 3, 4, 5, 6, 7])
y = np.array([1, 2, 3, 5, 8, 13, 20])

plt.plot(x, y)
plt.xlabel("x")
plt.ylabel("y")
plt.title("Line Chart")
plt.show()


plt.plot(x, x, marker="o", markersize=10, linestyle="--", linewidth=3, label="Normal")
plt.plot(x, y, marker="o", markersize=10, linestyle="--", linewidth=3, label="Fast")

plt.xlabel("x")
plt.ylabel("y")
plt.title("Two Line Chart")
plt.legend()
plt.show()


x_plot1 = np.array([1, 2, 3, 4, 5, 6, 7])
y_plot1 = np.array([1, 1, 2, 3, 5, 8, 13])

x_plot2 = np.array([0, 1, 2, 3, 4, 5, 6])
y_plot2 = np.array([2, 4, 6, 8, 10, 12, 14])

x_plot3 = np.array([0, 1, 3, 4])
y_plot3 = np.array([4, 6, 3, 4])

fig, axes = plt.subplots(1, 3, figsize=(15, 4))

axes[0].plot(x_plot1, y_plot1)
axes[0].set_title("First Chart")

axes[1].plot(x_plot2, y_plot2)
axes[1].set_title("Second Chart")

axes[2].plot(x_plot3, y_plot3)
axes[2].set_title("Third Chart")

fig.suptitle("My data visualization assignment")

plt.tight_layout()
plt.show()


#x = [1, 2, 3, 4, 5]
#y = [2, 4, 6, 8, 10]

#plt.plot(x, y)
#plt.xlabel("X")
#plt.ylabel("Y")
#plt.title("My Line Chart")
#plt.grid(True)

#plt.show()

#plt.plot([1,2,3,4]);
#plt.plot([233,52,12,545,45,233])
#print(plt.show())

#move=pd.DataFrame(df.release_year.value_counts(ascending=True))
#print(move)
#move=move.reset_index()
#print(plt.plot(move['release_year']))
#print(plt.show())

