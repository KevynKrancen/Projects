import React from 'react';
import { Box, TextField, Button } from '@mui/material';

export default function ContactForm({formik}: {formik: any}) {
  console.log('ContactForm rendered with formik:', formik);

  const handleSubmit = (e: React.FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    console.log('Form submit event triggered');
    formik.handleSubmit(e);
  };

  const handleButtonClick = () => {
    console.log('Send Message button clicked');
    console.log('Current form values:', formik.values);
    console.log('Form is valid:', formik.isValid);
    console.log('Form is submitting:', formik.isSubmitting);
  };

  return (
    <Box component="form" onSubmit={handleSubmit} noValidate sx={{ mt: 1 }}>
      <TextField
        margin="normal"
        required
        fullWidth
        id="from"
        label="From"
        name="from"
        autoComplete="email"
        autoFocus
        value={formik.values.from}
        error={formik.touched.from && Boolean(formik.errors.from)}
        helperText={formik.touched.from && formik.errors.from}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
      />
      <TextField
        margin="normal"
        required
        fullWidth
        id="to"
        label="To"
        name="to"
        autoComplete="email"
        value={formik.values.to}
        error={formik.touched.to && Boolean(formik.errors.to)}
        helperText={formik.touched.to && formik.errors.to}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
      />
      <TextField
        margin="normal"
        required
        fullWidth
        id="subject"
        label="Subject"
        name="subject"
        value={formik.values.subject}
        error={formik.touched.subject && Boolean(formik.errors.subject)}
        helperText={formik.touched.subject && formik.errors.subject}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
      />
      <TextField
        margin="normal"
        required
        fullWidth
        id="body"
        label="Body"
        name="body"
        multiline
        rows={4}
        value={formik.values.body}
        error={formik.touched.body && Boolean(formik.errors.body)}
        helperText={formik.touched.body && formik.errors.body}
        onChange={formik.handleChange}
        onBlur={formik.handleBlur}
      />
      <Button
        type="submit"
        fullWidth
        variant="contained"
        color="primary"
        sx={{ mt: 3, mb: 2 }}
        onClick={handleButtonClick}
      >
        Send Message
      </Button>
    </Box>
  )
}