import { Component } from '@angular/core';
import { FormBuilder, Validators } from '@angular/forms';
import { NavController } from '@ionic/angular/lazy';
import { Prioridad } from '../models/tarea';
import { TareasService } from '../services/tareas.service';

@Component({
  selector: 'app-nueva-tarea',
  templateUrl: './nueva-tarea.page.html',
  styleUrls: ['./nueva-tarea.page.scss'],
  standalone: false,
})
export class NuevaTareaPage {
  enviado = false;
  readonly formulario = this.fb.nonNullable.group({
    titulo: ['', [Validators.required, Validators.minLength(5)]],
    descripcion: ['', [Validators.required, Validators.maxLength(160)]],
    prioridad: ['Media' as Prioridad, Validators.required],
  });

  constructor(private readonly fb: FormBuilder, private readonly tareasService: TareasService, private readonly nav: NavController) {}

  guardar(): void {
    this.enviado = true;
    if (this.formulario.invalid) {
      this.formulario.markAllAsTouched();
      return;
    }
    this.tareasService.agregar(this.formulario.getRawValue());
    this.nav.navigateRoot('/home');
  }
}
