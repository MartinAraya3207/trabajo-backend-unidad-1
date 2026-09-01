class Servicio:
    def __init__(self, id, nombre, resumen, descripcion, caracteristicas, precio, duracion):
        self.id = id
        self.nombre = nombre
        self.resumen = resumen
        self.descripcion = descripcion
        self.caracteristicas = caracteristicas
        self.precio = precio
        self.duracion = duracion


servicios = [
    Servicio(1, 'Desarrollo de Sitios Web',
             'Sitios y aplicaciones web a medida, rápidos y responsivos para tu negocio.',
             'Diseñamos y desarrollamos sitios web a medida, rápidos, seguros y fáciles de mantener.',
             ['Diseño responsivo', 'Panel de administración', 'Optimización de velocidad', 'Formularios de contacto'],
             'Desde $450.000', '3 a 6 semanas'),

    Servicio(2, 'Aplicaciones Móviles',
             'Apps nativas e híbridas para Android e iOS, conectadas a tus sistemas.',
             'Desarrollamos apps móviles para Android e iOS conectadas a tu backend existente.',
             ['Apps nativas e híbridas', 'Notificaciones push', 'Conexión a API REST', 'Publicación en tiendas'],
             'Desde $890.000', '6 a 10 semanas'),

    Servicio(3, 'Consultoría en la Nube',
             'Migración y optimización de infraestructura en la nube para tu empresa.',
             'Migramos y optimizamos tu infraestructura en la nube, reduciendo costos y mejorando disponibilidad.',
             ['Diagnóstico de infraestructura', 'Migración de servidores', 'Respaldos automáticos', 'Monitoreo 24/7'],
             'Desde $600.000', '2 a 4 semanas'),

    Servicio(4, 'Ciberseguridad para Pymes',
             'Protege los datos de tu empresa y de tus clientes con buenas prácticas reales.',
             'Evaluamos la seguridad de tus sistemas y aplicamos buenas prácticas de protección de datos.',
             ['Auditoría de vulnerabilidades', 'Control de accesos', 'Recuperación ante incidentes', 'Capacitación al equipo'],
             'Desde $350.000', '2 a 3 semanas'),
]
