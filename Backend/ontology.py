from owlready2 import *
from datetime import *


#onto = get_ontology("C:\\Users\\darsh\\OneDrive\\Desktop\\CBES\\GIT-Web-Scraper-ontology-and-flask\\GIT-Web-Scraper-ontology-and-flask\\backend\\web_scraper_onto_5_11_23.owx").load()
onto = get_ontology(r"C:\Users\admin\OneDrive\Desktop\Component Based Soft Enterprise\GIT-Web-Scraper-main\backend\web_scraper_onto_5_11_23.owx").load()

# Language Properties
Prop_C = "C"
Prop_C_Plus_Plus = "C_Plus_Plus"
Prop_C_Sharp = "C_Sharp"



# License Properties

Prop_Academic_Free_License_v3_0 = "Academic_Free_License_v3_0"
Prop_Apache_License_2_0 = "Apache_License_2_0"
Prop_Artistic_License_2_0 = "Artistic_License_2_0"
Prop_BSD_2_Clause_Simplified_License = "BSD_2_Clause_Simplified_License"
Prop_BSD_3_Clause_Clear_License = "BSD_3_Clause_Clear_License"
Prop_BSD_3_Clause_New_or_Revised_License = "BSD_3_Clause_New_or_Revised_License"
Prop_BSD_4_Clause_Original_or_Old_License = "BSD_4_Clause_Original_or_Old_License"
Prop_BSD_License = "BSD_License"
Prop_BSD_Zero_Clause_License = "BSD_Zero_Clause_License"
Prop_Boost_Software_License_1_0 = "Boost_Software_License_1_0"
Prop_CERN_License = "CERN_License"
Prop_CERN_Open_Hardware_Licence_Version_2_Permissive = "CERN_Open_Hardware_Licence_Version_2_Permissive"
Prop_CERN_Open_Hardware_Licence_Version_2_Strongly_Reciprocal = "CERN_Open_Hardware_Licence_Version_2_Strongly_Reciprocal"
Prop_CERN_Open_Hardware_Licence_Version_2_Weakly_Reciprocal = "CERN_Open_Hardware_Licence_Version_2_Weakly_Reciprocal"
Prop_CeCILL_Free_Software_License_Agreement_v2_1 = "CeCILL_Free_Software_License_Agreement_v2_1"
Prop_Creative_Commons_Attribution_4_0_International = "Creative_Commons_Attribution_4_0_International"
Prop_Creative_Commons_Attribution_Share_Alike_4_0_International = "Creative_Commons_Attribution_Share_Alike_4_0_International"
Prop_Creative_Commons_License = "Creative_Commons_License"
Prop_Creative_Commons_Zero_v1_0_Universal = "Creative_Commons_Zero_v1_0_Universal"
Prop_Do_What_The_Fuck_You_Want_To_Public_License = "Do_What_The_Fuck_You_Want_To_Public_License"
Prop_Eclipse_Public_License = "Eclipse_Public_License"
Prop_Eclipse_Public_License_1_0 = "Eclipse_Public_License_1_0"
Prop_Eclipse_Public_License_2_0 = "Eclipse_Public_License_2_0"
Prop_Educational_Community_License_v2_0 = "Educational_Community_License_v2_0"
Prop_European_Union_Public_License = "European_Union_Public_License"
Prop_European_Union_Public_License_1_1 = "European_Union_Public_License_1_1"
Prop_European_Union_Public_License_1_2 = "European_Union_Public_License_1_2"
Prop_GNU_Affero_General_Public_License_v3_0 = "GNU_Affero_General_Public_License_v3_0"
Prop_GNU_Free_Documentation_License_v1_3 = "GNU_Free_Documentation_License_v1_3"
Prop_GNU_General_Public_License = "GNU_General_Public_License"
Prop_GNU_General_Public_License_v2_0 = "GNU_General_Public_License_v2_0"
Prop_GNU_General_Public_License_v3_0 = "GNU_General_Public_License_v3_0"
Prop_GNU_Lesser_General_Public_License = "GNU_Lesser_General_Public_License"
Prop_GNU_Lesser_General_Public_License_v2_1 = "GNU_Lesser_General_Public_License_v2_1"
Prop_GNU_Lesser_General_Public_License_v3_0 = "GNU_Lesser_General_Public_License_v3_0"
Prop_GNU_License = "GNU_License"
Prop_ISC_License = "ISC_License"
Prop_LaTeX_Project_Public_License_v1_3c = "LaTeX_Project_Public_License_v1_3c"
Prop_MIT_License = "MIT_License"
Prop_MIT_No_Attribution = "MIT_No_Attribution"
Prop_Microsoft_License = "Microsoft_License"
Prop_Microsoft_Public_License = "Microsoft_Public_License"
Prop_Microsoft_Reciprocal_License = "Microsoft_Reciprocal_License"
Prop_Mulan_Permissive_Software_License_Version_2 = "Mulan_Permissive_Software_License_Version_2"
Prop_Open_Data_Commons_Open_Database_License_v1_0 = "Open_Data_Commons_Open_Database_License_v1_0"
Prop_Open_Software_License_3_0 = "Open_Software_License_3_0"
Prop_PostgreSQL_License = "PostgreSQL_License"
Prop_SIL_Open_Font_License_1_1 = "SIL_Open_Font_License_1_1"
Prop_The_Unlicense = "The_Unlicense"
Prop_Universal_Permissive_License_v1_0 = "Universal_Permissive_License_v1_0"
Prop_University_of_Illinois__NCSA_Open_Source_License = "University_of_Illinois__NCSA_Open_Source_License"
Prop_Vim_License = "Vim_License"
Prop_zlib_License = "zlib_License"
Prop_No_License = "No_License"

