# Copyright (c) 2016, Dai MIKURUBE. All rights reserved.

try:
    from collections.abc import MutableMapping
except ImportError:
    from collections import MutableMapping


class AwsCredential(object):
    def __init__(self, access_key_id, secret_access_key):
        self.__access_key_id = access_key_id
        self.__secret_access_key = secret_access_key

    @property
    def access_key_id(self):
        return self.__access_key_id

    @property
    def secret_access_key(self):
        return self.__secret_access_key

    def __str__(self):
        return 'AwsCredential("%s")' % self.__access_key_id


class AwsCredentials(MutableMapping):
    def __init__(self, aws_credentials={}):
        if not isinstance(aws_credentials, dict):
            raise TypeError()
        self._aws_credentials = {}
        for profile, aws_credential in aws_credentials.iteritems():
            if not isinstance(aws_credential, AwsCredential):
                raise TypeError()
            self._aws_credentials[profile] = aws_credential

    def __getattr__(self, profile):
        if profile in self._aws_credentials:
            return self._aws_credentials[profile]
        raise AttributeError('No such profile "%s" is registered.' % profile)

    def __getitem__(self, profile):
        if profile in self._aws_credentials:
            return self._aws_credentials[profile]
        raise AttributeError('No such profile "%s" is registered.' % profile)

    def __setitem__(self, profile, aws_credential):
        if profile in self._aws_credentials:
            raise AttributeError('A profile "%s" is already registered.' % profile)
        if not isinstance(aws_credential, AwsCredential):
            raise TypeError()
        self._aws_credentials[profile] = aws_credential

    def __delitem__(self, profile):
        if profile in self._aws_credentials:
            raise AttributeError('A profile "%s" cannot be deleted.' % profile)
        else:
            raise AttributeError('No such profile "%s" is registered.' % profile)

    def __len__(self):
        return len(self._aws_credentials)

    def __iter__(self):
        for profile in sorted(self._aws_credentials):
            yield profile
