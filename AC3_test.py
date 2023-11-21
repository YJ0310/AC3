from AC3_data import set1, set2, set3, L, C
from scipy.optimize import curve_fit, minimize
import matplotlib.pyplot as plot
import numpy as np
import math

# initialize the constant variable
resistances = [10, 20, 50]  # Resistances of the three experiments
colors = ["red"]  # colour of the graph
voltage = 14  # voltage of the experiment
x = [set1.x, set2.x, set3.x]  # x values of the three experiments
y = [set1.y, set2.y, set3.y]  # y values of the three experiments
x_fit = np.linspace(1000, 4000, 500)  # define the x_fit
# can ask the user the choose the mode
# i = (
#     int(input(
#         "Which graph you want (1/2/3) \n 1 - R = 10 Ohm \n 2 - R = 20 Ohm \n 3 - R = 50 Ohm \n"
#     ))
#     - 1
# )


# define the function for the graph
def graph_function(f, resistance=10, L_fit=L, C_fit=C):
    w = 2 * math.pi * f
    X_L = w * L_fit
    X_C = 1 / (w * C_fit)
    Z = (resistance**2 + (X_L - X_C) ** 2) ** (1 / 2)
    return voltage / Z


# repeat ploting the graph for the three experiments
for i in range(3):
    # define the curve fit
    popt, pcov = curve_fit(
        graph_function, x[i], y[i], [resistances[i], L, C], maxfev=10000
    )
    print(abs(popt))  # check the value
    y_fit = graph_function(
        x_fit, popt[0], abs(popt[1]), abs(popt[2])
    )  # define the y_fit

    label = " ".join(["Resistance =", str(resistances[i]), "Ohm"])
    print("testing",x_fit[np.where(y_fit==max(y_fit))[0][0]])
    max_y_fit = "".join(["f_res =", f"{x_fit[np.where(y_fit==max(y_fit))[0][0]]:.3f}", "Hz"])
    # plot the graph
    plot.scatter(x[i], y[i], label=label, color=colors[0])
    plot.plot(x_fit, y_fit, color=colors[0], label=max_y_fit)
    plot.legend()
    plot.show()