all_licenses = [Prop_Academic_Free_License_v3_0,
Prop_Apache_License_2_0,
Prop_Artistic_License_2_0,
Prop_BSD_2_Clause_Simplified_License,
Prop_BSD_3_Clause_Clear_License,
Prop_BSD_3_Clause_New_or_Revised_License,
Prop_BSD_4_Clause_Original_or_Old_License,
Prop_BSD_License,
Prop_BSD_Zero_Clause_License,
Prop_Boost_Software_License_1_0,
Prop_CERN_License,
Prop_CERN_Open_Hardware_Licence_Version_2_Permissive,
Prop_CERN_Open_Hardware_Licence_Version_2_Strongly_Reciprocal,
Prop_CERN_Open_Hardware_Licence_Version_2_Weakly_Reciprocal,
Prop_CeCILL_Free_Software_License_Agreement_v2_1,
Prop_Creative_Commons_Attribution_4_0_International,
Prop_Creative_Commons_Attribution_Share_Alike_4_0_International,
Prop_Creative_Commons_License,
Prop_Creative_Commons_Zero_v1_0_Universal,
Prop_Do_What_The_Fuck_You_Want_To_Public_License,
Prop_Eclipse_Public_License,
Prop_Eclipse_Public_License_1_0,
Prop_Eclipse_Public_License_2_0,
Prop_Educational_Community_License_v2_0,
Prop_European_Union_Public_License,
Prop_European_Union_Public_License_1_1,
Prop_European_Union_Public_License_1_2,
Prop_GNU_Affero_General_Public_License_v3_0,
Prop_GNU_Free_Documentation_License_v1_3,
Prop_GNU_General_Public_License,
Prop_GNU_General_Public_License_v2_0,
Prop_GNU_General_Public_License_v3_0,
Prop_GNU_Lesser_General_Public_License,
Prop_GNU_Lesser_General_Public_License_v2_1,
Prop_GNU_Lesser_General_Public_License_v3_0,
Prop_GNU_License,
Prop_ISC_License ,
Prop_LaTeX_Project_Public_License_v1_3c,
Prop_MIT_License,
Prop_MIT_No_Attribution,
Prop_Microsoft_License,
Prop_Microsoft_Public_License,
Prop_Microsoft_Reciprocal_License,
Prop_Mulan_Permissive_Software_License_Version_2 ,
Prop_Open_Data_Commons_Open_Database_License_v1_0,
Prop_Open_Software_License_3_0,
Prop_PostgreSQL_License,
Prop_SIL_Open_Font_License_1_1,
Prop_The_Unlicense,
Prop_Universal_Permissive_License_v1_0,
Prop_University_of_Illinois__NCSA_Open_Source_License,
Prop_Vim_License,
Prop_zlib_License]

# Stars Properties
Prop_no_Stars = "no_Stars"
Prop_around_5_Stars = "around_5_Stars"
Prop_around_10_Stars = "around_10_Stars"
Prop_around_25_Stars = "around_25_Stars"
Prop_around_50_Stars = "around_50_Stars"
Prop_around_100_Stars = "around_100_Stars"
Prop_around_250_Stars = "around_250_Stars"
Prop_around_500_Stars = "around_500_Stars"
Prop_around_750_Stars = "around_750_Stars"
Prop_around_1000_Stars = "around_1000_Stars"
Prop_around_1500_Stars = "around_1500_Stars"
Prop_over_2000_Stars = "over_2000_Stars"

# Last Modified Range Properties
Prop_Today = "Today"
Prop_Yesterday = "Yesterday"
Prop_This_Week = "This_Week"
Prop_Week_Ago = "Week_Ago"
Prop_2_Weeks_Ago = "Two_Weeks_Ago"
Prop_Month_Ago = "Month_Ago"
Prop_2_Months_Ago = "Two_Months_Ago"
Prop_4_Months_Ago = "Four_Months_Ago"
Prop_6_Months_Ago = "Six_Months_Ago"
Prop_10_Months_Ago = "Ten_Months_Ago"
Prop_Year_Ago = "Year_Ago"
Prop_Over_A_Year_Ago = "Over_A_Year_Ago"
Prop_Over_2_Years_Ago = "Over_Two_Years_Ago"
Prop_No_LastModified = "No_LastModified"

# with onto:
#     sync_reasoner()

def clear_onto():
    count = 0
    for proj in onto.Project.instances():
        destroy_entity(proj)
        count += 1
    print(str(count) + " projects destroyed")
    
'''
create_project()
    @params:
        String title, String owner, String language, List<String> licenses, 
        int num_stars, datetime last_modified_date
        
    @returns:
        Success:
            - Project individual successully created
            - prints success message to console
        Fail:
            - No Project individual created
            - prints error message to console
Ex function call:
    create_project(title="This Project", owner="Connor", language=Prop_C, licenses=["BSD_License", "MIT_License"], num_stars=100, last_modified_date=datetime(2023, 4, 30))

'''
def create_project(title, owner, language, licenses, num_stars, last_modified_date):

    #onto = get_ontology("file:///Users/connornorton/Desktop/Python Workspace 2023/Web Scraper Ontology /web_scraper_ontology.owx").load()
    #with onto:

        my_project = onto.Project(title.replace(" ", "_"))
        
        my_project.title = str(title)
        
        my_project.owner = str(owner)
        
        my_project.hasLanguage = getattr(onto, language)
        
        for lic in licenses:
            my_project.hasLicense.append(getattr(onto, lic))
            #print("Added license: " + str(lic))
            
        my_project.has_Stars = num_stars
        
        my_project.has_Date_LastModified = last_modified_date
        set_last_modified_range(onto, my_project)
        
        return my_project
# end create_project()

def sync_ontology_updates():
    with onto:
        sync_reasoner()


