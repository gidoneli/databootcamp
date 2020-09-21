// Creating map object and point to Las Vegas Nevada
var myMap = L.map("map", {
    center: [36.1249185, -124.1398517],
    zoom: 5
});

// Adding tile layer to the map
L.tileLayer("https://api.mapbox.com/styles/v1/{id}/tiles/{z}/{x}/{y}?access_token={accessToken}", {
    attribution: "© <a href='https://www.mapbox.com/about/maps/'>Mapbox</a> © <a href='http://www.openstreetmap.org/copyright'>OpenStreetMap</a> <strong><a href='https://www.mapbox.com/map-feedback/' target='_blank'>Improve this map</a></strong>",
    maxZoom: 18,
    id: "mapbox/light-v9",
    accessToken: API_KEY
}).addTo(myMap);

// Store API query variables
var baseURL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_month.geojson";

//  GET color radius call to the query URL
d3.json(baseURL, function(data) {
    function styleInfo(feature) {
        return {
            opacity: 1,
            fillOpacity: 1,
            fillColor: magColor(feature.properties.mag),
            color: "#000000",
            radius: magRadius(feature.properties.mag),
            stroke: true,
            weight: 0.5
        };
    }
    // Set colors based on magnitude (mag) of Earthquates
    function magColor(mag) {
        if (mag > 5) {
            return '#ea2c2c'
        } else if (mag > 4) {
            return '#ea822c'
        } else if (mag > 3) {
            return '#ee9c00'
        } else if (mag > 2) {
            return '#eecc00'
        } else if (mag > 1) {
            return '#d3ff49'
        } else {
            return '#95ff4c'
        }
    }

    // Set radius based on magnitude (mag) of Earthquates
    function magRadius(mag) {
        if (mag === 0) {
            return 1;
        }
        return mag * 5;
    }
    // GeoJSON layer
    L.geoJson(data.features, {
        // Circles
        pointToLayer: function(feature, latlng) {
            return L.circleMarker(latlng, { radius: magRadius(feature.properties.mag) });
        },

        // cirecle style
        style: function(feature) {
            return {
                fillColor: magColor(feature.properties.mag),
                fillOpacity: 0.5,
                weight: 0.1,
                color: 'black'
            }
        },

        // popup for each marker
        onEachFeature: function(feature, layer) {
            layer.bindPopup("<h4 style='text-align:center;'>" + new Date(feature.properties.time) + "</h4> <hr> <h5 style='text-align:center;'>" + "Magnitude: " + feature.properties.mag + "<br>Location: " + feature.properties.place);
        }
    }).addTo(myMap);

    var legend = L.control({ position: 'bottomright' });

    legend.onAdd = function(myMap) {

        var div = L.DomUtil.create('div', 'info legend'),
            grades = [1, 2, 3, 4, 5],
            labels = [];

        for (var i = 0; i < grades.length; i++) {
            div.innerHTML +=
                '<i style="background:' + magColor(grades[i] + 1) + '"></i> ' +
                grades[i] + (grades[i + 1] ? '&ndash;' + grades[i + 1] + '<br>' : '+');
        }

        return div;
    };

    legend.addTo(myMap);

});