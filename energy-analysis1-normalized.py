import pandas as pd
import os

# Define the folder structure
replicas = ['30-5-Run1', '30-5-Run2', '30-5-Run3']
folders = ['D5-D5', 'G5-G5', 'L5-L5']
temps = ['290K/Energy', '295K/Energy', '300K/Energy', '305K/Energy', '310K/Energy', 
         '315K/Energy', '320K/Energy', '325K/Energy', '330K/Energy']
         
normalization_factors = {
	'D5-D5': {'lig': 9.80, 'pni': 45, 'both-final': 9.80},
	'G5-G5': {'lig': 5, 'pni': 45, 'both-final': 5},
	'L5-L5': {'lig': 8.75, 'pni': 45, 'both-final': 8.75}
	}

# List to store the results
results = []

# Loop through each folder and temperature to analyze data across replicas
for folder in folders:
    for temp in temps:
        combined_df = []

        # Loop through each replica for the current folder and temperature
        for replica in replicas:
            # Path to the current folder/replica/temperature combination
            path = os.path.join(replica, folder, temp)
            file_names = ['lig.dat', 'pni.dat', 'both-final.dat']
            data = {}

            # Read each data file in the current path
            for file_name in file_names:
                file_path = os.path.join(path, file_name)
                data[file_name.split('.')[0]] = pd.read_csv(file_path, header=None, names=[file_name.split('.')[0]])

            # Concatenate the data into a single DataFrame for this replica
            df = pd.concat(data.values(), axis=1)

            # Process dist.dat file
            dist_file_path = os.path.join(path, 'dist.dat')
            dist_data = pd.read_csv(dist_file_path, delim_whitespace=True, header=None, skiprows=1, names=['col1', 'dist']).iloc[:99, 1]
            df['dist'] = dist_data.reset_index(drop=True)
            
            # Append the DataFrame for this replica to the combined list
            combined_df.append(df)

        # Concatenate all DataFrames from the three replicas into one combined DataFrame
        final_df = pd.concat(combined_df, ignore_index=True)
        
        # Normalize the specified columns based on the current folder
        norm_factors = normalization_factors[folder]
        final_df['lig'] /= norm_factors['lig']
        final_df['pni'] /= norm_factors['pni']
        final_df['both-final'] /= norm_factors['both-final']

        # Define columns of interest for statistics calculation
        columns_of_interest = ['pni', 'lig', 'both-final']

        # Separate data based on the 'dist' column condition
        dist_below_12 = final_df[final_df['dist'] < 12]
        dist_above_12 = final_df[final_df['dist'] > 12]

        # Calculate mean and standard deviation for each column of interest for dist < 12
        for col in columns_of_interest:
            mean_below = dist_below_12[col].mean()
            std_below = dist_below_12[col].std()
            results.append({'Folder': folder, 'Temperature': temp, 'Condition': 'dist < 12', 
                            'Column': col, 'Mean': mean_below, 'Std Dev': std_below})

        # Calculate mean and standard deviation for each column of interest for dist > 12
        for col in columns_of_interest:
            mean_above = dist_above_12[col].mean()
            std_above = dist_above_12[col].std()
            results.append({'Folder': folder, 'Temperature': temp, 'Condition': 'dist > 12', 
                            'Column': col, 'Mean': mean_above, 'Std Dev': std_above})

# Convert results to a DataFrame
results_df = pd.DataFrame(results)

# Define the column ordering to group by folder
folders_conditions = []
for folder in folders:
    folders_conditions.extend([f"{folder} dist > 12", f"{folder} dist < 12"])

energy_types = ['pni', 'lig', 'both-final']
# Create tables with the updated column ordering
for energy in energy_types:
    # Initialize an empty DataFrame for the current energy type
    table = pd.DataFrame(index=temps, columns=folders_conditions)

    # Populate the table with mean ± std values
    for temp in temps:
        for folder in folders:
            for condition in ['dist > 12', 'dist < 12']:
                # Filter data for the current combination
                condition_data = results_df[
                    (results_df['Column'] == energy) &
                    (results_df['Folder'] == folder) &
                    (results_df['Temperature'] == temp) &
                    (results_df['Condition'] == condition)
                ]

                if not condition_data.empty:
                    # Extract mean and std values
                    mean = condition_data['Mean'].values[0]
                    std = condition_data['Std Dev'].values[0]

                    # Format as mean ± std
                    formatted_value = f"{mean:.2f} ± {std:.2f}"

                    # Add to the table
                    table.loc[temp, f"{folder} {condition}"] = formatted_value

    # Save the table to a CSV file
    table.to_csv(f"{energy}_summary_table.csv", sep=' ', index_label='Temperature')
    print(f"Table for {energy}:")
    print(table)

print("END")
