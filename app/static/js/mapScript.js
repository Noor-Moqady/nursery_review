var map;
var marker;

function onMapClick(e) {
    var lat = e.latlng.lat.toFixed(5); // Format latitude
    var lng = e.latlng.lng.toFixed(5); // Format longitude
    var locationText = lat + ", " + lng;

    // Update the input field value
    document.getElementById('nursery_location').value = locationText;

    // Check if marker already exists
    if (marker) {
        // Update the marker position
        marker.setLatLng(e.latlng);
    } else {
        // Create a new marker and add it to the map
        marker = L.marker(e.latlng).addTo(map);
    }
}

function initMap(latitude, longitude) {
    map = L.map('mapid').setView([latitude, longitude], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    map.on('click', onMapClick);
}

function getLocation() {
    if (navigator.geolocation) {
        navigator.geolocation.getCurrentPosition(function(position) {
            initMap(position.coords.latitude, position.coords.longitude);
        }, function() {
            alert("Geolocation is not supported by this browser.");
            initMap(51.505, -0.09); // Default location
        });
    } else {
        alert("Geolocation is not supported by this browser.");
        initMap(51.505, -0.09); // Default location
    }
}


document.addEventListener('DOMContentLoaded', function() {
    var locElements = document.querySelectorAll('.loc_info');

    locElements.forEach(function(elem) {
        var coords = elem.textContent.split(',').map(function(item) {
            return item.trim();
        });

        if (coords.length === 2) {
            fetchAddress(coords[0], coords[1], function(address) {
                elem.nextElementSibling.textContent = address;
            });
        }
    });
});

function fetchAddress(lat, lng, callback) {
    var url = `https://nominatim.openstreetmap.org/reverse?format=json&lat=${lat}&lon=${lng}`;

    fetch(url)
        .then(response => response.json())
        .then(data => {
            if (data.address) {
                callback(data.display_name);
            } else {
                callback('Address not found');
            }
        })
        .catch(error => {
            console.error('Error:', error);
            callback('Error fetching address');
        });
}

getLocation();