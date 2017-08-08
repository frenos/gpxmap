import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import argparse
from xml.dom import minidom
from sys import argv

def plotFiles(filename, attribute, outputfilename):
    plt.title(attribute + ' over time')
    plt.xlabel('datapoint')
    plt.ylabel(attribute)

    xml = minidom.parse(filename)

    plotvalues = []
    for trkpt in xml.getElementsByTagName('trkpt'):
        plotvalues.append(trkpt.getElementsByTagName(attribute)[0].firstChild.nodeValue)
    plt.plot(plotvalues, label=filename)
    plt.legend()

    plt.savefig(outputfilename)
    plt.close()

    return outputfilename