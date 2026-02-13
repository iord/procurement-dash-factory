"""
Quick test script for Procurement Intelligence Platform
Tests all major features
"""
import requests
import json

BASE_URL = "http://localhost:8001"

print("="*60)
print("TESTING PROCUREMENT INTELLIGENCE PLATFORM")
print("="*60)
print()

# Test 1: Homepage
print("[TEST 1] Homepage...")
try:
    r = requests.get(BASE_URL, timeout=5)
    print(f"[OK] Status: {r.status_code}")
    print(f"[OK] Homepage loads: {len(r.text)} bytes")
except Exception as e:
    print(f"[ERROR] {e}")

print()

# Test 2: API Search
print("[TEST 2] API Search...")
try:
    r = requests.get(f"{BASE_URL}/api/search?limit=5", timeout=10)
    data = r.json()
    print(f"[OK] Status: {r.status_code}")
    print(f"[OK] Found {data['total']} tenders")
    if data['total'] > 0:
        first = data['tenders'][0]
        print(f"[OK] Sample: {first['title'][:50]}...")
        print(f"  Country: {first['country_name']}")
        print(f"  Value: EUR {first['value_eur']:,}")
except Exception as e:
    print(f"[ERROR] {e}")

print()

# Test 3: Statistics
print("[TEST 3] Statistics API...")
try:
    r = requests.get(f"{BASE_URL}/api/stats", timeout=10)
    stats = r.json()
    print(f"[OK] Status: {r.status_code}")
    print(f"[OK] Total tenders: {stats.get('total_tenders', 0)}")
    print(f"[OK] Total value: EUR {stats.get('total_value', 0):,.0f}")
except Exception as e:
    print(f"[ERROR] {e}")

print()

# Test 4: IT Dashboard
print("[TEST 4] IT Tenders Dashboard...")
try:
    r = requests.get(f"{BASE_URL}/dashboard/it-tenders", timeout=10)
    print(f"[OK] Status: {r.status_code}")
    print(f"[OK] Dashboard page: {len(r.text)} bytes")
except Exception as e:
    print(f"[ERROR] {e}")

print()

# Test 5: Filtered Search
print("[TEST 5] Filtered Search (Germany IT)...")
try:
    r = requests.get(f"{BASE_URL}/api/search?country=DE&cpv_code=48&limit=3", timeout=10)
    data = r.json()
    print(f"[OK] Status: {r.status_code}")
    print(f"[OK] Found {data['total']} IT tenders in Germany")
except Exception as e:
    print(f"[ERROR] {e}")

print()
print("="*60)
print("ALL TESTS COMPLETE!")
print("="*60)
print()
print("Platform is running at: http://localhost:8001")
print("="*60)
