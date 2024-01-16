# General helper functions
from serializers import ImageSerializer
from base.models import UploadImage

from dotenv import load_dotenv
load_dotenv()
import os

def image_uploader(image) -> str:
    # Assuming ImageSerializer is a serializer for your UploadImage model
    image_serializer = ImageSerializer(data={"image": image})

    if image_serializer.is_valid():
        # Save the image instance to the database
        image_instance = UploadImage(
            image=image
        )

        image_instance.save()
        app_path = os.environ.get("QUIZLY_API_URL") + "/media/"
        # Return the path or URL of the saved image
        return app_path + str(image_instance.image)
    else:
        # Handle the case where the serializer is not valid
        raise ValueError("Unable to upload image")

