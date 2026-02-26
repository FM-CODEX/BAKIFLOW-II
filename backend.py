# ==========================================
# BAKIFLOW - BACKEND 
# ==========================================
# Este servidor conecta el frontend con la base de datos
# Usando Flask y CORS

from flask import Flask, request, jsonify
from flask_cors import CORS
import psycopg2
from psycopg2.extras import RealDictCursor

# Configuración del servidor
app = Flask(__name__)
CORS(app)

# Configuración de la base de datos
DB_CONFIG = {
    'host': 'localhost',
    'port': 5432,
    'database': 'bakiflow_db',
    'user': 'bakiflow',
    'password': 'bakiflow123'
}

# Función A: Conectar a la BD
def get_db_connection():
    try:
        conn = psycopg2.connect(**DB_CONFIG, cursor_factory=RealDictCursor)
        return conn
    except Exception as e:
        print(f"Error conectando a la base de datos: {e}")
        return None

# ruta de prueba
@app.route("/")
def home():
    return jsonify({
        "message": "Bienvenido a BAKIFLOW API",
        "descripcion": "Dale vida a la ropa nuevamente",
        "version": "2.0.0",
        "endpoints": [
            "GET  /productos - Lista todos los productos",
            "GET  /productos/<id> - Detalle de un producto",
            "GET  /carrito - Ver carrito",
            "POST /carrito - Agregar producto al carrito",
            "DELETE /carrito/<id> - Eliminar del carrito",
            "DELETE /carrito - Vaciar carrito"
        ]
    })

