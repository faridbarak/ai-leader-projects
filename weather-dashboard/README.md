# 🌤️ Weather Dashboard

A modern, responsive weather dashboard that fetches real-time weather data from the OpenWeather API.

## Features

✅ **Current Weather Display**
- Real-time temperature, humidity, wind speed
- Weather description and conditions
- Feels-like temperature
- Pressure and visibility information
- Weather icons

✅ **5-Day Forecast**
- Daily weather predictions
- Temperature trends
- Weather conditions

✅ **Location-Based Weather**
- Search by city name
- Geolocation support (get weather for your location)
- Last searched city memory

✅ **Favorite Cities**
- Save favorite cities
- Quick access to saved locations
- Local storage persistence

✅ **Responsive Design**
- Mobile-friendly interface
- Adaptive grid layouts
- Touch-friendly buttons

✅ **Modern UI**
- Beautiful gradient backgrounds
- Smooth animations
- Weather-themed color scheme
- Loading states and error handling

## Getting Started

### Prerequisites
- A free API key from [OpenWeatherMap](https://openweathermap.org/api)

### Installation

1. Clone or download this repository
2. Open the repository folder
3. Edit `script.js` and replace `YOUR_OPENWEATHER_API_KEY` with your actual API key:
   ```javascript
   const API_KEY = 'your_api_key_here';
   ```
4. Open `index.html` in your web browser

### Getting an API Key

1. Visit [OpenWeatherMap](https://openweathermap.org/api)
2. Sign up for a free account
3. Go to your API keys section
4. Copy the "Current weather data" API key
5. Paste it into the `script.js` file

## Usage

### Search for a City
1. Type a city name in the search box
2. Press Enter or click the Search button
3. View current weather and 5-day forecast

### Use Your Location
1. Click the location button (📍)
2. Allow browser location access when prompted
3. Weather for your location will display automatically

### Add to Favorites
1. Search for a city
2. Click "Add to Favorites" button
3. Access saved cities from the Favorites section

### Remove from Favorites
- Click the ✕ button next to a favorite city

## Data Displayed

### Current Weather
- Temperature (°C)
- Weather condition (Sunny, Cloudy, etc.)
- Humidity (%)
- Wind speed (m/s)
- Visibility (km)
- Atmospheric pressure (hPa)
- Feels-like temperature (°C)
- Cloud coverage (%)

### Forecast
- 5-day weather forecast
- Daily temperature predictions
- Weather conditions for each day

## Local Storage

The app uses browser local storage to save:
- Favorite cities list
- Last searched city

Data persists even after closing the browser.

## Technologies Used

- **HTML5** - Structure
- **CSS3** - Styling with gradients and animations
- **JavaScript (ES6+)** - Functionality and API calls
- **OpenWeather API** - Weather data
- **Font Awesome** - Icons
- **Local Storage API** - Data persistence

## API Used

[OpenWeatherMap API](https://openweathermap.org/api)
- Current weather data endpoint
- 5-day forecast endpoint

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers (iOS Safari, Chrome Mobile)

## Known Limitations

- Requires a free OpenWeatherMap API key
- Geolocation requires HTTPS on production (HTTP works on localhost)
- Free API tier has rate limits

## Future Enhancements

- [ ] Temperature unit toggle (Celsius/Fahrenheit)
- [ ] Air quality index display
- [ ] UV index information
- [ ] Severe weather alerts
- [ ] Multiple language support
- [ ] Dark mode theme
- [ ] Weather history/trends
- [ ] Hourly forecast
- [ ] Precipitation chances

## Troubleshooting

### "City not found" error
- Check the spelling of the city name
- Try using a larger city name
- Some small towns may not be available

### Location button not working
- Ensure you've allowed browser location access
- Check if HTTPS is being used (on production)
- Location services must be enabled on your device

### No data showing
- Verify your API key is correct in `script.js`
- Check your internet connection
- Check the browser console for errors (F12)
- Ensure your API key is active

## License

Free to use and modify for personal and commercial projects.

## Contributing

Feel free to fork and submit pull requests for improvements!

## Support

For API-related questions, visit [OpenWeatherMap Documentation](https://openweathermap.org/api)
