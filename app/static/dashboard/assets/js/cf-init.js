(function ($) {
  // Svg
  /*
   * Replace all SVG images with inline SVG
   */
  $(function () {
    $("img.svg").each(function () {
      var $img = $(this);
      var imgID = $img.attr("id");
      var imgClass = $img.attr("class");
      var imgURL = $img.attr("src");
      $.get(
        imgURL,
        function (data) {
          // Get the SVG tag, ignore the rest
          var $svg = $(data).find("svg");

          // Add replaced image's ID to the new SVG
          if (typeof imgID !== "undefined") {
            $svg = $svg.attr("id", imgID);
          }
          // Add replaced image's classes to the new SVG
          if (typeof imgClass !== "undefined") {
            $svg = $svg.attr("class", imgClass + " replaced-svg");
          }

          // Remove any invalid XML tags as per http://validator.w3.org
          $svg = $svg.removeAttr("xmlns:a");

          // Check if the viewport is set, if the viewport is not set the SVG wont't scale.
          if (
            !$svg.attr("viewBox") &&
            $svg.attr("height") &&
            $svg.attr("width")
          ) {
            $svg.attr(
              "viewBox",
              "0 0 " + $svg.attr("height") + " " + $svg.attr("width")
            );
          }

          // Replace image with new SVG
          $img.replaceWith($svg);
        },
        "xml"
      );
    });
  });

  let date = new Date().getFullYear();
  if (document.querySelector("#year")) {
    document.querySelector("#year").innerHTML = date;
  }

  $(function () {
    var path = $(".sidebar a");
    var settings = $("#setting");
    var settingsNav = $("#setting-nav a");
    for (var i = 0; i < path.length; i++) {
      var element = path[i];
      if (window.location.href.includes(element.href)) {
        element.parentElement.classList.add("mm-active");
      } else if (
        settingsNav.filter(
          (i, data) => window.location.href.includes(data.href) && data
        ).length
      ) {
        settingsNav
          .filter(
            (i, data) => window.location.href.includes(data.href) && data
          )[0]
          .classList.add("active_");
      } else if (window.location.pathname === "/") {
        if (element.href.includes("index.html")) {
          element.parentElement.classList.add("mm-active");
        }
      } else {
        element.parentElement.classList.remove("mm-active");
      }
    }
    if (
      settingsNav.filter(
        (i, data) => window.location.href.includes(data.href) && data
      ).length
    ) {
      settings.addClass("mm-active");
    }
  });

  // MetisMenu
  $("#menu").metisMenu();
  // scrollbar

  if (document.querySelector("#menu")) {
    new PerfectScrollbar("#menu");
    new PerfectScrollbar("#gg_notification");
  }
})(jQuery);

function copy(value) {
  
  navigator.clipboard.writeText(value);

  /* Alert the copied text */
  alert("Copied the text: " + value);
}
function copyApi(dValue) {
  let value = dValue ? dValue : "https://www.codeefly.con/join/12345";
  navigator.clipboard.writeText(value);

  /* Alert the copied text */
  alert("Copied Key: " + value);
}

//  Preloader
jQuery(window).on("load", function () {
  $(".preloader").fadeOut(500);
  $("main").addClass("show");
});
