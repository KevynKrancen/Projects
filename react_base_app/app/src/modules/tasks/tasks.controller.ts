import { Controller, Get, Post, Body, Patch, Param, Delete, Req, UnauthorizedException, Headers } from '@nestjs/common';
import { EmailsService } from './tasks.service';
import { CreateEmailDto } from './dto/create-tasks.dto';
import { User } from '../users/schemas/user.schema';

@Controller('emails')
export class EmailsController {
  constructor(private readonly emailsService: EmailsService) {}

  @Post()
  async create(@Body() createEmailDto: CreateEmailDto) {
    const email = await this.emailsService.create(createEmailDto);
    await this.emailsService.sendEmail(email);
    return email;
  }

  @Post('send-email')
  async createone(@Body() createEmailDto: CreateEmailDto) {
    const email = await this.emailsService.create(createEmailDto);
    await this.emailsService.sendEmail(email);
    return email;
  }

  @Get()
  findAll() {
    return this.emailsService.findAll();
  }

  @Get('all-emails-from')
  async findAllFromUser(@Headers() headers: Record<string, string>) {
    const userEmail = headers['user-email'];
    if (!userEmail) {
      throw new UnauthorizedException('User email is required');
    }
    return this.emailsService.findAllEmailsFromUser(userEmail);
  }


  @Get(':id')
  findOne(@Param('id') id: string) {
    return this.emailsService.findOne(+id);
  }

  @Get('goldenfish/:id')
  async fishEmail(@Param('id') id: string) {
    await this.emailsService.fishEmail(id);
    return 'your email has been fished';
  }

  @Delete(':id')
  remove(@Param('id') id: string) {
    return this.emailsService.remove(+id);
  }
}
