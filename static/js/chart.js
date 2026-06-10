// =========================
// POLLUTANT BAR CHART
// =========================

const barCtx = document.getElementById('barChart');

if (barCtx) {

    new Chart(barCtx, {

        type: 'bar',

        data: {

            labels: [
                'PM2.5',
                'PM10',
                'NO',
                'NO2',
                'NH3',
                'CO',
                'SO2',
                'O3'
            ],

            datasets: [{

                label: 'Pollutant Concentration',

            data: [

    pollutionData.pm25,
    pollutionData.pm10,
    pollutionData.no,
    pollutionData.no2,
    pollutionData.nh3,
    pollutionData.co,
    pollutionData.so2,
    pollutionData.o3

],

                backgroundColor: [
                    '#3498db',
                    '#2ecc71',
                    '#f1c40f',
                    '#e74c3c',
                    '#9b59b6',
                    '#1abc9c',
                    '#e67e22',
                    '#34495e'
                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                title: {

                    display: true,

                    text: 'Current Pollutant Levels'

                }

            }

        }

    });

}

// =========================
// MONTHLY AQI TREND
// =========================

const lineCtx = document.getElementById('lineChart');

if (lineCtx) {

    new Chart(lineCtx, {

        type: 'line',

        data: {

            labels: [
                'Jan',
                'Feb',
                'Mar',
                'Apr',
                'May',
                'Jun',
                'Jul',
                'Aug'
            ],

            datasets: [{

                label: 'Average AQI',

                data: [
                    110,
                    125,
                    140,
                    170,
                    190,
                    165,
                    150,
                    130
                ],

                borderColor: '#0d6efd',

                backgroundColor:
                    'rgba(13,110,253,0.2)',

                fill: true,

                tension: 0.4

            }]

        },

        options: {

            responsive: true,

            plugins: {

                title: {

                    display: true,

                    text: 'AQI Trend'

                }

            }

        }

    });

}

// =========================
// AQI CATEGORY DISTRIBUTION
// =========================

const pieCtx = document.getElementById('pieChart');

if (pieCtx) {

    new Chart(pieCtx, {

        type: 'pie',

        data: {

            labels: [
                'Good',
                'Satisfactory',
                'Moderate',
                'Poor',
                'Very Poor',
                'Severe'
            ],

            datasets: [{

                data: [
                    15,
                    25,
                    35,
                    12,
                    8,
                    5
                ],

                backgroundColor: [

                    '#28a745',
                    '#20c997',
                    '#ffc107',
                    '#fd7e14',
                    '#dc3545',
                    '#6f42c1'

                ]

            }]

        },

        options: {

            responsive: true

        }

    });

}

// =========================
// POLLUTION SOURCES
// =========================

const doughnutCtx =
    document.getElementById('doughnutChart');

if (doughnutCtx) {

    new Chart(doughnutCtx, {

        type: 'doughnut',

        data: {

            labels: [

                'Vehicles',
                'Industries',
                'Construction',
                'Domestic Sources'

            ],

            datasets: [{

                data: [

                    40,
                    30,
                    20,
                    10

                ],

                backgroundColor: [

                    '#007bff',
                    '#28a745',
                    '#ffc107',
                    '#dc3545'

                ]

            }]

        },

        options: {

            responsive: true,

            plugins: {

                title: {

                    display: true,

                    text: 'Pollution Sources'

                }

            }

        }

    });

}

