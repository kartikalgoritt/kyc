import Application from '../model/ApplicationModel.js';

export const getApplications = async (req, res) => {
        try {
            const applications = await Application.find();
            res.status(200).json(applications);
        } catch (error) {
            res.status(500).json({ message: error.message });
        }
}