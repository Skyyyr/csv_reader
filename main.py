import csv

# A variable to stop the loop
end = False
# While you haven't found a proper file to open
while end == False:
    # Wait for the user to input what type of animal they would like to inquire about
    user_input = input("What type of animal would you like to inquire about today?\n")
    # Concat the user input to the proper file type
    file_to_open = "data/" + user_input + ".csv"
    # Try to open it
    try:
        with open(file_to_open, newline='') as file:
            # We use the dictionary reader to pull our headers to use
            csv_reader = csv.DictReader(file, skipinitialspace=True)
            # For the rows in the file
            for row in csv_reader:
                # Output the data in a readable way
                print(f"{row['name']} is a {row['age']} year old {row['breed']}")
            # Close the file
            file.close()
            # We found the file, and output the proper data so stop looping
            end = True
    # We failed to open it, let's let the user know and repeat
    except:
        print(f"We don't have {user_input} today.")
