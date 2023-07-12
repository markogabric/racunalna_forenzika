import hashlib

# Set the path to the USB image file
image_path = 'imageFESB.00'

given_hash = "201cdee056cfc8c0996328e3c2115b513a141f5c"

# Compute the SHA-1 hash of the bitstream image
with open(image_path, 'rb') as f:
    image_hash = hashlib.sha1(f.read()).hexdigest()

# Compare the hashes to verify the integrity of the image
if given_hash == image_hash:
    print('Bitstream image verified successfully')
else:
    print('Error: bitstream image verification failed')