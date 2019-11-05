import pytest

def test_rsa_encrypt_api_no_args(client):
	response = client.get("/api/rsa/encrypt/hellohello").get_json()
	assert response["status"] == 200
	assert response["content"] == "6cf7959ce3a43fa05dbefc3817cc46ff70bbbe9be3e1b9f5e36efff4ffebc753"

def test_rsa_encrypt_with_modulus_no_exponent(client):
	response = client.get("/api/rsa/encrypt/encryptme?n=42415848681349757752051718300081957764285461076124699639321472972771140363879").get_json()
	assert response["status"] == 200
	assert response["content"] == "42a6954d787430c4252776119ca37bc71b623e033b910919e0e913fc77ba663b"

def test_rsa_encrypt_with_modulus_and_exponent(client):
	response = client.get("/api/rsa/encrypt/encryptor?n=57059114227085536700476775966118909332477157261612895882553491815762042000863&e=3").get_json()
	assert response["status"] == 200
	assert response["content"] == "fec61958cefda4644eb8fc47e801038629df981bcac502fa58f48"
def test_rsa_decrypt_api_with_no_args(client):
	response = client.get("/api/rsa/decrypt/aa5b6230e615aef5634c8539360553805a10226c1e391098e7dd151acca855ce").get_json()
	assert response["status"] == 200
	assert response["content"] == "686f77617265796f75646f696e67"

def test_rsa_decrypt_api_with_primes_and_no_exponent(client):
	response = client.get("/api/rsa/decrypt/206991fe0867bd3ba8bfe9909571823e70768b1619b4c217a51e0351dbe3c002?p=298291149001187106516343162843485948857&q=293090360400911233395047143355539618309").get_json()
	assert response["status"] == 200
	assert response["content"] == "686f77617265796f75646f696e67"

def test_rsa_decrypt_api_with_primes_and_exponent(client):
	response = client.get("/api/rsa/decrypt/6556b5ddc65ff60e96c2b6199f55a1bfb5795dba137338896b4f44bafb033cc3?p=229879532427966175084676861557706702641&q=264648503145758440844248349637667375171&e=17").get_json()
	assert response["status"] == 200
	assert response["content"] == "6c6f72656d697073756d64696d73756d79756d79756d"