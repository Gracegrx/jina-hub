import tempfile
import os

import numpy as np

from .. import CustomKerasImageEncoder
from jina.executors.metas import get_default_metas
from tests.unit.executors.encoders.image import ImageTestCase
from jina.executors import BaseExecutor


def rm_files(file_paths):
    for file_path in file_paths:
        if os.path.exists(file_path):
            if os.path.isfile(file_path):
                os.remove(file_path)
            elif os.path.isdir(file_path):
                shutil.rmtree(file_path, ignore_errors=False, onerror=None)

class TestNet:
    def __init__(self):
        self.model = None
        self.input_shape = (224, 224, 3)
        self.conv = Conv2D(32, (3, 3), padding='same', name='conv1', input_shape=self.input_shape)
        self.activation_relu = Activation('relu')
        self.flatten = Flatten()
        self.dense = Dense(10, name='dense')
        self.activation_softmax = Activation('softmax')

    def create_model(self):
        self.model = Sequential()
        self.model.add(self.conv)
        self.model.add(self.activation_relu)
        self.model.add(self.flatten)
        self.model.add(self.dense)
        self.model.add(self.activation_softmax)
        return self.model

def _get_encoder(self, metas):
    from tensorflow.keras.models import Sequential
    from tensorflow.keras.layers import Conv2D, Activation, Flatten, Dense
    path = tempfile.NamedTemporaryFile().name
    self.add_tmpfile(path)
    model = TestNet().create_model()
    model.save(path)
    self.target_output_dim = 10
    self.input_dim = 224
    return CustomKerasImageEncoder(channel_axis=1, model_path=path, layer_name='dense')

def test_encoding_results(self):
    encoder = self.get_encoder()
    if encoder is None:
        return
    test_data = np.random.rand(2, 3, self.input_dim, self.input_dim)
    encoded_data = encoder.encode(test_data)
    assert encoded_data.shape == (2, self.target_output_dim)

def test_save_and_load(self):
    encoder = self.get_encoder()
    if encoder is None:
        return
    test_data = np.random.rand(2, 3, self.input_dim, self.input_dim)
    encoded_data_control = encoder.encode(test_data)
    encoder.touch()
    encoder.save()
    self.assertTrue(os.path.exists(encoder.save_abspath))
    encoder_loaded = BaseExecutor.load(encoder.save_abspath)
    encoded_data_test = encoder_loaded.encode(test_data)
    assert encoder_loaded.channel_axis == encoder.channel_axis
    np.testing.assert_array_equal(encoded_data_control, encoded_data_test)

def test_save_and_load_config(self):
    encoder = self.get_encoder()
    if encoder is None:
        return
    encoder.save_config()
    self.assertTrue(os.path.exists(encoder.config_abspath))
    encoder_loaded = BaseExecutor.load_config(encoder.config_abspath)
    assert encoder_loaded.channel_axis == encoder.channel_axis