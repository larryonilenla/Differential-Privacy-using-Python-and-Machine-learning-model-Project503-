# Differential Privacy with Laplace Mechanism

## Overview

This repository contains code and documentation for implementing differential privacy using the Laplace mechanism in the context of machine learning model training. The goal is to assess the impact of privacy-preserving techniques on the training accuracy of a machine learning model when applied to sensitive datasets.

## Files

1. **Swipe_ModelTraining - G10.ipynb**: Jupyter notebook containing the machine learning model training process. It compares the training accuracy of the model with the actual dataset.

2. **laplace_mechanism.py**: Python script implementing the Laplace mechanism for adding noise to a dataset. It reads data from **OversampledSwipeData.csv**, adds noise based on specified parameters, and outputs the noisy dataset to **NoisyOversampledSwipeData.csv**.

## Usage

### 1. Model Training

Execute the **Swipe_ModelTraining - G10.ipynb** notebook to train the machine learning model and evaluate its accuracy on the original dataset.

### 2. Differential Privacy Mechanism

Run the **laplace_mechanism.py** script to add noise to the dataset. Customize the following parameters:

- `noise_percentage`: Percentage of the dataset to add noise to.
- `noise_scale`: Selected subset of the dataset to add noise to.
- `sensitivity`: Sensitivity parameter for Laplace noise generation.
- `privacy_budget`: Privacy budget for differential privacy.

```bash
python laplace_mechanism.py
```

The script will generate a new dataset (**NoisyOversampledSwipeData.csv**) with added noise.

### 3. Evaluate Differential Privacy Impact

Re-run the **Swipe_ModelTraining - G10.ipynb** notebook using the noisy dataset to observe the impact of differential privacy mechanisms on the training accuracy. Take notes of the accuracy at different `noise_percentage` and `noise_scale` settings.

## Dependencies

- Python 3.x
- Jupyter Notebook
- Pandas

Install dependencies using:

```bash
pip install pandas
```

## Contributors

- [Md Morshedul Islam, Phd]
- [Olanrewaju Onilenla]
- [Bright Balogun]

## License

This project is licensed under the [MIT License](LICENSE).

Feel free to contribute, open issues, or provide feedback!
