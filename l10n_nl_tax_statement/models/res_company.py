# Copyright 2017-2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResCompany(models.Model):
    _inherit = "res.company"

    l10n_nl_tax_invoice_basis = fields.Boolean(
        string="NL Tax Invoice Basis", default=True
    )
    l10n_nl_tax_journal_id = fields.Many2one(
        comodel_name="account.journal",
        string="NL Tax Statement Closing Entry Journal",
    )
    l10n_nl_tax_partner_id = fields.Many2one(
        comodel_name="res.partner",
        string="NL Tax Statement Tax Authority Partner",
    )
    l10n_nl_tax_payable_account_id = fields.Many2one(
        comodel_name="account.account",
        string="NL Tax Statement Payable Tax Account",
    )
    l10n_nl_tax_receivable_account_id = fields.Many2one(
        comodel_name="account.account",
        string="NL Tax Statement Receivable Tax Account",
    )
    l10n_nl_tax_rounding_profit_account_id = fields.Many2one(
        comodel_name="account.account",
        string="NL Tax Statement Rounding Profit Account",
    )
    l10n_nl_tax_rounding_profit_loss_id = fields.Many2one(
        comodel_name="account.account",
        string="NL Tax Statement Rounding Profit Account",
    )
