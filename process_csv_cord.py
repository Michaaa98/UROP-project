import pandas as pd
import numpy as np
import pyproj

def wgs84_to_utm48n_chunk(chunk):
    # Define WGS84 and UTM48N projections
    src_crs = "EPSG:4326"  # WGS84
    target_crs = "EPSG:32648"  # UTM zone 48N (Phenom Phen)

    # create transform object
    transformer = pyproj.Transformer.from_crs(src_crs, target_crs, always_xy=True)

    # Extract coordinates
    start_lat = chunk['start_lat'].values
    start_lon = chunk['start_lon'].values
    end_lat = chunk['end_lat'].values
    end_lon = chunk['end_lon'].values

    # Perform the coordinate transformation
    start_x, start_y = transformer.transform(start_lon, start_lat)
    end_x, end_y = transformer.transform(end_lon, end_lat)

    # create new columns in dataframe containing the new coordinates
    chunk['start_x'] = start_x
    chunk['start_y'] = start_y
    chunk['end_x'] = end_x
    chunk['end_y'] = end_y

    return chunk

def main():
    csv_file_path = r"C:\Users\miche\OneDrive - Singapore University of Technology and Design\03.18 - ML Generated Data for Simulation - Method 1 Version 1\Activity Plan - Method 1 Combined.csv"

    chunk_size = 10000

    # list to store transformed chunks
    transformed_chunks = []

    # Read the CSV file in chunks
    for chunk in pd.read_csv(csv_file_path, usecols=[0, 1, 2, 3, 4, 8, 9], header=None, skiprows=1, chunksize=chunk_size):
        # Rename columns for clarity
        chunk.columns = ['id', 'start_lat', 'start_lon', 'end_lat', 'end_lon', 'mode', 'time']
        # Apply coordinate transformation to the chunk
        transformed_chunk = wgs84_to_utm48n_chunk(chunk)
        transformed_chunks.append(transformed_chunk)

    # concatenate all transformed chunks into a single DataFrame
    transformed_data = pd.concat(transformed_chunks)


    # Save transformed data to CSV
    output_csv_path = "transformed_data.csv"
    transformed_data.to_csv(output_csv_path, index=False)
    print(f"Transformed data saved to {output_csv_path}")

if __name__ == "__main__":
    main()
