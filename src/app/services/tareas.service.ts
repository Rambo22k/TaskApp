import { Injectable } from '@angular/core';
import { Tarea } from '../models/tarea';

const STORAGE_KEY = 'taskapp-tareas';

@Injectable({ providedIn: 'root' })
export class TareasService {
  private tareas: Tarea[] = this.cargar();

  obtenerTodas(): Tarea[] {
    return [...this.tareas];
  }

  agregar(datos: Omit<Tarea, 'id' | 'completada'>): void {
    this.tareas = [{ ...datos, id: globalThis.crypto?.randomUUID?.() ?? `${Date.now()}-${Math.random()}`, completada: false }, ...this.tareas];
    this.guardar();
  }

  cambiarEstado(id: string, completada: boolean): void {
    this.tareas = this.tareas.map(tarea => tarea.id === id ? { ...tarea, completada } : tarea);
    this.guardar();
  }

  eliminar(id: string): void {
    this.tareas = this.tareas.filter(tarea => tarea.id !== id);
    this.guardar();
  }

  private cargar(): Tarea[] {
    try {
      const datos = localStorage.getItem(STORAGE_KEY);
      return datos ? JSON.parse(datos) as Tarea[] : [];
    } catch {
      return [];
    }
  }

  private guardar(): void {
    localStorage.setItem(STORAGE_KEY, JSON.stringify(this.tareas));
  }
}
