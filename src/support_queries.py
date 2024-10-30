# Centro hospitalario identificador de hosñitales y nombres 
query_creation_hospitales = """
create table if not exists hospitales (
    ncodi INT primary key,
    name VARCHAR(300)
);
"""

# Tipos de hospityalizacion de los hospitales 
query_creation_tipo_hosp = """
create table if not exists tipo_hospitalizacion (
    tipo_id SERIAL primary key,
    nombre VARCHAR(100) unique not null
    );
"""

# Gastos
query_creation_gastos = """
create table if not exists gastos (
    gastos_id SERIAL primary key,
    año INT not null,
    totalcompra NUMERIC , 
    producfarma NUMERIC , 
    materialsani NUMERIC , 
    implantes NUMERIC , 
    restomateriasani NUMERIC , 
    servcontratado NUMERIC , 
    trabajocontratado NUMERIC , 
    xrestocompras NUMERIC , 
    variaexistencias NUMERIC , 
    servexteriores NUMERIC , 
    sumistro NUMERIC , 
    xrestoserviexter NUMERIC , 
    gastopersonal NUMERIC , 
    sueldos NUMERIC , 
    indemnizacion NUMERIC , 
    segsocempresa NUMERIC , 
    otrgassocial NUMERIC , 
    dotaamortizacion NUMERIC , 
    perdidadeterioro NUMERIC , 
    xrestogasto NUMERIC , 
    totcompragasto NUMERIC,
    ncodi INT references hospitales(ncodi)
);
"""

# Ingresos hospitalizaciones 
query_creation_ingresos = """
create table if not exists ingresos (
    id_ingresos serial primary key,
    particulares NUMERIC,
    aseguradoras NUMERIC,
    aseguradoras_enfermedad NUMERIC,
    aseguradoras_trafico NUMERIC,
    mutuas NUMERIC,
    ncodi references hospitales(ncodi),
    tipo_id references tipo_hospitalizacion(tipo_id)
);"""