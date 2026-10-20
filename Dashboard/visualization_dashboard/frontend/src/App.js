import React, { useState, useEffect } from 'react';
import axios from 'axios';
import { Container, Row, Col } from 'react-bootstrap';
import { Line } from 'react-chartjs-2';
// import { Chart as ChartJS } from 'chart.js';

function App() {
  const [data, setData] = useState([]);
  
  useEffect(() => {
    axios.get('http://localhost:8000/api/data/')
      .then(response => {
        setData(response.data);
      })
      .catch(error => console.error(error));
  }, []);

  // Example visualization (can customize further with D3.js, Chart.js, etc.)
  const chartData = {
    labels: data.map(item => item.year),
    datasets: [
      {
        label: 'Intensity Over Years',
        data: data.map(item => item.intensity),
        borderColor: 'rgba(75,192,192,1)',
        fill: false,
      }
    ]
  };

  return (
    <Container>
      <Row>
        <Col>
          <h1>Data Visualization Dashboard</h1>
          <Line data={chartData} />
        </Col>
      </Row>
    </Container>
  );
}

export default App;




// import logo from './logo.svg';
// import './App.css';

// function App() {
//   return (
//     <div className="App">
//       <header className="App-header">
//         <img src={logo} className="App-logo" alt="logo" />
//         <p>
//           Edit <code>src/App.js</code> and save to reload.
//         </p>
//         <a
//           className="App-link"
//           href="https://reactjs.org"
//           target="_blank"
//           rel="noopener noreferrer"
//         >
//           Learn React
//         </a>
//       </header>
//     </div>
//   );
// }

// export default App;


