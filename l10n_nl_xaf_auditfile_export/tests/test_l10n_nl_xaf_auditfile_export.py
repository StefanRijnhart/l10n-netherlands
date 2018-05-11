# -*- coding: utf-8 -*-
# © 2017 Therp BV <http://therp.nl>
# Copyright 2018 Noviat
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).
from base64 import b64decode
from StringIO import StringIO
from zipfile import ZipFile

from openerp.tests.common import TransactionCase


class TestL10nNlXafAuditfileExport(TransactionCase):

    def test_l10n_nl_xaf_auditfile_export_default(self):
        export = self.env['xaf.auditfile.export'].create({})
        export.button_generate()
        self.assertTrue(export.auditfile)
        zf = StringIO(b64decode(export.auditfile))
        with ZipFile(zf, 'r') as archive:
            contents = archive.read(archive.namelist()[0])
        self.assertTrue(contents.startswith('<?xml '))

    def test_l10n_nl_xaf_auditfile_export_all(self):
        export = self.env['xaf.auditfile.export'].create(
            {'data_export': 'all'})
        export.button_generate()
        self.assertTrue(export.auditfile)
        zf = StringIO(b64decode(export.auditfile))
        with ZipFile(zf, 'r') as archive:
            contents = archive.read(archive.namelist()[0])
        self.assertTrue(contents.startswith('<?xml '))