# Funcionalidad 1: Obtener los productos
@app.route("/productos", methods=['GET'])
def get_productos():
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    try:
        # 2: Cursor
        cursor = conn.cursor()
        # 3: Query SQL
        cursor.execute("""
            SELECT id, nombre, descripcion, categoria, talla,    
                   precio, condicion, imagen_url, disponible, stock, creado_en
            FROM productos 
            WHERE disponible = true 
            ORDER BY creado_en DESC
        """)
        # 5: Resultado
        productos = cursor.fetchall()
        cursor.close()
        conn.close()
        
        # 6: Respuesta
        return jsonify({
            "success": True,
            "count": len(productos),
            "productos": productos
        }), 200
        
        #Si algo sale mal, retorna error
    except Exception as e:
        print(f"Error en /productos: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

#Funcionalidad 2: obtener productos por su ID
@app.route("/productos/<int:id>", methods=['GET'])
def get_producto_by_id(id):
    # 1: Conexión de BD
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT id, nombre, descripcion, categoria, talla, 
                   precio, condicion, imagen_url, disponible, stock, creado_en
            FROM productos 
            WHERE id = %s
        """, (id,))
        producto = cursor.fetchone()
        cursor.close()
        conn.close()
        # 6: Validamos si ecnontramos el producto
        if producto:
            return jsonify({"success": True, "producto": producto}), 200
        else:
            # 6: En caso de no encontrarlo, retorna error
            return jsonify({"success": False, "error": f"Producto con ID {id} no encontrado"}), 404
            
    except Exception as e:
        print(f"Error en /productos/{id}: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

#Funcionalidad 3: ver carrito
@app.route("/carrito", methods=['GET'])
def get_carrito():
    """
    Obtiene todos los productos del carrito con su información completa
    JOIN entre carrito y productos para mostrar detalles
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute("""
            SELECT 
                c.id as carrito_id,
                c.producto_id,
                c.cantidad,
                c.agregado_en,
                p.nombre,
                p.precio,
                p.imagen_url,
                p.categoria,
                p.talla,
                (p.precio * c.cantidad) as subtotal
            FROM carrito c
            INNER JOIN productos p ON c.producto_id = p.id
            ORDER BY c.agregado_en DESC
        """)
        items = cursor.fetchall()
        
        # Calcular total
        total = sum(float(item['subtotal']) for item in items)
        
        cursor.close()
        conn.close()
        
        return jsonify({
            "success": True,
            "items": items,
            "total": total,
            "cantidad_items": len(items)
        }), 200
        
    except Exception as e:
        print(f"Error en /carrito GET: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

#Funcionalidad 4: Agregar productos al carrito
@app.route("/carrito", methods=['POST'])
def agregar_al_carrito():
    """
    Agrega un producto al carrito
    Body: { "producto_id": 1, "cantidad": 2 }
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    try:
        data = request.get_json()
        producto_id = data.get('producto_id')
        cantidad = data.get('cantidad', 1)
        
        if not producto_id:
            return jsonify({"error": "Falta producto_id"}), 400
        
        cursor = conn.cursor()
        
        # Verificar que el producto existe y tiene stock
        cursor.execute("SELECT stock FROM productos WHERE id = %s", (producto_id,))
        producto = cursor.fetchone()
        
        if not producto:
            cursor.close()
            conn.close()
            return jsonify({"error": "Producto no encontrado"}), 404
        
        if producto['stock'] < cantidad:
            cursor.close()
            conn.close()
            return jsonify({"error": f"Stock insuficiente. Solo hay {producto['stock']} disponibles"}), 400
        
        # Verificar si ya está en el carrito
        cursor.execute("SELECT id, cantidad FROM carrito WHERE producto_id = %s", (producto_id,))
        item_existente = cursor.fetchone()
        
        if item_existente:
            # Actualizar cantidad
            nueva_cantidad = item_existente['cantidad'] + cantidad
            cursor.execute("""
                UPDATE carrito 
                SET cantidad = %s 
                WHERE id = %s
            """, (nueva_cantidad, item_existente['id']))
        else:
            # Insertar nuevo item
            cursor.execute("""
                INSERT INTO carrito (producto_id, cantidad) 
                VALUES (%s, %s)
            """, (producto_id, cantidad))
        
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({
            "success": True,
            "message": "Producto agregado al carrito"
        }), 201
        
    except Exception as e:
        print(f"Error en /carrito POST: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

#Funcionalidad 5: Eliminar producto del carrito
@app.route("/carrito/<int:carrito_id>", methods=['DELETE'])
def eliminar_del_carrito(carrito_id):
    """
    Elimina un item del carrito por su ID
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM carrito WHERE id = %s", (carrito_id,))
        conn.commit()
        
        if cursor.rowcount == 0:
            cursor.close()
            conn.close()
            return jsonify({"error": "Item no encontrado"}), 404
        
        cursor.close()
        conn.close()
        
        return jsonify({
            "success": True,
            "message": "Producto eliminado del carrito"
        }), 200
        
    except Exception as e:
        print(f"Error en /carrito DELETE: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

#Funcionalidad 6: Eliminar articulos del carrito
@app.route("/carrito", methods=['DELETE'])
def vaciar_carrito():
    """
    Elimina todos los items del carrito
    """
    conn = get_db_connection()
    if not conn:
        return jsonify({"error": "No se pudo conectar a la base de datos"}), 500
    
    try:
        cursor = conn.cursor()
        cursor.execute("DELETE FROM carrito")
        conn.commit()
        cursor.close()
        conn.close()
        
        return jsonify({
            "success": True,
            "message": "Carrito vaciado"
        }), 200
        
    except Exception as e:
        print(f"Error al vaciar carrito: {e}")
        return jsonify({"success": False, "error": str(e)}), 500

# Iniciamos el servidor, se ejecuta el servidor Flask 
if __name__ == '__main__':
    print("Iniciando servidor BAKIFLOW...")
    print("Servidor corriendo en: http://localhost:3000")
    print("Endpoints disponibles:")
    print("   - GET    /productos")
    print("   - GET    /productos/<id>")
    print("   - GET    /carrito")
    print("   - POST   /carrito")
    print("   - DELETE /carrito/<id>")
    print("   - DELETE /carrito")
    print("")
    print("Presiona Ctrl+C para detener el servidor")
    print("="*50)
    
    app.run(host="127.0.0.1", port=3000, debug=True)
