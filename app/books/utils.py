import hashlib

def hashlib_book_info(book_title,publisher_name):
    combiner_info = f"{book_title}|{publisher_name}"
    combiner_info_bytes = combiner_info.encode('utf-8')
    sha_256_hash = hashlib.sha256(combiner_info_bytes).hexdigest()
    return sha_256_hash
