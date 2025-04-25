import mongoose from "mongoose";
import dotenv from "dotenv";
dotenv.config();

const connectDB = async () => {
    try {
        await mongoose.connect("mongodb+srv://kartik61003:algoritt%40123@cluster0.e9tile1.mongodb.net/identity_documents?retryWrites=true&w=majority&appName=Cluster0");
        console.log("MongoDB connected successfully");
    } catch (error) {
        console.error("MongoDB connection failed:", error.message);
        process.exit(1); // Exit the process with failure
    }
}

export default connectDB;
