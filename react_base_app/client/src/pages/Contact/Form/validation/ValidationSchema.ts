import * as yup from 'yup';

export const ValidationSchema = yup.object().shape({
  from: yup
    .string()
    .required('From email is required')
    .email('Must be a valid email'),
  to: yup
    .string()
    .required('To email is required')
    .email('Must be a valid email'),
  subject: yup
    .string()
    .required('Subject is required')
    .max(100, 'Subject cannot exceed 100 characters'),
  body: yup
    .string()
    .required('Message body is required')
    .min(10, 'Message must be at least 10 characters long')
    .max(1000, 'Message cannot exceed 1000 characters'),
});