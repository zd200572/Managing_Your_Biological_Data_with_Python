from pylab import figure, plot, text, axis, savefig, title, xlabel, ylabel, legend


nucleotides = ['A', 'T', 'G', 'U']
x1 = [2.0, 4.0, 6.0, 8.0]
x2 = [x -0.5 for x in x1]
ydata = [[606, 1024, 759, 398], 
		 [762, 912, 639, 591]]
xticks = (nucleotides)

figure()
plot(x1, ydata[0], 'rd', label = 'E.coli 23S')
plot(x2, ydata[1], 'go', label = 'Thermophilus 23S')
title('RNA nucleotides in the ribosome')
xlabel('RNA')
ylabel('base count')
legend()
savefig('plot_of_ATGU.png', dpi = 300)