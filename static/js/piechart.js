var svg;
var w;
var h;

function PieChart(options) {
  svg = d3.select("svg"),
      width = +svg.attr("width"),
      height = +svg.attr("height"),
      radius = Math.min(width, height) / 2,
      g = svg.append("g").attr("transform", "translate(" + width / 2 + "," + height / 2 + ")");

  w = +svg.attr("width");
  h = +svg.attr("height");

  var color = d3.scaleOrdinal(["#98abc5", "#8a89a6", "#7b6888", "#6b486b", "#a05d56", "#d0743c", "#ff8c00"]);

  var pie = d3.pie()
  .sort(null)
  .value(function(d) { return d.frequency; });

  var path = d3.arc()
  .outerRadius(radius - 10)
  .innerRadius(0);

  var label = d3.arc()
  .outerRadius(radius - 40)
  .innerRadius(radius - 40);

  d3.json(options.data, function(data) {

    data.forEach(function(d) {
      d.subreddit = d.subreddit;
      d.frequency = +d.frequency;
    });


    var arc = g.selectAll(".arc")
    .data(pie(data))
    .enter().append("g")
    .attr("class", "arc");

    arc.append("path")
    .attr("d", path)
    .attr("fill", function(d) { return color(d.data.subreddit); });

    arc.append("text")
    .attr("transform", function(d) { return "translate(" + label.centroid(d) + ")"; })
    .attr("dy", "0.35em")
    .text(function(d) { return d.data.subreddit; });
  });
}

function SaveButton(options) {
  // Set-up the export button
  d3.select('#saveButton').on('click', function(){
    var svgString = getSVGString(svg.node());
    console.log(svgString);
    svgString2Image( svgString, 2*w, 2*h, 'jpeg', save ); // passes Blob and filesize String to the callback
    function save( dataBlob, filesize ){
      saveAs( dataBlob, 'D3 vis exported to JPEG.jpeg' ); // FileSaver.js function
    }
  });

  // Below are the functions that handle actual exporting:
  // getSVGString ( svgNode ) and svgString2Image( svgString, width, height, format, callback )
  function getSVGString( svgNode ) {
    svgNode.setAttribute('xlink', 'http://www.w3.org/1999/xlink');
    var cssStyleText = getCSSStyles( svgNode );
    appendCSS( cssStyleText, svgNode );

    var serializer = new XMLSerializer();
    var svgString = serializer.serializeToString(d3.select('svg').node());
    svgString = svgString.replace(/(\w+)?:?xlink=/g, 'xmlns:xlink='); // Fix root xlink without namespace
    svgString = svgString.replace(/NS\d+:href/g, 'xlink:href'); // Safari NS namespace fix

    return svgString;

    function getCSSStyles( parentElement ) {
      var selectorTextArr = [];

      // Add Parent element Id and Classes to the list
      selectorTextArr.push( '#'+parentElement.id );
      for (var c = 0; c < parentElement.classList.length; c++)
        if ( !contains('.'+parentElement.classList[c], selectorTextArr) )
          selectorTextArr.push( '.'+parentElement.classList[c] );

      // Add Children element Ids and Classes to the list
      var nodes = parentElement.getElementsByTagName("*");
      for (var i = 0; i < nodes.length; i++) {
        var id = nodes[i].id;
        if ( !contains('#'+id, selectorTextArr) )
          selectorTextArr.push( '#'+id );

        var classes = nodes[i].classList;
        for (var c = 0; c < classes.length; c++)
          if ( !contains('.'+classes[c], selectorTextArr) )
            selectorTextArr.push( '.'+classes[c] );
      }

      // Extract CSS Rules
      var extractedCSSText = "";
      for (var i = 0; i < document.styleSheets.length; i++) {
        var s = document.styleSheets[i];

        try {
          if(!s.cssRules) continue;
        } catch( e ) {
          if(e.name !== 'SecurityError') throw e; // for Firefox
          continue;
        }

        var cssRules = s.cssRules;
        for (var r = 0; r < cssRules.length; r++) {
          if ( contains( cssRules[r].selectorText, selectorTextArr ) )
            extractedCSSText += cssRules[r].cssText;
        }
      }


      return extractedCSSText;

      function contains(str,arr) {
        return arr.indexOf( str ) === -1 ? false : true;
      }

    }

    function appendCSS( cssText, element ) {
      var styleElement = document.createElement("style");
      styleElement.setAttribute("type","text/css");
      styleElement.innerHTML = cssText;
      var refNode = element.hasChildNodes() ? element.children[0] : null;
      element.insertBefore( styleElement, refNode );
    }
  }


  function svgString2Image( svgString, width, height, format, callback ) {
    var format = format ? format : 'png';

    var imgsrc = 'data:image/svg+xml;base64,'+ btoa( unescape( encodeURIComponent( svgString ) ) ); // Convert SVG string to data URL

    var canvas = document.createElement("canvas");
    var context = canvas.getContext("2d");

    canvas.width = width;
    canvas.height = height;

    var image = new Image();
    image.onload = function() {
      context.clearRect ( 0, 0, width, height );
      context.drawImage(image, 0, 0, width, height);

      canvas.toBlob( function(blob) {
        var filesize = Math.round( blob.length/1024 ) + ' KB';
        if ( callback ) callback( blob, filesize );
      });


    };

    image.src = imgsrc;
  }

}
