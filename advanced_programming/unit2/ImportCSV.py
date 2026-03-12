import csv


def get_records(filename):
    """Return a list of records from a CSV file.

    Args:
        filename (str): Filename in current path

    Returns:
        list: Records
    """
    records = []

    with open(filename, "r") as file:
        rows = list(csv.reader(file))

        records = []
        # Column headings are the first line in the csv.
        cols = rows[0]

        for row in rows[1:]:
            if len(row) != len(cols):
                # Invalid row, ignore.
                continue

            data = dict()

            for i, col in enumerate(cols):
                # Create a dictionary of data keyed by the column headings.
                data[col] = row[i]

            # Keep a list of dictionaries for all the rows.
            records.append(data)

    return records
