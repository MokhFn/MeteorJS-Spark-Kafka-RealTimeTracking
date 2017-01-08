
if(Meteor.isServer){
    Meteor.publish("Coordinates",function () {
        return Coordinates.find({}, {
            sort  : {processed_at : -1},
            limit : 1
            }
        )
    });
}
