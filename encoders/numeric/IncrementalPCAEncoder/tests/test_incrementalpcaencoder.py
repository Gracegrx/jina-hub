import numpy as np
from .. import IncrementalPCAEncoder
from tests.unit.executors.encoders.numeric import NumericTestCase


class IncrementalPCATestCase(NumericTestCase):
    def _get_encoder(self):
        self.input_dim = 28
        self.target_output_dim = 2
        encoder = IncrementalPCAEncoder(
            output_dim=self.target_output_dim, whiten=True, num_features=self.input_dim)
        train_data = np.random.rand(1000, self.input_dim)
        encoder.train(train_data)
        return encoder