def set_last_modified_range(onto, project):
    
    if project.has_Date_LastModified == None:
        print("This project has no last modified date")
        project.hasLastModifiedAge = onto.No_LastModified
        project.has_Age_LastModified = 0
        #print("Project set to No Last Modified")
        return
    # Get today's date and time
    now = datetime.now()

    lm_date = datetime.combine(project.has_Date_LastModified, datetime.min.time())
    
    d = lm_date - datetime.now()
    num_days = d.days
    #print(abs(num_days))
    
    if num_days > 0:
        print("invalid date")
    elif abs(num_days) == 1:
        project.hasLastModifiedAge = onto.Today_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified Today")
    elif abs(num_days) in range(1, 3): 
        project.hasLastModifiedAge = onto.Yesterday_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified Yesterday")
    elif abs(num_days) in range(3, 8): 
        project.hasLastModifiedAge = onto.This_Week_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified This Week")
    elif abs(num_days) in range(8, 14):
        project.hasLastModifiedAge = onto.Week_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified Last Week")
    elif abs(num_days) in range(14, 23):
        project.hasLastModifiedAge = onto.Two_Weeks_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified 2 Weeks Ago")
    elif abs(num_days) in range(23, 38): 
        project.hasLastModifiedAge = onto.Month_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified This Month")
    elif abs(num_days) in range(38, 78):
        project.hasLastModifiedAge = onto.Two_Months_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified 2 Months Ago")
    elif abs(num_days) in range(78, 138):
        project.hasLastModifiedAge = onto.Four_Months_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified 4 Months ago")
    elif abs(num_days) in range(138, 231):
        project.hasLastModifiedAge = onto.Six_Months_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified 6 Months ago")
    elif abs(num_days) in range(231, 352):
        project.hasLastModifiedAge = onto.Ten_Months_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified 10 Months ago")
    elif abs(num_days) in range(352, 372):
        project.hasLastModifiedAge = onto.Year_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified a year ago")
    elif abs(num_days) in range(372, 731):
        project.hasLastModifiedAge = onto.Over_A_Year_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified Over a Year ago")
    elif abs(num_days) in range(731, 741):
        project.hasLastModifiedAge = onto.Two_Years_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified 2 Years ago")
    elif abs(num_days) > 740:
        project.hasLastModifiedAge = onto.Over_Two_Years_Ago_LastModified
        project.has_Age_LastModified = abs(num_days)
        #print("Project set to Last Modified Over 2 Years ago")
    else:
        print("Failed to set Last Modified Age Range")
    
# end of set_last_modified_range(onto, project)

# TODO: method to convert a individual and its properties to a string
def toString(proj):
    return "Title: " + str(proj.title) + "\nOwner: " + str(proj.owner) + "\nLanguage: " + str(proj.hasLanguage.name) + "\nLicense(s): " + str([lic.name for lic in proj.hasLicense]) + "\nStars: " + str(proj.has_Stars) + "\nLast Modified Date: " + str(proj.has_Date_LastModified) + "\nDays since last modification: " + str(proj.has_Age_LastModified) + "\nLast Modified Date Range: " + str(proj.hasLastModifiedAge.name)

'''
get_individuals_Project_WithLanguage(verbosity=1, lang=None):
- Returns a list of the titles of the projects that match the criteria

    @params and returns:
        verbosity: (default = 0)
            if set to 0, only returns the titles of the projects
            if set to 1, prints the IRI name and titles of each project and then returns the titles as a list
            if set to 2, calls & the toString() for each project and then returns the titles as a list
        lang: (default = None)
            if set to None, returns all Projects that belong to the Project_WithLanguage class
            if set to Prop_C, returns all Projects that belong to the Project_InC class
            if set to Prop_C_Plus_Plus, returns all Projects that belong to the Project_InC_Plus_Plus class
            if set to Prop_C_Sharp, returns all Projects that belong to the Project_InC_Sharp class
    notes:
        Verbosity of 2 needs debugging


Must run reasoner before calling or will return empty
'''
def get_individuals_Project_WithLanguage(verbosity=0, lang=None):
    
    if lang is None:
        if onto.Project_WithStars is not None:
            individuals = [ind.name for ind in onto.Project_WithLanguage.instances()]
            if verbosity == 0:
                return individuals
            elif verbosity == 1:
                for ind in onto.Project_WithLanguage.instances():
                    print(ind.name + " - " + ind.title)
                return individuals   
            elif verbosity == 2: 
                for ind in onto.Project_WithLanguage.instances():
                    print(toString(ind))
                return individuals
            else:
                return individuals
        else:
            return []
    elif lang == Prop_C:
        if onto.Project_InC is not None:
            individuals = [ind.name for ind in onto.Project_InC.instances()]
            
            if verbosity == 0:
                return individuals
            elif verbosity == 1:
                for ind in onto.Project_WithLanguage.instances():
                    print(ind.name + " - " + ind.title)
                return individuals   
            elif verbosity == 2: 
                for ind in onto.Project_WithLanguage.instances():
                    print(toString(ind))
                return individuals
            else:
                return individuals
        else:
            return []
        
    elif lang == Prop_C_Plus_Plus:
        if onto.Project_InC_Plus_Plus is not None:
            individuals = [ind.name for ind in onto.Project_InC_Plus_Plus.instances()] 
            
            if verbosity == 0:
                return individuals
            elif verbosity == 1:
                for ind in onto.Project_WithLanguage.instances():
                    print(ind.name + " - " + ind.title)
                return individuals   
            elif verbosity == 2: 
                for ind in onto.Project_WithLanguage.instances():
                    print(toString(ind))
                return individuals
            else:
                return individuals
        else:
            return []
        
    elif lang == Prop_C_Sharp:
        if onto.Project_inC_Sharp is not None:
            individuals = [ind.name for ind in onto.Project_InC_Sharp.instances()]
            
            if verbosity == 0:
                return individuals
            elif verbosity == 1:
                for ind in onto.Project_WithLanguage.instances():
                    print(ind.name + " - " + ind.title)
                return individuals   
            elif verbosity == 2: 
                for ind in onto.Project_WithLanguage.instances():
                    print(toString(ind))
                return individuals
            else:
                return individuals
        else:
            return []
    else:
        print("Invalid lang parameter")
        return
# end of get_individuals_Project_WithLanguage()
 
#print(get_individuals_Project_WithLanguage(verbosity=0, lang=None))

list_ambiguous_licenses = { "GNU_General_Public_License_v2_0", "GNU_General_Public_License_v3_0", "GNU_Lesser_General_Public_License_v2_1", "GNU_Lesser_General_Public_License_v3_0"}
def get_individuals_Project_WithLicense(verbosity=0, license_value = None):


    if license_value is None:
       individuals = [ind.name for ind in onto.Project_WithLicense.instances()]
       if verbosity == 0:
           return individuals
       elif verbosity == 1:
           for ind in onto.Project_WithLicense.instances():
               print(ind.name + " - " + ind.title)
           return individuals  
       elif verbosity == 2:
           for ind in onto.Project_WithLicense.instances():
               print(toString(ind))
           return individuals
       else:
           return individuals
    else:
        if license_value in list_ambiguous_licenses:
            license_value = Prop_GNU_General_Public_License
        lic = "Project_With" + license_value
        individuals = [ind for ind in (getattr(onto, lic)).instances()]
        if individuals is None:
            print("No projects present with license " + license_value)
            return
        else:
            print("Trying to fetch this license detail: " + license_value)
            if verbosity == 0:
                return [project.name for project in individuals]
            elif verbosity == 1:
                  for project in individuals:
                      print(project.name + " - " + project.title)
                  return [project.name for project in individuals]
            elif verbosity == 2:
                for project in individuals:
                    print(toString(project))
                return [project.name for project in individuals]
            else:
                return [project.name for project in individuals]
            
            
