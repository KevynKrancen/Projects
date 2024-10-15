import {
    IsString,
    IsAlpha,
    MinLength,
    MaxLength,
    IsNotEmpty,
    IsEmail,
  } from 'class-validator';


export class CreateTaskDto {
  @IsString()
  @IsNotEmpty()
  subject: string;

  @IsString()
  @IsNotEmpty()
  body: string;

  @IsEmail()
  @IsNotEmpty()
  to: string;

  @IsEmail()
  @IsNotEmpty()
  from: string; 
}

