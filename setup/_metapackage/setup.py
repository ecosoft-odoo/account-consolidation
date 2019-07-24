import setuptools

with open('VERSION.txt', 'r') as f:
    version = f.read().strip()

setuptools.setup(
    name="odoo12-addons-oca-account-consolidation",
    description="Meta package for oca-account-consolidation Odoo addons",
    version=version,
    install_requires=[
        'odoo12-addon-account_invoice_consolidated',
    ],
    classifiers=[
        'Programming Language :: Python',
        'Framework :: Odoo',
    ]
)
