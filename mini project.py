import pandas as pd

# Load the data from the Excel sheet
candidate_data = pd.read_excel(r"""./candidate_data.xlsx""")

# Iterate through each row of the data
for index, row in candidate_data.iterrows():
    # Check if the candidate has scored less than 85% in any subject
    if (row.iloc[2:8] < 80).any():
        print( row['Name'], "is not eligible for any job interview.")
        print("Links to improve their scores:")
        print("- Coursera: https://www.coursera.org/")
        print("- Udemy: https://www.udemy.com/")    
        print("- Unacademy: https://unacademy.com/")
        print("Links for practice:")
        print("- GeeksforGeeks: https://www.geeksforgeeks.org/")
        print("- VSCode Playground: https://code.visualstudio.com/playgrounds")
        print("Open LinkedIn and GitHub profiles to get recommendations.")
        print("\n\n")
    else:
        # Check if the candidate has scored above 90% in Engineering Mathematics and Data Structures Using C
        if (row["Engineering Mathematics"] >= 97) and (row["Data Structures using C"] >= 95):
            print(row['Name'], "is eligible for Data Science.")
            print("Recommended resource: FreeCodeCamp YouTube channel - https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print("\n\n")
        # Check if the candidate has scored above 90% in Engineering Mathematics and DBMS
        elif (row["Engineering Mathematics"] >= 90) and (row["DBMS"] >= 90):
            print( row['Name'], "is eligible for Database.")
            print("Recommended resource: FreeCodeCamp YouTube channel - https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print("\n\n")
        # Check if the candidate has scored above 90% in AI and AI
        elif (row["Artificial Intelligence"] >= 90) and (row["Machine Learning"] >= 90):
            print( row['Name'], "is eligible for AI.")
            print("Recommended resource: FreeCodeCamp YouTube channel - https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print("\n\n")
        # Check if the candidate has scored above 90% in AI and DBMS
        elif (row["Machine Learning"] >= 90) and (row["DBMS"] >= 90):
            print( row['Name'], "is eligible for Machine Learning.")
            print("Recommended resource: FreeCodeCamp YouTube channel - https://www.youtube.com/channel/UC8butISFwT-Wl7EV0hUK0BQ")
            print("\n\n")
        # Check if the candidate has scored above 90% in Engineering Mathematics and Digital Electronics for AI
        elif (row["Engineering Mathematics"] >= 90) and (row["Digital Electronics for AI"] >= 90):
            print( row['Name'], "is eligible for UI/UX Design and Web Development.")
            print("Recommended resource: FreeCodeCamp YouTube channel - https://www.youtube.com/channel/UC8")
            print("\n\n") 

while True:
    name = input("Enter a name to search or type STOP to exit: ")
    if(name=='STOP'):
        break
    result = candidate_data.loc[candidate_data['Name'] == name]
    row_data = candidate_data.index[candidate_data['Name'] == name]
    row = candidate_data.iloc[row_data]
    if name in candidate_data['Name'].values:
        eligibility = ''
        if ((result.iloc[:,2:8] < 85).any().any()):
            eligibility = row['Name'] + " is not eligible for any job interview."
        else:
            if (result["Engineering Mathematics"] >= 97).any() and (result["Data Structures using C"] >= 95).any():
                eligibility = result['Name'] + " is eligible for Data Science."
            elif (result["Engineering Mathematics"] >= 90).any() and (result["DBMS"] >= 90).any():
                eligibility = result['Name'] + " is eligible for Database."
            elif (result["Artificial Intelligence"] >= 90).any() and (result["Machine Learning"] >= 90).any():
                eligibility = result['Name'] +" is eligible for AI."
            elif (result["Machine Learning"] >= 90).any and (result["DBMS"] >= 90).any():
                eligibility = result['Name']+ " is eligible for Machine Learning."
            elif (result["Engineering Mathematics"] >= 90).any() and (result["Digital Electronics for AI"] >= 90).any():
                eligibility = result['Name']+ " is eligible for UI/UX Design and Web Development."
        print(eligibility)
    else:
        print("Name Does Not Exist In Directory")