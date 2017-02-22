
module.exports = {
    status_history:function(id){
        return "/api/campgrounds/" + id + "/status_history.json?closures=True";
    },
    regions:"/api/regions.json",
    parks:"/api/parks.json",
    park_price_history:function (id) {
       return "/api/parks/"+id+"/price_history.json";
    },
    park_current_price:function (id,arrival) {
      return "/api/parks/"+id+"/current_price.json?arrival="+arrival;
    },
    park:function (id) {
       return "/api/parks/"+id+".json";
    },
    // Campgrounds
    campgrounds:"/api/campgrounds.json",
    campground:function (id) {
        return "/api/campgrounds/"+id+".json";
    },
    campground_price_history: function(id){
        return "/api/campgrounds/"+ id +"/price_history.json";
    },
    campground_current_price:function (id,start,end) {
       return "/api/campgrounds/"+ id +"/current_price.json?arrival="+start+"&departure="+end;
    },
    campgroundStayHistory: function(id){
        return "/api/campgrounds/" + id + "/stay_history.json"
    },
    campground_stay_history_detail: function(id){
        return "/api/campground_stay_history/"+ id +".json";
    },
    campground_stay_history: "/api/campground_stay_history.json",
    addPrice: function(id){
        return "/api/campgrounds/"+ id +"/addPrice.json";
    },
    editPrice: function(id){
        return "/api/campgrounds/"+ id +"/updatePrice.json";
    },
    campgroundCampsites: function(id){
        return "/api/campgrounds/" + id + "/campsites.json"
    },
    opencloseCG: function(id){
        return "/api/campgrounds/" + id + "/open_close.json"
    },
    deleteBookingRange: function (id) {
        return "/api/campground_booking_ranges/" + id + ".json"
    },
    campground_status_history_detail: function(id){
        return "/api/campground_booking_ranges/"+ id +".json?original=true";
    },
    delete_campground_price: function(id){
        return "/api/campgrounds/" + id + "/deletePrice.json";
    },
    // Campsites
    campsites:"/api/campsites.json",
    campsites_stay_history: "/api/campsites_stay_history.json",
    campsites_stay_history_detail: function(id){
        return "/api/campsites_stay_history/"+ id +".json";
    },
    campsites_price_history: function(id){
        return "/api/campsites/"+ id +"/price_history.json";
    },
    campsites_status_history:function(id){
        return "/api/campsites/" + id + "/status_history.json?closures=True"
    },
    campsite:function (id) {
        return "/api/campsites/"+id+".json";
    },
    campsiteStayHistory: function(id){
        return "/api/campsites/" + id + "/stay_history.json"
    },
    opencloseCS: function(id){
        return "/api/campsites/" + id + "/open_close.json"
    },
    deleteCampsiteBookingRange: function (id) {
        return "/api/campsite_booking_ranges/" + id + ".json"
    },
    campsite_status_history_detail: function(id){
        return "/api/campsite_booking_ranges/"+ id +".json?original=true";
    },
    available_campsites:function(campground,arrival,departure){
      return "/api/campgrounds/"+campground+"/available_campsites.json?arrival="+arrival+"&departure="+departure;
    },
    features:"/api/features.json",
    campsite_rate: "/api/campsite_rate.json",
    campsiterate_detail:function (id) {
        return "/api/campsite_rate/"+id+".json"
    },
    rates:"/api/rates.json",

    // campsite types
    campsite_classes:"/api/campsite_classes.json",
    campsite_classes_active:"/api/campsite_classes.json?active_only=true",
    campsite_class:function (id) {
        return "/api/campsite_classes/"+id+".json"
    },
    addCampsiteClassPrice: function(id){
        return "/api/campsite_classes/"+id+"/addPrice.json"
    },
    editCampsiteClassPrice(id) {
        return "/api/campsite_classes/"+id+"/updatePrice.json"
    },
    deleteCampsiteClassPrice(id) {
        return "/api/campsite_classes/"+id+"/deletePrice.json"
    },
    campsiteclass_price_history: function(id){
        return "/api/campsite_classes/"+ id +"/price_history.json";
    },
    closureReasons:function () {
        return "/api/closureReasons.json";
    },
    openReasons:function () {
        return "/api/openReasons.json";
    },
    priceReasons:function () {
        return "/api/priceReasons.json";
    },
    maxStayReasons:function () {
        return "/api/maxStayReasons.json";
    },
    bulkPricing: function(){
        return "/api/bulkPricing";
    },
    //bookings
    bookings:"/api/booking.json",
    //other
    countries:"https://restcountries.eu/rest/v1/?fullText=true",
    users: "/api/users.json",
    usersLookup: function (q) {
       return  encodeURI("/api/users.json?q="+q);
    }
};
