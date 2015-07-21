//Color scales
var shortColor = d3.scale.ordinal()
.range(
    ["#ba0c2f" //Red
    ,"#1b365d" //blue
    ,"#ea7600" //Orange
    ,"#93328e" //purple
    ,"#0095c8" //lightblue
    ,"#b7bf10"] //Yellow
);

var longColor = d3.scale.ordinal()
.range(
    ['#00688c'
    ,'#be84bb'
    ,'#662363'
    ,'#b7bf10'
    ,'#0c192d'
    ,'#1b365d'
    ,'#cceaf4'
    ,'#f2ad66'
    ,'#ea7600'
    ,'#0095c8'
    ,'#595d07'
    ,'#66bfde'
    ,'#471845'
    ,'#e9d6e8'
    ,'#820820'
    ,'#93328e'
    ,'#004862'
    ,'#f7f2cf'
    ,'#80850b'
    ,'#f7ced5'
    ,'#d4d970'
    ,'#d1d7df'
    ,'#122541'
    ,'#76869e'
    ,'#5b0516'
    ,'#fbe4cc'
    ,'#ba0c2f'
    ,'#723900'
    ,'#d66d82'
    ,'#a35200']
);

//Number formatting
function abbrNum(number, decPlaces) {
    // 2 decimal places => 100, 3 => 1000, etc
    decPlaces = Math.pow(10,decPlaces);

    // Enumerate number abbreviations
    var abbrev = [ "k", "m", "b", "t" ];

    // Go through the array backwards, so we do the largest first
    for (var i=abbrev.length-1; i>=0; i--) {

        // Convert array index to "1000", "1000000", etc
        var size = Math.pow(10,(i+1)*3);

        // If the number is bigger or equal do the abbreviation
        if(size <= number) {
             // Here, we multiply by decPlaces, round, and then divide by decPlaces.
             // This gives us nice rounding to a particular decimal place.
             number = Math.round(number*decPlaces/size)/decPlaces;

             // Handle special case where we round up to the next abbreviation
             if((number == 1000) && (i < abbrev.length - 1)) {
                 number = 1;
                 i++;
             }

             // Add the letter for the abbreviation
             number += abbrev[i];

             // We are done... stop
             break;
        }
    }

    return number;
};

//Tooltip functions
$(document).ready(function(){
    $("body").append("<div class='tooltip' id='tooltip' style='position:absolute;background-color: rgb(255, 255, 255); border: 1px solid rgb(128, 128, 128); opacity: 0.9; padding: 1px 5px;'></div>");
    window.hideTooltip = function() {
        return $('#tooltip').hide();
    };

    window.hideTooltip();
});

window.updatePosition = function(event) {
  var curX, curY, tth, ttleft, tttop, ttw, wscrX, wscrY, xOffset, yOffset;
  xOffset = 20;
  yOffset = 10;
  ttw = $("#tooltip").width();
  tth = $("#tooltip").height();
  wscrY = $(window).scrollTop();
  wscrX = $(window).scrollLeft();
  curX = document.all ? event.clientX + wscrX : event.pageX;
  curY = document.all ? event.clientY + wscrY : event.pageY;
  ttleft = (curX - wscrX + xOffset * 2 + ttw) > $(window).width() ? curX - ttw - xOffset * 2 : curX + xOffset;
  if (ttleft < wscrX + xOffset) {
    ttleft = wscrX + xOffset;
  }
  tttop = (curY - wscrY + yOffset * 2 + tth) > $(window).height() ? curY - tth - yOffset * 2 : curY + yOffset;
  if (tttop < wscrY + yOffset) {
    tttop = curY + yOffset;
  }
  return $("#tooltip").css('top', tttop + 'px').css('left', ttleft + 'px');
};

window.showTooltip = function(content, event) {
  $('#tooltip').html(content);
  $('#tooltip').show();
  return window.updatePosition(event);
};

show_details = function(data, i, element) {
    var content;
    d3.select(element)
    .attr("stroke-width","2px");
    content = "<span class=\"tooltip\"> " + data + "</span><br/>";
    return showTooltip(content, d3.event);};
hide_details = function(data, i, element) {
    d3.select(element)
    .attr("stroke-width","1px");
    return hideTooltip();}


