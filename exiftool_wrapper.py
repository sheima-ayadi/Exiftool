import sys  # Used to get command-line arguments
import exiftool  # Used to extract metadata from images
import webbrowser  # Used to open URLs in the web browser

def extract_metadata(image_path):
    """
    Extract metadata from an image file.
    
    Args:
        image_path (str): The path to the image file.
    
    Returns:
        dict: A dictionary containing the metadata of the image.
    """
    # Use ExifTool to read the metadata from the image file
    with exiftool.ExifTool() as et:
        metadata = et.get_metadata(image_path)
    return metadata

def open_google_maps(latitude, longitude):
    """
    Open Google Maps with the given latitude and longitude.
    
    Args:
        latitude (float): Latitude of the location.
        longitude (float): Longitude of the location.
    """
    # Create the Google Maps URL using the latitude and longitude
    google_maps_url = f"https://www.google.com/maps/search/?api=1&query={latitude},{longitude}"
  
    webbrowser.open(google_maps_url)

if __name__ == "__main__":
    
    if len(sys.argv) != 2:
       
        print("Usage: exiftool_wrapper.py <image_path>")
        sys.exit(1)
    
    # Get the image path from the command-line argument
    image_path = sys.argv[1]
    # Extract metadata from the image
    metadata = extract_metadata(image_path)
    
    # Try to get the latitude and longitude from the metadata
    latitude = metadata.get("EXIF:GPSLatitude")
    longitude = metadata.get("EXIF:GPSLongitude")
    
    # Check if both latitude and longitude are found
    if latitude and longitude:
        print("Location found! Opening in Google Maps...")
        open_google_maps(latitude, longitude)  
    else:
        print("Location not found in metadata.")  
