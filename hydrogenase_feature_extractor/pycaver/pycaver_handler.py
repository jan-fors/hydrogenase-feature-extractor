from pathlib import Path
import subprocess

def run_pycaver(
    input_structure: Path, caver_params: dict, starting_point: tuple, output_dir: Path
):
    """ """
    cmd = [
        "pycaver",
        str(input_structure),
        f"-o {str(output_dir)}",
        f"--shell_radius {caver_params['shell_radius']}",
        f"--shell_depth {caver_params['shell_depth']}",
        f"--probe_radius {caver_params['probe_radius']}",
        f"--max_distance {caver_params['max_distance']}",
        f"--desired_radius {caver_params['desired_radius']}",
        f"--starting_point_coordinates {str(starting_point[0])} {str(starting_point[1])} {str(starting_point[2])}"
    ]
    result = subprocess.run(" ".join(cmd), shell=True)


def check_results():
    pass