# print(get_individuals_Project_WithLicense(verbosity=0, license_value=Prop_GNU_Lesser_General_Public_License_v2_1))

'''
get_individuals_Project_WithStars(verbosity=1, star_range=None):
- Returns a list of the titles of the projects that match the criteria

    @params and returns:
        verbosity: (default = 0)
            if set to 0, only returns the titles of the projects
            if set to 1, prints the IRI name and title of each project AND then returns the titles as a list
            if set to 2, calls & the toString() for each project and then returns the titles as a list
        star_range: (default = None)
            if set to None, returns all Projects that belong to the Project_WithStars class
            if set to Prop_xxxxx, returns all Projects that belong to the Project_With_Prop_xxxxx
    notes:
        - Verbosity of 2 needs debugging
        - Must run reasoner before calling or will return empty
'''
def get_individuals_Project_WithStars(verbosity=0, star_range=None):
        if star_range is None:
            if onto.Project_WithStars is not None:
                individuals = [ind.name for ind in onto.Project_WithStars.instances()]
                
                if verbosity == 0:
                    return individuals
                elif verbosity == 1:
                    for ind in onto.Project_WithStars.instances():
                        print(ind.name + " - " + ind.title)
                    return individuals   
                elif verbosity == 2: 
                    for ind in onto.Project_WithStars.instances():
                        print(toString(ind))
                    return individuals
                else:
                    return individuals
            else:
                return []
        else:
            prop = "Project_With_" + star_range
            if getattr(onto, prop) is not None:   
                individuals = [ind for ind in (getattr(onto, prop)).instances()]
                if verbosity == 0:
                    return individuals
                elif verbosity == 1:
                    for ind in prop.instances():
                        print(ind.name + " - " + ind.title)
                    return individuals   
                elif verbosity == 2: 
                    for ind in prop.instances():
                        print(toString(ind))
                    return individuals
                else:
                    return individuals
            else:
                return []

# end of get_individuals_Project_WithStars()
 
'''
get_individuals_Project_WithLastModified(verbosity=1, last_modified_range=None):
- Returns a list of the titles of the projects that match the criteria

    @params and returns:
        verbosity: (default = 0)
            if set to 0, only returns the titles of the projects
            if set to 1, prints the IRI name and title of each project AND then returns the titles as a list
            if set to 2, calls & the toString() for each project and then returns the titles as a list
        last_modified_range: (default = None)
            if set to None, returns all Projects that belong to the Project_WithStars class
            if set to Prop_xxxxx, returns all Projects that belong to the Project_LastModified_Prop_xxxxx
    notes:
        - Verbosity of 2 needs debugging
        - Must run reasoner before calling or will return empty
'''
def get_individuals_Project_WithLastModified(verbosity=0, last_modified_range=None):
        if last_modified_range is None:
            if onto.Project_WithLastModified is not None:
                individuals = [ind.name for ind in onto.Project_WithLastModified.instances()]
                
                if verbosity == 0:
                    return individuals
                elif verbosity == 1:
                    for ind in onto.Project_WithStars.instances():
                        print(ind.name + " - " + ind.title)
                    return individuals   
                elif verbosity == 2: 
                    for ind in onto.Project_WithStars.instances():
                        print(toString(ind))
                    return individuals
                else:
                    return individuals
            else:
                return []
        else:
            prop = "Project_LastModified_" + last_modified_range
            if getattr(onto, prop) is not None:   
                individuals = [ind for ind in (getattr(onto, prop)).instances()]
                if verbosity == 0:
                    return individuals
                elif verbosity == 1:
                    for ind in prop.instances():
                        print(ind.name + " - " + ind.title)
                    return individuals   
                elif verbosity == 2: 
                    for ind in prop.instances():
                        print(toString(ind))
                    return individuals
                else:
                    return individuals
            else:
                return []

# end of get_individuals_Project_WithStars()
 

# Sample Project Creation for testing
c = create_project(title="Sample Project 1", owner="Connor", language=Prop_C, licenses=["MIT_License"], num_stars=3000, last_modified_date=datetime(2023, 5, 10))
destroy_entity(c)
d = create_project(title="Sample Project 2", owner="Darshil", language=Prop_C_Plus_Plus, licenses=["GNU_General_Public_License"], num_stars=2000, last_modified_date=datetime(2023, 5, 4))
destroy_entity(d)
e =  create_project(title="Sample Project 3", owner="Luke", language=Prop_C_Sharp, licenses=[Prop_BSD_2_Clause_Simplified_License], num_stars=1251, last_modified_date=datetime(2023, 5, 1))
destroy_entity(e)
f = create_project(title="Sample Project 4", owner="Luke", language=Prop_C_Sharp, licenses=[Prop_GNU_General_Public_License_v3_0], num_stars=1251, last_modified_date=datetime(2023, 5, 1))
destroy_entity(f)
g = create_project(title="Sample Project 5", owner="Luke", language=Prop_C_Sharp, licenses=[Prop_GNU_Lesser_General_Public_License_v3_0], num_stars=1251, last_modified_date=datetime(2023, 5, 1))
destroy_entity(g)
h = create_project(title="Sample Project 6", owner="Luke", language=Prop_C_Sharp, licenses=[Prop_Microsoft_Public_License], num_stars=1251, last_modified_date=datetime(2023, 5, 1))
destroy_entity(h)
z = create_project(title="Sample Project 7", owner="Luke", language=Prop_C_Sharp, licenses=[Prop_PostgreSQL_License], num_stars=1251, last_modified_date=datetime(2023, 5, 1))

