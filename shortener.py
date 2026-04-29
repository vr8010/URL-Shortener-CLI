import random
import string
from db import get_connection

def generate_short_code(length=6):
    chars = string.ascii_letters + string.digits
    return ''.join(random.choices(chars, k=length))

def shorten_url(original_url):
    conn = get_connection()
    cursor = conn.cursor()

    # Check if URL already has a short code
    cursor.execute("SELECT short_code FROM urls WHERE original_url = ?", (original_url,))
    row = cursor.fetchone()
    if row:
        conn.close()
        return row[0]

    # Generate a unique short code
    while True:
        code = generate_short_code()
        cursor.execute("SELECT id FROM urls WHERE short_code = ?", (code,))
        if not cursor.fetchone():
            break

    cursor.execute("INSERT INTO urls (original_url, short_code) VALUES (?, ?)", (original_url, code))
    conn.commit()
    conn.close()
    return code






def get_original_url(short_code):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("SELECT original_url FROM urls WHERE short_code = ?", (short_code,))
    row = cursor.fetchone()
    conn.close()
    return row[0] if row else None
