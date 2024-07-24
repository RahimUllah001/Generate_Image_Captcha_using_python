from captcha.image import ImageCaptcha
import random
import string

# Create an instance of the ImageCaptcha class
image_captcha = ImageCaptcha()

# Generate a random string of letters and digits for the CAPTCHA
def generate_captcha_text(length=6):
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=length))

# Generate the CAPTCHA image
captcha_text = generate_captcha_text()
captcha_image = image_captcha.generate_image(captcha_text)

# Save the CAPTCHA image
captcha_image.save('captcha_image.png')

print(f"Captcha Text: {captcha_text}")
