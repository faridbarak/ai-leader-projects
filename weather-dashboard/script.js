// Configuration
const API_KEY = 5429c5e396605186203f6a6390bec138; // Get free key from openweathermap.org
const BASE_URL = 'https://api.openweathermap.org';

// DOM Elements
const searchInput = document.getElementById('searchInput');
const searchBtn = document.getElementById('searchBtn');
const locationBtn = document.getElementById('locationBtn');
const loadingSpinner = document.getElementById('loadingSpinner');
const errorMessage = document.getElementById('errorMessage');
const currentWeatherDiv = document.getElementById('currentWeather');
const forecastSection = document.getElementById('forecastSection');
const favoritesList = document.getElementById('favoritesList');

// State
let favorites = JSON.parse(localStorage.getItem('favorites')) || [];
let currentWeatherData = null;

// Event Listeners
searchBtn.addEventListener('click', handleSearch);
searchInput.addEventListener('keypress', (e) => e.key === 'Enter' && handleSearch());
locationBtn.addEventListener('click', handleLocationClick);

// Initialize
window.addEventListener('load', () => {
    renderFavorites();
    // Try to load last searched city or use default
    const lastCity = localStorage.getItem('lastCity');
    if (lastCity) {
        fetchWeather(lastCity);
    }
});

// Search Handler
function handleSearch() {
    const city = searchInput.value.trim();
    if (city) {
        fetchWeather(city);
        searchInput.value = '';
    }
}

// Location Handler
function handleLocationClick() {
    if ('geolocation' in navigator) {
        showLoading(true);
        navigator.geolocation.getCurrentPosition(
            (position) => {
                const { latitude, longitude } = position.coords;
                fetchWeatherByCoords(latitude, longitude);
            },
            (error) => {
                showError('Unable to get your location. Please enable location services.');
                showLoading(false);
            }
        );
    } else {
        showError('Geolocation is not supported by your browser.');
    }
}

// Fetch Weather by City Name
async function fetchWeather(city) {
    showLoading(true);
    hideError();

    try {
        // Get current weather
        const currentResponse = await fetch(
            `${BASE_URL}/data/2.5/weather?q=${city}&appid=${API_KEY}&units=metric`
        );

        if (!currentResponse.ok) {
            throw new Error('City not found');
        }

        const currentData = await currentResponse.json();
        currentWeatherData = currentData;
        localStorage.setItem('lastCity', city);

        // Get forecast and air quality
        const { lat, lon } = currentData.coord;
        await Promise.all([
            fetchForecast(lat, lon),
            // Optional: Fetch air quality or UV index from another endpoint
        ]);

        displayWeather(currentData);
    } catch (error) {
        showError(error.message);
    } finally {
        showLoading(false);
    }
}

