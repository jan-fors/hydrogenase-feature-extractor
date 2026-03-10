import argparse
from src.main import main

def _verify_inputs(args):
    """"""
    #TODO check if db exists

    #TODO check if input file exists and has valid format

    pass

def _extract_args(args):
    """"""
    return args.input_path, args.output, args.output_dir, args.results_table

def cli(args):
    """
    """
    
    _verify_inputs(args)

    input_path, output, output_dir, results_table = _extract_args(args)

    main(input_path, output, output_dir, results_table)


if __name__ == "__main__":
    parser = argparse.ArgumentParser(prog='hydrogenase-feature-extractor',
                    description='Takes an input structure and extracts relevant coordinates from it.',
                    epilog='')
    parser.add_argument("input_path", help="Path to the input structure.")
    parser.add_argument("output", help="Name of the output.")
    parser.add_argument("--output_dir", "-o", default=".", help="Specify the output directory, default .")
    parser.add_argument("--results_table", "-r", action="store_true", help="Whether to write the results to a table.")

    args = parser.parse_args()

    cli(args)