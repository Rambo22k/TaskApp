import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ReactiveFormsModule } from '@angular/forms';

import { IonicModule } from '@ionic/angular/lazy';

import { NuevaTareaPageRoutingModule } from './nueva-tarea-routing.module';

import { NuevaTareaPage } from './nueva-tarea.page';

@NgModule({
  imports: [
    CommonModule,
    ReactiveFormsModule,
    IonicModule,
    NuevaTareaPageRoutingModule
  ],
  declarations: [NuevaTareaPage]
})
export class NuevaTareaPageModule {}
