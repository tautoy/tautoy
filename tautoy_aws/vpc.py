# Copyright (c) 2016, Dai MIKURUBE. All rights reserved.


class GetAwsVpcByTags(AbstractTask):
    def __init(self, future_vpc_id, **kwargs):
        self._account = kwargs['account']
        self._region  = kwargs['region']
        self._tags    = kwargs['tags']
        pass

    def do(self):
        return []  # Next tasks to trigger.


class CreateAwsVpc(AbstractTask):
    pass


class UpdateAwsVpc(AbstractTask):
    pass
