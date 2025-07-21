import { Component } from '@angular/core';
import { CommonModule } from '@angular/common';
import { AgentService } from '../services/agent';

interface Message {
  content: string;
  isUser: boolean;
  timestamp: Date;
}

@Component({
  selector: 'app-chat',
  imports: [CommonModule],
  templateUrl: './chat.html',
  styleUrl: './chat.css'
})
export class ChatComponent {
  messages: Message[] = [];
  isLoading = false;

  constructor(private agentService: AgentService) {}

  sendMessage(textarea: HTMLTextAreaElement) {
    const message = textarea.value.trim();
    console.log('Send button clicked!');
    console.log('Current message:', message);
    
    if (!message || this.isLoading) {
      console.log('Returning early - validation failed');
      return;
    }

    // Add user message
    this.messages.push({
      content: message,
      isUser: true,
      timestamp: new Date()
    });

    textarea.value = '';
    this.isLoading = true;

    console.log('Sending message to API:', message);

    // Send to agent
    this.agentService.sendMessage(message).subscribe({
      next: (response) => {
        console.log('Received response:', response);
        this.messages.push({
          content: response.response,
          isUser: false,
          timestamp: new Date()
        });
        this.isLoading = false;
      },
      error: (error) => {
        console.error('API Error:', error);
        this.messages.push({
          content: 'Sorry, there was an error processing your request.',
          isUser: false,
          timestamp: new Date()
        });
        this.isLoading = false;
      }
    });
  }

  onKeyPress(event: KeyboardEvent, textarea: HTMLTextAreaElement) {
    if (event.key === 'Enter' && !event.shiftKey) {
      event.preventDefault();
      this.sendMessage(textarea);
    }
  }

  getMessageValue(textarea: HTMLTextAreaElement): string {
    return textarea.value || '';
  }
}
