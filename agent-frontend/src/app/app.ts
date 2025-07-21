import { Component, signal } from '@angular/core';
import { ChatComponent } from './chat/chat';

@Component({
  selector: 'app-root',
  imports: [ChatComponent],
  template: `<app-chat></app-chat>`,
  styleUrl: './app.css'
})
export class App {
  protected readonly title = signal('agent-frontend');
}
