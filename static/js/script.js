function recipeClick(){
    var url = document.getElementById('url').getAttribute('data');
    window.location.assign(url)
}

var inputMap, displayMap;

function initMap() {
    console.log('hello');
    myLatLng = { lat: 34.397, lng: 150.644 }
    displayMap = new google.maps.Map(document.getElementById('map'), {
        center: { lat: 55.860916, lng: -4.251433 },
        scrollwheel: false,
        zoom: 8
    });

    const marker = new google.maps.Marker({
        position: myLatLng,
        displayMap,
        title: "contentString",
    });

    const infowindow = new google.maps.InfoWindow({
        content: "contentString",
    });

    marker.addListener("mouseover", () => {
        infowindow.open({
            anchor: marker,
            displayMap,
            shouldFocus: false,
        });
    });

    marker.addListener('mouseout', () => {
        infowindow.close();
    });

    marker.setMap(displayMap);

    console.log('here');
    myLatLng = { lat: 34.397, lng: 150.644 }
    inputMap = new google.maps.Map(document.getElementById('test'), {
        center: { lat: 34.397, lng: 150.644 },
        scrollwheel: false,
        zoom: 2
    });

    let infoWindow = new google.maps.InfoWindow({
        content: "Click the map to get Lat/Lng!",
        position: myLatLng,
      });

      infoWindow.open(inputMap);
      inputMap.addListener("click", (mapsMouseEvent) => {
        // Close the current InfoWindow.
        infoWindow.close();
        // Create a new InfoWindow.
        infoWindow = new google.maps.InfoWindow({
          position: mapsMouseEvent.latLng,
        });
        infoWindow.setContent(
          JSON.stringify(mapsMouseEvent.latLng.toJSON(), null, 2)
        );
        infoWindow.open(inputMap);
      });
}