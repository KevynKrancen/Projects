import * as dotenv from 'dotenv';
import { join } from 'path';

const envPath = join(__dirname, '..', '.env');
const result = dotenv.config({ path: envPath });

import { NestFactory } from '@nestjs/core';
import { AppModule } from './app.module';

async function bootstrap() {
  const app = await NestFactory.create(AppModule, {
    cors: {
      origin: 'http://localhost:3000',
      credentials: true
    },
  });
  await app.listen(process.env.SERVER_PORT || 3002);
}
bootstrap();
