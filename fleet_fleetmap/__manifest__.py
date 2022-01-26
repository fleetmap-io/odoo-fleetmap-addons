{
    'name' : 'Fleetmap',
    'version' : '0.0.1',
    'sequence': 185,
    'summary' : 'Fleetmap Management',
    'category': 'Human Resources/Fleet',
    'website' : '',
    'depends': ['fleet'],
    'data': ['views/fleet_vehicle_views.xml'],
    'external_dependencies': {
        'python' : ['pytraccar','asyncio','aiohttp']
    },
    'auto_install': False,
    'license': 'LGPL-3'
}
