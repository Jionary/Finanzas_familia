CREATE TABLE IF NOT EXISTS usuarios(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL
);

CREATE TABLE IF NOT EXISTS categorias(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    tipo TEXT CHECK(tipo IN ('GASTO', 'INGRESO')) NOT NULL
);

CREATE TABLE IF NOT EXISTS tickets(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    establecimiento TEXT NOT NULL,
    fecha DATE NOT NULL,
    monto_total REAL DEFAULT 0.0,
    notas TEXT,
    creado_en DATETIME DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE
);

CREATE TABLE IF NOT EXISTS tickets_items(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    ticket_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    concepto TEXT NOT NULL, 
    cantidad REAL DEFAULT 1.0,
    precio_unitario REAL NOT NULL,
    monto_subtotal REAL GENERATED ALWAYS AS (cantidad * precio_unitario) STORED,
    FOREIGN KEY (ticket_id) REFERENCES tickets(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);

CREATE TABLE IF NOT EXISTS gastos_fijos(
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    usuario_id INTEGER NOT NULL,
    categoria_id INTEGER NOT NULL,
    concepto TEXT NOT NULL,
    monto REAL NOT NULL,
    frecuencia TEXT CHECK (frecuencia IN ('MENSUAL', 'ANUAL')) DEFAULT 'MENSUAL',
    dia_pago INTEGER CHECK (dia_pago BETWEEN 1 AND 31),
    activo INTEGER DEFAULT 1,
    FOREIGN KEY (usuario_id) REFERENCES usuarios(id) ON DELETE CASCADE,
    FOREIGN KEY (categoria_id) REFERENCES categorias(id)
);