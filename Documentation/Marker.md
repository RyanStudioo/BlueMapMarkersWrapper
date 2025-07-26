*[<u>Back to README.md</u>](../README.md)*
# Markers
 - [BaseMarker](#basemarker)

## BaseMarker
> class bluemap_wrapper.BaseMarker

The Base class of all other Markers
### Attributes
 - [key](#key-str)
 - [label](#label-str)
 - [position](#position-position)

> Attributes
### key (str)
The key of the Marker
### label (str)
The given name for a Marker
### position (Position)
The position of a marker

<br/>

## ExtrudeMarker(BaseMarker)
> class bluemap_wrapper.ExtrudeMarker

A Marker with a 3D shape
### Attributes
 - [BaseMarker Attributes](#attributes)
 - [shape](#shape-listposition)
 - [shape_min_y](#shape_min_y-int)
 - [shape_max_y](#shape_max_y-int)
 - [detail](#detail-optionalunionstr-none)

> Attributes
### shape (list[[Position]()])
A list of coordinates that traces the shape on the x and z axis
### shape_min_y (int)
The lowest point of the shape
### shape_max_y (int)
The tallest point of the shape
### detail (Optional[Union[str, None]])
HTML information of the Marker
 
<br/>

## HTMLMarker(BaseMarker)
> class bluemap_wrapper.HTMLMarker
 
A Marker that displays HTML code
### Attributes
 - [BaseMarker Attributes](#attributes)
 - [html](#html-str)
 - [classes](#classes-optionalunionliststr-none)

> Attributes
### html (str)
HTML information of the Marker
### classes (Optional[Union[list[str], None])
a list of CSS classes to be applied to [html](#html-str) 

<br/>

## LineMarker(BaseMarker)
> class bluemap_wrapper.LineMarker
 
A Marker that displays a line connecting several points
### Attributes
 - [BaseMarker Attributes](#attributes)
 - [line](#line-listposition)
 - [detail](#detail-str)

> Attributes
### line (list[[Position]()])
A list of Position Objects that forms the line
### detail (str)
HTML information of the Marker

<br/>

## POIMarker(BaseMarker)
> class bluemap_wrapper.POIMarker
 
A Marker that displays a line connecting several points
### Attributes
 - [BaseMarker Attributes](#attributes)
 - [line](#line-listposition)
 - [detail](#detail-str)

> Attributes
### line (list[[Position]()])
A list of Position Objects that forms the line
### detail (str)
HTML information of the Marker