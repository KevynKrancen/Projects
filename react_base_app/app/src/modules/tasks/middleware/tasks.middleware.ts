import { Injectable, NestMiddleware } from '@nestjs/common';
import { Request, Response, NextFunction } from 'express';
import { ConfigService } from '@nestjs/config';

@Injectable()
export class SetUrlFishMiddleware implements NestMiddleware {
  constructor(private configService: ConfigService) {}

  use(req: Request, res: Response, next: NextFunction) {
    if (req.method === 'POST' && req.path === '/emails') {
      const baseUrl = process.env.BASE_URL || 'http://localhost:3002';
      req.body.urlFish = `${baseUrl}/emails/goldenfish/${req.body._id}`;
    }
    next();
  }
}