# create_project(title="Sample Project 1", owner="Connor", language=Prop_C, licenses=[Prop_GNU_Lesser_General_Public_License, Prop_Academic_Free_License_v3_0], num_stars=3000, last_modified_date=datetime(2023, 5, 5))
# create_project(title="Sample Project 2", owner="Darshil", language=Prop_C_Plus_Plus, licenses=[Prop_GNU_License], num_stars=2000, last_modified_date=datetime(2023, 5, 4))
# create_project(title="Sample Project 3", owner="Luke", language=Prop_C_Sharp, licenses=[Prop_MIT_License], num_stars=1251, last_modified_date=datetime(2023, 5, 1))
# create_project(title="Sample Project 4", owner="Rishab", language=Prop_C, licenses=[Prop_BSD_License], num_stars=1000, last_modified_date=datetime(2023, 4, 25))
# create_project(title="Sample Project 5", owner="Renato", language=Prop_C, licenses=[Prop_Creative_Commons_License], num_stars=750, last_modified_date=datetime(2023, 4, 20))
# create_project(title="Sample Project 6", owner="Connor", language=Prop_C_Plus_Plus, licenses=[Prop_Academic_Free_License_v3_0, Prop_GNU_Affero_General_Public_License_v3_0], num_stars=520, last_modified_date=datetime(2023, 4, 4))
# create_project(title="Sample Project 7", owner="Darshil", language=Prop_C_Plus_Plus, licenses=[Prop_GNU_License], num_stars=250, last_modified_date=datetime(2023, 3, 4))
# create_project(title="Sample Project 8", owner="Luke", language=Prop_C_Sharp, licenses=[Prop_MIT_License, Prop_Artistic_License_2_0], num_stars=100, last_modified_date=datetime(2023, 1, 4))
# create_project(title="Sample Project 9", owner="Rishab", language=Prop_C, licenses=[Prop_BSD_License, Prop_Boost_Software_License_1_0], num_stars=50, last_modified_date=datetime(2022, 11, 10))
# create_project(title="Sample Project 10", owner="Renato", language=Prop_C_Plus_Plus, licenses=[Prop_GNU_General_Public_License_v3_0], num_stars=25, last_modified_date=datetime(2022, 7, 10))
# create_project(title="Sample Project 11", owner="Charles", language=Prop_C_Sharp, licenses=[Prop_MIT_License, Prop_Artistic_License_2_0, Prop_CERN_Open_Hardware_Licence_Version_2_Permissive], num_stars=10, last_modified_date=datetime(2022, 5, 4))
# create_project(title="Sample Project 12", owner="Julia", language=Prop_C, licenses=[Prop_BSD_3_Clause_Clear_License, Prop_Educational_Community_License_v2_0, Prop_GNU_Free_Documentation_License_v1_3], num_stars=4, last_modified_date=datetime(2022, 4, 10))
# create_project(title="Sample Project 13", owner="Andrea", language=Prop_C_Plus_Plus, licenses=[Prop_GNU_General_Public_License_v3_0, Prop_Mulan_Permissive_Software_License_Version_2, Prop_SIL_Open_Font_License_1_1], num_stars=0, last_modified_date=datetime(2021, 5, 4))
# create_project(title="Sample Project 14", owner="Doug", language=Prop_C_Sharp, licenses=[Prop_BSD_3_Clause_New_or_Revised_License, Prop_BSD_3_Clause_Clear_License], num_stars=666, last_modified_date=datetime(2019, 5, 5))


with onto:
    sync_reasoner(debug=1)
    
#print(get_individuals_Project_WithLastModified(verbosity=0, last_modified_range=Prop_Over_2_Years_Ago))
#print(get_individuals_Project_WithStars(verbosity=0, star_range=Prop_over_2000_Stars))


# TODO Make this intersection not union
'''
merge_filtered_individuals()
    - This function takes 2 lists of Project individuals and returns a single list of individual ordered according to order option chosen
    @params:
        list1, list2 - lists of Project individuals returned by a search function (get_individuals_Project......())
        order - ["by title", "by stars", "by license", "by last modified range"]
            "by title": orders projects alphabetically by title
            "by stars": orders projects from projects with most stars to projects with fewest stars
            "by license": orders projects alpabetically by their first license
            "by last modified range": orders projects by when they were last modified with the projects being modified most recently first
    @return:
        Success:
            A list of projects
        Fail:
            Prints error message to console

'''
def merge_filtered_individuals(list1, list2, order="by title"):
    # print("Type of List 1: " + str(type(list1)))
    # print("Type of List 2: " + str(type(list2)))
    
    merged_list = list1 + list2
    sorted_list = []
    if order == "by title":
        return sorted(list(set(merged_list)))
    elif order == "by stars":
        if onto.Project_With_over_2000_Stars != None:
            for proj in onto.Project_With_over_2000_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_1500_Stars != None:
            for proj in onto.Project_With_around_1500_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_1000_Stars != None:
            for proj in onto.Project_With_around_1000_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_750_Stars != None:
            for proj in onto.Project_With_around_750_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_500_Stars != None:
            for proj in onto.Project_With_around_500_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_250_Stars != None:
            for proj in onto.Project_With_around_250_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_100_Stars != None:
            for proj in onto.Project_With_around_100_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_50_Stars != None:
            for proj in onto.Project_With_around_50_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_25_Stars != None:
            for proj in onto.Project_With_around_25_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_10_Stars != None:
            for proj in onto.Project_With_around_10_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_around_5_Stars != None:
            for proj in onto.Project_With_around_5_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_With_no_Stars != None:
            for proj in onto.Project_With_no_Stars.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        return sorted_list
    elif order == "by license":
        temp_dict_store = {}
        for each_project in merged_list:
            temp_dict_store[each_project] = str(getattr(onto,each_project).hasLicense).split(".").pop()[:-1]
        sorted_dictionary = dict(sorted(temp_dict_store.items(), key=lambda item: item[1]))
        # TESTING
        # for each in sorted_dictionary:
        #     print("Project License: " + sorted_dictionary[each] + " Project: " + each)
        sorted_list = list(sorted_dictionary.keys())
        return sorted_list
    elif order == "by last modified range":
        if onto.Project_LastModified_Today != None:
            for proj in onto.Project_LastModified_Today.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Yesterday != None:
            for proj in onto.Project_LastModified_Yesterday.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_This_Week != None:
            for proj in onto.Project_LastModified_This_Week.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Week_Ago != None:
            for proj in onto.Project_LastModified_Week_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Two_Weeks_Ago != None:
            for proj in onto.Project_LastModified_Two_Weeks_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Month_Ago != None:
            for proj in onto.Project_LastModified_Month_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Two_Months_Ago != None:
            for proj in onto.Project_LastModified_Two_Months_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Four_Months_Ago != None:
            for proj in onto.Project_LastModified_Four_Months_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Six_Months_Ago != None:
            for proj in onto.Project_LastModified_Six_Months_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Ten_Months_Ago != None:
            for proj in onto.Project_LastModified_Ten_Months_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Year_Ago != None:
            for proj in onto.Project_LastModified_Year_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Over_A_Year_Ago!= None:
            for proj in onto.Project_LastModified_Over_A_Year_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Two_Years_Ago != None:
            for proj in onto.Project_LastModified_Two_Years_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        if onto.Project_LastModified_Over_Two_Years_Ago != None:
            for proj in onto.Project_LastModified_Over_Two_Years_Ago.instances():
                if proj.name in merged_list :
                    sorted_list.append(proj.name)
        return sorted_list
    else:
        print("Error with merge")
        return
