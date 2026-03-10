import csv
from src.utils.constants import (
    RESULT_TABLE_COLUMNS,
    RESULT_TABLE_NAME
)


def write_to_results_table(output_dir : str, name : str, results : dict):
    """
    """
    with open(f"{output_dir}/{RESULT_TABLE_NAME}.csv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=RESULT_TABLE_COLUMNS)

        if csvfile.tell() == 0: # write header only if file is empty
            writer.writeheader()

        row = {"input_path": name}
        row.update(results)

        writer.writerow(row)
    