*[<u>Back to README.md</u>](../README.md)*
# MarkerSets
 - [MarkerSet](#markerset)

## MarkerSet
> class bluemap_wrapper.MarkerSet

A MarkerSet is a set of markers. They may have similar properties such as land markers in the lands plugin, or may be
custom made.

### Attributes
 - [key](#key-str)
 - [label](#label-str)
 - [markers](#markers-listmarkermarkermdmarkers)
 - [length](#length-int)
### Methods
 - [extrude_markers()](#extrude_markers)
 - [html_markers()](#html_markers)
 - [line_markers()](#line_markers)
 - [poi_markers()](#poi_markers)
 - [shape_markers()](#shape_markers)

<br/>

> Attributes
### key (str)
The key of the [MarkerSet](#markerset)
### label (str)
The set name of the [MarkerSet](#markerset)
### markers (list[[Marker](Marker.md#markers)])
A list of markers in the [MarkerSet](#markerset)
### length (int)
The amount of markers in [markers](#markers-listmarkermarkermdmarkers)

<br/>

> Methods
### extrude_markers()
#### Returns:
A list of ExtrudeMarker Objects from [markers](#markers-listmarkermarkermdmarkers)
#### Return Type:
list(Union[[ExtrudeMarker](Marker.md#extrudemarkerbasemarker), None])

### html_markers()
#### Returns:
A list of HTMLMarker Objects from [markers](#markers-listmarkermarkermdmarkers)
#### Return Type:
list(Union[[HTMLMarker](Marker.md#htmlmarkerbasemarker), None])

### line_markers()
#### Returns:
A list of LineMarker Objects from [markers](#markers-listmarkermarkermdmarkers)
#### Return Type:
list(Union[[LineMarker](Marker.md#linemarkerbasemarker), None])

### poi_markers()
#### Returns:
A list of POIMarker Objects from [markers](#markers-listmarkermarkermdmarkers)
#### Return Type:
list(Union[[POIMarker](Marker.md#poimarkerbasemarker), None])

### shape_markers()
#### Returns:
A list of ShapeMarker Objects from [markers](#markers-listmarkermarkermdmarkers)
#### Return Type:
list(Union[[ShapeMarker](Marker.md#shapemarkerbasemarker), None])