<p align="center">
  <img width="450" src="https://github.com/elliesch/rf_bedform_mapping/blob/main/figs/logo.png"/>
</p>

# `bedmap`: A Python package for the Automatic Detection of Glacially-derived Bedforms

The `bedmap` workflow automates the detection of glacially-derived bedforms for landforms identified from the Topographic Position Index (TPI) tool using machine learning. Users can pick one of three trained ensemble models (Random Forest, XGBoost, or the ensemble average of both) to detect bedforms from positive relief landforms, and choose to output detections as bedform probabilities or as binarized predictions. `bedmap` also includes a routine for running a scientifically-driven prefiltering routine on TPI data to prepare it for use with machine learning models.

`bedmap` can be used directly in Python, or as part of our ArcGIS pipeline, which incorporated with TPI, allows for the detection of bedforms directly from DEMs. Check out the notebooks available here or on CryoCloud for examples of how to apply `bedmap` to your data, or follow the quickstart guide below.

# Installation

`bedmap` can be installed using `pip`:

```bash
pip install bedmap
```

Note that the `bedmap` package requires Python 3.9 or later.

# Quickstart

Import the main interface:

```python
from bedmap import ClassifyBedforms
```

Automatically detect bedforms from a TPI output CSV:

```python
# Instantiate bedmap
landforms = ClassifyBedforms(
  input_csv='~/path/to/your/TPI/CSV',  # path to your input TPI csv
  model='ensemble_average',            # machine learning model choice
  threshold=0.45,                      # probability threshold
  probability=False                    # output as a binary prediction
)

# Define the predicted landforms
predicted_bedforms = landforms.predicted_bedforms
```

# References & Attribution
The code is under development and will be described in a paper and Jupyter Book.
If you make use of this code in your research, please cite:
```
LaTeX citations to go here.
```

If you make use of the training data in your research, please cite:
```
@misc{mckenzie2022_dataset,
 author={Marion A {McKenzie} and Lauren M {Simkins} and Sarah M {Principato}},
 title={{Streamlined subglacial bedforms across the deglaciated Northern Hemisphere}},
 year={2022},
 doi={10.1594/PANGAEA.939999},
 url={https://doi.org/10.1594/PANGAEA.939999},
 type={data set},
 publisher={PANGAEA}
}
```

If you make use of the Wisconsin Bay Lobe data in your research, please cite:

[![DOI](https://zenodo.org/badge/768265366.svg)](https://zenodo.org/doi/10.5281/zenodo.11660146)
```
@misc{wiscbaylobe_dataset,
  author       = {Ellianna {Abrahams} and Marion A {McKenzie},
  title        = {bedmap: A Python package for the Automatic Detection of Glacially-Derived Bedforms},
  year         = {2024},
  doi          = {10.5281/zenodo.11660146},
  url          = {https://zenodo.org/doi/10.5281/zenodo.11660146},
  note         = {Pre-release}
}
```

