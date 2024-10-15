import { Module } from '@nestjs/common';
import { AppController } from './app.controller';
import { AppService } from './app.service';
import { GlobalService } from './global/global.service';
import { DatabaseModule } from './database/database.module';
import { UsersModule } from './modules/users/users.module';
import { AuthModule } from './modules/auth/auth.module';
import { GlobalModule } from './global/global.module';
import { ConfigModule } from '@nestjs/config';
import { MongooseModule } from '@nestjs/mongoose';
import { EmailsModule } from './modules/emails/emails.module';

@Module({
  imports: [
    ConfigModule.forRoot({
      isGlobal: true,
      envFilePath: '.env',
    }),
    MongooseModule.forRoot(process.env.DB_CONNEXION_STRING),
    UsersModule,
    AuthModule,
    GlobalModule,
    EmailsModule,
  ],
  controllers: [AppController],
  providers: [AppService, GlobalService],
})
export class AppModule {}
