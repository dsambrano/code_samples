import pylab
import scipy
text = '''Deshawn Loves Crystal
the MOSTEST!!!!
Happy V day
Baby!!'''
x = scipy.linspace(-2,2,1000)
y1 = scipy.sqrt(1-(abs(x)-1)**2)
y2 = -3*scipy.sqrt(1-(abs(x)/2)**0.5)
pylab.fill_between(x, y1, color='#5900b3')
pylab.fill_between(x, y2, color='#5900b3')
pylab.xlim([-2.5, 2.5])
pylab.ylim([-3.1, 1.1])
pylab.text(0,-1.3, text, fontsize=24, fontweight='bold',
           color='white', horizontalalignment='center')
pylab.savefig('heart.png')

