import os
import cloudinary
import cloudinary.uploader
from cloudinary.utils import cloudinary_url

# Configuration       
cloudinary.config( 
    cloud_name = "dwqmkxylf", 
    api_key = "864323972947951", 
    api_secret = "-F240JVgSVguwii6E117XcSLnts", # Click 'View API Keys' above to copy your API secret
    secure=True
)

# Upload an image
upload_result = cloudinary.uploader.upload("https://res.cloudinary.com/demo/image/upload/getting-started/shoes.jpg",
                                           public_id="shoes")
print(upload_result["secure_url"])

# Optimize delivery by resizing and applying auto-format and auto-quality
optimize_url, _ = cloudinary_url("shoes", fetch_format="auto", quality="auto")
print(optimize_url)

# Transform the image: auto-crop to square aspect_ratio
auto_crop_url, _ = cloudinary_url("shoes", width=500, height=500, crop="auto", gravity="auto")
print(auto_crop_url)


os.envrion['DEV'] = '1'
os.environ['DATABASE_URL'] = "postgres://ulb3rhbcgqg:oWiNeSgNrwYt@ep-gentle-mountain-a23bxz6h-pooler.eu-central-1.aws.neon.tech/swore_mumbo_draw_532644?sslmode=require"
os.environ.setdefault("SECRET_KEY", "#gxc1234")