from pylab import figure, plot, savefig, barh, axis, xlabel, ylabel, title, yticks
inf = open('neuron_data.txt')
ydata = []
for line in inf:
	ydata.append(float(line.strip()))

xdata = [x for x in range(1, len(ydata) + 1)]
figure()
barh(xdata, ydata)
yticks(xdata)
#axis([ 0, 500, 0, 10])
title('neuron length fig')
ylabel('sample')
xlabel('neuron length of sample')
savefig('neuron.png', dpi = 300)