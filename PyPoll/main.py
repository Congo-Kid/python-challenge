#import modules
import csv
import os


file=os.path.join('election_data.csv')
#open csv file with the election data
with open(file,'r') as csvfile:

    #read file
    csvread=csv.reader(open('election_data.csv'))

    #create dictionary to hold voterIDs correlated with the candidate they voted for
    voteInfo = {}

    for row in csvread:
        #start looping through voter info, assign rows "i" for voter id, "c" county, "v" who was voted for
        i,c,v = row
        #county data unnecessary, only need contain id info and candidate
        #assign this and add to dictionary for all data
        voteInfo[i] = v                                     
    #remove top row labels
    del voteInfo["Voter ID"]                                
    
    #count total number of votes from the voter IDs in the dictionary
    total_votes = len(voteInfo)   

    #create list where candidate names will go for counting
    VoteCounter = {}                                       

    #search all the votes for unique candidate names. When found, start up a vote counter 
    #in the dictionary as a value for the unique candidate
    for value in voteInfo.values():                         
        if not value in VoteCounter:
            VoteCounter[value] = 1
        else:
            VoteCounter[value] =  VoteCounter[value] + 1

    Winner = ""
    number_of_votes = 0

    #iterate through dictionary to determine the winner  
    for key, value in VoteCounter.items():                  
        if VoteCounter[key] > number_of_votes:
            number_of_votes = VoteCounter[key]
            Winner = key
        
        # figure out vote percentages and add to values 
        VoteCounter[key] = [value] + [round(100*(value/total_votes),2)]

         #print election results
    #print('Election Results')                               
    #print('-------------------------')
    #print('Total Votes: '+ str(total_votes))
    #for candidate in VoteCounter:
        #print( candidate + ':  ' + str(VoteCounter[candidate][1]) + '% (' + str(VoteCounter[candidate][0]) + ')')
        #print('-------------------------')
    #print('Winner: ' + Winner)
    #print('-------------------------')

    #output file path
    output_file = os.path.join('pypoll_output.txt')                             

    #write results to new file
    with open(output_file,'w') as write_file:                

    #write text to file 
        write_file.writelines('Election Results'+ '\n')
        write_file.writelines('-------------------------' + '\n')
        write_file.writelines('Total Votes: '+ str(total_votes) + '\n')
        write_file.writelines('-------------------------' + '\n')
        #loop through each candidate
        for candidate in VoteCounter:
            write_file.writelines(candidate + ':  ' + str(VoteCounter[candidate][1]) + '% (' + str(VoteCounter[candidate][0]) + ')' + '\n')
        write_file.writelines('-------------------------' + '\n')
        write_file.writelines('Winner: ' + Winner + '\n')
        

#open file and print copy to terminal
with open(output_file,'r') as readfile:
    print(readfile.read())
