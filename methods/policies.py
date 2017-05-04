# Bitdefender, 2017

from torch.autograd import Variable

class DeterministicPolicy(object):
    def __init__(self, estimator):
        """Assumes estimator returns an autograd.Variable"""

        self.name = "DP"
        self.estimator = estimator

    def get_action(self, state_batch):
        """ Takes best action based on estimated state-action values."""
        return self.estimator(Variable(state_batch, volatile=True)).data.max(1)


class StochasticPolicy(object):
    def __init__(self, estimator):
        raise NotImplemented("Stochastic policy not implemented yet.")
