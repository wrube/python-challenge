
# import libraries
import csv
import pathlib

# setup working directory and data file path
working_dir = pathlib.Path.cwd()
data_path = working_dir / "resources" / "election_data.csv"

# open and read file 
file = data_path.open(mode="r", encoding="utf-8", newline="")
reader = csv.reader(file)

# store election data in a dictionary with the keys as the candidates and the ballot number
# and county as a list in a list e.g. {"candidate A": [[ballotID1, countyA], [ballotID2, countyB]]}
election = {}
row_counter = 1
for row in reader:
    # store header
    if row_counter == 1:
        header = row
    # populate election dictionary
    else:
        ballot_no = int(row[0])
        county = row[1]
        candidate = row[2]
        if candidate not in election:
            election[candidate] = [[ballot_no, county]]
        else:
            election[candidate].append([ballot_no, county])
    row_counter += 1

# summarise the election data in a list with candidate name and votes received
election_results = [[candidate, len(vote)] for candidate, vote in election.items()]

# calculate the total votes of the entire election
total_votes = sum([election_results[i][1] for i in range(len(election_results))])

def perc_won(votes, total_votes):
    """
    Output: float - percentage won of total votes

    Input:  votes - number of votes
            total_votes - the total number of votes in election
    """
    return 100 * votes/total_votes

# generate a string with the election results for each candidate
results_string = ""
for i in range(len(election_results)):
    candidate = election_results[i][0]
    votes_won = election_results[i][1]
    results_string += f"{candidate}: {perc_won(votes_won, total_votes):.3f}% ({votes_won})\n"

# determine the winner
# first create a list with just the results received for each candidate
votes_list = [election_results[i][1] for i in range(len(election_results))]
winner_index = votes_list.index(max(votes_list)) # index for winner
election_winner = election_results[winner_index][0]


# output results into console and file
output_text = \
f"""Election Results

----------------------------
Total Votes: {total_votes}
----------------------------

{results_string}
----------------------------
Winner: {election_winner}
----------------------------
"""

print(output_text)

output_file = working_dir / "pypoll_output.txt"
with output_file.open(mode="w", encoding="utf-8") as file:
    file.write(output_text)

