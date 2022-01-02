from arcgis.gis import GIS


def connectToPortal(username, password, client_id):
    gis = GIS("https://ricckli-tc.maps.arcgis.com", username=username,
              password=password, client_id=client_id)
    items = gis.content.search(query="owner:" + gis.users.me.username,
                               item_type="Feature Layer",
                               max_items=100)
    print(items)
    return items
