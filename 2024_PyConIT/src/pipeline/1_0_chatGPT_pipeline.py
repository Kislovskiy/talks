import csv


def read_csv_and_compute_average(filename):
    scores = []

    with open(filename, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            try:
                # Try converting the Score to an integer
                score = int(row["Score"])
                scores.append(score)
            except ValueError:
                # Skip the row if the conversion fails
                print(f"Invalid score '{row['Score']}' for {row['Name']}, skipping.")

    if scores:
        average_score = sum(scores) / len(scores)
        print(f"The average score for the class is: {average_score:.2f}")
    else:
        print("No valid scores found.")


# Call the function with the CSV file path
read_csv_and_compute_average("data/example.csv")