# end of merge_filtered_individuals()

# Test
list3 = merge_filtered_individuals(get_individuals_Project_WithLicense(license_value = Prop_Academic_Free_License_v3_0),get_individuals_Project_WithLanguage(lang=Prop_C), order="by license")
print(list3)


print("Microsoft license: " + str(onto.Project_WithPostgreSQL_License.instances()))

# with onto:
#     sync_reasoner(debug=1)


# ________EXAMPLES OF SIMPLE QUERIES ________

# Return all projects that use C
# print(list(onto.search(hasLanguage = onto.C)))

# Return all projects that use Educational_Community_License_v2_0
# print(list(onto.search(hasLicense = onto.Educational_Community_License_v2_0)))

# Return all projects that have around 100 stars
# print(list(onto.Project_With_around_100_Stars.instances()))

# # Get the data property
# my_data_property = onto.has_Date_LastModified

# # Retrieve the individuals with the specific xsd:dateTime value
# my_individuals = [individual for individual in onto.individuals() if my_data_property[individual] == "2020-01-01T00:00:00"]

# # Print the names of the individuals
# for individual in my_individuals:
#     print(individual.name)

# Returns all projects that use C, C++, or C#
# print(list(onto.search(type = onto.Projects, hasLanguage = "*")))

# Returns all projects that use C, C++, or C#
# print(list(onto.search(type = onto.Projects, hasLanguage = "*")))

# print(list(onto.search(iri = "*Age")))
'''
[web_scraper_ontology.Month_Ago_Age, web_scraper_ontology.ProjectAge, web_scraper_ontology.Projects_WithAge, web_scraper_ontology.This_Week_Age, web_scraper_ontology.Today_Age,
web_scraper_ontology.Week_Ago_Age, web_scraper_ontology.Year_Ago_Age, web_scraper_ontology.hasAge, web_scraper_ontology.hasLastModifiedAge]
'''
#_________END: EXAMPLES OF SIMPLE QUERIES_____________

'''
Function that returns all projects that match a certain Object Property value
    @Returns:
        Success: 
            - A list of projects matching the search
            - if no projects match, returns empty list and prints message to console
        Fail:
            - Prints

Supported Object Properties include: 
    "hasLanguage"
        SUPPORTED VALUES: "C", "C_Plus_Plus", "C_Sharp"
    "hasLicense"
        SUPPORTED VALUES: {Academic_Free_License_v3_0 , Apache_License_2_0 , Artistic_License_2_0 , BSD_2_Clause_Simplified_License , BSD_3_Clause_Clear_License , BSD_3_Clause_New_or_Revised_License , 
        BSD_4_Clause_Original_or_Old_License , BSD_License , BSD_Zero_Clause_License , Boost_Software_License_1_0 , CERN_License , CERN_Open_Hardware_Licence_Version_2_Permissive , 
        CERN_Open_Hardware_Licence_Version_2_Strongly_Reciprocal , CERN_Open_Hardware_Licence_Version_2_Weakly_Reciprocal , CeCILL_Free_Software_License_Agreement_v2_1 , 
        Creative_Commons_Attribution_4_0_International , Creative_Commons_Attribution_Share_Alike_4_0_International , Creative_Commons_License , Creative_Commons_Zero_v1_0_Universal , 
        Do_What_The_Fuck_You_Want_To_Public_License , Eclipse_Public_License , Eclipse_Public_License_1_0 , Eclipse_Public_License_2_0 , Educational_Community_License_v2_0 , 
        European_Union_Public_License , European_Union_Public_License_1_1 , European_Union_Public_License_1_2 , GNU_Affero_General_Public_License_v3_0 , GNU_Free_Documentation_License_v1_3 ,
        GNU_General_Public_License , GNU_General_Public_License_v2_0 , GNU_General_Public_License_v3_0 , GNU_Lesser_General_Public_License , GNU_Lesser_General_Public_License_v2_1 ,
        GNU_Lesser_General_Public_License_v3_0 , GNU_License , ISC_License , LaTeX_Project_Public_License_v1_3c , MIT_License , MIT_No_Attribution , Microsoft_License , 
        Microsoft_Public_License , Microsoft_Reciprocal_License , Mulan_Permissive_Software_License_Version_2 , Open_Data_Commons_Open_Database_License_v1_0 , Open_Software_License_3_0 ,
        PostgreSQL_License , SIL_Open_Font_License_1_1 , The_Unlicense , Universal_Permissive_License_v1_0 , University_of_Illinois__NCSA_Open_Source_License , Vim_License , zlib_License}
'''
def find_projects_with_obj_property_x_and_value_y(onto, property, value):
    
    # hasLanguage property
    if property == "hasLanguage":        
        if(value == "C"):
            v = onto.C
        elif(value == "C_Sharp"):
            v = onto.C_Sharp
        elif(value == "C_Plus_Plus"):
            v = onto.C_Plus_Plus
        else:
            print("Invalid value parameter for hasLanguage property")
            return
        
        projects = (onto.search(hasLanguage = v))
        
        if projects is not None:
            return list(projects)
        else:
            return "no project with " + str(property) + " value of " + str(value)
    
    # hasLicense property
    if property == "hasLicense":        
        lic = getattr(onto, str(value))
        if lic != None:
            lics = list(onto.search(hasLicense = lic))
            if lics is None:
                return str([l.name for l in lics])
            else:
                return "no project with " + str(property) + " value of " + str(value)
        print("Invalid value parameter for hasLicense property")
        return
            
        
    # Return all projects that use C#
    # print(list(onto.search(hasLanguage = onto.C_Sharp)))
    
    # Return all projects that use C++
    # print(list(onto.search(hasLanguage = onto.C_Plus_Plus)))

    # Return all projects that use C
    # print(list(onto.search(hasLanguage = onto.C)))

    # Returns all projects that use C, C++, or C#
    # print(list(onto.search(type = onto.Projects, hasLanguage = "*")))

    # Returns all projects that use C, C++, or C#
    # print(list(onto.search(type = onto.Projects, hasLanguage = "*")))
    
    
