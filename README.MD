# 🚀 Actividad: Contribuyendo al Procesador de Datos

¡Bienvenido al proyecto! Para mantener la integridad de nuestro código, no permitimos cambios directos en la rama principal. Debes proponer tus mejoras mediante un **Pull Request**.

## 📋 Tu Misión
Debes implementar la lógica de limpieza de nombres en `main.py` para que la función `procesar_nombres` cumpla con:
1. **Limpieza:** Quitar espacios en blanco laterales.
2. **Normalización:** Formato "Nombre" (Mayúscula inicial, resto minúscula).
3. **Seguridad:** Ignorar cualquier entrada que esté vacía después de limpiar.

## 🛠️ Pasos de la Actividad

### 1. Fork del Proyecto
Haz clic en el botón **"Fork"** en la esquina superior derecha de este repositorio para crear una copia en tu cuenta.

### 2. Clonar y Trabajar
Clona **tu fork** localmente:
```bash
git clone [https://github.com/TU_USUARIO/nombre-del-repo.git](https://github.com/TU_USUARIO/nombre-del-repo.git)
cd nombre-del-repo
```

Implementa la lógica en el archivo. Verifica que funcione ejecutando:

```bash
python main.py
```

### 3. Subir cambios a tu Fork

```bash
git add main.py
git commit -m "Implementación de lógica de limpieza"
git push origin main
```

### 4. Abrir el Pull Request (PR)
Ve a tu repositorio en GitHub y haz clic en "New Pull Request". Asegúrate de que apunte al repositorio original del profesor.

### 5. El Conflicto ⚠️
El "Maintainer" (profesor) ha actualizado el código base mientras tú trabajabas. GitHub te avisará que "This branch has conflicts that must be resolved".

### 6. Resolución del Conflicto
Para solucionar esto desde tu máquina:

Agrega el repositorio original como remoto:

```bash
git remote add upstream https://github.com/EricRamirezS/FullStack-MergeConflicts.git
```

Trae los cambios del profesor:

```bash
git fetch upstream
git merge upstream/main
```

Resuelve el conflicto en el archivo, guarda, haz commit y vuelve a subir (push) a tu fork. ¡El Pull Request se actualizará automáticamente!
