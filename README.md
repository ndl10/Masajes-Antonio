# Primera version de centro de masajes Toñin,

# 💆‍♂️ Masajes Antonio - Proyecto Full Stack

Este proyecto es una práctica personal para aprender y experimentar con el desarrollo **Full Stack**, creando una especie de **plataforma de servicios de masajes** que podría evolucionar hacia un pequeño ecommerce o página de reservas.

---

## 🚀 Tecnologías usadas

### 🔹 Backend
- [Flask](https://flask.palletsprojects.com/) (API REST)
- [SQLite](https://www.sqlite.org/) (base de datos ligera para desarrollo)
- [SQLAlchemy](https://www.sqlalchemy.org/) (ORM)
- Gestión de usuarios, servicios y masajistas
- Primeros pasos con autenticación vía **JWT** (pendiente de refinar)

### 🔹 Frontend
- [React](https://react.dev/) con Vite
- React Router (navegación entre vistas)
- Context API para manejar la autenticación y estado global
- Estilos sencillos con CSS
- Listado de **servicios** y **masajistas** en formato **cards**

---

## 📌 Funcionalidades implementadas

✅ API con CRUD básico:
- **Usuarios** (creación, eliminación, roles admin/cliente)
- **Masajistas** (con especialidades e imágenes)
- **Servicios** (con precios, descripción, disponibilidad)
- **Ofertas** (relación entre masajistas y servicios)

✅ Frontend con dos vistas principales:
- Página de **Servicios** (listado en cards)
- Página de **Masajistas** (listado en cards)

✅ Contexto de autenticación en React (`AuthContext`):
- Guardado de token y rol en localStorage
- Control básico de login/logout

---

## ⚠️ Estado actual

El proyecto está en fase de **aprendizaje y pruebas**:
- Backend y frontend ya conectan y muestran datos.
- El sistema de **login con JWT** aún requiere ajustes para estar 100% funcional.
- Próximo objetivo: simplificar la experiencia de usuario (ej. integración directa con WhatsApp como canal de contacto).

---

## 📂 Estructura del proyecto

