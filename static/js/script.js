function recipeClick() {
    var url = document.getElementById('url').getAttribute('data');
    window.location.assign(url)
}

var inputMap, displayMap, locations, markers = [];

function initMap() {
    // displayMap = new google.maps.Map(document.getElementById('map'), {
    //     center: { lat: 55.860916, lng: -4.251433 },
    //     scrollwheel: true,
    //     zoom: 9
    // });

    // locations.array.forEach(element => {
    //     var marker = new google.maps.Marker({
    //         position: {lat:element['Latitude'], lng:element['Longitude']},
    //         displayMap,
    //         title: element['Name'],
    //     });

    //     var infowindow = new google.maps.InfoWindow({
    //         content: element['Name'],
    //     });

    //     marker.addListener("click", () => {
    //         infowindow.open({
    //             anchor: marker,
    //             displayMap,
    //             shouldFocus: false,
    //         });
    //     });

    //     marker.addListener('click', () => {
    //         infowindow.close();
    //     });

    //     marker.setMap(displayMap);
    // });

    // console.log('here');
    // myLatLng = { lat: 34.397, lng: 150.644 }
    // inputMap = new google.maps.Map(document.getElementById('test'), {
    //     center: { lat: 34.397, lng: 150.644 },
    //     scrollwheel: false,
    //     zoom: 2
    // });

    // let infoWindow = new google.maps.InfoWindow({
    //     content: "Click the map to get Lat/Lng!",
    //     position: myLatLng,
    // });

    // infoWindow.open(inputMap);
    // inputMap.addListener("click", (mapsMouseEvent) => {
    //     // Close the current InfoWindow.
    //     infoWindow.close();
    //     // Create a new InfoWindow.
    //     infoWindow = new google.maps.InfoWindow({
    //         position: mapsMouseEvent.latLng,
    //     });
    //     infoWindow.setContent(
    //         JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
    //     );
    //     infoWindow.open(inputMap);
    // });
}

function refreshMarkers(locations) {

    first = locations['restaurants'][0]
   
    displayMap = new google.maps.Map(document.getElementById('map'), {
        center: {lat: first['Latitude'], lng: first['Longitude']},
        scrollwheel: true,
        zoom: 9
    });

    locations['restaurants'].forEach(element => {
        var marker = new google.maps.Marker({
            position: { lat: element['Latitude'], lng: element['Longitude'] },
            displayMap,
            title: element['Name'],
        });

        var infowindow = new google.maps.InfoWindow({
            content: element['Name'],
        });

        marker.addListener("mouseover", () => {
            infowindow.open({
                anchor: marker,
                displayMap,
                shouldFocus: false,
            });
        });

        marker.addListener('click', () => {
            infowindow.close();
        });

        marker.setMap(displayMap);
        markers.push(marker)
        console.log(markers, "makers");

    });
}

function handleSubmitByLocation() {
    document.getElementById("map").style.display = 'flex';
    var place = document.getElementById('search-map-restaurants').value;
    const xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function () {
        if (this.readyState == 4 && this.status == 200) {
            locations = JSON.parse(this.responseText);
            refreshMarkers(locations);

        }
    };
    xhttp.open("GET", place + '/');
    console.log('"GET", place + ' / '');
    xhttp.send();
}