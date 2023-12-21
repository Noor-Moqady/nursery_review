var map;

function initMapWithLocation(latitude, longitude) {
    map = L.map('mapid').setView([latitude, longitude], 13);

    L.tileLayer('https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png', {
        maxZoom: 19,
        attribution: '© OpenStreetMap contributors'
    }).addTo(map);

    // Add a marker at the given location
    L.marker([latitude, longitude]).addTo(map);
}

function getCoordinatesFromElement() {
    var locElement = document.getElementById('nursery_loc');
    if (locElement) {
        var coords = locElement.innerText.split(',').map(function(item) {
            return parseFloat(item.trim());
        });
        if (coords.length === 2) {
            initMapWithLocation(coords[0], coords[1]);
        } else {
            console.error('Invalid coordinates format in nursery_loc element');
        }
    } else {
        console.error('nursery_loc element not found');
    }
}



getCoordinatesFromElement();