# print(find_projects_with_obj_property_x_and_value_y(onto, "hasLanguage", "C_Sharp"))
#=====================================================================================
#license_handler() is a function to extarct licese values from projects
#Each project can contain 1 or more than 1 license
#function returns list of license name present in the passed project object.
def license_handler(each_project):
    temp_lic = []                                   #Variable to hold licenses
    license_count = len(each_project.hasLicense)            #Takiing a count of license one project has
    #print("Each project: " + str(each_project.name) + " Number of license: " + str(license_count))
    print("Details of Each project: ")
    print(str(each_project.hasLicense))
    if license_count > 1:
        temp_int_lic = str(each_project.hasLicense).split(" ")[(-1)*license_count:]
        #print("temporary license varaible: " + str(each_project.hasLicense))
        for each_lic in temp_int_lic:
            temp_lic.append(each_lic.split(".").pop()[:-1])             #making a list if a project has more than one license 
                #print("Printing License where license count is more than 1: " + str(temp_lic))
        return temp_lic
    else:
        temp_lic.append(str(each_project.hasLicense).split(".").pop()[:-1])
        return temp_lic
    
def star_filter(each_project,stars):
    result = None
    if stars == "over_2000_Stars":
            print("I am in greater 2000")
            if each_project in onto.Project_With_over_2000_Stars.instances():
                        print(" I am in the final if")
                        result = each_project.name
    elif stars == "around_1500_Stars":
            if each_project in onto.Project_With_around_1500_Stars.instances():
                        print(" I am in the final elif")
                        result = each_project.name
    elif stars == "around_1000_Stars":
            if each_project in onto.Project_With_around_1000_Stars.instances():
                        result = each_project.name
    elif stars == "around_750_Stars":
            if each_project in onto.Project_With_around_750_Stars.instances():
                result = each_project.name
    elif stars == "around_500_Stars":
            if each_project in onto.Project_With_around_500_Stars.instances():
                result = each_project.name
    elif stars == "around_250_Stars":
            if each_project in onto.Project_With_around_250_Stars.instances():
                result = each_project.name
    elif stars == "around_100_Stars":
            if each_project in onto.Project_With_around_100_Stars.instances():
                result = each_project.name
    elif stars == "around_50_Stars":
            if each_project in onto.Project_With_around_50_Stars.instances():
                result = each_project.name
    elif stars == "around_25_Stars":
            if each_project in onto.Project_With_around_25_Stars.instances():
                result = each_project.name
    elif stars == "around_10_Stars":
            if each_project in onto.Project_With_around_10_Stars.instances():
                result = each_project.name
    elif stars == "around_5_Stars":
            if each_project in onto.Project_With_around_5_Stars.instances():
                result = each_project.name
    elif stars == "no_Stars":
            if each_project in onto.Project_With_no_Stars.instances():
                result = each_project.name
    
    return result

def date_filter(each_project, date):
    print("Native date")
    result = None
    if date == "Today":
        if each_project in onto.Project_LastModified_Today.instances():
            result = each_project.name
    elif date == "Yesterday":
        if each_project in onto.Project_LastModified_Yesterday.instances():
            result = each_project.name
    elif date == "This_Week":
        if each_project in onto.Project_LastModified_This_Week.instances():
            result = each_project.name
    elif date == "Week_Ago":
        if each_project in onto.Project_LastModified_Week_Ago.instances():
            result = each_project.name
    elif date == "Two_Weeks_Ago":
        if each_project in onto.Project_LastModified_Two_Weeks_Ago.instances():
            result = each_project.name        
    elif date == "Month_Ago":
        if each_project in onto.Project_LastModified_Month_Ago.instances():
            result = each_project.name
    elif date == "Two_Months_Ago":
        if each_project in onto.Project_LastModified_Two_Months_Ago.instances():
            result = each_project.name
    elif date == "Four_Months_Ago":
        if each_project in onto.Project_LastModified_Four_Months_Ago.instances():
            result = each_project.name
    elif date == "Six_Months_Ago":
        if each_project in onto.Project_LastModified_Six_Months_Ago.instances():
            result = each_project.name
    elif date == "Ten_Months_Ago":
        if each_project in onto.Project_LastModified_Ten_Months_Ago.instances():
            result = each_project.name
    elif date == "Year_Ago":
        if each_project in onto.Project_LastModified_Year_Ago.instances():
            result = each_project.name
    elif date == "Over_A_Year_Ago":
        if each_project in onto.Project_LastModified_Over_A_Year_Ago.instances():
            result = each_project.name
    elif date == "Two_Years_Ago":
        if each_project in onto.Project_LastModified_Two_Years_Ago.instances():
            result = each_project.name
    elif date == "Over_Two_Years_Ago":
        if each_project in onto.Project_LastModified_Over_Two_Years_Ago.instances():
            result = each_project.name
    return result

