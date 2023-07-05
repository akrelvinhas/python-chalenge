import csv
import os

# Read election data from CSV file
CSV_PATH = os.path.join("Resources", "election_data.csv")
polloutput = os.path.join("analysis", "pypollanalysis.txt")
os.chdir(os.path.dirname(os.path.realpath(__file__)))

with open(CSV_PATH) as csv_file:
    csv_reader = csv.reader(csv_file)
    header = next(csv_reader)  # Skip header row

    total_votes = 0
    candidates = {}

    for row in csv_reader:
        candidate = row[2]
        total_votes += 1
        candidates[candidate] = candidates.get(candidate, 0) + 1

    # percentage of votes
    results = []
    for candidate, votes in candidates.items():
        percentage = (votes / total_votes) * 100
        results.append((candidate, percentage, votes))

    # Find winner 
    winner = max(results, key=lambda x: x[2])

    # Print analysis results
    print("Election Results")
    print("-------------------------")
    print(f"Total Votes: {total_votes}")
    print("-------------------------")
    for candidate, percentage, votes in results:
        print(f"{candidate}: {percentage:.3f}% ({votes})")
    print("-------------------------")
    print(f"Winner: {winner[0]}")
    print("-------------------------")

with open(polloutput, mode="wt") as f:
    f.write("Election Results\n")
    f.write("-------------------------\n")
    f.write(f"Total Votes: {total_votes}\n")
    f.write("-------------------------\n")
    for candidate, percentage, votes in results:
        f.write(f"{candidate}: {percentage:.3f}% ({votes})\n")
    f.write("-------------------------\n")
    f.write(f"Winner: {winner[0]}\n")
    f.write("-------------------------\n")