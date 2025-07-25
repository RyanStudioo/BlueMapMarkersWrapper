*[<u>Back to README.md</u>](../README.md)*
# Clients
- [Client](#client)
- [AsyncClient](#asyncclient)

## Client
> class bluemap_wrapper.Client

Synchronous Client for requesting, uses the requests library.

Slower than [AsyncClient](#asyncclient), more suitable for short and simple projects

### Parameters

- [base_url](#base_url-str)


### Methods

- [fetch_maps](#fetch_maps)
- [fetch_marker_collection](#)
- [fetch_player_collection]()
- [fetch_collection]()

<br/>

> Parameters

### base_url (str)
The base url of the Blue Map

<br/>

> Methods
## fetch_maps()
Get a list of available maps from the API.
### Returns:
A list of strings of available maps
### Return Type:
List[Union[Text, None]]

<br/>

## fetch_marker_collection()
Get a list of available maps from the API.
### Parameters:
 - world (str): The name of the world to fetch from
### Returns:
MarkerCollection Object with all available marker collections
### Return Type:
[MarkerCollection]()

<br/>

## fetch_players_collection()
Get a list of all visible players from the API.
### Parameters:
 - world (str): The name of the world to fetch from
### Returns:
PlayerCollection Object with all available players
### Return Type:
[PlayerCollection]()

## fetch_collection()
Get a lists of MarkerSets and visible players form the API. Offers faster performance due to threaded requesting
#### Parameters:
 - world (str): The name of the world to fetch from
### Returns:
Collection Object with a MarkerCollection and PlayerCollection Object
### Return Type:
[Collection]()


<br/><br/>



## AsyncClient
> class bluemap_wrapper.AsyncClient

Asynchronous Client for requesting, uses the aiohttp library.

Faster than [Client](#client), suitable for larger and more complex projects

### Parameters

- [base_url](#base_url-str-1)

### Methods

- [*await* fetch_maps](#await-fetch_maps)
- [*await* fetch_marker_collection](#await-fetch_marker_collection)
- [*await* fetch_player_collection](#await-fetch_players_collection)
- [*await* fetch_collection](#await-fetch_collection)

<br/>

> Parameters

### base_url (str)
The base url of the Blue Map

<br/>

> Methods
## *await* fetch_maps()
Get a list of available maps from the API.
### Returns:
A list of strings of available maps
### Return Type:
List[Union[Text, None]]

<br/>

## *await* fetch_marker_collection()
Get a list of available maps from the API.
### Parameters:
 - world (str): The name of the world to fetch from
### Returns:
MarkerCollection Object with all available marker collections
### Return Type:
[MarkerCollection]()

<br/>

## *await* fetch_players_collection()
Get a list of all visible players from the API.
### Parameters:
 - world (str): The name of the world to fetch from
### Returns:
PlayerCollection Object with all available players
### Return Type:
[PlayerCollection]()

## *await* fetch_collection()
Get a lists of MarkerSets and visible players form the API. Offers faster performance due to threaded requesting
### Parameters:
 - world (str): The name of the world to fetch from
### Returns:
Collection Object with a MarkerCollection and PlayerCollection Object
### Return Type:
[Collection]()