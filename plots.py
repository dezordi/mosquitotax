#!/usr/bin/python3
# -*- coding: utf-8 -*-
###############################>GENERAL-INFORMATIONS<###############################
"""
Build in Python 3.6.5+

Author:
Filipe Dezordi
zimmer.filipe@gmail.com
https://dezordi.github.io/

"""
###############################>LIBRARIES<###############################
import pandas as pd
import numpy as np
import argparse, re
import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.style as style
from matplotlib.colors import ListedColormap


###############################>ARGUMENTS<###############################
parser = argparse.ArgumentParser(description = 'Create beeswarm plots of .tax files')
parser.add_argument("-in", "--input", help="TSV file (mos_tax.tsv)", required=True)
parser.add_argument("-md","--mode",help="Create plots about Genus, Subgenus, Specie or Year? default = Genus",default='Genus', choices=['Genus','Subgenus','Specie','Year'])
parser.add_argument("-st","--specifictax",help="Pass specific taxon to generate plots, e.g. Aedes Culex",nargs='+')
parser.add_argument("-pt","--plottype",help="Choose the type of graph, default = Bar",default='Bar', choices=['Donut','Bar','Hist'])
parser.add_argument("-gb","--groupby",help="Treshold value to group taxon in 'Others' category, default = 30",default = int(30), type=int)
parser.add_argument("-cm","--colormap",help="Choose seaborn colors, default=rainbow",default='rainbow')
args = parser.parse_args()
input_file = args.input
plot_mode = args.mode
plot_type = args.plottype
specific_tax = args.specifictax
group_by = args.groupby
color_palette = args.colormap
###############################>SNS-STYLE<###############################
sns.set(style="ticks")
my_cmap = ListedColormap(sns.color_palette(color_palette))
###############################>Functions<###############################
def taxonomy_distribuition(tsv_file,plot_type):
    if plot_type == 'Bar':
        tax_count = df[plot_mode].value_counts()
        df2 = pd.DataFrame(tax_count)
        df2.columns = ['Number']
        bar_plot =sns.barplot(x=df2.index.values, y='Number', data=df2,palette=color_palette)
        sns.despine(fig=None, top=True, right=True, left=False, bottom=False, offset=None, trim=False)
        bar_plot.set_ylabel('Number of species')
        bar_plot.set_xlabel(plot_mode)
        bar_plot.set_xticklabels(bar_plot.get_xticklabels(),rotation=90)
        bar_plot.annotate('Sources: plot(https://github.com/dezordi/mosquitotax), taxonomy(http://mosquito-taxonomic-inventory.info/).', xy=(1, 0), xycoords='axes fraction', fontsize=6, xytext=(0, 265), textcoords='offset points',ha='right', va='top')
        plt.savefig(input_file+'.bar_plot.pdf',dpi=300,bbox_inches='tight')
        plt.clf()
    if plot_type == 'Donut':
        tax_count = df[plot_mode].value_counts()
        df2 = pd.DataFrame(tax_count)
        df2.columns = ['Number']
        my_circle=plt.Circle((0,0), 0.5, color='white')
        donut_plot = df2.plot.pie(y='Number', cmap = my_cmap,radius=1.7,labels=None)
        donut_plot.set_ylabel('')
        df2.reset_index(level=0, inplace=True)
        list_ = [df2.columns.values.tolist()] + df2.values.tolist()
        labels_list = [''.join(str(x)) for x in list_]
        del labels_list[0]
        labels = []
        for i in labels_list:
            i = re.sub(r"\['",'',i)
            i = re.sub(r"', ",'  ',i)
            i = re.sub(r"\]",'',i)
            labels.append(i)
        donut_plot.legend(loc='center left', bbox_to_anchor=(1.2, 0.5), ncol=1, fancybox=True, prop={'size': 12},title=plot_mode+' and Nº species', labels=labels)
        donut_plot.annotate('Sources: plot(https://github.com/dezordi/mosquitotax), taxonomy(http://mosquito-taxonomic-inventory.info/).', xy=(1, 0), xycoords='axes fraction', fontsize=8, xytext=(30, -65), textcoords='offset points',ha='right', va='top')
        p=plt.gcf()
        p.gca().add_artist(my_circle)
        plt.savefig(input_file+'.donut_plot.pdf',dpi=300,bbox_inches='tight')
        plt.clf()
    if plot_type == "Hist":
        df.dropna(inplace=True)
        df['Year'].loc[(df['Year'] <= 1800)] = 1800
        df['Year'].loc[(df['Year'] > 1800) & (df['Year'] <= 1850)] = 1850
        df['Year'].loc[(df['Year'] > 1850) & (df['Year'] <= 1900)] = 1900
        data = df['Year'].tolist()
        data = list(map(int, data))
        dist_plot = sns.distplot(data)
        plt.savefig(input_file+'.hist_plot.pdf',dpi=300,bbox_inches='tight')
        plt.clf()



if __name__ == '__main__':
    '''
    Main Routine
    This block of code is executed, whenever the script
    is started from the command line.
    '''

    ###############################>DATAFRAME<###############################
    df = pd.read_csv(input_file, sep='\t',header = 0)
    if specific_tax != None:
        df = df.loc[df[plot_mode].isin(specific_tax)]
    tax_count = df[plot_mode].value_counts()
    tax_low= tax_count[tax_count <= group_by]
    tax_low_list = tax_low.index
    for i in tax_low_list:
        df[plot_mode] = df[plot_mode].replace({i:'Others'})

    taxonomy_distribuition(input_file,plot_type)