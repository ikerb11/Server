
{
    'name': "reservas",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Iker",

    # any module necessary for this one to work correctly
    'depends': ['base'],

    # always loaded
    'data': ["views/reserva.xml", "views/cliente.xml" , "views/habitacion.xml" ,'security/ir.model.access.csv'],
    "application":True,
    "installable":True
}
