{
    'name': 'Sweden â€” AdressfÃ¤ltsordning',
    'version': '19.0.2.0.0',
    'category': 'Localization',
    'summary': 'Ordnar adressfÃ¤lt postnummer/stad/lÃ¤n och visar SE-postnummer som NNN NN.',
    'author': 'Fredrik Arvas / Arvas International AB',
    'license': 'LGPL-3',
    'depends': ['contacts'],
    'data': [
        'views/res_partner_views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'l10n_se_partner/static/src/zip_field.js',
        ],
    },
    'installable': True,
    'auto_install': False,
    'application': False,
}