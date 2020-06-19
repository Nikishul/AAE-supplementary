import os
import tensorflow as tf

import numpy as np
import pandas as pd

import argparse

def generate(energy_threshold, n):
    
    decoder = tf.keras.models.load_model(r'decoder.h5')
    z = tf.random.normal([n, 10], mean=0.0, stddev=1.0)
    energy = np.zeros(shape=(n,1))
    energy.fill(energy_threshold)
    decoder_input = tf.concat([z, energy], axis=1)
    generated = decoder(decoder_input, training=False)
    fps = np.round(generated).astype(int)
    df = pd.DataFrame(fps)
    df.to_csv('generated_fps_threshold_{}.csv'.format(energy_threshold), index=False)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()

    parser.add_argument('--energy', type=float, default=-8.,
                        help='Energy threshold to generate with')
    parser.add_argument('--number_fps', type=int, default=10,
                        help='Amount of fingerprints to generate')
    args = parser.parse_args()
    generate(args.energy, args.n)