# hydrogenase-feature-extractor

Extracts quantitative features from hydrogenase protein structures for
comparative analysis and downstream computational workflows.

## Run
```sh
do python -m src.cli <pdb> <out> -r -o <output folder>
```

```sh
for pdb in <src folder>/*.pdb ; do python -m src.cli $pdb out -r ; done
```