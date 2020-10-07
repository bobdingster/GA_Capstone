Restaurants = {
  init: function(restaurant_names) {
    this.autoComplete(restaurant_names)
    this.searchIconClick()
  },

  autoComplete: function(restaurant_names) {
    $(".input-text.restaurant" ).autocomplete({
      source: restaurant_names
    });
  },

  searchIconClick: function(){
    $(".search").on("click", function() {
      $(".search img").hide();
      $(".loader").show();
    })
  }
}