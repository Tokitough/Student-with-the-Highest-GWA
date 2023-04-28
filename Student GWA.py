# Read a file
with open("GWA.txt") as file:
    # Initialize lowest possible gwa and name
    gwa_value = 5.00
    highest_student = ""
     # Read file line by line
    for line in file: 
        # Split name and gwa
        name, gwa_str = line.strip().split("-")
        # If gwa is lower than initialized gwa, take the highest gwa and name
        gwa = float(gwa_str)
        if gwa < gwa_value:
            gwa_value = gwa
            highest_student = name
# Print the student who got the highest GWA
print("\033[95mThe student with the highest GWA is " + highest_student + "with a GWA of " + str(gwa_value))