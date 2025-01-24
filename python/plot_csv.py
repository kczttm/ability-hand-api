from csvReader import *
import matplotlib.pyplot as plt
import argparse

"""
Plot CSV files in the format generated by the PPP unstuffing plotter/logger, if the csv
and print to console options are used. 
"""


if __name__ == "__main__":
	parser = argparse.ArgumentParser(description='Plot rt-plotter-sdl csv files')
	parser.add_argument('--name', type=str, help="filename", default='log.csv')
	args=parser.parse_args()


	data = read_csv(args.name,'\n')
	fdata,names = format_csv(data)


	time = fdata[len(fdata)-1]  #copy out time vector, which all other lines are referenced to
	fdata = fdata[0:len(fdata)-1]   #remove last element which is always time in milliseconds


	fig,ax =  plt.subplots()
	for i, fd in enumerate(fdata):
		ax.plot(time,np.array(fd), label=names[i])
		ax.set_xlabel('time (s)')
		ax.set_ylabel('Value')
	handles, labels = ax.get_legend_handles_labels()
	ax.legend(handles, labels)

	plt.show()


