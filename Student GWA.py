# Read a file
with open("GWA.txt") as file:
    # Initialize lowest possible gwa and name
    gwa_value = 5.00
    highest_student = ""
     # read file line by line
    for line in file: 
        # split name and gwa
        name, gwa_str = line.strip().split("-")