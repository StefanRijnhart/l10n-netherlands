# Copyright 2017-2020 Onestein (<https://www.onestein.eu>)
# License AGPL-3.0 or later (https://www.gnu.org/licenses/agpl).

from odoo import fields, models


class ResConfigSettings(models.TransientModel):
    _inherit = "res.config.settings"

    l10n_nl_tax_invoice_basis = fields.Boolean(
        string="NL Tax Invoice Basis",
        related="company_id.l10n_nl_tax_invoice_basis",
        readonly=False,
    )
    l10n_nl_tax_journal_id = fields.Many2one(
        string="NL Tax Statement Closing Entry Journal",
        related="company_id.l10n_nl_tax_journal_id",
    )
    l10n_nl_tax_partner_id = fields.Many2one(
        string="NL Tax Statement Tax Authority Partner",
        related="company_id.l10n_nl_tax_partner_id",
    )
    l10n_nl_tax_payable_account_id = fields.Many2one(
        string="NL Tax Statement Payable Account",
        related="company_id.l10n_nl_payable_account_id",
    )
    l10n_nl_tax_receivable_account_id = fields.Many2one(
        string="NL Tax Statement Payable Account",
        related="company_id.l10n_nl_receivable_account_id",
    )
    l10n_nl_tax_rounding_profit_account_id = fields.Many2one(
        string="NL Tax Statement Rounding Profit Account",
        related="company_id.l10n_nl_rounding_profit_account_id",
    )
    l10n_nl_tax_rounding_profit_loss_id = fields.Many2one(
        string="NL Tax Statement Rounding Profit Account",
        related="company_id.l10n_nl_rounding_profit_account_id",
    )
