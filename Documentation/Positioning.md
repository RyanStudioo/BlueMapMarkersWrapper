*[<u>Back to README.md</u>](../README.md)*
# Positions
 - [Coordinate](#position)
 - [Rotation](#rotation)

## Position
> class BlueMapWrapper.Coordinate

A set of x, y and z coordinates to mark a point

### Attributes
 - [x](#x-float)
 - [y](#y-float)
 - [z](#z-float)

> Attributes
### x (float)
X coordinate
### y (float)
Y coordinate, if a Y coordinate is not given (eg. [ShapeMarker](Marker.md#shapemarkerbasemarker)), this value will default at 0
### z (float)
Z coordinate

## Rotation
> class BlueMapWrapper.Rotation

A pitch, roll, and yaw to determine the direction a player is facing

### Attributes
 - [pitch](#pitch-float)
 - [roll](#roll-float)
 - [yaw](#yaw-float)

> Attributes
### pitch (float)
The rotation of a player's head on the Y axis (up-down)
### roll (float)
rotation of head to the sides (I honestly have no clue)
### yaw (float)
The rotation of a player's head on the X-Z axis (left-right)