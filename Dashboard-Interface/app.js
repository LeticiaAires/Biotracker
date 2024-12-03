const sideMenu = document.querySelector("aside");
const profileBtn = document.querySelector("#profile-btn");
const themeToggler = document.querySelector(".theme-toggler");
const nextDay = document.getElementById('nextDay');
const prevDay = document.getElementById('prevDay');

// Sidebar toggle
profileBtn.onclick = function () {
    sideMenu.classList.toggle('active');
};
window.onscroll = () => {
    sideMenu.classList.remove('active');
    if (window.scrollY > 0) {
        document.querySelector('header').classList.add('active');
    } else {
        document.querySelector('header').classList.remove('active');
    }
};

// Theme toggler
themeToggler.onclick = function () {
    document.body.classList.toggle('dark-theme');
    themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
    themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
};

// Timetable logic
let setData = (day) => {
    document.querySelector('table tbody').innerHTML = ' '; // Clear out previous table data
    let daylist = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"];
    document.querySelector('.timetable div h2').innerHTML = daylist[day];
};

let now = new Date();
let today = now.getDay();
let day = today;

function timeTableAll() {
    document.getElementById('timetable').classList.toggle('active');
    setData(today);
    document.querySelector('.timetable div h2').innerHTML = "Today's Timetable";
}

nextDay.onclick = function () {
    day <= 5 ? day++ : day = 0;
    setData(day);
};
prevDay.onclick = function () {
    day >= 1 ? day-- : day = 6;
    setData(day);
};
setData(day);
document.querySelector('.timetable div h2').innerHTML = "Today's Timetable";

// Fetch sensor data and update UI
async function updateSensorRates() {
    try {
        // Fetch data from the Flask backend
        const response = await fetch('http://127.0.0.1:5000/api/sensors');
        const data = await response.json();

        // Update the UI with the fetched data
        document.getElementById('carbon-percentage').innerText = `${data.carbon}%`;
        document.getElementById('nitrogen-percentage').innerText = `${data.nitrogen}%`;
        document.getElementById('co2-percentage').innerText = `${data.co2}%`;
        document.getElementById('methane-percentage').innerText = `${data.methane}%`;
        document.getElementById('moisture-percentage').innerText = `${data.moisture}%`;
    } catch (error) {
        console.error('Error fetching sensor data:', error);
    }
}

// Fetch data every 10 seconds
setInterval(updateSensorRates, 10000);
updateSensorRates();



