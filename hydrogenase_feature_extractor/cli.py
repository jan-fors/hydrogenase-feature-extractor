import argparse
from hydrogenase_feature_extractor.main import main
import os
from pathlib import Path
from hydrogenase_feature_extractor.utils.constants import (
    FINGERPRINT_RADIUS,
    SHELL_DEPTH,
    SHELL_RADIUS,
    PROBE_RADIUS,
    DESIRED_RADIUS,
    MAX_DISTANCE
)

def _verify_inputs(args):
    """"""
    #TODO check if db exists

    #TODO check if input file exists and has valid format

    pass

def _extract_args(args):
    """"""
    caver_params = {
        "shell_radius": args.shell_radius,
        "shell_depth": args.shell_depth,
        "probe_radius": args.probe_radius,
        "desired_radius": args.desired_radius,
        "max_distance": args.max_distance
    }
    return args.input_path, args.output_dir, args.results_tables, args.tunnel, args.fingerprint_radius, caver_params

def cli(args):
    """
    """
    
    _verify_inputs(args)

    input_path, output_dir, results_table, tunnel, fingeprint_radius, caver_params = _extract_args(args)

    # check if outputfolder exists if not create it
    output_dir = output_dir / Path(input_path.stem)
    if not os.path.exists(output_dir):
        os.makedirs(output_dir, exist_ok=True)

    main(input_path, output_dir, results_table, tunnel, fingeprint_radius, caver_params)

def entry():
    parser = argparse.ArgumentParser(prog='hydrogenase-feature-extractor',
                        description='Takes an input structure and extracts relevant coordinates from it.',
                        epilog='')
    parser.add_argument("input_path", type=Path, help="Path to the input structure.")
    parser.add_argument("--output_dir", "-o", default=".", help="Specify the output directory. [.]")
    parser.add_argument("--results_tables", "-r", action="store_true", help="Whether to write the results to a table.")

    parser.add_argument("--tunnel", action="store_true")
    parser.add_argument("--shell_radius", type=float, default=SHELL_RADIUS, help=f"Shell Radius. [{SHELL_RADIUS}]")
    parser.add_argument("--shell_depth", type=float, default=SHELL_DEPTH, help=f"Shell Depth. [{SHELL_DEPTH}]")
    parser.add_argument("--probe_radius", type=float, default=PROBE_RADIUS, help=f"Probe Radius. [{PROBE_RADIUS}]")
    parser.add_argument("--desired_radius", type=float, default=DESIRED_RADIUS, help=f"Desired Radius. [{DESIRED_RADIUS}]")
    parser.add_argument("--max_distance", type=float, default=MAX_DISTANCE, help=f"Max distance. [{MAX_DISTANCE}]")

    parser.add_argument("--fingerprint_radius", type=float, default=FINGERPRINT_RADIUS, help=f"Fingerprint Radius. [{FINGERPRINT_RADIUS}]")
    
    args = parser.parse_args()

    cli(args)

if __name__ == "__main__":
    entry()