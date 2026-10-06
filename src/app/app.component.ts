import { Component } from '@angular/core';
@Component({
  selector: 'app-root',
  templateUrl: 'app.component.html',
  styleUrls: ['app.component.scss'],
  standalone: false,
})
export class AppComponent {
  protected readonly appPages = [
    
    { title: 'Mis tareas', url: '/home', icon: 'checkbox' },
    { title: 'Nueva tarea', url: '/nueva-tarea', icon: 'add-circle' },

  ];
}
