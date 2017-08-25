import { Component, OnInit } from '@angular/core'

import { TeamService } from './services/team.service'

@Component({
  selector: 'admin',
  templateUrl: './admin.component.html'
})
export class AdminComponent implements OnInit {
  allTeamNames: any;
  selectedTeamIDs: any;
  teamScores: any;

  // objectKeys = Object.keys;

  constructor(
    private teamService: TeamService
  ) {}

  ngOnInit() {
    this.getAllTeamNames();
  }

  private getAllTeamNames() {
    this.teamService.getAllTeamNames().subscribe(
      data => {
        this.allTeamNames = data;
      },
      error => {}
    );
  }

  getTeamScores() {
    alert(`${ this.selectedTeamIDs }`);
    return this.teamService.getTeamScores(
      this.selectedTeamIDs
    ).subscribe(
      data => {
        console.log(data);
        this.teamScores = data;
      }
    );
  }
}
