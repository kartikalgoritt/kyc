import express from "express";
import cors from "cors";
import dotenv from "dotenv";
import connectDB from "./database/db.js";
import routes from "./routes/routes.js";




const app = express()
dotenv.config();
const port = process.env.PORT || 5000;



app.use(cors());
app.use(express.json());
app.use(express.urlencoded({ extended: true }));
app.use('/', routes)


await connectDB()



app.listen(port, () => {
    console.log(`App listening on port ${port}`)
})