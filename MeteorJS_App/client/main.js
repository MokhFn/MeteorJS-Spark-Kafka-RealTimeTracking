if(Meteor.isClient){
    Meteor.subscribe("Coordinates");

    Template.coordinates.helpers({
        'coordinates' : function () {
            return Coordinates.findOne({},
                {sort :
                    {processed_at : -1}
                });
        }
    });

    Meteor.startup(function() {
        GoogleMaps.load();
    });

    Template.body.helpers({
        'exampleMapOptions': function() {
            // Make sure the maps API has loaded
            if (GoogleMaps.loaded()) {
                // Map initialization options
                return {
                    center: new google.maps.LatLng(36.7479795, 10.290745499999957),
                    zoom: 10
                };
            }
        }
    });

    Template.body.onCreated(function() {
        // We can use the `ready` callback to interact with the map API once the map is ready.

        GoogleMaps.ready('exampleMap', function(map) {

            function placeMarker(location,timeout) {
                window.setTimeout(function() {
                    var marker = new google.maps.Marker({
                        position: new google.maps.LatLng(location.lat, location.long),
                        map: map.instance,
                        animation: google.maps.Animation.DROP
                    });
                }, timeout);
            }
            this.markerObserve = Coordinates.find({}).observe({
                added: function(m) {
                    placeMarker(m,200);  // obviously depends on the structure of Markers documents
                }
            });
            //markers go here
        });
    });

    Template.body.destroyed = function() {
        this.markerObserve.stop();
    }

}
