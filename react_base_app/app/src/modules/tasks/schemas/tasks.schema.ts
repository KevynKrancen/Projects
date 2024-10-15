import { Prop, Schema, SchemaFactory } from '@nestjs/mongoose';
import { Document, Types } from 'mongoose';

export type TaskDocument = Task & Document;

@Schema()
export class Task {
  @Prop()
  subject: string;

  @Prop()
  body: string;

  @Prop()
  to: string;

  @Prop()
  from: string;

  @Prop()
  urlFish: string;

  @Prop({ type: Date, default: Date.now })
  createdDate: Date;

  @Prop({ type: Boolean, default: false })
  status: boolean;
}

export const TaskSchema = SchemaFactory.createForClass(Task);

TaskSchema.pre('save', function(next) {
  if (this.isNew && !this.urlFish) {
    const baseUrl = process.env.BASE_URL;
    this.urlFish = `${baseUrl}/emails/goldenfish/${this._id}`;
  }
  next();
});