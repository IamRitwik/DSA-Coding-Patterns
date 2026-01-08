from LRU_cache import LRUCache
# Time: O(1)
# Space: O(N)
def test_lru_cache():
    print("Running LRU Cache tests...")
    
    # Test case 1: Basic functionality and capacity
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    assert cache.get(1) == 1, "Error: get(1) should be 1"
    
    cache.put(3, 3) # Should evict 2 (since 1 was recently accessed)
    assert cache.get(2) == -1, "Error: key 2 should have been evicted"
    assert cache.get(3) == 3, "Error: get(3) should be 3"
    assert cache.get(1) == 1, "Error: get(1) should be 1"
    
    # Test case 2: Updating existing key
    cache.put(1, 100)
    assert cache.get(1) == 100, "Error: get(1) should be 100"
    
    # Test case 3: Capacity check with update
    cache.put(4, 4) # Should evict 3
    assert cache.get(3) == -1, "Error: key 3 should have been evicted"
    assert cache.get(1) == 100, "Error: get(1) should be 100"
    assert cache.get(4) == 4, "Error: get(4) should be 4"

    # Test case 4: Cache size never exceeds capacity
    assert len(cache.hashmap) == 2, f"Error: cache size should be 2, got {len(cache.hashmap)}"

    print("All tests passed!")

if __name__ == "__main__":
    try:
        test_lru_cache()
    except AssertionError as e:
        print(f"Test failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")
