import { Module, NestModule, MiddlewareConsumer } from '@nestjs/common';
import { MongooseModule } from '@nestjs/mongoose';
import { TasksController } from './tasks.controller';
import { TasksService } from './tasks.service';
import { Email, EmailSchema } from './schemas/tasks.schema';
import { GmailGateway } from './tasks.gateway';

@Module({
  imports: [MongooseModule.forFeature([{ name: Email.name, schema: EmailSchema }])],
  controllers: [TasksController],
  providers: [TasksService, GmailGateway],
})
export class TasksModule {}
