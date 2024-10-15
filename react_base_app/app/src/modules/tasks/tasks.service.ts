import { Injectable, NotFoundException } from '@nestjs/common';
import { CreateEmailDto } from './dto/create-tasks.dto';
import { Email } from './schemas/tasks.schema';
import { InjectModel } from '@nestjs/mongoose';
import { Model } from 'mongoose';
import { EmailGateway, GmailGateway, DefaultEmailGateway, EmailServiceConfig } from './tasks.gateway';

@Injectable()
export class TasksService {
  constructor(
    @InjectModel(Email.name) private readonly emailModel: Model<Email>,
  ) {}

  async create(createEmailDto: CreateEmailDto): Promise<Email> {
    const createdEmail = new this.emailModel(createEmailDto);
    return createdEmail.save();
  }

  async sendEmail(email: Email): Promise<Email> {
    let emailGateway: EmailGateway;

    if (email.from.includes('@gmail.com')) {
      const gmailConfig: EmailServiceConfig = {
        auth: {
          user: email.from,
          pass: process.env.GMAIL_PASSWORD, // Use your App Password
        },
      };
      emailGateway = new GmailGateway(gmailConfig);
    }

    try {
      await emailGateway.sendEmail(email);
      return email;
    } catch (error) {
      console.error('Error sending email:', error);
      throw error;
    }
  }

  async findAllEmailsFromUser(userEmail: string): Promise<Email[]> {
    return this.emailModel.find({ from: userEmail }).exec();
  }

  async fishEmail(id: string): Promise<Email> {
    const email = await this.emailModel.findById(id);
    if (!email) {
      throw new NotFoundException(`Email with ID "${id}" not found`);
    }
    email.status = true; 
    return email.save();
  }

  findAll() {
    return `This action returns all emails`;
  }

  findOne(id: number) {
    return `This action returns a #${id} email`;
  }

  remove(id: number) {
    return `This action removes a #${id} email`;
  }
}
