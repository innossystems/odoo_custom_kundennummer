from odoo import api, fields, models, _

class ResPartner(models.Model):
    _inherit = 'res.partner'

    kundennummer = fields.Char(
        string='Kundennummer',
        readonly=True,
        copy=False,
        store=True
    )
    lieferantennummer = fields.Char(
        string='Lieferantennummer',
        readonly=True,
        copy=False,
        store=True
    )

    @api.model
    def create(self, vals):
        # Überprüfen, ob der Partner eine Firma ist und die Kundennummer fehlt
        if vals.get('is_company'):
            if not vals.get('x_studio_kundennummer'):
                vals['x_studio_kundennummer'] = self.env['ir.sequence'].next_by_code('res.partner.kundennummer.id') or _('New')
            if not vals.get('x_studio_lieferantennummer'):
                vals['x_studio_lieferantennummer'] = self.env['ir.sequence'].next_by_code('res.partner.lieferantennummer.id') or _('New')
        
        # Aufruf der Super-Methode
        return super(ResPartner, self).create(vals)

    def write(self, vals):
        # Bestehenden Kontakten Kundennummer und Lieferantennummer zuweisen, wenn sie fehlen
        for record in self:
            if record.is_company:
                if not record.x_studio_kundennummer:
                    vals['x_studio_kundennummer'] = self.env['ir.sequence'].next_by_code('res.partner.kundennummer.id') or _('New')
                if not record.x_studio_lieferantennummer:
                    vals['x_studio_lieferantennummer'] = self.env['ir.sequence'].next_by_code('res.partner.lieferantennummer.id') or _('New')
        
        # Aufruf der Super-Methode
        return super(ResPartner, self).write(vals)