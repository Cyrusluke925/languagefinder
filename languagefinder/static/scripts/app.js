    const apiKey = `AIzaSyBHLett8djBo62dDXj0EjCimF8Rd6E8cxg`
    const geoUrl = `https://maps.googleapis.com/maps/api/geocode/json?`

    let map = new google.maps.Map(document.getElementById('map'), {
    center: {lat: 38.397, lng: -100.644},
    zoom: 4.5
    });



    function geoString(inputFieldData) {
        let newInputFieldStr = '';
        for (var i = 0; i < inputFieldData.length; i += 1) {
            let currentElement = inputFieldData[i];
            if (currentElement === ' ') {
                newInputFieldStr += '+'
            } else {
                newInputFieldStr += currentElement;
        }


    }
    return newInputFieldStr
    }
    $('.geoCodingForm').on('submit', function(e) {
        e.preventDefault()
        let inputFieldData = $('.addressBar').val();
        let newString = geoString(inputFieldData)
        var geoLocationUrl = `${geoUrl}address=${newString}&key=${apiKey}`
        console.log(geoLocationUrl);
        $.ajax({
            method: "GET",
            url: `${geoLocationUrl}`,
            success: addressSuccess,
            error: function addressError(err1, err2, err3) {
                console.log(err1)
                console.log(err2)
                console.log(err3)
            }

        })


    function addressSuccess(response) {
        let latitudeLocation = response.results[0].geometry.location.lat;
        let longitudeLocation = response.results[0].geometry.location.lng;
        console.log(`The Latitude is ${latitudeLocation} and the longitude is ${longitudeLocation}` )
        let latlng = {lat: latitudeLocation, lng: longitudeLocation}
        let map = new google.maps.Map(document.getElementById('map'), {
        center: latlng,
        zoom: 10
        });

        let color = 'blue'

    let marker = new google.maps.Marker({
        position: latlng,
        map: map,
        title: "Marker Example",
        icon: 'http://maps.google.com/mapfiles/ms/icons/'+color+'.png'
    })
    document.forms['addressForm'].reset()
    }

    })



let color;

$('#JavaScript').on('click', function javaScriptText() {
    $('#menuLink1').text('JavaScript')
    color = 'yellow'
})

$('#Python').on('click', function javaScriptText() {
    $('#menuLink1').text('Python')
    color = 'green'
})

$('#Ruby').on('click', function javaScriptText() {
    $('#menuLink1').text('Ruby')
    color = 'red'
})


$('.geoCodingFormSearch').on('submit', function(e) {
    e.preventDefault();
    let language = $('#menuLink1').text()
    let inputFieldData = $('.addressBar').val();
    let newString = geoString(inputFieldData)
    var geoLocationUrl = `${geoUrl}address=${newString}&key=${apiKey}`

    


    
    if (language !== 'Languages') {
        $.ajax({
            method: "GET",
            url: `${geoLocationUrl}`,
            success: newAddressSuccess,
            error: function addressError(err1, err2, err3) {
                console.log(err1)
                console.log(err2)
                console.log(err3)
            }
    })
}

function newAddressSuccess(response) {
    console.log(color)
    let latitudeLocation = response.results[0].geometry.location.lat;
    let longitudeLocation = response.results[0].geometry.location.lng;
    let markerData = {
        title: language,
        latitude: latitudeLocation,
        longitude: longitudeLocation,
        marker: 'http://maps.google.com/mapfiles/ms/icons/'+color+'.png'
    }

    console.log(`The Latitude is ${latitudeLocation} and the longitude is ${longitudeLocation}` )
    let latlng = {lat: latitudeLocation, lng: longitudeLocation}

    $.ajax({
        method: 'POST',
        url: `language/new`,
        data: markerData,
        success: function onSuccess(response) {
            console.log('success!!')
        },
        error: function onError(err1, err2, err3) {
            console.log(err1)
        }

    })

}

})
