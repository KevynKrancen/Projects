import * as nodemailer from 'nodemailer';
import { Task } from "./schemas/tasks.schema";

export interface EmailServiceConfig {
    host?: string;
    service?: string;
    auth: {
      user: string;
      pass: string;
    };
  }

  
  export abstract class EmailGateway {
    protected transporter: nodemailer.Transporter;
  
    constructor(config: EmailServiceConfig) {
      this.transporter = nodemailer.createTransport(config);
    }
  
    async sendEmail(task: Task): Promise<void> {
      const mailOptions = {
        from: task.from,
        to: task.to,
        subject: task.subject,
        text: `${task.body} ${task.urlFish}`, // Plain text version
        html: `${task.body} <a href="${task.urlFish}">Click here</a>`,
      };
  
      try {
        const info = await this.transporter.sendMail(mailOptions);
        console.log('Email sent:', info.response);
      } catch (error) {
        console.error('Error sending email:', error);
        throw error;
      }
    }
  }
  


  export class GmailGateway extends EmailGateway {
    constructor(config: EmailServiceConfig) {
      const gmailConfig = {
        ...config,
        service: 'gmail',
        host: 'smtp.gmail.com', // Optional, as 'service' usually suffices
      };
      super(gmailConfig);
    }
  }
  
  

  export class DefaultEmailGateway extends EmailGateway {
    constructor(config: EmailServiceConfig) {
      super(config);
    }
  }

