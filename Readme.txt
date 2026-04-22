# 📱 Senda URJC - Prototipo Backend + Frontend

## 📌 Descripción del proyecto

Este repositorio contiene un **prototipo funcional** del sistema *Senda URJC*, desarrollado para la asignatura de Análisis e Ingeniería de Requisitos.

El objetivo del sistema es proporcionar rutas seguras dentro del campus universitario, incorporando funcionalidades de seguridad como el modo *“Voy contigo”* y el reporte de incidencias.

---

## 🧱 Arquitectura del sistema

El proyecto sigue una arquitectura cliente-servidor:

* **Backend**: API REST desarrollada en Python con FastAPI
* **Frontend**: Interfaz web desarrollada en React

---

## ⚙️ Requisitos previos

Antes de ejecutar la aplicación, instala:

* Python 3.8 o superior
* Node.js (v16 o superior)
* npm

---

## 📁 Estructura del repositorio

```
/backend
 ├── main.py
 ├── models.py
 ├── database.py
 ├── auth.py
 ├── routes_api.py
 ├── voy_contigo.py
 ├── incidents.py
 └── stats.py

/frontend
 ├── src/
 │   ├── App.js
 │   ├── Login.js
 │   ├── Routes.js
 │   ├── VoyContigo.js
 │   ├── Incident.js
 │   └── api.js
```

---

## 🚀 Despliegue y ejecución

### 🔧 1. Backend

#### Instalación de dependencias

```bash
cd backend
pip install fastapi uvicorn
```

#### Ejecución del servidor

```bash
uvicorn main:app --reload
```

El backend estará disponible en:
👉 [http://127.0.0.1:8000](http://127.0.0.1:8000)

Documentación interactiva:
👉 [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

---

### 🌐 2. Frontend

#### Instalación

```bash
cd frontend
npm install
```

#### Ejecución

```bash
npm start
```

La aplicación se abrirá en:
👉 [http://localhost:3000](http://localhost:3000)

---

## 🔗 Configuración de conexión

El frontend se conecta al backend en:

```
http://127.0.0.1:8000
```

Si se modifica, actualizar:

```
frontend/src/api.js
```

---

## 🧪 Funcionalidades disponibles

### 🔐 Autenticación

* Endpoint: `/login`
* Usuario de prueba:

  * [user@urjc.es](mailto:user@urjc.es)
  * 1234

---

### 🗺️ Rutas seguras

* Endpoint: `/routes`
* Genera hasta 3 rutas
* Ordenadas por índice de seguridad

---

### 🛡️ Modo “Voy contigo”

* `/voy_contigo/start`
* `/voy_contigo/check`
* Simula seguimiento y prealertas

---

### ⚠️ Incidencias

* `/incident`
* Permite registrar incidencias del entorno

---

### 📊 Estadísticas

* `/stats`
* Muestra número total de incidencias

---

## 🧠 Consideraciones técnicas

* Sistema prototipo (no producción)
* Datos almacenados en memoria
* Algoritmos simplificados
* Sin autenticación real SSO

---

## 🔄 Posibles mejoras

* Base de datos real (SQLite/PostgreSQL)
* Autenticación JWT
* Integración con mapas (Leaflet / Google Maps)
* Notificaciones en tiempo real
* Aplicación móvil

---

## 📘 Uso académico

Este proyecto ha sido desarrollado exclusivamente con fines académicos.

---

## 👨‍💻 Autor

Estudiante de Ingeniería del Software - URJC

---

##
