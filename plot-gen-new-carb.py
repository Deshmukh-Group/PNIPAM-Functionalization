#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 10 2024
@author: syjoshi
"""
############################################################################INITIALIZE###########################################################################################################################

#import required libraries
import numpy as np
import matplotlib.pyplot as plt
#import seaborn as sns

#create dictionary with folder names as keys and filenames as values
rdf_dict = {
    "C1-single": ["CG1-W", "carb1-W"],
    "C3-single": ["CG1-W", "carb1-W", "carb2-W", "carb3-W"],
    "C1": ["CG1-W", "carb1-W"],
    "C3": ["CG1-W", "carb1-W", "carb2-W", "carb3-W"],
    "C6": ["CG1-W", "carb1-W", "carb2-W", "carb3-W", "carb4-W", "carb5-W", "carb6-W"]
    }

rdf_dict1 = {
    "C1": ["CG1-W", "carb1-W"],
    "C3": ["CG1-W", "carb1-W", "carb2-W", "carb3-W"],
    "C6": ["CG1-W", "carb1-W", "carb2-W", "carb3-W", "carb4-W", "carb5-W", "carb6-W"]
    }

temps = [290, 295, 300, 305, 310, 315, 320, 325, 330]
dist_files = ["rad-PNI"]
evolve_files = ["rad"]
evolve_files2 = ["lig-wat-final"] #["pni","lig","both-final","pni-wat-final","lig-wat-final"]
#evolve_files2 = ["pni-wat-final","lig-wat-final","wat"]
#evolve_files2 = ["waters"]
evolve_files3 = ["dist"]

#############################################################################PLOT-RDFs###########################################################################################################################
# print("Plotting RDFs...")

# # Function to read data from a file
# def read_data(filename):
#     data = np.loadtxt(filename, skiprows=1)
#     return data[:, 0], data[:, 1]

# # Function to compute row-wise averages of two arrays
# def compute_rowwise_average(arr1, arr2):
#     return (arr1 + arr2) / 2

# # Plot average RDFs
# for fname in rdf_dict.keys():
#     for n in range(len(rdf_dict[fname])):
#         plt.figure(figsize=(10, 7), dpi=300)
#         line_colors = ['black', 'navy', 'blue', 'darkturquoise', 'green', 'gold', 'red', 'darkorange', 'purple']
#         plt.clf()
#         for i, temp in enumerate(temps):  
#             print("Plotting RDF in " + fname + " folder at " + str(temp) + "K for " + rdf_dict[fname][n] + "...")
#             file1 = "carb-Run1/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"
#             file2 = "carb-Run2/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"
#             file3 = "carb-Run3/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"

#             data1_col1, data1_col2 = read_data(file1)
#             data2_col1, data2_col2 = read_data(file2)
#             data3_col1, data3_col2 = read_data(file3)
            
#             # Compute row-wise averages
#             avg_col1 = compute_rowwise_average(data1_col1, compute_rowwise_average(data2_col1, data3_col1))
#             avg_col2 = compute_rowwise_average(data1_col2, compute_rowwise_average(data2_col2, data3_col2))
            
#             # Compute standard deviation
#             std_col1 = np.std([data1_col1, data2_col1, data3_col1], axis=0)
#             std_col2 = np.std([data1_col2, data2_col2, data3_col2], axis=0)
            
#             # Plot mean line
#             plt.plot(avg_col1, avg_col2, label=str(temp) + "K", linewidth=1.5, color=line_colors[i])
            
#             # Plot shaded region for standard deviation
#             #plt.fill_between(avg_col1, avg_col2 - std_col2, avg_col2 + std_col2, alpha=0.2, color=line_colors[i], edgecolor=None)
        
#         # Make plot frames thicker
#         plt.gca().spines['left'].set_linewidth(2.0)
#         plt.gca().spines['bottom'].set_linewidth(2.0)
#         plt.gca().spines['right'].set_linewidth(2.0)
#         plt.gca().spines['top'].set_linewidth(2.0)
        
#         # Make x and y axes labels and ticks larger and bold
#         plt.xlabel("Distance (Å)", fontsize=30, fontweight='bold')
#         plt.ylabel("g(r)", fontsize=30, fontweight='bold')
#         plt.xticks(fontsize=20)
#         plt.yticks(fontsize=20)
#         plt.xlim(0, 25)
#         #plt.ylim(0.1, 0.3)
#         #plt.set_yticks(range(0, 20, 5))
        
#         # Define a list for legends and colors of each line in the plot
#         #legend_labels = [str(temp) + "K" for temp in temps]
#         plt.tight_layout()
#         plt.savefig("rdf_" + rdf_dict[fname][n] + "_" + fname + ".png", dpi=300)

#############################################################################PLOT-RDFs-Zoomed###########################################################################################################################
# print("Plotting RDFs...")

# # Function to read data from a file
# def read_data(filename):
#     data = np.loadtxt(filename, skiprows=1)
#     return data[:, 0], data[:, 1]

# # Function to compute row-wise averages of two arrays
# def compute_rowwise_average(arr1, arr2):
#     return (arr1 + arr2) / 2

# # Plot average RDFs
# for fname in rdf_dict.keys():
#     for n in range(len(rdf_dict[fname])):
#         plt.figure(figsize=(10, 7), dpi=300)
#         line_colors = ['black', 'navy', 'blue', 'darkturquoise', 'green', 'gold', 'red', 'darkorange', 'purple']
#         plt.clf()
#         for i, temp in enumerate(temps):  
#             print("Plotting RDF in " + fname + " folder at " + str(temp) + "K for " + rdf_dict[fname][n] + "...")
#             file1 = "carb-Run1/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"
#             file2 = "carb-Run2/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"
#             file3 = "carb-Run3/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"

#             data1_col1, data1_col2 = read_data(file1)
#             data2_col1, data2_col2 = read_data(file2)
#             data3_col1, data3_col2 = read_data(file3)
            
#             # Compute row-wise averages
#             avg_col1 = compute_rowwise_average(data1_col1, compute_rowwise_average(data2_col1, data3_col1))
#             avg_col2 = compute_rowwise_average(data1_col2, compute_rowwise_average(data2_col2, data3_col2))
            
#             # Compute standard deviation
#             std_col1 = np.std([data1_col1, data2_col1, data3_col1], axis=0)
#             std_col2 = np.std([data1_col2, data2_col2, data3_col2], axis=0)
            
#             # Plot mean line
#             plt.plot(avg_col1, avg_col2, label=str(temp) + "K", linewidth=5, color=line_colors[i])
            
#             # Plot shaded region for standard deviation
#             #plt.fill_between(avg_col1, avg_col2 - std_col2, avg_col2 + std_col2, alpha=0.2, color=line_colors[i], edgecolor=None)
        
#         # Make plot frames thicker
#         plt.gca().spines['left'].set_linewidth(2.0)
#         plt.gca().spines['bottom'].set_linewidth(2.0)
#         plt.gca().spines['right'].set_linewidth(2.0)
#         plt.gca().spines['top'].set_linewidth(2.0)
        
#         # Make x and y axes labels and ticks larger and bold
#         plt.xlabel("", fontsize=30, fontweight='bold')
#         plt.ylabel("", fontsize=30, fontweight='bold')
#         plt.xticks(fontsize=30)
#         plt.yticks(fontsize=30)
#         plt.xlim(4.0, 5.2)
#         #plt.set_xticks(range(4.2, 5.2, 0.5))
#         plt.ylim(0.7, 1.0)
#         #plt.set_yticks(range(0.7, 1.0, 0.1))
        
#         # Define a list for legends and colors of each line in the plot
#         #legend_labels = [str(temp) + "K" for temp in temps]
#         plt.tight_layout()
#         plt.savefig("rdf_zoomed_" + rdf_dict[fname][n] + "_" + fname + ".png", dpi=300)
#         plt.close()

#############################################################################PLOT- RDF_subplots###########################################################################################################################
# print("Plotting RDF subplots...")

# #Function to read data from a file
# def read_data(filename):
#     data = np.loadtxt(filename, skiprows=1)
#     return data[:, 0], data[:, 1]

# #function to compute row-wise averages of two arrays
# def compute_rowwise_average(arr1, arr2):
#     return (arr1 + arr2) / 2

# # Plot average evolutions
# for fname in rdf_dict.keys():
#     for n in range(len(rdf_dict[fname])):
#         fig = plt.figure(figsize=(20, 15), dpi=300)
#         gs = fig.add_gridspec(3, 3, hspace=0.05, wspace=0.05)
#         (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = gs.subplots(sharex='col', sharey='row')
#         line_colors = ['black', 'navy', 'blue', 'darkturquoise', 'green', 'gold', 'red', 'darkorange', 'purple']
#         for i, temp in enumerate(temps):  
#             print("Plotting RDF in " + fname + " folder at " + str(temp) + "K for " + rdf_dict[fname][n] + "...")
#             file1 = "30-5-Run1/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"
#             file2 = "30-5-Run2/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"
#             file3 = "30-5-Run3/" + fname + "/" + str(temp) + "K/" + rdf_dict[fname][n] + ".dat"

#             data1_col1, data1_col2 = read_data(file1)
#             data2_col1, data2_col2 = read_data(file2)
#             data3_col1, data3_col2 = read_data(file3)
            
#             # Compute row-wise averages
#             avg_col1 = compute_rowwise_average(data1_col1, compute_rowwise_average(data2_col1, data3_col1))
#             avg_col2 = compute_rowwise_average(data1_col2, compute_rowwise_average(data2_col2, data3_col2))
            
#             # Compute standard deviation
#             std_col1 = np.std([data1_col1, data2_col1, data3_col1], axis=0)
#             std_col2 = np.std([data1_col2, data2_col2, data3_col2], axis=0)
            
#             # Plot evolution in subplots
#             for j, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]):
#                 if i == j:
#                     ax.plot(avg_col1, avg_col2, label=str(temp) + "K", linewidth=1.5, color=line_colors[i], zorder=10)
#                     ax.fill_between(avg_col1, avg_col2 - std_col2, avg_col2 + std_col2, alpha=0.2, color=line_colors[i], edgecolor=None)
#                     #ax.text(0.05, 0.95, f"({chr(97+j)})", transform=ax.transAxes, fontsize=32, fontweight='bold', va='top', ha='left')
#                     ax.text(0.95, 0.10, str(temp) + "K", transform=ax.transAxes, fontsize=20, va='top', ha='right')
                
#                 # Make plot frames thicker
#                 ax.spines['left'].set_linewidth(2.5)
#                 ax.spines['bottom'].set_linewidth(2.5)
#                 ax.spines['right'].set_linewidth(2.5)
#                 ax.spines['top'].set_linewidth(2.5)
                
#                 #ax.set_xlim(4, 6)
#                 ax.set_xticks(range(0, 25, 5))
#                 #ax.set_ylim(0.7, 1.5)
                    
#                 # Add vertical and horizontal lines at x and ytick locations
#                 for ele_X in ax.get_xticks().tolist():
#                     ax.axvline(x=ele_X, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
#                 for ele_Y in ax.get_yticks().tolist():
#                     ax.axhline(y=ele_Y, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
                
#         plt.tight_layout()
#         plt.savefig("rdf_subplots_" + rdf_dict[fname][n] + "_" + fname + ".png", dpi=300)
#         #plt.show()


#############################################################################PLOT-DIST###########################################################################################################################
print("Plotting distributions...")

#Function to read data from a file
def read_data(filename):
    data = np.loadtxt(filename, skiprows=1)
    return data[:, 1]

#Plot property distributions for Rg and SASA
for fname in rdf_dict.keys():
    for n in range(len(dist_files)):
        plt.figure(figsize=(10, 7), dpi=300)
        line_colors = ['black', 'navy', 'blue', 'darkturquoise', 'green', 'gold', 'red', 'darkorange', 'purple']
        plt.clf()
        for i, temp in enumerate(temps):  
            print("Plotting distribution in " + fname + " folder at " + str(temp) + "K for " + dist_files[n] + "...")
            file1 = "carb-Run1/" + fname + "/" + str(temp) + "K/" + dist_files[n] + ".dat"
            file2 = "carb-Run2/" + fname + "/" + str(temp) + "K/" + dist_files[n] + ".dat"
            file3 = "carb-Run3/" + fname + "/" + str(temp) + "K/" + dist_files[n] + ".dat"

            data1 = read_data(file1)
            data2 = read_data(file2)
            data3 = read_data(file3)
            data = np.concatenate((data1, data2, data3))

            mean_data = np.mean(data); std_data = np.std(data)
            print("Mean:", mean_data)
            print("Standard Deviation:", std_data)

            #plot violin plot for data
            violin_parts = plt.violinplot(data, positions=[temp], widths=4, showmeans=True, showmedians=False, showextrema=False)
            #add dot in place of line for the mean
            plt.plot(temp, mean_data, 'D', color='black', markersize=4, zorder=10)
            plt.setp(violin_parts['bodies'], facecolor=line_colors[i], alpha=0.5)
            plt.setp(violin_parts['bodies'], edgecolor=line_colors[i] , linewidth=2)
            plt.setp(violin_parts['cmeans'], color='black', linewidth=1)
            plt.text(temp, 22, f"{np.mean(data):.2f}", fontsize=15, fontweight='bold', ha='center', va='center', color='white', bbox=dict(facecolor='grey', edgecolor='black', boxstyle='round,pad=0.3', alpha=1.0, linewidth=1.5))
            plt.axvline(x=temp, color='black', linestyle='dashed', linewidth=0.5)
        
        if dist_files[n] == "rad-PNI":
            #plt.axhline(y=15, color='black', linestyle='dashed', linewidth=1)
            #plt.text(333, 15.25, "Transition Line", fontsize=10, fontweight='bold', rotation='vertical', va='baseline')
            plt.ylim(8, 22)
            plt.ylabel("Radius of Gyration (Å)", fontsize=30, fontweight='bold')
        else:
            plt.ylabel("Solvent Accessible Surface Area (Å²)", fontsize=25, fontweight='bold')

        # Make plot frames thicker
        plt.gca().spines['left'].set_linewidth(2.0)
        plt.gca().spines['bottom'].set_linewidth(2.0)
        plt.gca().spines['right'].set_linewidth(2.0)
        plt.gca().spines['top'].set_linewidth(2.0)
        
        # Make x and y axes labels and ticks larger and bold
        plt.xlabel("Temperature (K)", fontsize=30, fontweight='bold')
        plt.xticks(fontsize=20)
        plt.yticks(fontsize=20)
        plt.tight_layout()

        #plt.savefig(dist_files[n] + "_" + fname + ".png", dpi=300)

# #############################################################################PLOT-EVOLVE###########################################################################################################################
# print("Plotting evolution 1...")

# #Function to read data from a file
# def read_data(filename):
#     data = np.loadtxt(filename, skiprows=1)
#     return data[:, 1]

# #function to compute row-wise averages of two arrays
# def compute_rowwise_average(arr1, arr2):
#     return (arr1 + arr2) / 2

# # Plot average evolutions
# for fname in rdf_dict.keys():
#     for n in range(len(evolve_files)):
#         fig = plt.figure(figsize=(20, 15), dpi=300)
#         gs = fig.add_gridspec(3, 3, hspace=0.05, wspace=0.05)
#         (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = gs.subplots(sharex='col', sharey='row')
#         line_colors = ['black', 'navy', 'blue', 'darkturquoise', 'green', 'gold', 'red', 'darkorange', 'purple']
#         for i, temp in enumerate(temps):  
#             print("Plotting evolution in " + fname + " folder at " + str(temp) + "K for " + evolve_files[n] + "...")
#             file1 = "carb-Run1/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files[n] + ".dat"
#             file2 = "carb-Run2/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files[n] + ".dat"
#             file3 = "carb-Run3/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files[n] + ".dat"

#             data1 = read_data(file1)
#             data2 = read_data(file2)
#             data3 = read_data(file3)
            
#             # Compute row-wise averages and standard deviations
#             avg_col1 = compute_rowwise_average(data1, compute_rowwise_average(data2, data3))
#             std_col1 = np.std([data1, data2, data3], axis=0)
            
#             # Plot evolution in subplots
#             for j, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]):
#                 if i == j:
#                     ax.plot(avg_col1, label=str(temp) + "K", linewidth=3, color=line_colors[i], markeredgecolor='black')
#                     ax.fill_between(range(len(avg_col1)), avg_col1 - std_col1, avg_col1 + std_col1, alpha=0.4, color=line_colors[i], edgecolor='None')
#                     #ax.text(0.05, 0.95, f"({chr(97+j)})", transform=ax.transAxes, fontsize=32, fontweight='bold', va='top', ha='left')
#                     ax.text(0.95, 0.95, str(temp) + "K", transform=ax.transAxes, fontsize=20, va='top', ha='right')
                
#                 # Make plot frames thicker
#                 ax.spines['left'].set_linewidth(2.5)
#                 ax.spines['bottom'].set_linewidth(2.5)
#                 ax.spines['right'].set_linewidth(2.5)
#                 ax.spines['top'].set_linewidth(2.5)
                
#                 if evolve_files[n] == "rad":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(8, 22)
#                     ax.set_yticks(range(8, 22, 4))
                    
#                 # Add vertical and horizontal lines at x and ytick locations
#                 for ele_X in ax.get_xticks().tolist():
#                     ax.axvline(x=ele_X, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
#                 for ele_Y in ax.get_yticks().tolist():
#                     ax.axhline(y=ele_Y, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
                
        
#         plt.tight_layout()
#         plt.savefig(evolve_files[n] + "_" + fname + ".png", dpi=300)
#         plt.show()

#############################################################################PLOT-EVOLVE###########################################################################################################################
# print("Plotting evolution 2...")

# #Function to read data from a file
# def read_data(filename):
#     data = np.loadtxt(filename)
#     return data

# #function to compute row-wise averages of two arrays
# def compute_rowwise_average(arr1, arr2):
#     return (arr1 + arr2) / 2

# # Plot average evolutions
# for fname in rdf_dict1.keys():
#     for n in range(len(evolve_files2)):
#         fig = plt.figure(figsize=(20, 15), dpi=300)
#         gs = fig.add_gridspec(3, 3, hspace=0.05, wspace=0.05)
#         (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = gs.subplots(sharex='col', sharey='row')
#         line_colors = ['black', 'navy', 'blue', 'darkturquoise', 'green', 'gold', 'red', 'darkorange', 'purple']
#         for i, temp in enumerate(temps):  
#             print("Plotting evolution in " + fname + " folder at " + str(temp) + "K for " + evolve_files2[n] + "...")
#             file1 = "carb-Run1/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files2[n] + ".dat"
#             file2 = "carb-Run2/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files2[n] + ".dat"
#             file3 = "carb-Run3/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files2[n] + ".dat"

#             data1 = read_data(file1)
#             data2 = read_data(file2)
#             data3 = read_data(file3)
            
#             # Compute row-wise averages and standard deviations
#             avg_col1 = compute_rowwise_average(data1, compute_rowwise_average(data2, data3))
#             std_col1 = np.std([data1, data2, data3], axis=0)
            
#             # Plot evolution in subplots
#             for j, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]):
#                 if i == j:
#                     ax.plot(avg_col1, label=str(temp) + "K", linewidth=3, color=line_colors[i], markeredgecolor='black')
#                     ax.fill_between(range(len(avg_col1)), avg_col1 - std_col1, avg_col1 + std_col1, alpha=0.4, color=line_colors[i], edgecolor='None')
#                     #ax.text(0.05, 0.95, f"({chr(97+j)})", transform=ax.transAxes, fontsize=32, fontweight='bold', va='top', ha='left')
#                     ax.text(0.95, 0.95, str(temp) + "K", transform=ax.transAxes, fontsize=20, va='top', ha='right')
                
#                 # Make plot frames thicker
#                 ax.spines['left'].set_linewidth(2.5)
#                 ax.spines['bottom'].set_linewidth(2.5)
#                 ax.spines['right'].set_linewidth(2.5)
#                 ax.spines['top'].set_linewidth(2.5)
                
#                 if evolve_files2[n] == "pni":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(-125, -65)
#                     ax.set_yticks(range(-125, -65, 15))
#                 elif evolve_files2[n] == "lig":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(-120, 10)
#                     ax.set_yticks(range(-120, 10, 30))
#                 elif evolve_files2[n] == "both-final":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(-100, 0)
#                     ax.set_yticks(range(-150, 0, 30))
#                 elif evolve_files2[n] == "waters":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(0, 80)
#                     ax.set_yticks(range(0, 80, 20))
#                 elif evolve_files2[n] == "pni-wat-final":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(160000, 190000)
#                     ax.set_yticks(range(160000, 190000, 6000))
#                 elif evolve_files2[n] == "lig-wat-final":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(160000, 190000)
#                     ax.set_yticks(range(160000, 190000, 6000))
                    
#                 # Add vertical and horizontal lines at x and ytick locations
#                 for ele_X in ax.get_xticks().tolist():
#                     ax.axvline(x=ele_X, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
#                 for ele_Y in ax.get_yticks().tolist():
#                     ax.axhline(y=ele_Y, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
        
#         plt.tight_layout()
#         plt.savefig(evolve_files2[n] + "_" + fname + ".png", dpi=300)
#         plt.close()

#############################################################################PLOT-EVOLVE###########################################################################################################################
# print("Plotting evolution 3...")

# #Function to read data from a file
# def read_data(filename):
#     data = np.loadtxt(filename, skiprows=1)
#     return data[:, 1]

# #function to compute row-wise averages of two arrays
# def compute_rowwise_average(arr1, arr2):
#     return (arr1 + arr2) / 2

# # Plot average evolutions
# for fname in rdf_dict1.keys():
#     for n in range(len(evolve_files3)):
#         fig = plt.figure(figsize=(20, 15), dpi=300)
#         gs = fig.add_gridspec(3, 3, hspace=0.05, wspace=0.05)
#         (ax1, ax2, ax3), (ax4, ax5, ax6), (ax7, ax8, ax9) = gs.subplots(sharex='col', sharey='row')
#         line_colors = ['black', 'navy', 'blue', 'darkturquoise', 'green', 'gold', 'red', 'darkorange', 'purple']
#         for i, temp in enumerate(temps):  
#             print("Plotting evolution in " + fname + " folder at " + str(temp) + "K for " + evolve_files3[n] + "...")
#             file1 = "carb-Run1/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files3[n] + ".dat"
#             file2 = "carb-Run2/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files3[n] + ".dat"
#             file3 = "carb-Run3/" + fname + "/" + str(temp) + "K/Energy/" + evolve_files3[n] + ".dat"

#             data1 = read_data(file1)
#             data2 = read_data(file2)
#             data3 = read_data(file3)
            
#             # Compute row-wise averages and standard deviations
#             avg_col1 = compute_rowwise_average(data1, compute_rowwise_average(data2, data3))
#             std_col1 = np.std([data1, data2, data3], axis=0)
            
#             # Plot evolution in subplots
#             for j, ax in enumerate([ax1, ax2, ax3, ax4, ax5, ax6, ax7, ax8, ax9]):
#                 if i == j:
#                     ax.plot(avg_col1, label=str(temp) + "K", linewidth=3, color=line_colors[i], markeredgecolor='black')
#                     ax.fill_between(range(len(avg_col1)), avg_col1 - std_col1, avg_col1 + std_col1, alpha=0.4, color=line_colors[i], edgecolor='None')
#                     #ax.text(0.05, 0.95, f"({chr(97+j)})", transform=ax.transAxes, fontsize=32, fontweight='bold', va='top', ha='left')
#                     ax.text(0.95, 0.95, str(temp) + "K", transform=ax.transAxes, fontsize=20, va='top', ha='right')
                
#                 # Make plot frames thicker
#                 ax.spines['left'].set_linewidth(2.5)
#                 ax.spines['bottom'].set_linewidth(2.5)
#                 ax.spines['right'].set_linewidth(2.5)
#                 ax.spines['top'].set_linewidth(2.5)
                
#                 if evolve_files3[n] == "dist":
#                     ax.set_xlim(0, 99)
#                     ax.set_xticks(range(0, 100, 20))
#                     ax.tick_params(axis='both', which='major', labelsize=20)
#                     ax.set_ylim(0, 79)
#                     ax.set_yticks(range(0, 80, 20))
                    
#                 # Add vertical and horizontal lines at x and ytick locations
#                 for ele_X in ax.get_xticks().tolist():
#                     ax.axvline(x=ele_X, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
#                 for ele_Y in ax.get_yticks().tolist():
#                     ax.axhline(y=ele_Y, color='grey', linestyle='dashed', linewidth=0.8, alpha=0.8)
        
#         plt.tight_layout()
#         plt.savefig(evolve_files3[n] + "_" + fname + ".png", dpi=300)