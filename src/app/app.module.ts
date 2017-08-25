import { NgModule } from '@angular/core';
import { FormsModule } from '@angular/forms'
import { HttpModule } from '@angular/http'
import { BrowserModule } from '@angular/platform-browser';
import { RouterModule, Routes } from '@angular/router'

import { AdminComponent } from "./admin.component"
import { AlertComponent } from "./alert.component"
import { AppComponent } from './app.component';
import { LoginComponent } from "./login.component";
import { MentorComponent } from "./mentor.component"
import { AlertService } from "./services/alert.service"
import { AuthenticationService} from "./services/authentication.service"
import { TeamService } from "./services/team.service"


export const ROUTES: Routes = [
  {path: '', redirectTo: '/login', pathMatch: 'full'},
  {path: 'login', component: LoginComponent},
  {path: 'logout', redirectTo: '/login', pathMatch: 'full'},
  {path: 'admin', component: AdminComponent},
  {path: 'mentor', component: MentorComponent}
];

@NgModule({
  declarations: [
    AdminComponent,
    AlertComponent,
    AppComponent,
    LoginComponent,
    MentorComponent
  ],
  imports: [
    BrowserModule,
    FormsModule,
    HttpModule,
    RouterModule.forRoot(ROUTES)
  ],
  providers: [
    AlertService,
    AuthenticationService,
    TeamService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
