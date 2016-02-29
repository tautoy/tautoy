# Copyright (c) 2016, Dai MIKURUBE. All rights reserved.

from tautoy_aws.credentials import AwsCredential, AwsCredentials

import unittest


class AwsCredentialsTest(unittest.TestCase):
    def test_one_credential(self):
        cred = AwsCredential('foo', 'barbar')
        self.assertEqual('foo', cred.access_key_id)
        self.assertEqual('barbar', cred.secret_access_key)
        self.assertEqual('AwsCredential("foo")', str(cred))

    def test_credentials(self):
        creds = AwsCredentials({
            'personal': AwsCredential('mine', 'secret'),
            'production': AwsCredential('company', 'top_secret'),
        })
        self.assertEqual('mine', creds.personal.access_key_id)
        self.assertRaises(AttributeError, lambda: creds.nobody)
        self.assertEqual('company', creds['production'].access_key_id)
        creds['test'] = AwsCredential('tester', 'nonsecret')
        self.assertEqual('nonsecret', creds.test.secret_access_key)
        self.assertEqual(3, len(creds))


if __name__ == '__main__':
    unittest.main()
