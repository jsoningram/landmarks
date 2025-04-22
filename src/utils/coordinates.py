from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS


def get_exif_data(image_path):
    image = Image.open(image_path)
    exif_data = image._getexif()
    if not exif_data:
        return {}

    exif = {}
    for tag_id, value in exif_data.items():
        tag = TAGS.get(tag_id, tag_id)
        if tag == "GPSInfo":
            gps_data = {}
            for key in value:
                gps_tag = GPSTAGS.get(key, key)
                gps_data[gps_tag] = value[key]
            exif["GPSInfo"] = gps_data
        else:
            exif[tag] = value
    return exif


def get_decimal_from_dms(dms, ref):
    degrees = dms[0][0] / dms[0][1]
    minutes = dms[1][0] / dms[1][1]
    seconds = dms[2][0] / dms[2][1]

    decimal = degrees + (minutes / 60.0) + (seconds / 3600.0)
    if ref in ['S', 'W']:
        decimal = -decimal
    return decimal


def get_lat_lon(image_path):
    exif_data = get_exif_data(image_path)
    gps_info = exif_data.get("GPSInfo", {})

    if not gps_info:
        return None, None

    lat = gps_info.get("GPSLatitude")
    lat_ref = gps_info.get("GPSLatitudeRef")
    lon = gps_info.get("GPSLongitude")
    lon_ref = gps_info.get("GPSLongitudeRef")

    if lat and lon and lat_ref and lon_ref:
        return (
            get_decimal_from_dms(lat, lat_ref),
            get_decimal_from_dms(lon, lon_ref)
        )
    return None, None


def main():
    image_file = input('Image: ')
    latitude, longitude = get_lat_lon(f'./images/{image_file}')
    print(f'https://www.google.com/maps/?q={latitude},{longitude}')


if __name__ == '__main__':
    main()
