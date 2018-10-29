import matplotlib.pyplot as plt

# Data to plot

labels = "UofC IP", "Akamai Node", "NTP", "Auroral", "UofC Domain", "Others",
sizes = [19444, 2, 0, 4535, 1141, 26235,]
colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'azure', 'grey']
sizeReal = []
labelsReal = []
colorsReal = []
explode = ()
for size, label, color in zip(sizes, labels, colors):
        if size != 0:
                sizeReal.append(size)
                labelsReal.append(label)
                colorsReal.append(color)

# explode = (0)*len(sizeReal)  # explode 1st slice

# Plot
#explode=explode,
plt.pie(sizeReal,  labels=labelsReal, colors=colors,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Proportion of Different Types of DNS Response with Others")
plt.axis('equal')
plt.show()