def get_project_details_from_name(project_names):
    print("In the get project details")
    result = []
    for each_name in project_names:
        print("Each name type:" + str(type(each_name)))
        print("For this each_name I am throwing error: " + str(each_name))
        temp_dict = {}
        o = getattr(onto, str(each_name))        
        name = o.title
        owner = o.owner
        lang = str(o.hasLanguage).split(".").pop()
        stars = o.has_Stars
        last_update = o.has_Date_LastModified
        lic = license_handler(o)[0]
        temp_dict["lang"] = lang
        temp_dict["license"] = lic
        temp_dict["name"] = name
        temp_dict["owner"] = owner
        temp_dict["stars"] = str(stars)
        temp_dict["updated"] = str(last_update)

        print(f'''
                Project details
                     "lang": "{lang}",
                     "license": "{lic}",
                     "name": "{name}",
                     "owner": "{owner}",
                     "stars": {stars},
                     "updated": "{last_update}" ''')
        result.append(temp_dict)
    
    return result



def intersection_of_filters(license = None, language = None , date = None, stars = None):
    
    result = []
    
    if (license or language or date or stars) == None:
        print("No filters were passed")
        for each_project in onto.Project.instances():
            result.append(each_project.name)
        #return
    elif(license and language and date and stars) != None:
        for each_project in onto.Project.instances():
            temp_lang = str(each_project.hasLanguage).split(".").pop()
            if (temp_lang == language) == True:
                intermediate_license = license_handler(each_project)
                if (True if license in intermediate_license else False):
                    if star_filter(each_project,stars) is not None:
                        if date_filter(each_project,date) is not None:
                            result.append(date_filter(each_project,date))


        print("All filters present")
    elif(license and language and date) != None:
        for each_project in onto.Project.instances():
            temp_lang = str(each_project.hasLanguage).split(".").pop()
            if (temp_lang == language) == True:
                intermediate_license = license_handler(each_project)
                if (True if license in intermediate_license else False):
                        if date_filter(each_project,date) is not None:
                            result.append(date_filter(each_project,date))
        print("All filters present")
    elif(license and language and stars) != None:
        for each_project in onto.Project.instances():
            temp_lang = str(each_project.hasLanguage).split(".").pop()
            if (temp_lang == language) == True:
                print("Language checked")
                intermediate_license = license_handler(each_project)
                if (True if license in intermediate_license else False):
                    print("Cool! License also checked")
                    if star_filter(each_project,stars) is not None:
                            print("Even stars checked")
                            result.append(star_filter(each_project,stars))
        print("All filters present")
    elif(license and date and stars) != None:
            for each_project in onto.Project.instances():
                 intermediate_license = license_handler(each_project)
                 if (True if license in intermediate_license else False):
                    if star_filter(each_project,stars) is not None:
                        if date_filter(each_project,date) is not None:
                            result.append(date_filter(each_project,date))

    elif(language and date and stars) != None:
        for each_project in onto.Project.instances():
            temp_lange = str(each_project.hasLanguage).split(".").pop()
            if temp_lange == language:
                if star_filter(each_project,stars) is not None:
                    if date_filter(each_project,date) is not None:
                        result.append(date_filter(each_project,date))
    elif (license and language) != None:
        intermediate_license = []
        for each_project in onto.Project.instances():
            intermediate_license = license_handler(each_project)        
            temp_lang = str(each_project.hasLanguage).split(".").pop()
            print("License we are looking: "+ str(license)+ " intermediate License list we have= " + str(intermediate_license) + " Language= " + str(temp_lang))
            if (True if license in intermediate_license else False) and (temp_lang == language) == True :
                result.append(each_project.name)
                print("Filters are present")
    elif(license and stars) != None:
        for each_project in onto.Project.instances():
            intermediate_license = license_handler(each_project)        
            #temp_lang = str(each_project.hasLanguage).split(".").pop()
            #print("License= " + str(temp_lic) + " Language= " + str(temp_lang))
            if (True if license in intermediate_license else False):
                #result.append(star_filter(each_project, stars))
                if star_filter(each_project,stars) is not None:
                    print("We got some result")
                    print("printing the star filter: " + str(star_filter(each_project,stars)))
                    result.append(star_filter(each_project,stars))
                else:
                    print("We did not get result")
    elif(license and date):
        for each_project in onto.Project.instances():
            intermediate_license = license_handler(each_project)
            if (True if license in intermediate_license else False):
                print("I got the license." + str(each_project.name))
                temp_date = date_filter(each_project,date)
                print("Date for the project: " + str(temp_date))
                if temp_date != None:
                    print("We got some results!")
                    result.append(temp_date)
        print("Printing last result: " + str(result))        
    elif(language and stars):
        for each_project in onto.Project.instances():
            temp_lange = str(each_project.hasLanguage).split(".").pop()
            if temp_lange == language:
                if star_filter(each_project,stars) is not None:
                    result.append(star_filter(each_project,stars))
    elif(language and date):
        for each_project in onto.Project.instances():
            temp_lange = str(each_project.hasLanguage).split(".").pop()
            if temp_lange == language:
                if date_filter(each_project,date) is not None:
                    result.append(date_filter(each_project,date))
    elif(stars and date):
        for each_project in onto.Project.instances():
            if star_filter(each_project,stars) is not None:
                    if date_filter(each_project,date) is not None:
                        result.append(date_filter(each_project,date))
    elif stars != None:
        temp_result = get_individuals_Project_WithStars(verbosity=0, star_range=stars)
        for each_ind in temp_result:
            result.append(each_ind.name)

    elif date != None:
        print("Only date")
        temp_result = get_individuals_Project_WithLastModified(verbosity=0, last_modified_range=date)
        for each_ind in temp_result:
            result.append(each_ind.name)
        

    elif language != None:
        temp_result = get_individuals_Project_WithLanguage(verbosity=0, lang=language)
        for each_ind in temp_result:
            result.append(each_ind)
    
    elif license != None:
        temp_result = get_individuals_Project_WithLicense(verbosity=0, license_value=license)
        for each_ind in temp_result:
            result.append(each_ind) 

    if result != None:
        final_result = get_project_details_from_name(result)
    
    else:
        return result
    print("Getting detials :" + str(get_project_details_from_name(result)))

    return final_result




    # elif (license and date) != None:
       
    #     for each_project in onto.Project.instances():

