# Hydrogenase-Feature-Extractor
Python script that extracts structural information from NiFe-Hydrogenases for downstream analysis.

## Overview
A structural extraction tool that takes a NiFe-Hydrogenase structure as input and extracts information about the specific iron-sulfur clusters, their specific aminoacid environment, geometric distances between them and data about the protein gas channel network.

## Installation
Install directly from GitHub via pip:
```bash
conda create -n hfe python=3.12 -y
conda activate hfe

pip install git+https://github.com/solarflip/hydrogenase-feature-extractor
```

Or clone and install from source (useful for development):
```bash
git clone https://github.com/solarflip/hydrogenase-feature-extractor
cd tool-name
pip install -e .
```

## Usage

```bash
extract-hyd-features [input_path] [options]
```

### Example

```bash
extract-hyd-features file.pdb --output_dir out/ 
```

### Options

| Flag | Description | Default |
|---|---|---|
| `-o, --output_dir <path>` | Output file path | `./` |


## Citation

If you use this tool in your research, please cite:
t.b.p.

## License

[MIT](LICENSE)