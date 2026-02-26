-- ==========================================
-- SCRIPT DE INICIALIZACIÓN - BAKIFLOW
-- ==========================================
-- Crea las tablas y datos iniciales del proyecto

-- Eliminar tablas si existen (para poder recrearlas)
DROP TABLE IF EXISTS carrito;
DROP TABLE IF EXISTS productos;

-- ==========================================
-- TABLA 1: PRODUCTOS
-- ==========================================
-- Almacena la información de la ropa seminueva

CREATE TABLE productos (
    id SERIAL PRIMARY KEY,
    nombre VARCHAR(200) NOT NULL,
    descripcion TEXT,
    categoria VARCHAR(100),
    talla VARCHAR(20),
    precio DECIMAL(10, 2) NOT NULL,
    condicion VARCHAR(50),
    imagen_url VARCHAR(500),
    disponible BOOLEAN DEFAULT true,
    stock INTEGER DEFAULT 1,
    creado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

-- ==========================================
-- TABLA 2: CARRITO
-- ==========================================
-- Almacena los productos que el usuario agregó al carrito

CREATE TABLE carrito (
    id SERIAL PRIMARY KEY,
    producto_id INTEGER NOT NULL,
    cantidad INTEGER DEFAULT 1,
    agregado_en TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (producto_id) REFERENCES productos(id) ON DELETE CASCADE
);

-- ==========================================
-- INSERTAR PRODUCTOS DE EJEMPLO
-- ==========================================

INSERT INTO productos (nombre, descripcion, categoria, talla, precio, condicion, imagen_url, disponible, stock) 
VALUES
    (
        'Chamarra de Mezclilla Vintage',
        'Chamarra clásica de mezclilla en excelente estado, estilo retro años 90. Perfecta para darle vida a tu look casual.',
        'Chamarras',
        'M',
        450.00,
        'Excelente',
        'https://images.unsplash.com/photo-1551028719-00167b16eac5?w=400',
        true,
        3
    ),
    (
        'Sudadera Negra Básica',
        'Sudadera negra con capucha, muy cómoda para el día a día. Segunda vida garantizada.',
        'Sudaderas',
        'L',
        280.00,
        'Muy Buena',
        'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400',
        true,
        5
    ),
    (
        'Jeans Azul Clásico',
        'Pantalón de mezclilla corte recto, color azul índigo. Estilo atemporal que nunca pasa de moda.',
        'Pantalones',
        '32',
        350.00,
        'Buena',
        'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400',
        true,
        2
    ),
    (
        'Playera Blanca Vintage',
        'Playera básica blanca de algodón, suave y en buen estado. Un clásico que siempre funciona.',
        'Playeras',
        'S',
        150.00,
        'Muy Buena',
        'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400',
        true,
        7
    ),
    (
        'Abrigo Gris Lana',
        'Abrigo largo de lana gris, elegante y abrigador. Dale una segunda oportunidad a este abrigo de calidad.',
        'Abrigos',
        'L',
        850.00,
        'Excelente',
        'https://images.unsplash.com/photo-1539533018447-63fcce2678e3?w=400',
        true,
        1
    );

-- Verificar que se insertaron correctamente
SELECT * FROM productos;

-- ==========================================
-- NOTAS
-- ==========================================
-- La tabla 'carrito' inicia vacía (sin productos)
-- Los productos tienen stock para simular inventario real
-- FOREIGN KEY asegura que solo existan productos válidos en el carrito
