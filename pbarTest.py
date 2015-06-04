#pbar test
from progressbar import *

pbar1 = ProgressBar(widgets=[Percentage(), Bar()], maxval=15).start()
pbar2 = ProgressBar(widgets=[Percentage(), Bar()], maxval=300).start()

for i in range(15):
	time.sleep(.01)
	pbar1.update(i+1)
	for j in range(300):
		time.sleep(.01)
		pbar2.update(j+1)