// $(".panel-left").resizable({
//   handleSelector: ".splitter",
//   resizeHeight: false,
// });

// Split(['.panel-left','.panel-right'])

$(document).ready(function () {
  console.log("ready!");
  Split(['#right', '#left'], {
    gutterSize: 15,
    minSize: [400, 600],
  });
});