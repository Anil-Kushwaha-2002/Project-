// app.js

// Fetch the data from the API
fetch('/api/insights/')
    .then(response => response.json())
    .then(data => {
        // Extract the data for the chart
        const intensityData = data.map(item => item.intensity);
        const likelihoodData = data.map(item => item.likelihood);

        // Create the chart using Chart.js
        const ctx = document.getElementById('myChart').getContext('2d');
        const myChart = new Chart(ctx, {
            type: 'bar',
            data: {
                labels: ['Intensity', 'Likelihood'],
                datasets: [{
                    label: 'Insight Data',
                    data: [intensityData, likelihoodData],
                    backgroundColor: 'rgba(255, 99, 132, 0.2)',
                    borderColor: 'rgba(255, 99, 132, 1)',
                    borderWidth: 1
                }]
            }
        });
    });

// Function to handle filter submission
document.getElementById('filters').addEventListener('submit', function(event) {
    event.preventDefault(); // Prevent page reload on form submit
    
    const year = document.getElementById('yearFilter').value;
    const sector = document.getElementById('sectorFilter').value;

    // Fetch filtered data from the API
    fetch(`/api/insights/?year=${year}&sector=${sector}`)
        .then(response => response.json())
        .then(data => {
            // Update the chart with the filtered data
            const intensityData = data.map(item => item.intensity);
            const likelihoodData = data.map(item => item.likelihood);
            
            // Re-render the chart with the new data
            myChart.data.datasets[0].data = [intensityData, likelihoodData];
            myChart.update();
        });
});
