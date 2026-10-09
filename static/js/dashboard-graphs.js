/* ==========================================
   AI FARMER - CROP HEALTH & IRRIGATION CHARTS
   ========================================== */

document.addEventListener("DOMContentLoaded", function () {

    // Stop if the chart library has not loaded.
    if (typeof Chart === "undefined") {
        console.error("Chart.js is not loaded.");
        return;
    }

    // Crop health doughnut chart
    const cropCanvas = document.getElementById("cropHealthChart");

    if (cropCanvas) {
        new Chart(cropCanvas, {
            type: "doughnut",

            data: {
                labels: ["Healthy crops", "Disease detected"],

                datasets: [{
                    data: [70, 30],

                    backgroundColor: [
                        "#22c55e",
                        "#f97316"
                    ],

                    hoverBackgroundColor: [
                        "#16a34a",
                        "#ea580c"
                    ],

                    borderWidth: 4,
                    borderColor: "#ffffff",
                    hoverOffset: 8
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false,
                cutout: "70%",

                plugins: {
                    legend: {
                        display: false
                    },

                    tooltip: {
                        callbacks: {
                            label: function (context) {
                                return context.label + ": " +
                                    context.parsed + "%";
                            }
                        }
                    }
                }
            }
        });
    }

    // Irrigation weekly line chart
    const irrigationCanvas =
        document.getElementById("irrigationChart");

    if (irrigationCanvas) {
        const context = irrigationCanvas.getContext("2d");

        const gradient = context.createLinearGradient(0, 0, 0, 250);
        gradient.addColorStop(0, "rgba(59, 130, 246, 0.35)");
        gradient.addColorStop(1, "rgba(6, 182, 212, 0.01)");

        new Chart(irrigationCanvas, {
            type: "line",

            data: {
                labels: [
                    "Mon", "Tue", "Wed", "Thu",
                    "Fri", "Sat", "Sun"
                ],

                datasets: [{
                    label: "Water used (litres)",

                    data: [150, 180, 120, 220, 190, 240, 150],

                    borderColor: "#3b82f6",
                    backgroundColor: gradient,

                    fill: true,
                    tension: 0.4,

                    borderWidth: 3,

                    pointRadius: 4,
                    pointHoverRadius: 7,

                    pointBackgroundColor: "#06b6d4",
                    pointBorderColor: "#ffffff",
                    pointBorderWidth: 2
                }]
            },

            options: {
                responsive: true,
                maintainAspectRatio: false,

                interaction: {
                    intersect: false,
                    mode: "index"
                },

                plugins: {
                    legend: {
                        display: false
                    },

                    tooltip: {
                        backgroundColor: "#172554",
                        padding: 12,

                        callbacks: {
                            label: function (context) {
                                return " Water used: " +
                                    context.parsed.y + " L";
                            }
                        }
                    }
                },

                scales: {
                    x: {
                        grid: {
                            display: false
                        },

                        ticks: {
                            color: "#64748b"
                        },

                        border: {
                            display: false
                        }
                    },

                    y: {
                        beginAtZero: true,

                        title: {
                            display: true,
                            text: "Litres",
                            color: "#64748b"
                        },

                        ticks: {
                            color: "#64748b"
                        },

                        grid: {
                            color: "rgba(148, 163, 184, 0.15)"
                        },

                        border: {
                            display: false
                        }
                    }
                }
            }
        });
    }

});