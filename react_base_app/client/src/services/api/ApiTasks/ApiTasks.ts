import HttpClient from "../../../lib/HttpClient/HttpClient";
import { AxiosRequestConfig } from "axios";
import { ContactFormInterface } from "../../../interfaces/ContactFormInterface";
import { TaskInterface } from "../../../interfaces/Tasksinterfaces";

/**
 * The abstract class to extend from for each of the various service classes that require Api Email.
 */
export default class ApiTasks extends HttpClient {

  public static instance?: ApiTasks;

  constructor(baseUrl = process.env.REACT_APP_BASE_URL) {
    super(baseUrl);
  }
  public static getInstance(baseUrl = process.env.REACT_APP_BASE_URL): ApiTasks {
    if (!this.instance) {
      this.instance = new ApiTasks(baseUrl);
    }

    return this.instance;
  }

  public async sendTask(form: ContactFormInterface): Promise<ContactFormInterface | any> {
    console.log(form);
    const options:AxiosRequestConfig = {
      data: {
        subject: form.subject,
        body: form.body,
        to: form.to,
        from: form.from,
      },
    };
    try {
      const response = await this.post('tasks/send-task', options);
      return response.data;
    } catch (error) {
      throw error;
    }
  }

  public async getAllTasks(userEmail: string): Promise<TaskInterface[]> {
    try {
      const response = await this.get('tasks/all-tasks-from', {
        headers: {
          'user-email': userEmail
        }
      });
      return response.data;
    } catch (error) {
      throw error;
    }
  }

}