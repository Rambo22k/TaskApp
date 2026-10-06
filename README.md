# TaskApp

Aplicación móvil híbrida para organizar deberes y tareas académicas, desarrollada con Ionic y Angular.

**Repositorio:** [github.com/Rambo22k/TaskApp](https://github.com/Rambo22k/TaskApp)

## Funcionalidades

- Lista de tareas con título, descripción y prioridad Alta, Media o Baja.
- Creación de tareas mediante un formulario reactivo con validaciones.
- Título obligatorio con un mínimo de 5 caracteres.
- Descripción obligatoria de hasta 160 caracteres.
- Marcado de tareas completadas con el texto tachado.
- Eliminación de tareas.
- Persistencia en `localStorage` para conservar los datos al recargar la aplicación en el mismo navegador y dispositivo.
- Interfaz adaptada a dispositivos móviles con componentes Ionic.

## Requisitos

- Node.js y npm.
- Ionic CLI (opcional): `npm install -g @ionic/cli`.

## Instalar y ejecutar

En la carpeta del proyecto, instala las dependencias y ejecuta el servidor de desarrollo:

```bash
npm install
npx ionic serve
```

También puedes iniciar el servidor de Angular con:

```bash
npm start
```

## Estructura principal

- `src/app/home`: pantalla principal y listado de tareas.
- `src/app/nueva-tarea`: formulario para crear una tarea.
- `src/app/models/tarea.ts`: interfaz de datos y tipo de prioridad.
- `src/app/services/tareas.service.ts`: operaciones y persistencia de tareas.


