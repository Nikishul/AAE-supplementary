# AAE-supplementary

Decoder part of the adversarial autoencoder for generating molecular descriptors (fingerprints) of compounds with anti-HIV properties (inhibitors of gp120 protein, exposed on the surface of HIV-1)

## Installation

Using conda, create an environment and activate it:

```
conda env create -f environment.yml
activate aae
```

## Usage

In order to use the model for generating fingerprints with a certain binding energy threshold, run app.py with the following arguments:

* ```--energy```: Energy threshold to generate with.
* ```--number_fps```: Amount of fingerprints to generate.


## Example
```
python app.py --energy -9 --number_fps 100
```

## Note

As the training was based on compounds with binding energy property ranged from 0 to -14, model is not expected to generate coherent results outside those boundaries
