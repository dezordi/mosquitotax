# Mosquito tax

This repository store mosquito information about taxonomy 

## Dependencies

This script was build on python 3.6.5+ and have these dependencies:

- [pandas](https://pandas.pydata.org/)
- [numpy](https://numpy.org/)
- [argparse](https://docs.python.org/3/library/argparse.html)
- [seaborn](https://seaborn.pydata.org/)
- [matplotlib](https://matplotlib.org/)



## Recomended lectures
- [Mosquito Taxonomic Inventory ](http://mosquito-taxonomic-inventory.info/valid-species-list): To understand the criteria involved in this taxonomy structure
- [Recomende liteature about mosquito taxonomy ](http://mosquito-taxonomic-inventory.info/biblio): To keep up to date with this field.
- [Color palletes of seaborn ](https://medium.com/@morganjonesartist/color-guide-to-seaborn-palettes-da849406d44f): To pass with -cm argument.


## Usage
- To plot the number of species by genus in a bar plot.
> python plots.py -in mos_tax.tsv
![](img_eg/bar_plot.png)

- To plot the number of species in specific genus in a donut plot.
> python plots.py -in mos_tax.tsv -st Anopheles Culex Aedes -pt Donut -gb 1
![](img_eg/donut_plot.png)

- To get a help about the plots.py usage:
> python plots.py --help

## Interesting links about mosquitoes biology:
- [BOLDSYSTEMS ](https://www.boldsystems.org/index.php/Public_BINSearch?searchtype=records): To get barcode information;
- [VectorBase ](https://www.vectorbase.org/): To get genomes, transcriptomes, proteomes and other molecular information about mosquito and other vectors;
- [TIMETREE](http://www.timetree.org/): Put Culicidae in BUILD A TIME TREE Group to get the evolutionary tree with many information about geological scale and atmosphere levels, or just [Click here](https://itol.embl.de/tree/45462207268791593800428#) to see a cladogram of mosquitoes.


## Some considerations
If you use one of this plots, or the tsv table for some poupose, please put the correct source: plot(https://github.com/dezordi/mosquitotax), taxonomy(http://mosquito-taxonomic-inventory.info/).

All data used in these plots are recovered from [MTI](http://mosquito-taxonomic-inventory.info/sites/mosquito-taxonomic-inventory.info/files/Valid%20Species%20List_77.pdf).

## Disclaimer

- I'm not a computer engineer or some related professional, I'm just write this script to study python and to automatize some bioinformatics tasks. So fell free to commit changes that makes the code more efficient or more clean.
- This script will continue to be developed to englobe others functions, like create histograms with years of mosquito collection.