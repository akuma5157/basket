import { Component } from '@angular/core';

@Component({
  selector: 'app-root',
  template: `
    <app-time></app-time>
    <router-outlet></router-outlet>
  `,
  styles: []
})
export class AppComponent {
  title = 'basket';
}
