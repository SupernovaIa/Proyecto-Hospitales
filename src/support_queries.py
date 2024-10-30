# Centro hospitalario
query_creation_hospitales = """
create table if not exists hospitales (
    ncodi INT primary key,
    name VARCHAR(300)
);
"""

# Tipos
query_creation_tipo_hosp = """
create table if not exists tipo_hospitalizacion (
    tipo_id SERIAL primary key,
    nombre VARCHAR(100) unique not null
    );
"""

# Gastos
query_creation_gastos = """
create table if not exists gastos (
    gastos_id INT primary key,
    año INT not null,
    ncodi INT not null,
    totalcompra DECIMAL(10, 2) not null, 
    producfarma DECIMAL(10, 2) not null, 
    materialsani DECIMAL(10, 2) not null, 
    implantes DECIMAL(10, 2) not null, 
    restomateriasani DECIMAL(10, 2) not null, 
    servcontratado DECIMAL(10, 2) not null, 
    trabajocontratado DECIMAL(10, 2) not null, 
    xrestocompras DECIMAL(10, 2) not null, 
    variaexistencias DECIMAL(10, 2) not null, 
    servexteriores DECIMAL(10, 2) not null, 
    sumistro DECIMAL(10, 2) not null, 
    xrestoserviexter DECIMAL(10, 2) not null, 
    gastopersonal DECIMAL(10, 2) not null, 
    sueldos DECIMAL(10, 2) not null, 
    indemnizacion DECIMAL(10, 2) not null, 
    segsocempresa DECIMAL(10, 2) not null, 
    otrgassocial DECIMAL(10, 2) not null, 
    dotaamortizacion DECIMAL(10, 2) not null, 
    perdidadeterioro DECIMAL(10, 2) not null, 
    xrestogasto DECIMAL(10, 2) not null, 
    totcompragasto DECIMAL(10, 2) not null,
    foreign key (ncodi) references hospitales(ncodi)
);
"""

# Ingresos
query_creation_ingresos = """
create table if not exists ingresos (
    id_ingresos INT primary key,
    ncodi INT not null,
    particulares DECIMAL(10, 2),
    aseguradoras DECIMAL(10, 2),
    aseguradoras_enfermedad DECIMAL(10, 2),
    aseguradoras_trafico DECIMAL(10, 2),
    mutuas DECIMAL(10, 2),
    tipo_id INT not null,
    foreign key (ncodi) references hospitales(ncodi),
    foreign key (tipo_id) references tipo_hospitalizacion(tipo_id)
);"""