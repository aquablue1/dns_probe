import matplotlib.pyplot as plt

# Data to plot

labels = "UofC IP", "Akamai Node", "NTP", "Auroral", "UofC Domain", "Others",
sizes = [4147, 0, 0, 39, 670, 25543,]
colorsDict = {"UofC IP":'gold', "Akamai Node":'yellowgreen',
              "NTP":'lightcoral', "Auroral":'lightskyblue',
              "UofC Domain":'azure', "Others":'grey'}
sizeReal = []
labelsReal = []
colorsReal = []
explode = ()
for size, label in zip(sizes, labels):
        if size != 0:
                sizeReal.append(size)
                labelsReal.append(label)
                colorsReal.append(colorsDict[label])

# explode = (0)*len(sizeReal)  # explode 1st slice

# Plot
#explode=explode,
plt.pie(sizeReal,  labels=labelsReal, colors=colorsReal,
        autopct='%1.1f%%', shadow=True, startangle=140)
plt.title("Proportion of Different Types of DNS Response with Others")
plt.axis('equal')
plt.show()