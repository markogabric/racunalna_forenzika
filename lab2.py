import subprocess
import hashlib

image_path = '..\imageFESB.001'

given_hash = "201cdee056cfc8c0996328e3c2115b513a141f5c"

# Compute the SHA-1 hash of the bitstream image
with open(image_path, 'rb') as f:
    image_hash = hashlib.sha1(f.read()).hexdigest()

# Compare the hashes to verify the integrity of the image
if given_hash == image_hash:
    print('Bitstream image verified successfully')

    bitlocker2john_cmd = f'..\\john\\run\\bitlocker2john -i {image_path}'
    process = subprocess.Popen(bitlocker2john_cmd, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()

    keys = output.decode().strip().split('\n')
    recovery_key = [s for s in keys if "$bitlocker$1$" in s]
    print(f'BitLocker recovery key: {recovery_key[0]}')

    hashcat_cmd = f'hashcat -m 22100 -a 3 {recovery_key[0]} "218?d?d?d?d?d"'
    process = subprocess.call(hashcat_cmd, shell=True)

    cracked_password = subprocess.check_output([hashcat_cmd + " --show"], shell=True).decode()
    cracked_password = cracked_password.split(':')[-1]
    print(f"Password : {cracked_password}")
else:
    print('Error: bitstream image verification failed')