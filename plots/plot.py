import matplotlib.pyplot as plt
import numpy as np

# voltage across r_ref
v_r_ref = [
		0.100906,
	   	0.29932,
		0.49824,
		0.69848,
		0.90320,
		1.10293,
		1.3126,
		1.4915,
		1.7141,
		1.9098,
		2.1698,
		2.3159,
		2.4972
	]

# voltage across r_test
v_r_test = [
		0.118740,
		0.3441,
		0.564,
		0.78015,
		0.99673,
		1.2051,
		1.421,
		1.6036,
		1.8268,
		2.0283,
		2.2819,
		2.4377,
		2.6103
	]


# resistor values
r_ref = 1000
r_test = 1000


# get current using ohms law
i_r_ref = np.divide(v_r_ref, r_ref)
i_r_test = np.divide(v_r_test, r_test)

# find average difference in current
i_diff = []
for x in range(0,len(i_r_ref)):
	i_diff.append(abs(i_r_ref - i_r_test))

avg_diff = np.mean(i_diff)
print("Average difference : " + str(avg_diff * 1000) + "mA")

# convert to mA
i_r_ref = np.multiply(i_r_ref, 1000)
i_r_test = np.multiply(i_r_test, 1000)

# create figure
figure, ax = plt.subplots()

# plot and set axis labels
ax.plot(i_r_ref, i_r_test, "ko")
ax.set_xlabel("Current through reference resistor (mA)")
ax.set_ylabel("Current through test resistor (mA)")

# show the plot
plt.show()
