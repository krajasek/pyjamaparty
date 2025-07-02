import unittest
import threading
from pyjamaparty.patterns.singleton_pattern import singleton


class TestSingletonPattern(unittest.TestCase):

    def test_singleton_instance_uniqueness(self):
        @singleton
        class SingletonTest(object):
            def __init__(self, data=0):
                self.data = data

        instance_a = SingletonTest(10)
        instance_b = SingletonTest(20)

        self.assertIs(instance_a, instance_b)
        self.assertEqual(instance_a.data, 10)
        self.assertEqual(instance_b.data, 10)

    def test_singleton_thread_safety(self):
        @singleton
        class ThreadSafeSingleton(object):
            def __init__(self):
                # This is to simulate some work being done
                # during initialization.
                import time
                time.sleep(0.1)

        instances = []
        def worker():
            instances.append(ThreadSafeSingleton())

        threads = [threading.Thread(target=worker) for _ in range(10)]
        for t in threads:
            t.start()
        for t in threads:
            t.join()

        first_instance = instances[0]
        for i in range(1, len(instances)):
            self.assertIs(first_instance, instances[i])

    def test_singleton_statefulness(self):
        @singleton
        class StatefulSingleton(object):
            def __init__(self):
                self.value = 0

        s1 = StatefulSingleton()
        self.assertEqual(s1.value, 0)

        s1.value = 42
        s2 = StatefulSingleton()
        self.assertEqual(s2.value, 42)


if __name__ == '__main__':
    unittest.main()