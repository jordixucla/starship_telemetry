const ctx = document.getElementById('myChart').getContext('2d');
let myChart = new Chart(ctx, {
    type: 'line',
    data: {
        labels: [], // Placeholder for labels
        datasets: [{
            label: 'Booster',
            data: [], // Placeholder for data
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }, {
            label: 'Starship',
            data: [],
            borderColor: 'rgba(192, 75, 75, 1)',
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Speed'
            }
        },
        scales: {
            x: {
                type: 'category',
                stepSize: 1 // Adjust step size accordingly
            },
            y: {
                beginAtZero: true // Ensure y-axis starts at zero
            }
        }
    }
});

const ctx2 = document.getElementById('myChart2').getContext('2d');
let myChart2 = new Chart(ctx2, {
    type: 'line',
    data: {
        labels: [], // Placeholder for labels
        datasets: [{
            label: 'Booster',
            data: [], // Placeholder for data
            borderColor: 'rgba(75, 192, 192, 1)',
            borderWidth: 1
        }, {
            label: 'Starship',
            data: [],
            borderColor: 'rgba(75, 75, 192, 1)',
            borderWidth: 1
        }]
    },
    options: {
        plugins: {
            title: {
                display: true,
                text: 'Altitude'
            }
        },
        scales: {
            x: {
                type: 'category',
                stepSize: 1 // Adjust step size accordingly
            },
            y: {
                beginAtZero: true // Ensure y-axis starts at zero
            }
        }
    }
});

// Use a local server to serve the files instead of accessing them directly from the file system. 
// You can use a simple HTTP server like `http-server` or `live-server`.

async function fetchData() {
    console.log('Fetching data...');
    try {
        const response = await fetch(`data.txt?cache-bust=${new Date().getTime()}`);
        if (!response.ok) {
            throw new Error('Network response was not ok');
        }
        const text = await response.text();
        const rows = text.trim().split('\n');
        const labels = [];
        const data1 = [];
        const data2 = [];
        const data3 = [];
        const data4 = [];
        rows.forEach(row => {
            const [index, time, ba, bs, sa, ss] = row.split('\t');
            labels.push(time);
            console.log('Data:', { index, time, ba, bs, sa, ss });
            data1.push(parseFloat(ba));
            data2.push(parseFloat(bs));
            data3.push(parseFloat(sa));
            data4.push(parseFloat(ss));
        });
        return { labels, data1, data2, data3, data4 };
    } catch (error) {
        console.error('Failed to fetch data:', error);
        return { labels: [], data1: [], data2: [], data3: [], data4: [] };
    }
}

async function updateChart() {
    try {
        const { labels, data1, data2, data3, data4 } = await fetchData();
        myChart.data.labels = labels;
        myChart.data.datasets[0].data = data2;
        myChart.data.datasets[1].data = data4;
        myChart.update();

        myChart2.data.labels = labels;
        myChart2.data.datasets[0].data = data1;
        myChart2.data.datasets[1].data = data3;
        myChart2.update();
    } catch (error) {
        console.error('Failed to update chart:', error);
    }
}

setInterval(updateChart, 800);