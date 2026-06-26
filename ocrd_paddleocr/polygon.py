from shapely.geometry import Polygon, MultiPolygon, GeometryCollection


def flatten_polygon_geometry(geometry) -> list[Polygon]:
    """Return all polygon components from a Shapely geometry."""
    if geometry.is_empty:
        return []

    if isinstance(geometry, Polygon):
        return [geometry]

    if isinstance(geometry, MultiPolygon):
        return list(geometry.geoms)

    if isinstance(geometry, GeometryCollection):
        result = []
        for geom in geometry.geoms:
            result.extend(flatten_polygon_geometry(geom))
        return result

    return []
