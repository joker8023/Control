import { NgModule } from '@angular/core';
import { CommonModule } from '@angular/common';

@NgModule({
  imports: [
    CommonModule
  ],
  declarations: []
})

const mainRoutes: Routes = [
  {path: 'usermanagement', component: UserManagementComponent},]
export class MainModule { }
