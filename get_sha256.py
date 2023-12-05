import hashlib
import requests


def get_sha256_checksum(url):
    sha256_hash = hashlib.sha256()

    response = requests.get(url, stream=True)

    if response.status_code == 200:
        for chunk in response.iter_content(chunk_size=1024):
            sha256_hash.update(chunk)

        return sha256_hash.hexdigest()
    else:
        return None


if __name__ == "__main__":
    url = "https://github.com/jgrss/geowombat/archive/refs/tags/v2.1.15.tar.gz"
    print(get_sha256_checksum(url))
