#verkefni2_8
import os
import glob
import re
def parse_submissions(subm):
    file_contents = []
    #find all files ending in tcl in the subm. folder
    get_files = glob.glob(os.path.join(subm, '**/*.tcl'))
    for subm in get_files:
        with open(subm, 'r') as f:
            store_contents = [] #store contents of file in a single string
            for file in f:
                store_contents.append(file)
            file_contents.append(store_contents)

    filter_accepted = []
    for contents in file_contents:
        for text in contents:
            if 'Classify Accepted' in text: #only get accepted handins
                filter_accepted.append(contents)

    teams = []
    problems = []
    for x in sorted(filter_accepted):
        for string in x:
            if "Team " in string:
                string = re.sub(r'set\s', '', string) #remove the set from start of every string
                string = re.sub(r'\s{2,}', '', string) #extra whitespaces gone
                string = re.sub(r'Team ', '', string).splitlines() #isolating the team name
                teams.append(string[0])
            if "Problem " in string:
                string = re.sub(r'set\s', '', string)
                string = re.sub(r'\s{2,}', '', string)
                string = re.sub(r'Problem ', '', string).splitlines()
                problems.append(string[0])

    ret_list = []
    ret_list = list(zip(teams, problems))
    print(ret_list)
    
    return ret_list

parse_submissions('submissions')