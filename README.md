# TaskApp

Aplicación híbrida de gestión de tareas académicas creada con Ionic y Angular. Permite crear tareas, asignarles prioridad, marcar su estado, eliminarlas y conservar los datos en el navegador mediante `localStorage`.

## Requisitos

- Node.js y npm instalados.
- Ionic CLI (opcional): `npm install -g @ionic/cli`.

## Instalación y ejecución

Desde la carpeta del proyecto, ejecuta:

```bash
npm install
npx ionic serve
```

También puedes iniciar el servidor de Angular con `npm start`. La aplicación se abrirá en el navegador y se recargará al guardar cambios.

## Funciones

- Listado con título, descripción, prioridad y estado.
- Formulario reactivo: título obligatorio con mínimo 5 caracteres y descripción obligatoria de hasta 160 caracteres.
- Completar y eliminar tareas.
- Persistencia local en el navegador. Los datos pertenecen al navegador y dispositivo donde se crean.

## Estructura principal

- `src/app/home`: listado principal.
- `src/app/nueva-tarea`: formulario de alta.
- `src/app/models/tarea.ts`: modelo e interfaz de prioridad.
- `src/app/services/tareas.service.ts`: estado y persistencia local.


