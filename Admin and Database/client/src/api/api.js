import axios from 'axios';

export const getApplication = async (data) => {
    try {
        const response = await axios.get('http://localhost:5000/getApplications', {
            headers: {
                'Content-Type': 'application/json',
            },
            data: data,
        });
        return response.data;
    } catch (error) {
        throw error;
    }
};