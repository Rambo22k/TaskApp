import { Component } from '@angular/core';
import { Tarea } from '../models/tarea';
import { TareasService } from '../services/tareas.service';

@Component({
  selector: 'app-home',
  templateUrl: './home.page.html',
  styleUrls: ['./home.page.scss'],
  standalone: false,
})
export class HomePage {
  tareas: Tarea[] = [];

  constructor(private readonly tareasService: TareasService) {}

  ionViewWillEnter(): void {
    this.tareas = this.tareasService.obtenerTodas();
  }

  cambiarEstado(tarea: Tarea, event: CustomEvent): void {
    const completada = Boolean((event as CustomEvent<{ checked: boolean }>).detail.checked);
    this.tareasService.cambiarEstado(tarea.id, completada);
    this.tareas = this.tareasService.obtenerTodas();
  }

  eliminar(id: string): void {
    this.tareasService.eliminar(id);
    this.tareas = this.tareasService.obtenerTodas();
  }
}
