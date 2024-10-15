import React, { useState, useEffect } from 'react';
import { 
  Box, 
  Button, 
  Container, 
  Typography, 
  Table, 
  TableBody, 
  TableCell, 
  TableContainer, 
  TableHead, 
  TableRow, 
  Paper
} from '@mui/material';
import { Link } from "react-router-dom";
import { ProgressBar } from '../../components/global';
import { AuthClient } from '../../services';
import heroImage from '../../assets/images/landing-pages/image-cache.jpeg';
import './TasksPage.scss';
import { UserInterface } from '../../interfaces/UserInterface';
import { TaskInterface } from '../../interfaces/Tasksinterfaces';
import ApiTasks from '../../services/api/ApiTasks/ApiTasks';

function TasksPage() {  
  const [loading, setLoading] = useState(true);
  const [user, setUser] = useState<UserInterface | null>(null);
  const [emails, setEmails] = useState<TaskInterface[]>([]); 
  const [error, setError] = useState<string | null>(null);
  useEffect(() => {
    const fetchData = async () => {
      try {
        setLoading(true);
        const userResponse: UserInterface = await AuthClient.getInstance().getUser();
        setUser(userResponse);

        if (userResponse?.email) {
          const emailsResponse: TaskInterface[] = await ApiTasks.getInstance().getAllTasks(userResponse.email);
          if (Array.isArray(emailsResponse)) {
            setEmails(emailsResponse);
            console.log(emailsResponse);
          } else {
            console.error('Emails response is not an array:', emailsResponse);
            setError('Failed to fetch emails. Please try again later.');
          }
        }
      } catch (error: any) {
        console.error('Error fetching data:', error.response?.data || error.message);
        setError('An error occurred while fetching data. Please try again later.');
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <ProgressBar />;
  }
  
  return (
    <Box className="tasks-page-wrapper" style={{ backgroundImage: `url(${heroImage})` }}>
      <Box className="tasks-page-header">
        <Container>
          <Typography variant="h2" component="h1" gutterBottom>
            Task Management
          </Typography>
          <Typography variant="subtitle1" gutterBottom>
            Manage your tasks efficiently with our easy-to-use platform.
          </Typography>
          <Button 
            component={Link} 
            to='/home'
            className="custom-button primary"
          >
            Back to home
          </Button>
        </Container>
      </Box>
      <Container className="tasks-page-content">
        <Typography variant="h4" component="h2" gutterBottom>
          Recent Tasks
        </Typography>
        {error ? (
          <Typography color="error">{error}</Typography>
        ) : emails.length > 0 ? (
          <TableContainer component={Paper}>
            <Table aria-label="tasks table">
              <TableHead>
                <TableRow>
                  <TableCell>From</TableCell>
                  <TableCell>To</TableCell>
                  <TableCell>Title</TableCell>
                  <TableCell>Date</TableCell>
                  <TableCell>Status</TableCell>
                </TableRow>
              </TableHead>
              <TableBody>
                {emails.map((email) => (
                  <TableRow
                    key={email._id}
                    sx={{ '&:last-child td, &:last-child th': { border: 0 } }}
                  >
                    <TableCell component="th" scope="row">
                      {email.from}
                    </TableCell>
                    <TableCell>{email.to}</TableCell>
                    <TableCell>{email.subject}</TableCell>
                    <TableCell>{email.createdDate ? new Date(email.createdDate).toLocaleString() : ''}</TableCell>
                    <TableCell>{email.status ? 'Completed' : 'Pending'}</TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </TableContainer>
        ) : (
          <Typography>No tasks found. Create a new task to get started!</Typography>
        )}
      </Container>
    </Box>
  );
}

export default TasksPage;