function table(conf) {
    //Draw table
    var data = conf.data;
    if (typeof(conf.timeVar)!="undefined") {
        data.sort(function (a,b){
            if(a[conf.xVar] == b[conf.xVar]){
                return (a[conf.timeVar] < b[conf.timeVar]) ? -1 : (a[conf.timeVar] > b[conf.timeVar]) ? 1 : 0;
            }else{
                return (a[conf.xVar] < b[conf.xVar]) ? -1 : 1;
            };
        });
    }else{
        data.sort(function (a,b){
            if(a[conf.xVar] < b[conf.xVar]) return -1;
            if(a[conf.xVar] > b[conf.xVar]) return 1;
            return 0;
        });  
    };
    $tableDiv = $(conf.selector)
    var dataLen = data.length>1001?1001:data.length;
    var html = "<table>"
    var header = Object.keys(data[0]),
        headerLen = header.length;
        html += "<tr>"
        html += "<th>row</th>"
        for (var j = 0; j < headerLen; j++) {
            html += "<th>"
            html += header[j]
            html += "</th>"
        }
        html += "</tr>"
    for (var i = 0; i < dataLen; i++) {
        var row = data[i];
        html += "<tr>"
        html += "<td>"+i+"</td>"
        for (var key in row) {
            html += "<td>"
            html += row[key]
            html += "</td>"
        }
        html += "</tr>"
    }
    html += "</table>"
    $tableDiv.html(html)
};

function slider(timeVar){
    var html = "<div id='sliderHolder'>"
    html += "<p>"
	html += "<label for='year'>"+timeVar+": </label>"
	html += "<input type='text' id='year' style='border:0; color:#0800FF; font-weight:bold;' />"
    html += "<button id='play'>&#9658;</button>"
    html += "</p>"
    html += "<div id='slider'></div>"
    html += "</div>"
    return html
};

function bar(conf){
    var data = conf.data;
    data.sort(function (a,b){
        if(a[conf.yVar] < b[conf.yVar]) return -1;
        if(a[conf.yVar] > b[conf.yVar]) return 1;
        return 0;
    });
    xUnique = _.uniq(data,function(d){return d[conf.xVar]}).length == data.length;
    //Make chart
    var margin = {
        top: 10,
        right: 60,
        bottom: 30,
        left: 60
    };
    var svg = d3.select(conf.selector).append('svg');
    svg.html("")
    svg.attr('viewBox','0 0 1120 440'); 
    var g = svg.append('g')
        .attr('transform', 'translate(' + margin.left + ',' + margin.top + ')');
    
    var yScale = d3.scale.linear();
    
    var yAxis = d3.svg.axis()
        .scale(yScale)
        .orient("left");
        
    var yAxisContainer = g.append("g")
        .attr("class", "axis");
    
    var barContainer = g.append('g')
        .attr('class', 'barContainer');
        
    var availableWidth = 1000;
    var height = 400;
    
    var yMin = 0;
    var yMax = d3.max(data, function (d){
        return parseFloat(d[conf.yVar]);
    })
    
    yScale.domain([yMin, yMax]);
    yScale.range([height, 0])
    yScale.nice();
    
    if (conf.timeVar) {
        var timeExtent = d3.extent(data,function (d){
            return d[conf.timeVar];
        })
        var maxEntriesPerYear = d3.max(_.values(_.countBy(data, function(d) {
            return d[conf.timeVar];
        })));
        
        var yearMin = timeExtent[0];
        var yearMax = timeExtent[1];
        
        var filteredData = _.filter(data, function (d){
            return d[conf.timeVar] == yearMin;
        });
        //Slider config
        $(conf.selector).append(slider(conf.timeVar));
        $( "#year" ).val( yearMin );
        $( "#slider" ).slider({value:yearMin,
			min: yearMin,
			max: yearMax,
			step: 1,
			slide: function( event, ui ) {$( "#year" ).val( ui.value );}});
        var timeouts = [];
        play = function(){
            for(var timeout in timeouts){
                clearTimeout(timeouts[timeout])
            };
            timeouts = [];
            yearLen = yearMax-yearMin
            for(i=0;i<yearLen;i++){
                $('#slider').slider( "option", "value", yearMin)
                $('#year').val( yearMin)
                slideAnimate = setTimeout(function(){
                    var newTime = parseFloat($('#slider').slider( "option", "value" ))+1;
                    if (newTime<=yearMax) {
                        $('#slider').slider( "option", "value", newTime );
                        $('#year').val(newTime);
                    }
                },(i+1)*1000)
                timeouts.push(slideAnimate);
            }
        };
        $('#play').click(function(){play()})
        $('#slider').slider({slide: function (event,ui){
            $( "#year" ).val( ui.value );
            var filteredData = _.filter(data, function (d){
                return d[conf.timeVar] == $( "#slider" ).slider( "value" );
            });
            filteredData.sort(function (a,b){
                return b[conf.yVar] - a[conf.yVar];
            });
            drawBars(filteredData);
        }});
        $('#slider').slider({change: function (event,ui){
            $( "#year" ).val( ui.value );
            var filteredData = _.filter(data, function (d){
                return d[conf.timeVar] == $( "#slider" ).slider( "value" );
            });
            filteredData.sort(function (a,b){
                return b[conf.yVar] - a[conf.yVar];
            });
            drawBars(filteredData);
        }});
    } else {
        var maxEntriesPerYear = data.length,
        filteredData = data;
    };
    
    var padding = 2;
    var barWidth = (availableWidth / maxEntriesPerYear - padding) > 1 ? (availableWidth / maxEntriesPerYear - padding) : 1;

    filteredData.sort(function (a,b){
        return b[conf.yVar] - a[conf.yVar];
    });
    yAxis
        .ticks(4)
        //.tickFormat(function(d) {
        //    return logFormat(d)
        //})
        .tickFormat(function(d){return abbrNum(d, 2)})
        .tickPadding(15);
    
        yAxisContainer.transition().duration(500)
        .call(yAxis);
    
    function drawBars(data){
        var bars =  barContainer.selectAll('.bar')
            .data(data, function (d, i){
                return xUnique ? d[conf.xVar] : i;
            })
        
        bars.enter()
            .append('rect')
            .on("mousemove", function(d, i) {return show_details(
                conf.xVar + ": " + d[conf.xVar]
                + "<br/>"
                + conf.yVar + ": " + d[conf.yVar]
                + (conf.timeVar ? "<br/>" + conf.timeVar + ": " + d[conf.timeVar] : "")
                , i, this)})
            .on("mouseout", function(d, i) {return hide_details(d[conf.xVar], i, this);});
        
        bars.transition().duration(50)
            .attr({
                height: function (d) {
                    return height - yScale(d[conf.yVar]);
                },
                y: function (d) {
                    return yScale(d[conf.yVar]);
                },
        
                width: function (d) {
                    return barWidth;
                },
        
                x: function (d, i) {
                    return i * barWidth + i * padding;
                },
                class: "bar",
                
                fill: function(d, i) {return shortColor(d[conf.xVar])}
            })

        bars.exit().remove();
    };
    
    drawBars(filteredData);
};

