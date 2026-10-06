from pathlib import Path
from reportlab.lib import colors
from reportlab.lib.enums import TA_CENTER
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak

out = Path(__file__).with_name("paso-a-paso-taskapp.pdf")
styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="Cover", parent=styles["Title"], fontSize=30, leading=36, textColor=colors.HexColor("#202B4C"), alignment=TA_CENTER, spaceAfter=12))
styles.add(ParagraphStyle(name="Section", parent=styles["Heading1"], fontSize=18, leading=23, textColor=colors.HexColor("#5267DF"), spaceBefore=8, spaceAfter=10))
styles.add(ParagraphStyle(name="Body", parent=styles["BodyText"], fontSize=10, leading=15, textColor=colors.HexColor("#3F4964"), spaceAfter=8))
styles.add(ParagraphStyle(name="CodeBox", parent=styles["Code"], fontSize=9, leading=14, backColor=colors.HexColor("#F1F3FA"), borderPadding=8, spaceAfter=10))
def p(text, kind="Body"): return Paragraph(text, styles[kind])
story = [
 Spacer(1, 35*mm), p("TaskApp", "Cover"),
 p("Guía paso a paso de desarrollo", "Heading2"),
 Spacer(1, 10*mm),
 p("Aplicación híbrida para organizar deberes y tareas académicas con Ionic y Angular."),
 p("<b>Tecnologías:</b> Ionic, Angular, TypeScript, formularios reactivos y localStorage."),
 PageBreak(),
 p("1. Preparar el proyecto", "Section"),
 p("El proyecto utiliza páginas Angular independientes para el listado y el formulario. Instala las dependencias y arranca el servidor de desarrollo:"),
 p("npm install<br/>npx ionic serve", "CodeBox"),
 p("2. Definir el modelo y centralizar los datos", "Section"),
 p("La interfaz Tarea declara id, titulo, descripcion, prioridad y completada. Prioridad admite Alta, Media y Baja. El servicio TareasService concentra la consulta, creación, actualización y eliminación de tareas."),
 p("El servicio recupera el arreglo desde localStorage al iniciarse y guarda cada cambio como JSON. De este modo, los datos permanecen en el navegador al recargar la aplicación."),
 p("<b>Archivos:</b> src/app/models/tarea.ts y src/app/services/tareas.service.ts."),
 PageBreak(),
 p("3. Construir el listado principal", "Section"),
 p("La pantalla principal utiliza ion-header, ion-content e ion-footer. ion-list e ion-item muestran título, descripción e ion-badge con el color asociado a la prioridad. Si todavía no hay tareas, aparece un estado vacío con una invitación a crear una."),
 p("El ion-checkbox marca una tarea como completada y aplica tachado al texto. El botón con icono trash elimina la tarea. El ion-fab abre la pantalla de registro."),
 p("4. Crear el formulario reactivo", "Section"),
 p("La página NuevaTareaPage usa FormBuilder y ReactiveFormsModule. El título es obligatorio y debe tener al menos cinco caracteres; la descripción es obligatoria y admite hasta 160 caracteres. La prioridad inicia en Media."),
 p("Cuando el formulario es válido, guarda la tarea mediante el servicio y vuelve al listado. Si hay errores, marca los campos y muestra mensajes de validación."),
 p("<b>Archivos:</b> src/app/nueva-tarea/nueva-tarea.page.ts y sus archivos HTML y SCSS."),
 PageBreak(),
 p("5. Configurar navegación y ejecutar", "Section"),
 p("La ruta raíz redirige a /home. El formulario se encuentra en /nueva-tarea; al guardar, cancelar o volver atrás se regresa a la lista."),
 p("Instala y ejecuta en desarrollo con:"),
 p("npm install<br/>npx ionic serve", "CodeBox"),
 p("También se puede usar npm start para iniciar el servidor de Angular."),
 p("6. Usar TaskApp", "Section"),
 p("1. Pulsa + para crear una tarea.<br/>2. Escribe un título de cinco caracteres o más, una descripción y selecciona la prioridad.<br/>3. Guarda para añadirla a la lista.<br/>4. Marca la casilla para completarla o pulsa la papelera para eliminarla.<br/>5. Recarga el navegador para comprobar la persistencia local."),
 p("Estructura: src/app/home contiene el listado; src/app/nueva-tarea, el formulario; src/app/models, el modelo; src/app/services, la persistencia; README.md, las instrucciones.")
]
def footer(canvas, doc):
 canvas.saveState()
 canvas.setFont("Helvetica", 8)
 canvas.setFillColor(colors.HexColor("#8A91A5"))
 canvas.drawString(20*mm, 12*mm, "TaskApp · Guía de desarrollo")
 canvas.drawRightString(190*mm, 12*mm, str(doc.page))
 canvas.restoreState()
SimpleDocTemplate(str(out), pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=20*mm, bottomMargin=22*mm, title="TaskApp - Paso a paso").build(story, onFirstPage=footer, onLaterPages=footer)
print(out)
