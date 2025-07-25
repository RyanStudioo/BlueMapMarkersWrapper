# BlueMapWrapper.py
An open-sourced API wrapper for BlueMap for Python!!

This wrapper is used for getting information from existing Blue Maps, NOT to create one

## Versioning Information
> BlueMapWrapper.version_info
 
Returns a string with the version of the module

## Clients

### Client
> class BlueMapWrapper.Client

Synchronous Client for requesting. Uses the requests library.

#### Parameters

- [base_url](#base_url)

<br/>

#### Methods

- [fetch_maps](#fetch_maps)
- [fetch_marker_collection](#)
- [fetch_player_collection]()
- [fetch_collection]()

<br/>

> Parameters

#### base_url (str)
The base url of the Blue Map

<br/>

> Methods

### fetch_maps()
Get a list of available maps from the API.
#### Returns:
A list of strings of available maps
#### Return Type:
List[Union[Text, None]]

<br/><br/>

### fetch_marker_collection()
Get a list of available maps from the API.
#### Parameters:
 - world (str): The name of the world to fetch from
#### Returns:
MarkerCollection Object with all available marker collections
#### Return Type:
[MarkerCollection]()