function defaultValues(data, dim1, dim2, valueDim, defaultVal) {
    var uniDim1 = _.uniq(data,function(d){return d[dim1]}),
    uniDim2 = _.uniq(data,function(d){return d[dim2]});
    for(key1 in uniDim1){
        for(key2 in uniDim2){
            var match = _.find(data,function(d){
                return d[dim1] == uniDim1[key1][dim1] && d[dim2] == uniDim2[key2][dim2];     
            });
            if (typeof(match)=="undefined") {
                var obj = {};
                obj[dim1] = uniDim1[key1][dim1];
                obj[dim2] = uniDim2[key2][dim2];
                obj[valueDim] = defaultVal;
                obj['defaultVal'] = true;
                data.push(obj);
            }
        };
    };
};

function area(conf){
    var data = _.filter(conf.data, function (d){
                    return typeof(d[conf.yVar])=="number";
                });
    defaultValues(data, conf.xVar, conf.timeVar, conf.yVar, 0);
    data.sort(function (a,b){
        if(a[conf.timeVar] < b[conf.timeVar]) return -1;
        if(a[conf.timeVar] > b[conf.timeVar]) return 1;
        return 0;
    });
    var margin = {top: 20, right: 30, bottom: 30, left: 40};
    var svgParent = d3.select(conf.selector).append('svg');
    svgParent.attr('viewBox','0 0 800 400');
    var svg = svgParent.append("g")
    .attr("transform", "translate(" + margin.left + "," + margin.top + ")");
        
    width = 800 - margin.left - margin.right,
    height = 400 - margin.top - margin.bottom;
    
    var x = d3.scale.linear()
        .range([0, width]);

    var y = d3.scale.linear()
        .range([height, 0]);
        
    var xAxis = d3.svg.axis()
        .scale(x)
        .tickFormat(function(d){return d})
        .orient("bottom");
    
    var yAxis = d3.svg.axis()
        .scale(y)
        .tickFormat(function(d){return abbrNum(d,2)})
        .orient("left");

    var stack = d3.layout.stack()
        .offset("zero")
        .values(function(d) { return d.values; })
        .x(function(d) { return d[conf.timeVar]; })
        .y(function(d) { return d[conf.yVar]; });
        
    var nest = d3.nest()
        .key(function(d) { return d[conf.xVar]; });
        
    var area = d3.svg.area()
        .interpolate("linear")
        .x(function(d) { return x(d[conf.timeVar]); })
        .y0(function(d) { return y(d.y0); })
        .y1(function(d) { return y(d.y0 + d.y); });

    var layers = stack(nest.entries(data));
    
    x.domain(d3.extent(data, function(d) { return d[conf.timeVar]; }));
    y.domain([0, d3.max(data, function(d) { return d.y0 + d.y; })]);
    
    svg.selectAll(".layer")
        .data(layers)
      .enter().append("path")
        .attr("class", "layer")
        .attr("d", function(d) { return area(d.values); })
        .style("fill", function(d, i) { return longColor(i); })
        .on("mousemove", function(d, i) {return show_details(
                conf.xVar + ": " + d.key
                , i, this)})
        .on("mouseout", function(d, i) {return hide_details(d.key, i, this);});
        
    svg.append("g")
        .attr("class", "axis")
        .attr("transform", "translate(0," + height + ")")
        .call(xAxis);
  
    svg.append("g")
        .attr("class", "axis")
        .call(yAxis);
};