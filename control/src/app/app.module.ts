import { BrowserModule } from '@angular/platform-browser';
import { AppComponent } from './app.component';
import {FormsModule} from '@angular/forms';
import {BrowserAnimationsModule} from '@angular/platform-browser/animations';
import {CUSTOM_ELEMENTS_SCHEMA, NgModule} from '@angular/core';
import {RouterModule, Routes} from '@angular/router';
import { SignInComponent } from './sign-in/sign-in.component';
import { NgZorroAntdModule } from 'ng-zorro-antd';
import { MainComponent } from './main/main.component';

const appRoutes: Routes = [
  {path: '', redirectTo: 'signin', pathMatch: 'full'},
  {path: 'signin', component: SignInComponent},
  {path: 'main', component: MainComponent},
];
@NgModule({
  declarations: [
    AppComponent,
    SignInComponent,
    MainComponent
  ],
  imports: [
    FormsModule,
    BrowserModule,
    BrowserAnimationsModule,
    RouterModule.forRoot(appRoutes),
    NgZorroAntdModule.forRoot(),
  ],
  providers: [],
  schemas: [CUSTOM_ELEMENTS_SCHEMA],
  bootstrap: [AppComponent]
})
export class AppModule { }
