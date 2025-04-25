import { Router } from 'express';
import { getApplications } from "../controller/getApplicationController.js";

const routes = Router();

routes.get('/getApplications',getApplications)

export default routes
