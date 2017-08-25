import { Injectable } from '@angular/core'
import { Headers, Http, Response } from '@angular/http'

import 'rxjs/add/operator/map'
import 'rxjs/add/operator/mergeMap'

@Injectable()
export class AuthenticationService {
  constructor(private http: Http) {}

  private uerType() {
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');

    let currentUser = JSON.parse(localStorage.getItem('currentUser'));
    headers.append('Authorization', `JWT ${ currentUser.token }`);

    return this.http.get(
      'http://localhost:8000/api/v1/usertype/',
      {headers: headers}
    ).map((response: Response) => {
      let userType = response.json();
      localStorage.setItem('userType', userType.user_type)
    });
  }

  login(username: string, password: string){
    let headers = new Headers();
    headers.append('Content-Type', 'application/json');

    return this.http.post(
      'http://localhost:8000/api/v1/authenticate/',
      JSON.stringify({username: username, password: password}),
      {headers: headers}
    ).flatMap((response: Response) => {
      let user = response.json();
      if (user && user.token) {
        localStorage.setItem('currentUser', JSON.stringify(user));
      }
      return this.uerType();
    });
  }

  logout() {
    localStorage.removeItem('currentUser');
    localStorage.removeItem('userType');
  }
}
