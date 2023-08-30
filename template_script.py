from PIL import Image

class ImageService:
    template_path = "Figma_Version.png"
    template = Image.open(template_path).convert('RGBA')
    template_width, template_height = template.size

    @classmethod
    def handle_image_upload(cls, file_path):
        # Open the uploaded image
        try:
            uploaded_image = Image.open(file_path).convert('RGBA')
        except Exception as e:
            print(f"Error: Unable to open the uploaded image: {e}")
            return

        uploaded_width, uploaded_height = uploaded_image.size

        # Define the fixed dimensions back to their original values
        fixed_width = 5000
        fixed_height = 3350

        # Scale the uploaded image to fit the fixed dimensions
        scaled_image = uploaded_image.resize((fixed_width, fixed_height), Image.LANCZOS)

        # Manually adjust the position of the scaled image
        x = 550  # Adjust the value based on your desired position from the left edge
        y = 80  # Adjust the value based on your desired position from the top edge

        # Create a new transparent image with the template's size
        combined_image = Image.new('RGBA', (cls.template_width, cls.template_height), (0, 0, 0, 0))

        # Paste the scaled image onto the transparent image with the mask
        combined_image.paste(scaled_image, (x, y))

        # Combine the scaled image with the template using the alpha channel
        cls.template = Image.alpha_composite(cls.template, combined_image)

    @classmethod
    def save_resulting_image(cls, output_path):
        # Save the resulting image with higher quality
        cls.template.save(output_path)

if __name__ == "__main__":
    # Replace with the actual file paths for the uploaded image and output image
    uploaded_image_path = "20230729330.JPG"
    output_path = "output.png"

    # Perform image upload, scaling, and embedding on the template
    ImageService.handle_image_upload(uploaded_image_path)

    # Save the resulting image
    ImageService.save_resulting_image(output_path)

    print("Image processing complete. Result saved as 'output.png'.")


# import os
# import boto3
# from PIL import Image

# s3 = boto3.client('s3')

# class ImageService:
#     template_path = "Figma_Version.png"
#     template = Image.open(template_path).convert('RGBA')
#     template_width, template_height = template.size

#     @classmethod
#     def handle_image_upload(cls, file_path):
#         try:
#             uploaded_image = Image.open(file_path).convert('RGBA')
#         except Exception as e:
#             print(f"Error: Unable to open the uploaded image: {e}")
#             return

#         uploaded_width, uploaded_height = uploaded_image.size

#         fixed_width = 5000
#         fixed_height = 3350
#         scaled_image = uploaded_image.resize((fixed_width, fixed_height), Image.LANCZOS)

#         x = 550
#         y = 80

#         combined_image = Image.new('RGBA', (cls.template_width, cls.template_height), (0, 0, 0, 0))
#         combined_image.paste(scaled_image, (x, y))
#         cls.template = Image.alpha_composite(cls.template, combined_image)

#     @classmethod
#     def save_resulting_image(cls, output_path):
#         cls.template.save(output_path)

# def lambda_handler(event, context):
#     uploaded_image_key = "20230729330.JPG"
#     output_key = "output.png"

#     temp_local_path = '/tmp/' + uploaded_image_key
#     output_local_path = '/tmp/' + output_key

#     s3.download_file('your-s3-bucket-name', uploaded_image_key, temp_local_path)

#     ImageService.handle_image_upload(temp_local_path)
#     ImageService.save_resulting_image(output_local_path)

#     s3.upload_file(output_local_path, 'your-s3-bucket-name', output_key)

#     return "Image processing complete. Result saved as 'output.png'."
