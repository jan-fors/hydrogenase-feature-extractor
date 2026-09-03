import csv
from hydrogenase_feature_extractor.utils.constants import (
    RESULT_TABLE_COLUMNS,
    RESULT_TABLE_NAME,
    RAW_RESULT_TABLE_NAME
)
import os

def write_to_results_table(output_dir : str, name : str, results : dict):
    """
    """
    with open(f"{output_dir}/{RESULT_TABLE_NAME}.tsv", "a", newline="") as csvfile:
        writer = csv.DictWriter(csvfile, fieldnames=RESULT_TABLE_COLUMNS ,delimiter="\t", )

        if csvfile.tell() == 0: # write header only if file is empty
            writer.writeheader()

        row = {"input_path": name}
        row.update(results)

        writer.writerow(row)
    


def write_to_raw_results_table(output_dir: str, name: str, results: dict):
    """
    Appends a row to the CSV, writing a header only when the file is new/empty.
    Handles variable columns by using extrasaction='ignore' and restval='' 
    so missing fields are left blank rather than raising errors.
    """
    filepath = f"{output_dir}/{RAW_RESULT_TABLE_NAME}.tsv"
    file_exists = os.path.isfile(filepath) and os.path.getsize(filepath) > 0

    row = {"input_path": name}
    row.update(results)

    # Fixed columns always appear first, dynamic ones follow
    fixed_cols = ["input_path"]
    dynamic_cols = [k for k in row if k not in fixed_cols]
    fieldnames = fixed_cols + dynamic_cols

    with open(filepath, "a", newline="") as csvfile:
        writer = csv.DictWriter(
            csvfile,
            fieldnames=fieldnames,
            extrasaction="ignore",  # silently drop keys not in fieldnames
            restval="",  
                       delimiter="\t",            # fill missing fields with empty string
        )
        if not file_exists:
            writer.writeheader()
        writer.writerow(row)