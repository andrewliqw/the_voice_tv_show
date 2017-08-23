import { Component, OnInit } from '@angular/core'
import { ActivatedRoute, Router } from '@angular/router'

import { AlertService } from "./services/alert.service"
import { AuthenticationService } from './services/authentication.service'

@Component({
  selector: 'login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {
  model: any = {};
  loading = false;
  returnUrl: string;

  constructor(
    private alertService: AlertService,
    private authenticationService: AuthenticationService,
    private route: ActivatedRoute,
    private router: Router
  ) {}

  ngOnInit() {
    this.authenticationService.logout();

    this.returnUrl = this.route.snapshot.queryParams['returnUrl'] || '/';
  }

  login() {
    this.loading = true;
    this.authenticationService.login(
      this.model.username,
      this.model.password
    ).subscribe(
      data => {
        let userType = localStorage.getItem('userType');
        if (userType === 'admin') {
          this.router.navigate(['/admin']);
        } else {
          this.router.navigate(['/mentor']);
        }
      },
      error => {
        this.alertService.error(error);
        this.loading = false;
      }
    );
  }
}
