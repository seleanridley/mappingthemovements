var svg;
var w;
var h;

function LineGraph(options) {
  // set the dimensions and margins of the graph
  var margin = {top: 20, right: 20, bottom: 30, left: 50},
      width = 960 - margin.left - margin.right,
      height = 500 - margin.top - margin.bottom;

  w = width;
  h = height;

  //generate code
  function domain () {
    this.stroke="#000"
    this.d="M-6,450.5H0.5V0.5H-6"
  }

  function g () {

  }

  // parse the date / time
  var parseTime = d3.timeParse("%Y-%m-%d");

  // set the ranges
  var x = d3.scaleTime().range([0, width]);
  var y = d3.scaleLinear().range([height, 0]);

  // define the line
  var valueline = d3.line()
  .x(function(d) { return x(d["date created"]); })
  .y(function(d) { return y(d["comments"]); });

  // append the svg obgect to the body of the page
  // appends a 'group' element to 'svg'
  // moves the 'group' element to the top left margin
  svg = d3.select(options.container).append("svg")
  .attr("width", width + margin.left + margin.right)
  .attr("height", height + margin.top + margin.bottom)
  .append("g")
  .attr("transform",
      "translate(" + margin.left + "," + margin.top + ")");


  // Get the data
  d3.json(options.data, function(error, data) {
    if (error) throw error;

    // trigger render
    draw(data, "submissions");
  });

  function draw(data, country) {

    var data = data[country];

    // format the data
    data.forEach(function(d) {
      d["date created"] = parseTime(d["date created"]);
      d.comments = +d.comments;
    });

    // sort years ascending
    data.sort(function(a, b){
      return a["date created"]-b["date created"];
    });

    // Scale the range of the data
    x.domain(d3.extent(data, function(d) { return d["date created"]; }));
    y.domain([0, d3.max(data, function(d) {
      return d["comments"]; })]);

    // Add the valueline path.
    svg.append("path")
    .data([data])
    .attr("class", "line")
    .attr("d", valueline);

    // Add the X Axis
    svg.append("g")
    .attr("transform", "translate(0," + height + ")")
    .attr("class", "axisBlue")
    .call(d3.axisBottom(x));

    // Add the Y Axis
    svg.append("g")
    .attr("class", "axisBlue")
    .call(d3.axisLeft(y));
  }
}


function SaveButton(options) {
  // Set-up the export button
  d3.select('#saveButton').on('click', function(){
    var svgString = getSVGString(svg.node())
    svgString2Image( svgString, 2*w, 2*h, 'png', save ); // passes Blob and filesize String to the callback
    function save( dataBlob, filesize ){
      saveAs( dataBlob, 'D3 vis exported to png.png' ); // FileSaver.js function
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