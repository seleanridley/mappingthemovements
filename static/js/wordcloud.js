var svg;
var width;
var height;

function WordCloud(options) {
  var margin = {top: 70, right: 100, bottom: 0, left: 100},
      w = 1200 - margin.left - margin.right,
      h = 400 - margin.top - margin.bottom;
      width = w;
      height = h;

  // create the svg
  svg = d3.select(options.container).append("svg")
  .attr('height', h + margin.top + margin.bottom)
  .attr('width', w + margin.left + margin.right)

  // set the ranges for the scales
  var xScale = d3.scaleLinear().range([10, 100]);

  var focus = svg.append('g')
  .attr("transform", "translate(" + [w/2, h/2+margin.top] + ")")

  var colorMap = ['red', '#a38b07'];

  // seeded random number generator
  var arng = new alea('hello.');

  var data;
  d3.json(options.data, function(error, d) {
    if (error) throw error;
    data = d;
    var word_entries = d3.entries(data['count']);
    xScale.domain(d3.extent(word_entries, function(d) {return d.value;}));

    makeCloud();

    function makeCloud() {
      d3.layout.cloud().size([w, h])
      .timeInterval(20)
      .words(word_entries)
      .fontSize(function(d) { return xScale(+d.value); })
      .text(function(d) { return d.key; })
      .font("Impact")
      .random(arng)
      .on("end", function(output) {
        // sometimes the word cloud can't fit all the words- then redraw
        // https://github.com/jasondavies/d3-cloud/issues/36
        if (word_entries.length !== output.length) {
          console.log("not all words included- recreating");
          makeCloud();
          return undefined;
        } else { draw(output); }
      })
      .start();
    }

    d3.layout.cloud().stop();

  });

  function draw(words) {
    focus.selectAll("text")
    .data(words)
    .enter().append("text")
    .style("font-size", function(d) { return xScale(d.value) + "px"; })
    .style("font-family", "Impact")
    .style("fill", function(d, i) { return colorMap[~~(arng() *2)]; })
    .attr("text-anchor", "middle")
    .attr("transform", function(d) {
      return "translate(" + [d.x, d.y] + ")rotate(" + d.rotate + ")";
    })
    .text(function(d) { return d.key; });
  }
}

function SaveButton(options) {
  // Set-up the export button
  d3.select('#saveButton').on('click', function(){
    var svgString = getSVGString(svg.node());
    svgString2Image( svgString, 2*width, 2*height, 'png', save ); // passes Blob and filesize String to the callback

    function save( dataBlob, filesize ){
      saveAs( dataBlob, 'wordcloud.png' ); // FileSaver.js function
    }
  });

  // Below are the functions that handle actual exporting:
  // getSVGString ( svgNode ) and svgString2Image( svgString, width, height, format, callback )
  function getSVGString( svgNode ) {
  	svgNode.setAttribute('xlink', 'http://www.w3.org/1999/xlink');
  	var cssStyleText = getCSSStyles( svgNode );
  	appendCSS( cssStyleText, svgNode );

  	var serializer = new XMLSerializer();
  	var svgString = serializer.serializeToString(svgNode);
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
