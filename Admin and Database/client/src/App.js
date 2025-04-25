import { useEffect, useState } from 'react';
import './App.css';
import Application from './components/Application';
import { getApplication } from './api/api.js'; // Adjust the import path as necessary

function App() {
  const [applications, setApplications] = useState([]);

  const fetchRequest = async () => {
    try {
      const response = await getApplication();
      return response; // Return the fetched data
    } catch (error) {
      console.error('Error fetching data:', error);
      return []; // Return an empty array in case of an error
    }
  };

  useEffect(() => {
    // Fetch data when the component mounts
    const fetchData = async () => {
      const data = await fetchRequest();
      setApplications(data); // Set the fetched data to state
    };
    fetchData();
  }, []);

  console.log(applications);
  return (
    <div className="App">
      <header className="App-header">
        <h1>Admin Portal</h1>
        <h2>Applications</h2>
      </header>
      <main className="container">
        <div className="applications-container">
          {applications.map((application) => (
            <Application key={application._id} application={application} />
          ))}
        </div>
      </main>
    </div>
  );
}

export default App;