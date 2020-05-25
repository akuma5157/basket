import { Component } from '@angular/core';
import { TimeService } from 'src/api';

@Component({
  selector: 'app-time',
  template: `
    <button type="button" class="btn btn-primary" (click)="onSubmit()">
    Get Time
    </button>
    <div *ngIf="message" [ngClass]="message.cssClass">{{message.text}}</div>
   `,
  styles: []
})
export class TimeComponent {
    message: any;
  constructor(private timeService: TimeService) { }

  onSubmit() {
    const message = {
      "text": null,
      "cssClass": null
    }
    console.log("getting server time..");
    this.timeService.getTime().subscribe(
      server_time => {
        console.log("server time: ", server_time);
        message.cssClass = 'alert alert-dismissible alert-success';
        message.text = server_time;
      },
      error => {
        console.log(error);
        message.cssClass = 'alert alert-dismissible alert-danger';
        message.text = error;
      }
    );
    this.message = message;
  }
}
