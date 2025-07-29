*[<u>Back to README.md</u>](../README.md)*
# Collections
- [Collection](#collection)
- [MarkerCollection](#markercollection)
- [PlayerCollection](#playercollection)

## Collection
> class bluemap_wrapper.Collection

Contains a [MarkerCollection](#markercollection) and [PlayerCollection](#playercollection) Object

Used when a simultaneous marker and player request is made

### Attributes
 - [marker_collection](#marker_collection-markercollection)
 - [player_collection](#player_collection-playercollection)


> Attributes

### marker_collection ([MarkerCollection](#markercollection))
a MarkerCollection Object

### player_collection ([PlayerCollection](#playercollection))
a PlayerCollection Object

<br/>

## MarkerCollection
> class bluemap_wrapper.MarkerCollection

Contains a list of MarkerSet Objects

This class is also Iterable on its own

### Attributes
 - [marker_sets](#marker_sets-listmarkerset)
 - [length](#length-int)

### Methods
 - [from_key()](#from_keykey)

> Attributes

### marker_sets (list[[MarkerSet](MarkerSet.md#markerset)])
A list of MarkerSet Objects

### length (int)
The amount of MarkerSet Objects in [marker_sets](#marker_sets-listmarkerset)

<br/>

> Methods
### from_key(key)
Get a MarkerSet from [marker_sets](#marker_sets-listmarkerset) by its name
#### Parameters
 - key (str): The name of the MarkerSet, a key from bluemap_wrapper.KEYS can be used, or a custom one can be entered
#### Returns:
Returns a Requested MarkerSet
#### Return Type:
Union[[MarkerSet](MarkerSet.md#markerset), None]

<br/>

## PlayerCollection
> class bluemap_wrapper.PlayerCollection

Contains a list of Player Objects

This class is also Iterable on its own

### Attributes
 - [players](#players-listplayer)
 - [length](#length-int-1)

### Methods
 - [is_foreign()](#is_foreign)
 - [not_foreign](#not_foreign)
 - [from_uuid()](#from_uuiduuid)
 - [from_name()](#from_namename)

> Attributes

### players (list[[Player]()])
A list of Player Objects

### length (int)
The amount of Player Objects in [players](#players-listplayer)

<br/>

> Methods
### is_foreign()
Get a list of players who have the foreign attribute (not in the world requested)
#### Returns:
A list of Player Objects that are foreign
#### Return Type:
list(Union[[Player](), None])

<br/>

### not_foreign()
Get a list of players who do not have the foreign attribute (in the world requested)
#### Returns:
A list of Player Objects that are not foreign
#### Return Type:
list(Union[[Player](), None])

<br/>

### from_uuid(uuid)
Get a Player Object by uuid
#### Parameters
 - uuid (str): The UUID of the Player, the UUID must be exact with "-" in it
#### Returns:
a Player object with the requested UUID
#### Return Type:
Union[Player, None]

<br/>

### from_name(name)
Get a Player Object from its Name
#### Parameters
 - name (str): The name of the Player
#### Returns:
a Player object with the requested name
#### Return Type:
Union[Player, None]





