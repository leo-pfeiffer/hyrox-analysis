import os
import glob
import pandas as pd


def merge_csv_files(input_dir, output_file):
    """
    Merges all CSV files in the given directory into a single CSV.

    Parameters:
    - input_dir (str): Path to the directory containing CSV files.
    - output_file (str): Path for the merged output CSV file.
    """
    # Find all CSV files in the directory
    csv_pattern = os.path.join(input_dir, '*.csv')
    csv_files = glob.glob(csv_pattern)

    if not csv_files:
        print(f"No CSV files found in directory: {input_dir}")
        return

    # Read and concatenate all CSVs
    df_list = [pd.read_csv(csv) for csv in csv_files]
    combined_df = pd.concat(df_list, ignore_index=True)

    # Save the merged DataFrame to a new CSV
    combined_df.to_csv(output_file, index=False)
    print(f"Merged {len(csv_files)} files into {output_file}")


if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description="Merge CSV files in a directory into one CSV.")
    parser.add_argument("input_dir", help="Directory containing CSV files to merge")
    parser.add_argument("output_file", help="Output path for the merged CSV file")
    args = parser.parse_args()

    merge_csv_files(args.input_dir, args.output_file)
