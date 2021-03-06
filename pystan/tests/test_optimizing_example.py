import unittest

from pystan import StanModel
import numpy as np


class TestOptimizingExample(unittest.TestCase):
    """Test optimizing example from documentation"""

    ocode = """
    data {
        int<lower=1> N;
        real y[N];
    }
    parameters {
        real mu;
    }
    model {
        y ~ normal(mu, 1);
    }
    """

    sm = StanModel(model_code=ocode)

    def test_optimizing(self):
        sm = self.sm
        np.random.seed(3)
        y2 = np.random.normal(size=20)
        op = sm.optimizing(data=dict(y=y2, N=len(y2)))
        self.assertAlmostEqual(op['mu'], np.mean(y2))
