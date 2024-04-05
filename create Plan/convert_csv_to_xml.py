import pandas as pd
import matsim
import datetime
import gzip


def convert_time(start_time):
    # Format the time as "HH:MM:SS"
    time_str = start_time.strftime("%H:%M:%S")
    start_hours, minutes, seconds = map(int, time_str.split(':'))

    # Calculate the total number of seconds since midnight
    start_time = start_hours * 3600 + minutes * 60 + seconds

    return start_time

def main():
    # Read the CSV file into a chunk DataFrame
    csv_file_path = r"transformed_data.csv"
    data = pd.read_csv(csv_file_path, usecols=[0, 5, 6, 7, 8, 9, 10], header=None, skiprows=1,
                       chunksize=1000)

    # Prepare to write the XML file
    with gzip.open("plans_new1.xml.gz", 'wb+') as f_write:
        writer = matsim.writers.PopulationWriter(f_write)
        writer.start_population()

        progress_counter = 0  # Initialize progress counter

        for chunk in data:
            chunk.columns = ['id', 'mode', 'time','start_lon', 'start_lat', 'end_lon', 'end_lat']
            df = pd.DataFrame(chunk)


            grouped = df.groupby('id')

            for person_id, group in grouped:
                # Start writing the person
                writer.start_person(person_id)

                # Write the person's data
                start_lat = group.iloc[0]['start_lat']
                start_lon = group.iloc[0]['start_lon']
                end_lat = group.iloc[-1]['end_lat']
                end_lon = group.iloc[-1]['end_lon']
                start_time = convert_time(datetime.datetime.fromtimestamp(group.iloc[0]['time']))
                travel_mode = group.iloc[-1]['mode']

                writer.start_plan(selected=True)

                # add activity for start location
                writer.add_activity(type='trip', x=start_lon,
                                    y=start_lat,
                                    end_time=start_time)


                if travel_mode == 'Walking':
                    travel_mode = 'walk'
                elif travel_mode == 'Car':
                    travel_mode = 'car'
                elif travel_mode == 'Motorcycle':
                    travel_mode = 'bike'
                elif travel_mode == 'Tuktuk':
                    travel_mode = 'other'


                # Add leg
                writer.add_leg(mode=travel_mode)

                # Add activity for end location
                writer.add_activity(type='end', x=end_lon,
                                    y=end_lat,
                                    end_time=start_time)



                writer.end_plan()
                writer.end_person()

                # Increment progress counter
                progress_counter += 1

                # Print progress after every 10000 persons
                if progress_counter % 10000 == 0:
                    print(f"Processed {progress_counter} persons.")


        # End writing the population
        writer.end_population()


if __name__ == "__main__":
    main()
