# Copyright (c) 2016, Dai MIKURUBE. All rights reserved.

import abc


class AbstractTask(object):
    __metaclass__ = abc.ABCMeta

    def __init__(self, targets, **kwargs):
        self._targets = targets
        pass

    @abc.abstractmethod
    def do(self):
        raise NotImplementedError('Not implemented.')

    @abc.abstractmethod
    def __str__(self):
        return 'AbstractTask'
