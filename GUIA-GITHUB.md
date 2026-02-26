# 📤 Guía para Subir BAKIFLOW a GitHub

---

## 🎯 PASO A PASO: Subir tu Proyecto

### **PASO 1: Crear Repositorio en GitHub**

1. Ve a https://github.com
2. Click en **"New"** (o el botón +)
3. Llena los datos:
   - **Repository name**: `bakiflow`
   - **Description**: "Ecommerce de ropa seminueva - Proyecto de Desarrollo Web"
   - **Public** (para que tu profesor lo vea)
   - ❌ NO marques: "Add a README file"
   - ❌ NO marques: "Add .gitignore"
   - ❌ NO marques: "Choose a license"
4. Click en **"Create repository"**

GitHub te mostrará una página con comandos. **Déjala abierta.**

---

### **PASO 2: Configurar Git (solo primera vez)**

```bash
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"
```

**Ejemplo:**
```bash
git config --global user.name "Juan Pérez"
git config --global user.email "juan.perez@up.edu.mx"
```

**⚠️ Importante:** Usa el mismo email de tu cuenta de GitHub.

---

### **PASO 3: Inicializar Git en tu Proyecto**

```bash
# Ve a la carpeta de tu proyecto
cd bakiflow

# Inicializa Git
git init

# Verifica que estés en la carpeta correcta
ls
# Deberías ver: backend.py, index.html, docker-compose.yml, etc.
```

---

### **PASO 4: Agregar Archivos al Repositorio**

```bash
# Ver qué archivos hay
git status

# Agregar TODOS los archivos
git add .

# Ver que están listos para commit
git status
# Deberías ver archivos en verde
```

---

### **PASO 5: Hacer tu Primer Commit**

```bash
git commit -m "Initial commit: BAKIFLOW con funcionalidades completas"
```

**¿Qué es un commit?**
Es como una "foto" de tu proyecto en este momento. Queda guardado en el historial.

---

### **PASO 6: Conectar con GitHub**

Copia la URL de tu repositorio de GitHub (la que te mostró al crear el repo):

```
https://github.com/TU-USUARIO/bakiflow.git
```

Ejecuta:

```bash
git remote add origin https://github.com/TU-USUARIO/bakiflow.git

# Verifica que se conectó
git remote -v
```

---

### **PASO 7: Subir tu Código a GitHub**

```bash
# Cambiar nombre de rama a "main"
git branch -M main

# Subir todo a GitHub
git push -u origin main
```

**GitHub te pedirá autenticación:**
- Username: Tu usuario de GitHub
- Password: **Token de acceso personal** (NO tu contraseña)

#### Cómo crear un token:

1. GitHub → Click en tu foto → **Settings**
2. Scroll abajo → **Developer settings**
3. **Personal access tokens** → **Tokens (classic)**
4. **Generate new token** → **Generate new token (classic)**
5. Nombre: "BAKIFLOW local"
6. Marca: ☑️ `repo` (full control)
7. Scroll abajo → **Generate token**
8. **¡COPIA EL TOKEN!** (solo lo verás una vez)
9. Pégalo cuando te pida "Password"

---

### **PASO 8: Verificar en GitHub**

Abre tu navegador y ve a:
```
https://github.com/TU-USUARIO/bakiflow
```

**Deberías ver todos tus archivos** ✅

---

## 📝 Hacer Cambios Posteriores

Cuando hagas cambios en tu código:

```bash
# 1. Ver qué cambió
git status

# 2. Agregar cambios
git add .

# 3. Hacer commit con mensaje descriptivo
git commit -m "Agrego funcionalidad de búsqueda de productos"

# 4. Subir a GitHub
git push
```

---

## 🎓 Para tu Entrega

### **Opción 1: Link del repositorio completo**

Envía:
```
https://github.com/TU-USUARIO/bakiflow
```

### **Opción 2: Link de commit específico**

Si hiciste varios commits y quieres mostrar uno específico:

1. Ve a tu repositorio en GitHub
2. Click en **"Commits"**
3. Click en el commit que quieres mostrar
4. Copia la URL, será algo como:
   ```
   https://github.com/TU-USUARIO/bakiflow/commit/abc1234567890
   ```

---

## 📊 Comandos Rápidos Completos

```bash
# Configurar Git (solo una vez)
git config --global user.name "Tu Nombre"
git config --global user.email "tu@email.com"

# Ir al proyecto
cd bakiflow

# Inicializar Git
git init

# Agregar todos los archivos
git add .

# Primer commit
git commit -m "Initial commit: BAKIFLOW con funcionalidades completas"

# Conectar con GitHub
git remote add origin https://github.com/TU-USUARIO/bakiflow.git

# Subir
git branch -M main
git push -u origin main
```

---

## ✅ Checklist de Entrega

- [ ] Repositorio creado en GitHub
- [ ] Código subido correctamente
- [ ] README.md visible en GitHub
- [ ] Todos los archivos presentes:
  - [ ] backend.py
  - [ ] index.html
  - [ ] agregar-producto.html
  - [ ] styles.css
  - [ ] docker-compose.yml
  - [ ] database/init.sql
  - [ ] requirements.txt
  - [ ] README.md
- [ ] Link del repositorio copiado
- [ ] Link enviado al profesor

---

## 🎯 Formato del Mensaje para tu Profesor

```
Profesor,

Le comparto el link de mi proyecto BAKIFLOW:
https://github.com/TU-USUARIO/bakiflow

Funcionalidades implementadas:
1. Vista adicional: agregar-producto.html (formulario para crear productos)
2. Endpoint POST /productos en el backend (crea productos en la BD)
3. Script SQL: database/init.sql (inicializa tablas y datos)
4. README.md con instrucciones completas de inicialización

Saludos,
[Tu nombre]
```

---

## 🐛 Problemas Comunes

### Error: "remote origin already exists"

```bash
git remote remove origin
git remote add origin https://github.com/TU-USUARIO/bakiflow.git
```

### Error: "failed to push"

```bash
git pull origin main --allow-unrelated-histories
git push -u origin main
```

### Error: "Authentication failed"

Necesitas usar un **Personal Access Token**, no tu contraseña de GitHub.

---

¡Listo para subir! 🚀