// Fetch Weather by Coordinates
async function fetchWeatherByCoords(lat, lon) {
    showLoading(true);
    hideError();

    try {
        const response = await fetch(
            `${BASE_URL}/data/2.5/weather?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
        );

        if (!response.ok) throw new Error('Failed to fetch weather');

        const data = await response.json();
        currentWeatherData = data;
        localStorage.setItem('lastCity', data.name);

        const { coord } = data;
        await fetchForecast(coord.lat, coord.lon);
        displayWeather(data);
    } catch (error) {
        showError(error.message);
    } finally {
        showLoading(false);
    }
}

// Fetch Forecast
async function fetchForecast(lat, lon) {
    try {
        const response = await fetch(
            `${BASE_URL}/data/2.5/forecast?lat=${lat}&lon=${lon}&appid=${API_KEY}&units=metric`
        );

        if (!response.ok) throw new Error('Failed to fetch forecast');

        const data = await response.json();
        displayForecast(data);
    } catch (error) {
        console.error('Forecast error:', error);
    }
}

// Display Current Weather
function displayWeather(data) {
    const {
        name,
        sys,
        main,
        weather,
        wind,
        visibility,
        clouds,
    } = data;

    const weatherIcon = `https://openweathermap.org/img/wn/${weather[0].icon}@4x.png`;
    const date = new Date().toLocaleDateString('en-US', {
        weekday: 'long',
        year: 'numeric',
        month: 'long',
        day: 'numeric',
    });

    document.getElementById('cityName').textContent = `${name}, ${sys.country}`;
    document.getElementById('date').textContent = date;
    document.getElementById('temperature').textContent = Math.round(main.temp);
    document.getElementById('weatherDescription').textContent = weather[0].description;
    document.getElementById('weatherIcon').src = weatherIcon;
    document.getElementById('humidity').textContent = `${main.humidity}%`;
    document.getElementById('windSpeed').textContent = `${wind.speed} m/s`;
    document.getElementById('visibility').textContent = `${(visibility / 1000).toFixed(1)} km`;
    document.getElementById('pressure').textContent = `${main.pressure} hPa`;
    document.getElementById('feelsLike').textContent = `${Math.round(main.feels_like)}°C`;
    document.getElementById('uvIndex').textContent = `${clouds.all}%`;

    currentWeatherDiv.classList.remove('hidden');
}

// Display Forecast
function displayForecast(data) {
    const forecastContainer = document.getElementById('forecastContainer');
    forecastContainer.innerHTML = '';

    // Get forecast for every 8th entry (24-hour intervals)
    const dailyForecasts = data.list.filter((_, index) => index % 8 === 0).slice(0, 5);

    dailyForecasts.forEach((forecast) => {
        const date = new Date(forecast.dt * 1000);
        const day = date.toLocaleDateString('en-US', { weekday: 'short' });
        const icon = `https://openweathermap.org/img/wn/${forecast.weather[0].icon}@2x.png`;

        const card = document.createElement('div');
        card.className = 'forecast-card';
        card.innerHTML = `
            <div class="day">${day}</div>
            <img src="${icon}" alt="${forecast.weather[0].description}">
            <div class="temp">${Math.round(forecast.main.temp)}°C</div>
            <div class="description">${forecast.weather[0].main}</div>
        `;
        forecastContainer.appendChild(card);
    });

    forecastSection.classList.remove('hidden');
}

// Favorites Management
function addFavorite() {
    if (currentWeatherData) {
        const city = currentWeatherData.name;
        if (!favorites.includes(city)) {
            favorites.push(city);
            localStorage.setItem('favorites', JSON.stringify(favorites));
            renderFavorites();
        }
    }
}

function removeFavorite(city) {
    favorites = favorites.filter((fav) => fav !== city);
    localStorage.setItem('favorites', JSON.stringify(favorites));
    renderFavorites();
}

function renderFavorites() {
    favoritesList.innerHTML = '';

    if (favorites.length === 0) {
        favoritesList.innerHTML = '<p style="color: #999;">No favorite cities yet</p>';
        return;
    }

    favorites.forEach((city) => {
        const btn = document.createElement('button');
        btn.className = 'favorite-btn';
        btn.innerHTML = `
            <span>${city}</span>
            <span class="remove" onclick="removeFavorite('${city}')">✕</span>
        `;
        btn.addEventListener('click', () => fetchWeather(city));
        favoritesList.appendChild(btn);
    });
}

// Add favorite button to current weather (optional enhancement)
function addAddFavoriteButton() {
    if (currentWeatherData && !document.getElementById('addFavoriteBtn')) {
        const btn = document.createElement('button');
        btn.id = 'addFavoriteBtn';
        btn.textContent = '⭐ Add to Favorites';
        btn.style.cssText = `
            background: #FFD700;
            border: none;
            padding: 10px 20px;
            border-radius: 8px;
            cursor: pointer;
            font-weight: 600;
            margin-top: 20px;
        `;
        btn.addEventListener('click', addFavorite);
        currentWeatherDiv.appendChild(btn);
    }
}

// UI Helpers
function showLoading(show) {
    if (show) {
        loadingSpinner.classList.remove('hidden');
    } else {
        loadingSpinner.classList.add('hidden');
    }
}

function showError(message) {
    errorMessage.textContent = message;
    errorMessage.classList.remove('hidden');
}

function hideError() {
    errorMessage.classList.add('hidden');
}

// Temperature Unit Toggle (optional enhancement)
let isCelsius = true;
function toggleTemperatureUnit() {
    isCelsius = !isCelsius;
    if (currentWeatherData) {
        displayWeather(currentWeatherData);
    }
}
