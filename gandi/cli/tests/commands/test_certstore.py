# -*- coding: utf-8 -*-

from .base import CommandTestCase
from gandi.cli.commands import certstore


class CertStoreTestCase(CommandTestCase):

    def test_list(self):

        result = self.invoke_with_exceptions(certstore.list, [])

        self.assertEqual(result.output, """\
subject   : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test1.domain.fr
----------
subject   : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test1.domain.fr
----------
subject   : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test2.domain.fr
----------
subject   : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test3.domain.fr
----------
subject   : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test4.domain.fr
----------
subject   : /OU=Domain Control Validated/OU=Gandi Standard Wildcard SSL/CN=*.domain.fr
""")
        self.assertEqual(result.exit_code, 0)

    def test_info_fqdn(self):

        result = self.invoke_with_exceptions(certstore.info, ['test1.domain.fr'])

        self.assertEqual(result.output, """\
id          : 1
subject     : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test1.domain.fr
date_created: 20150407T00:00:00
date_expire : 20160316T00:00:00
	----------
	fqdn      : test1.domain.fr
	----------
	vhost     : test1.domain.fr
	type      : paas
----------
id          : 2
subject     : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test1.domain.fr
date_created: 20150407T00:00:00
date_expire : 20160316T00:00:00
	----------
	fqdn      : test1.domain.fr
	----------
	vhost     : test1.domain.fr
	type      : paas
""")
        self.assertEqual(result.exit_code, 0)

    def test_info_id(self):
        result = self.invoke_with_exceptions(certstore.info, ['1'])

        self.assertEqual(result.output, """\
id          : 1
subject     : /OU=Domain Control Validated/OU=Gandi Standard SSL/CN=test1.domain.fr
date_created: 20150407T00:00:00
date_expire : 20160316T00:00:00
	----------
	fqdn      : test1.domain.fr
	----------
	vhost     : test1.domain.fr
	type      : paas
""")
        self.assertEqual(result.exit_code, 0)
